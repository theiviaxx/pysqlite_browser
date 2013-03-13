import re

try:
    from PyQt4 import QtGui, QtCore, QtSql
except ImportError:
    from PySide import QtGui, QtCore, QtSql
from sqlscript_main import Ui_Dialog

from sqlitedatabase import SQLiteQuery

class ScriptDialog(QtGui.QDialog):
    def __init__(self, db, parent=None):
        super(ScriptDialog, self).__init__(parent)
        
        self._db = db
        
        self._ui = Ui_Dialog()
        self._ui.setupUi(self)
        self.setWindowModality(QtCore.Qt.WindowModal)
        
        self._ui.buttonBox.accepted.connect(self.__acceptHandler)
        self._ui.buttonBox.rejected.connect(self.close)
        self._ui.bBrowse.clicked.connect(self.browseHandler)
    
    def browseHandler(self):
        res = QtGui.QFileDialog.getOpenFileName(
            self,
            filter='SQL File (*.sql);;Text (*.txt)'
        )
        
        if res:
            self._ui.lFile.setText(res)
    
    def __acceptHandler(self):
        self._db.transaction()
        fh = open(self._ui.lFile.text(), 'rb')
        data = fh.read()
        fh.close()
        
        data = re.split(';', data)
        self._ui.progressBar.setMaximum(len(data))
        
        for i, query in enumerate(data):
            self._ui.progressBar.setValue(i)
            query = re.sub('\s', '', query)
            q = SQLiteQuery(self._db)
            q.exec_(query)
            err = q.lastError()
            if err.isValid() and self._ui.ckAbortOnError.isChecked():
                if err.databaseText().lower() == 'no query':
                    continue
                self._db.rollback()
                
                QtGui.QMessageBox.critical(
                    self,
                    'Script Error',
                    err.databaseText()
                )
                self.close()
                
                return False
        
        self._db.commit()
        
        QtGui.QMessageBox.information(
            self,
            'Script Complete',
            'Script execution was successful'
        )
        self.close()
        
        return False