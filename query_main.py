# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Dixon\Projects\pysqlite_browser\query.ui'
#
# Created: Sat Feb 23 22:11:13 2013
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(631, 528)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tQuery = QtGui.QTextEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setPointSize(10)
        self.tQuery.setFont(font)
        self.tQuery.setObjectName(_fromUtf8("tQuery"))
        self.verticalLayout_2.addWidget(self.tQuery)
        self.twTabs = QtGui.QTabWidget(self.splitter)
        self.twTabs.setDocumentMode(True)
        self.twTabs.setObjectName(_fromUtf8("twTabs"))
        self.tabMessages = QtGui.QWidget()
        self.tabMessages.setObjectName(_fromUtf8("tabMessages"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tabMessages)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.tMessages = QtGui.QPlainTextEdit(self.tabMessages)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setPointSize(10)
        self.tMessages.setFont(font)
        self.tMessages.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.tMessages.setReadOnly(True)
        self.tMessages.setObjectName(_fromUtf8("tMessages"))
        self.verticalLayout_7.addWidget(self.tMessages)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/information.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.twTabs.addTab(self.tabMessages, icon, _fromUtf8(""))
        self.tab_9 = QtGui.QWidget()
        self.tab_9.setObjectName(_fromUtf8("tab_9"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.tab_9)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setMargin(0)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.tdTable = TableDataWidget(self.tab_9)
        self.tdTable.setObjectName(_fromUtf8("tdTable"))
        self.verticalLayout_8.addWidget(self.tdTable)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/table.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.twTabs.addTab(self.tab_9, icon1, _fromUtf8(""))
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(Form)
        self.twTabs.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.twTabs.setTabText(self.twTabs.indexOf(self.tabMessages), QtGui.QApplication.translate("Form", "Messages", None, QtGui.QApplication.UnicodeUTF8))
        self.twTabs.setTabText(self.twTabs.indexOf(self.tab_9), QtGui.QApplication.translate("Form", "Table Data", None, QtGui.QApplication.UnicodeUTF8))

from tabledatawidget import TableDataWidget
import res_rc
