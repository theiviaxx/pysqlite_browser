# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Dixon\Projects\sqlpy\resultdata.ui'
#
# Created: Sat Feb 09 15:46:21 2013
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
        Form.resize(707, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget_4 = QtGui.QWidget(Form)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.toolButton_10 = QtGui.QToolButton(self.widget_4)
        self.toolButton_10.setMinimumSize(QtCore.QSize(24, 24))
        self.toolButton_10.setMaximumSize(QtCore.QSize(24, 24))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/application_go.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_10.setIcon(icon)
        self.toolButton_10.setAutoRaise(True)
        self.toolButton_10.setObjectName(_fromUtf8("toolButton_10"))
        self.horizontalLayout_3.addWidget(self.toolButton_10)
        self.toolButton_11 = QtGui.QToolButton(self.widget_4)
        self.toolButton_11.setMinimumSize(QtCore.QSize(24, 24))
        self.toolButton_11.setMaximumSize(QtCore.QSize(24, 24))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/table_go.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_11.setIcon(icon1)
        self.toolButton_11.setAutoRaise(True)
        self.toolButton_11.setObjectName(_fromUtf8("toolButton_11"))
        self.horizontalLayout_3.addWidget(self.toolButton_11)
        self.comboBox = QtGui.QComboBox(self.widget_4)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.toolButton_12 = QtGui.QToolButton(self.widget_4)
        self.toolButton_12.setMinimumSize(QtCore.QSize(24, 24))
        self.toolButton_12.setMaximumSize(QtCore.QSize(24, 24))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/table_add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_12.setIcon(icon2)
        self.toolButton_12.setAutoRaise(True)
        self.toolButton_12.setObjectName(_fromUtf8("toolButton_12"))
        self.horizontalLayout_3.addWidget(self.toolButton_12)
        self.toolButton_13 = QtGui.QToolButton(self.widget_4)
        self.toolButton_13.setMinimumSize(QtCore.QSize(24, 24))
        self.toolButton_13.setMaximumSize(QtCore.QSize(24, 24))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/table_multiple.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_13.setIcon(icon3)
        self.toolButton_13.setAutoRaise(True)
        self.toolButton_13.setObjectName(_fromUtf8("toolButton_13"))
        self.horizontalLayout_3.addWidget(self.toolButton_13)
        self.toolButton_14 = QtGui.QToolButton(self.widget_4)
        self.toolButton_14.setMinimumSize(QtCore.QSize(24, 24))
        self.toolButton_14.setMaximumSize(QtCore.QSize(24, 24))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/table_save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_14.setIcon(icon4)
        self.toolButton_14.setAutoRaise(True)
        self.toolButton_14.setObjectName(_fromUtf8("toolButton_14"))
        self.horizontalLayout_3.addWidget(self.toolButton_14)
        self.toolButton_15 = QtGui.QToolButton(self.widget_4)
        self.toolButton_15.setMinimumSize(QtCore.QSize(24, 24))
        self.toolButton_15.setMaximumSize(QtCore.QSize(24, 24))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/bin_empty.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_15.setIcon(icon5)
        self.toolButton_15.setAutoRaise(True)
        self.toolButton_15.setObjectName(_fromUtf8("toolButton_15"))
        self.horizontalLayout_3.addWidget(self.toolButton_15)
        self.toolButton_16 = QtGui.QToolButton(self.widget_4)
        self.toolButton_16.setMinimumSize(QtCore.QSize(24, 24))
        self.toolButton_16.setMaximumSize(QtCore.QSize(24, 24))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/table_delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_16.setIcon(icon6)
        self.toolButton_16.setAutoRaise(True)
        self.toolButton_16.setObjectName(_fromUtf8("toolButton_16"))
        self.horizontalLayout_3.addWidget(self.toolButton_16)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.toolButton_17 = QtGui.QToolButton(self.widget_4)
        self.toolButton_17.setMinimumSize(QtCore.QSize(24, 24))
        self.toolButton_17.setMaximumSize(QtCore.QSize(24, 24))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/filter.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_17.setIcon(icon7)
        self.toolButton_17.setAutoRaise(True)
        self.toolButton_17.setObjectName(_fromUtf8("toolButton_17"))
        self.horizontalLayout_3.addWidget(self.toolButton_17)
        self.toolButton_18 = QtGui.QToolButton(self.widget_4)
        self.toolButton_18.setMinimumSize(QtCore.QSize(24, 24))
        self.toolButton_18.setMaximumSize(QtCore.QSize(24, 24))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/table_refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_18.setIcon(icon8)
        self.toolButton_18.setAutoRaise(True)
        self.toolButton_18.setObjectName(_fromUtf8("toolButton_18"))
        self.horizontalLayout_3.addWidget(self.toolButton_18)
        self.ckLimit_2 = QtGui.QCheckBox(self.widget_4)
        self.ckLimit_2.setObjectName(_fromUtf8("ckLimit_2"))
        self.horizontalLayout_3.addWidget(self.ckLimit_2)
        self.label_4 = QtGui.QLabel(self.widget_4)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.iFirstRow_2 = QtGui.QSpinBox(self.widget_4)
        self.iFirstRow_2.setMaximum(1000000)
        self.iFirstRow_2.setObjectName(_fromUtf8("iFirstRow_2"))
        self.horizontalLayout_3.addWidget(self.iFirstRow_2)
        self.label_5 = QtGui.QLabel(self.widget_4)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.iLimit_2 = QtGui.QSpinBox(self.widget_4)
        self.iLimit_2.setMaximum(1000000)
        self.iLimit_2.setProperty(_fromUtf8("value"), 1000)
        self.iLimit_2.setObjectName(_fromUtf8("iLimit_2"))
        self.horizontalLayout_3.addWidget(self.iLimit_2)
        self.verticalLayout.addWidget(self.widget_4)
        self.table = QtGui.QTableView(Form)
        self.table.setSortingEnabled(True)
        self.table.setObjectName(_fromUtf8("table"))
        self.verticalLayout.addWidget(self.table)
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setMargin(2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.ckLimit_2.setText(QtGui.QApplication.translate("Form", "Limit rows", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "First row", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "# of rows", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Database: Name   Table: Table", None, QtGui.QApplication.UnicodeUTF8))

import res_rc
