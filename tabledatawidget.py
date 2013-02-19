import os
import json

from PyQt4 import QtGui, QtCore, QtSql
from tabledata_main import Ui_Form
from querymodel import QueryModel, QuerySortModel, USER_ROLE
from blobdialog import BlobDialog
from sqlitedatabase import SQLiteQuery
import commands

QUERY = "SELECT * FROM {table}{limit}"
LIMIT = " LIMIT {limit}"
DELETE = "DELETE FROM {table} WHERE id IN [{ids}]"
STYLE = """
QTableView { gridline-color: #b4b4b4; }
"""


class TableDelegate(QtGui.QItemDelegate):
    def createEditor(self, parent, option, index):
        if isinstance(index.data(USER_ROLE), (str, unicode)):
            widget = BlobDialog(parent)
            return widget
        
        return super(TableDelegate, self).createEditor(parent, option, index)
    
    def setEditorData(self, editor, index):
        if isinstance(index.data(USER_ROLE), (str, unicode)):
            editor.setContent(index.data())
        else:
            super(TableDelegate, self).setEditorData(editor, index)
    
    def setModelData(self, editor, model, index):
        if isinstance(index.data(USER_ROLE), (str, unicode)):
            value = editor.content()
            model.setData(index, value)
        else:
            super(TableDelegate, self).setModelData(editor, model, index)
    


class TableDataWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(TableDataWidget, self).__init__(parent)
        
        self._table = ''
        self._sortcolumn = 'rowid'
        self._sortorder = QtCore.Qt.AscendingOrder
        self._db = None
        self._model = QueryModel(self)
        self._proxy = QtGui.QSortFilterProxyModel(self)
        self._proxy.setSourceModel(self._model)
        self._proxy.setDynamicSortFilter(True)
        self._rowid = 0
        self._query = None
        
        self._ui = Ui_Form()
        self._ui.setupUi(self)
        self._ui.twGrid.setStyleSheet(STYLE)
        self._ui.twGrid.verticalHeader().setDefaultSectionSize(20)
        self._ui.iLimit.setKeyboardTracking(False)
        self._ui.twGrid.setModel(self._proxy)
        self._ui.tTable.setVisible(False)
        self._ui.twGrid.setItemDelegate(TableDelegate(self._ui.twGrid))
        
        self.bindEvents()
    
    def bindEvents(self):
        self._ui.iLimit.valueChanged.connect(self.updateQuery)
        self._ui.twGrid.clicked.connect(self.clickHandler)
        #self._ui.twGrid.doubleClicked.connect(self.doubleClickHandler)
        self._model.dataChanged.connect(self.dataChangeHandler)
        self._model.dataCommitted.connect(self.commitHandler)
        
        self._ui.bExportData.setDefaultAction(self._ui.actionExportData)
        self._ui.bCopyData.setDefaultAction(self._ui.actionCopy_Data)
        self._ui.bInsertRow.setDefaultAction(self._ui.actionInsert_Row)
        self._ui.bCopyRow.setDefaultAction(self._ui.actionDuplicateRow)
        self._ui.bSaveChanges.setDefaultAction(self._ui.actionSave_changes)
        self._ui.bRemoveSelectedRows.setDefaultAction(self._ui.actionDelete_Row)
        self._ui.bDiscardChanges.setDefaultAction(self._ui.actionDiscard_changes)
        self._ui.bRefresh.setDefaultAction(self._ui.actionRefresh)
        
        self._ui.actionInsert_Row.triggered.connect(self.insertRowHandler)
        self._ui.actionDuplicateRow.triggered.connect(self.duplicateRows)
        self._ui.actionSave_changes.triggered.connect(self._model.commitQueue)
        self._ui.actionDiscard_changes.triggered.connect(self._model.flushQueue)
        self._ui.actionDelete_Row.triggered.connect(self.deleteSelectedRows)
        self._ui.actionRefresh.triggered.connect(self.updateQuery)
    
    def setDatabase(self, db):
        self._db = db
        self._model.setDatabase(self._db)
        self._ui.lDatabase.setText(os.path.split(db.databaseName())[-1])
    
    def setQuery(self, query):
        self._query = query
    
    def setTable(self, table):
        self._table = table
        self._model.setTable(table)
        self.updateQuery()
        self._proxy.invalidate()
        self._ui.lTable.setText(table)
    
    def updateQuery(self, *args):
        self._model.setQuery(self.getQuery())
    
    def getQuery(self):
        if self._ui.ckLimit.isChecked():
            limit = LIMIT.format(limit=self._ui.iLimit.value())
        else:
            limit = ''
        
        query = QUERY.format(
            table=self._table,
            column=self._sortcolumn,
            limit=limit
        )
        
        return query
    
    def clickHandler(self, index):
        if self._model.rowid(index) != self._rowid:
            self._model.commitQueue()
        
        self._rowid = self._model.rowid(index)
    
    def dataChangeHandler(self, tl, br):
        self._ui.bSaveChanges.setEnabled(True)
        self._ui.bDiscardChanges.setEnabled(True)
    
    def commitHandler(self):
        self._ui.bSaveChanges.setEnabled(False)
        self._ui.bDiscardChanges.setEnabled(False)
    
    def deleteSelectedRows(self):
        sel = self._ui.twGrid.selectionModel()
        indexes = sel.selectedRows()
        
        res = QtGui.QMessageBox.question(
            self,
            'Delete Rows',
            'Are you sure you wish to delete the selected (%i) rows?  This is not undoable.' % len(indexes),
            QtGui.QMessageBox.Yes,
            QtGui.QMessageBox.No,
        )
        if res == QtGui.QMessageBox.Yes:
            query = DELETE.format(
                table=self._table,
                ids=','.join([str(i.data()) for i in indexes])
            )
            
            q = SQLiteQuery()
            q.exec_(query)
            
            err = q.lastError()
            if err.isValid():
                ## -- handle error here
                pass
            else:
                self._db.commit()
                self._db.appendQuery(q)
    
    def insertRowHandler(self):
        commands.insertRow(self._db, self._table)
    
    def duplicateRows(self):
        sel = self._ui.twGrid.selectionModel()
        record = self._db.record(self._table)
        fields = [record.field(i).name() for i in xrange(record.count())]
        n = len(fields)
        l = sel.selectedIndexes()
        rows = zip(*[l[i::n] for i in range(1, n + 1)])
        queries = []
        for row in rows:
            values = [r.data() for r in row]
            for i, v in enumerate(values):
                if isinstance(v, (str, unicode)):
                    values[i] = "'%s'" % v
                else:
                    values[i] = str(v)
            
            query = "INSERT INTO {table} ({fields}) VALUES ({values})".format(
                table=self._table,
                fields=','.join(fields),
                values=','.join(values)
            )
            queries.append(query)
        
        self._query.execute(queries)
    