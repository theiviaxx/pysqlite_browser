from PyQt4 import QtGui, QtCore, QtSql
from blob_main import Ui_Dialog


class BlobDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(BlobDialog, self).__init__(parent)
        
        self._ui = Ui_Dialog()
        self._ui.setupUi(self)
        self.resize(720, 400)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self._ui.tContent.textChanged.connect(self.__contentChanged)
        self._ui.bText.clicked.connect(self.__textHandler)
        self._ui.bImage.clicked.connect(self.__imageHandler)
        self._ui.bOk.clicked.connect(self.__acceptHandler)
        self._ui.bCancel.clicked.connect(self.close)
        
        self._initialValue = u''
        self._isaccepted = False
    
    def content(self):
        if self._isaccepted:
            if self._ui.ckSetNull.isChecked():
                return None
            
            return self._ui.tContent.document().toPlainText()
        else:
            return self._initialValue
    
    def setContent(self, content):
        self._ui.tContent.setPlainText(content)
        self._initialValue = unicode(content)
    
    def __imageHandler(self):
        self._ui.tContent.setVisible(False)
        self._ui.wImage.setVisible(True)
        data = QtCore.QByteArray(self._ui.tContent.document().toPlainText())
        pixmap = QtGui.QPixmap(self)
        pixmap.loadFromData(data)
        self._ui.lImage.setPixmap(pixmap)

    def __textHandler(self):
        self._ui.tContent.setVisible(True)
        self._ui.wImage.setVisible(False)
    
    def __contentChanged(self):
        content = self._ui.tContent.document().toPlainText()
        self._ui.lSize.setText(str(len(unicode(content))))
    
    def __acceptHandler(self):
        self._isaccepted = True
        self.close()
