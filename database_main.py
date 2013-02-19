# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Dixon\Projects\sqlpy\database.ui'
#
# Created: Mon Feb 11 20:38:56 2013
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
        Form.resize(925, 628)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setLineWidth(0)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget_2 = QtGui.QWidget(self.splitter)
        self.widget_2.setStyleSheet(_fromUtf8("QWidget {\n"
"background: #d2d9e2;\n"
"}"))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tvTables = QtGui.QTreeView(self.widget_2)
        self.tvTables.setObjectName(_fromUtf8("tvTables"))
        self.tvTables.header().setVisible(False)
        self.verticalLayout_3.addWidget(self.tvTables)
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.splitter_2 = QtGui.QSplitter(self.widget)
        self.splitter_2.setLineWidth(0)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.tbTabs = QtGui.QTabWidget(self.splitter_2)
        self.tbTabs.setDocumentMode(True)
        self.tbTabs.setTabsClosable(True)
        self.tbTabs.setObjectName(_fromUtf8("tbTabs"))
        self.verticalLayout_2.addWidget(self.splitter_2)
        self.horizontalLayout.addWidget(self.splitter)

        self.retranslateUi(Form)
        self.tbTabs.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))

import res_rc
