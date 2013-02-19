from collections import OrderedDict

from PyQt4 import QtGui, QtCore, QtSql
from database_main import Ui_Form
from constants import FIELD_TYPES

from querywidget import QueryWidget
import commands


class DatabaseWidet(QtGui.QWidget):
    def __init__(self, database, menu, parent=None):
        super(DatabaseWidet, self).__init__(parent)
        
        self._table = ''
        self._tableicon = QtGui.QIcon(QtGui.QPixmap(":/icons/table.png"))
        self._columnicon = QtGui.QIcon(QtGui.QPixmap(":/icons/table_column.png"))
        self.queryicon = QtGui.QIcon(QtGui.QPixmap(":/icons/script.png"))
        self.histicon = QtGui.QIcon(QtGui.QPixmap(":/icons/calendar_view_day.png"))
        self._menu = menu
        
        self._ui = Ui_Form()
        self._ui.setupUi(self)
        self._ui.splitter.setStretchFactor(1, 1)
        
        self._db = commands.openDatabase(database)
        
        self._model = QtGui.QStandardItemModel()
        self.reload()
        self._ui.tvTables.setModel(self._model)
        
        ## -- add a query
        self.addQueryEditor()
        
        ## -- add history
        self.addHistory()
        
        self.bindEvents()
        self.setTable(self._model.index(0, 0, QtCore.QModelIndex()))
    
    def bindEvents(self):
        self._ui.tvTables.clicked.connect(self.setTable)
        self._ui.tbTabs.currentChanged.connect(self.tabChangeHandler)
    
    def contextMenuEvent(self, event):
        pos = event.globalPos()
        index = self._ui.tvTables.indexAt(event.pos())
        if index.isValid():
            action = self._menu.popup(pos)
            event.accept()
    
    def setTable(self, index):
        self._table = self.__getParentTable(index)
        for i in xrange(self._ui.tbTabs.count()):
            widget = self._ui.tbTabs.widget(i)
            if isinstance(widget, QueryWidget):
                widget.setTable(self._table)
    
    def table(self):
        return self._table
    
    def database(self):
        return self._db.databaseName()
    
    def close(self):
        self._db.close()
    
    def reload(self):
        self._model.clear()
        dbfields = OrderedDict()
        for table in self._db.tables():
            item = QtGui.QStandardItem(self._tableicon, table)
            self._model.appendRow(item)
            fields = commands.getFieldTypes(self._db, table)
            columns = QtGui.QStandardItem('Columns')
            item.appendRow(columns)
            for field, type_ in fields.iteritems():
                fielditem = QtGui.QStandardItem(self._columnicon, '%s (%s)' % (field, type_))
                columns.appendRow(fielditem)
            
            columns.setText('Columns (%i)' % len(fields.keys()))
            dbfields[table] = fields
        
        self._db.setFields(dbfields)
    
    def addQueryEditor(self):
        qwidget = QueryWidget(self._db, self)
        self._ui.tbTabs.addTab(qwidget, self.queryicon, 'Query')
    
    def addHistory(self):
        hwidget = QtGui.QTextEdit(self)
        hwidget.setReadOnly(True)
        hwidget.setFontFamily('Courier New')
        self._ui.tbTabs.addTab(hwidget, self.histicon, 'History')
    
    def tabChangeHandler(self, index):
        if self._ui.tbTabs.tabText(index) == 'History':
            widget = self._ui.tbTabs.widget(index)
            widget.clear()
            for line in self._db.history():
                widget.insertHtml('%s<br />' % line)
    
    def executeQuery(self):
        widget = self._ui.tbTabs.currentWidget()
        widget.executeInput()
    
    def truncateTable(self):
        res, msg = commands.truncateTable(self._db, self._table)
        if not res:
            QtGui.QMessageBox.critical(
                self,
                'Table Error',
                'Failed to truncate table:\n\n%s' % msg
            )
    
    def __getParentTable(self, index):
        parent = index.parent()
        while parent.isValid():
            index = parent
            parent = index.parent()
        
        return index.data()
