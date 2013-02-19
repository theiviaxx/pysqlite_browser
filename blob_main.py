# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Dixon\Projects\sqlpy\blob.ui'
#
# Created: Mon Feb 18 15:45:30 2013
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(802, 467)
        Dialog.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.bText = QtGui.QPushButton(self.widget)
        self.bText.setCheckable(True)
        self.bText.setChecked(True)
        self.bText.setObjectName(_fromUtf8("bText"))
        self.buttonGroup = QtGui.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.bText)
        self.horizontalLayout.addWidget(self.bText)
        self.bImage = QtGui.QPushButton(self.widget)
        self.bImage.setCheckable(True)
        self.bImage.setChecked(False)
        self.bImage.setObjectName(_fromUtf8("bImage"))
        self.buttonGroup.addButton(self.bImage)
        self.horizontalLayout.addWidget(self.bImage)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ckSetNull = QtGui.QCheckBox(self.widget)
        self.ckSetNull.setObjectName(_fromUtf8("ckSetNull"))
        self.horizontalLayout.addWidget(self.ckSetNull)
        self.verticalLayout.addWidget(self.widget)
        self.tContent = QtGui.QPlainTextEdit(Dialog)
        self.tContent.setObjectName(_fromUtf8("tContent"))
        self.verticalLayout.addWidget(self.tContent)
        self.wImage = QtGui.QWidget(Dialog)
        self.wImage.setObjectName(_fromUtf8("wImage"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.wImage)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lImage = QtGui.QLabel(self.wImage)
        self.lImage.setObjectName(_fromUtf8("lImage"))
        self.verticalLayout_2.addWidget(self.lImage)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.wImage)
        self.widget_2 = QtGui.QWidget(Dialog)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.widget_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.lSize = QtGui.QLabel(self.widget_2)
        self.lSize.setObjectName(_fromUtf8("lSize"))
        self.horizontalLayout_2.addWidget(self.lSize)
        self.label_2 = QtGui.QLabel(self.widget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.bOk = QtGui.QPushButton(self.widget_2)
        self.bOk.setObjectName(_fromUtf8("bOk"))
        self.horizontalLayout_2.addWidget(self.bOk)
        self.bCancel = QtGui.QPushButton(self.widget_2)
        self.bCancel.setObjectName(_fromUtf8("bCancel"))
        self.horizontalLayout_2.addWidget(self.bCancel)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.bText.setText(QtGui.QApplication.translate("Dialog", "Text", None, QtGui.QApplication.UnicodeUTF8))
        self.bImage.setText(QtGui.QApplication.translate("Dialog", "Image", None, QtGui.QApplication.UnicodeUTF8))
        self.ckSetNull.setText(QtGui.QApplication.translate("Dialog", "Set Null", None, QtGui.QApplication.UnicodeUTF8))
        self.lImage.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Size:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "bytes", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setText(QtGui.QApplication.translate("Dialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.bCancel.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

