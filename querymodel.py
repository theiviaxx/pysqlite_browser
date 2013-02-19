
import time

from PyQt4 import QtGui, QtCore, QtSql

from sqlitedatabase import SQLiteQuery

USER_ROLE = QtCore.Qt.UserRole + 1


class ModelSignal(QtCore.QObject):
    dataCommitted = QtCore.pyqtSignal()


class QueryModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None):
        super(QueryModel, self).__init__(parent)
        
        signals = ModelSignal(self)
        
        self._query = ''
        self._db = None
        self._history = []
        self._data = [[]]
        self._headers = []
        self._table = ''
        self._updates = []
        self._queue = []
        self._rowid = 0
        self._readonly = False
        self.dataCommitted = signals.dataCommitted
    
    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self._data)
    
    def columnCount(self, parent=QtCore.QModelIndex()):
        return len(self._headers)
    
    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole or role == USER_ROLE:
            if self._db.getType(self._table, index.column()) == 'real' and role == QtCore.Qt.DisplayRole:
                return str(self._data[index.row()][index.column()])
            return self._data[index.row()][index.column()]
        return None
    
    def setData(self, index, value, role=QtCore.Qt.EditRole):
        self._data[index.row()][index.column()] = value
        self._rowid = self._data[index.row()][0]
        quoted = self._db.getType(self._table, index.column()) == 'text'
        if quoted:
            value = "'%s'" % value
        
        self._updates.append((self._headers[index.column()], value))

        self.dataChanged.emit(index, index)
        return True
    
    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self._headers[section]
    
    def flags(self, index):
        flags = super(QueryModel, self).flags(index)
        if not self._readonly:
            flags |= QtCore.Qt.ItemIsEditable
        
        return flags
    
    def insertRows(self, row, count, parent, data):
        self._data = [[]]
        self.beginInsertRows(parent, row, row + count)
        self._data = data
        self.endInsertRows()
    
    def appendInsertRow(self):
        self.beginInsertRows(QtCore.QModelIndex(), self.rowCount(), 1)
        self._data.append(self._db.fields(self._table).keys())
        self.endInsertRows()
    
    def removeRows(self, row, count, parent):
        self.beginInsertRows(parent, row, row + count)
        self._data = data[row:row + count]
        self.endInsertRows()
    
    ## -- new methods
    def rowid(self, index):
        return self._data[index.row()][0]
    
    def setDatabase(self, db):
        self._db = db
    
    def setQuery(self, query):
        self._query = query
        self.query()
    
    def setTable(self, table):
        self._table = table
        self.setHeaders()
    
    def setHeaders(self, headers=None):
        self._headers = []
        if headers is None:
            for f in self._db.fields(self._table).iterkeys():
                self._headers.append(f)
        else:
            self._headers = headers
    
    def setReadOnly(self, val):
        self._readonly = val
    
    def query(self):
        q = SQLiteQuery()
        q.exec_(self._query)
        self._db.appendQuery(q)
        self.setRecords(q)
    
    def setRecords(self, result):
        self.reset()
        
        ids = []
        count = result.record().count()
        while result.next():
            i = 0
            val = result.value(i)
            fields = []
            while i < count:
                fields.append(val)
                i += 1
                val = result.value(i)
            ids.append(fields)
        
        self.insertRows(0, len(ids) - 1, QtCore.QModelIndex(), ids)
    
    def commitQueue(self):
        self._db.transaction()
        success = True
        if self._updates:
            q = SQLiteQuery()
            query = "UPDATE {table} SET {sets} WHERE rowid = {rowid}"
            sets = ','.join(['%s = %s' % (x, y) for x, y in self._updates])
            query = query.format(table=self._table, sets=sets, rowid=self._rowid)
            q.exec_(query)
            err = q.lastError()
            if err.isValid():
                self._db.rollback()
                success = False
            else:
                self._db.commit()
                self._db.appendQuery(q)
            
            self._updates = []
        
            self.dataCommitted.emit()
        
        return success
    
    def flushQueue(self):
        self._updates = []
        self.query()
        self.dataCommitted.emit()



class QuerySortModel(QtGui.QSortFilterProxyModel):
    def lessThan(self, left, right):
        l = self.sourceModel().data(left)
        r = self.sourceModel().data(right)
        
        return l > r
