
import sys

import sip
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)
from PyQt4 import QtGui, QtCore, QtSql
from sqlpy_main import Ui_MainWindow
from databasewidget import DatabaseWidet

import commands


class Window(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        
        self.bindEvents()
    
    def bindEvents(self):
        self._ui.actionOpen.triggered.connect(self.addDatabse)
        self._ui.actionExecute_All_Queries.triggered.connect(self.executeQuery)
        self._ui.tbDatabases.tabCloseRequested.connect(self.removeDataBase)
        self._ui.actionTruncate_Table.triggered.connect(self.truncateTable)
        self._ui.actionNew_Query_Editor.triggered.connect(self.newQueryEditor)
        self._ui.actionRefresh.triggered.connect(self.reloadDatabase)
        self._ui.actionNew.triggered.connect(self.newDatabase)
        self._ui.actionNew_Memory_Database.triggered.connect(self.newMemoryDatabase)
    
    def addDatabse(self, dbfile=None):
        if not dbfile:
            dbfile = QtGui.QFileDialog.getOpenFileName(self, 'Pick a SQLite DB file')
        
        if dbfile:
            if self.hasDatabase(dbfile) == -1:
                name = dbfile.replace('\\', '/').split('/')[-1]
                dbicon = QtGui.QIcon(QtGui.QPixmap(":/icons/database.png"))
                widget = DatabaseWidet(dbfile, self._ui.menuTable, self)
                self._ui.tbDatabases.addTab(widget, dbicon, name)
            else:
                self._ui.tbDatabases.setCurrentIndex(self.hasDatabase(dbfile))
    
    def removeDataBase(self, index):
        widget = self._ui.tbDatabases.widget(index)
        widget.close()
        self._ui.tbDatabases.removeTab(index)
    
    def hasDatabase(self, name):
        for i in xrange(self._ui.tbDatabases.count()):
            widget = self._ui.tbDatabases.widget(i)
            if widget.database() == name:
                return i
        
        return -1
    
    def executeQuery(self):
        widget = self._ui.tbDatabases.currentWidget()
        if widget:
            widget.executeQuery()
    
    def reloadDatabase(self):
        widget = self._ui.tbDatabases.currentWidget()
        if widget:
            widget.reload()
    
    def truncateTable(self):
        widget = self._ui.tbDatabases.currentWidget()
        if widget:
            widget.truncateTable()
    
    def newQueryEditor(self):
        widget = self._ui.tbDatabases.currentWidget()
        if widget:
            widget.addQueryEditor()
    
    def newDatabase(self):
        dbfile = QtGui.QFileDialog.getSaveFileName(
            self,
            'Choose database file',
        )
        if dbfile:
            if commands.newDatabase(dbfile):
                self.addDatabse(dbfile)
    
    def newMemoryDatabase(self):
        self.addDatabse(':memory:')
    


def main():
    app = QtGui.QApplication(sys.argv)
    
    win = Window()
    win.show()
    
    sys.exit(app.exec_())

    
if __name__ == '__main__':
    main()