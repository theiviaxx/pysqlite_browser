# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Dixon\Projects\pysqlite_browser\exportdata.ui'
#
# Created: Tue Jul 23 21:23:13 2013
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
        Dialog.resize(623, 465)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.widget_4 = QtGui.QWidget(Dialog)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.widget_4)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/table_go.png")))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_2 = QtGui.QLabel(self.widget_4)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.line = QtGui.QFrame(Dialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.widget_5 = QtGui.QWidget(Dialog)
        self.widget_5.setObjectName(_fromUtf8("widget_5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.widget_5)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.eFile = QtGui.QLineEdit(self.widget_5)
        self.eFile.setObjectName(_fromUtf8("eFile"))
        self.horizontalLayout_3.addWidget(self.eFile)
        self.bBrowse = QtGui.QPushButton(self.widget_5)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bBrowse.setIcon(icon)
        self.bBrowse.setObjectName(_fromUtf8("bBrowse"))
        self.horizontalLayout_3.addWidget(self.bBrowse)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_2.addWidget(self.line_2)
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(self.widget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lvFields = QtGui.QListView(self.groupBox)
        self.lvFields.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.lvFields.setObjectName(_fromUtf8("lvFields"))
        self.verticalLayout.addWidget(self.lvFields)
        self.widget_6 = QtGui.QWidget(self.groupBox)
        self.widget_6.setObjectName(_fromUtf8("widget_6"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.bSelectAll = QtGui.QPushButton(self.widget_6)
        self.bSelectAll.setObjectName(_fromUtf8("bSelectAll"))
        self.horizontalLayout_4.addWidget(self.bSelectAll)
        self.bDeselectAll = QtGui.QPushButton(self.widget_6)
        self.bDeselectAll.setObjectName(_fromUtf8("bDeselectAll"))
        self.horizontalLayout_4.addWidget(self.bDeselectAll)
        self.verticalLayout.addWidget(self.widget_6)
        self.horizontalLayout.addWidget(self.groupBox)
        self.toolBox = QtGui.QToolBox(self.widget)
        self.toolBox.setStyleSheet(_fromUtf8("QToolBox::tab {\n"
"border: 1px solid #608058;\n"
"background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #eff3d7, stop:1 #bbca95);\n"
"}"))
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 323, 263))
        self.page.setObjectName(_fromUtf8("page"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.widget_3 = QtGui.QWidget(self.page)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.formLayout_2 = QtGui.QFormLayout(self.widget_3)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.ckEscapeChar = QtGui.QCheckBox(self.widget_3)
        self.ckEscapeChar.setChecked(True)
        self.ckEscapeChar.setObjectName(_fromUtf8("ckEscapeChar"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.ckEscapeChar)
        self.eEscapeChar = QtGui.QLineEdit(self.widget_3)
        self.eEscapeChar.setObjectName(_fromUtf8("eEscapeChar"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.eEscapeChar)
        self.ckLineTerminator = QtGui.QCheckBox(self.widget_3)
        self.ckLineTerminator.setChecked(True)
        self.ckLineTerminator.setObjectName(_fromUtf8("ckLineTerminator"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.ckLineTerminator)
        self.eLineTerminator = QtGui.QLineEdit(self.widget_3)
        self.eLineTerminator.setObjectName(_fromUtf8("eLineTerminator"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.eLineTerminator)
        self.ckAddColumns = QtGui.QCheckBox(self.widget_3)
        self.ckAddColumns.setObjectName(_fromUtf8("ckAddColumns"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.ckAddColumns)
        self.verticalLayout_4.addWidget(self.widget_3)
        self.groupBox_2 = QtGui.QGroupBox(self.page)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.rbFixedLength = QtGui.QRadioButton(self.groupBox_2)
        self.rbFixedLength.setObjectName(_fromUtf8("rbFixedLength"))
        self.buttonGroup = QtGui.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.rbFixedLength)
        self.verticalLayout_3.addWidget(self.rbFixedLength)
        self.rbVariableLength = QtGui.QRadioButton(self.groupBox_2)
        self.rbVariableLength.setChecked(True)
        self.rbVariableLength.setObjectName(_fromUtf8("rbVariableLength"))
        self.buttonGroup.addButton(self.rbVariableLength)
        self.verticalLayout_3.addWidget(self.rbVariableLength)
        self.wVariableLength = QtGui.QWidget(self.groupBox_2)
        self.wVariableLength.setObjectName(_fromUtf8("wVariableLength"))
        self.formLayout = QtGui.QFormLayout(self.wVariableLength)
        self.formLayout.setContentsMargins(16, 0, 0, 0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.ckDelimeter = QtGui.QCheckBox(self.wVariableLength)
        self.ckDelimeter.setChecked(True)
        self.ckDelimeter.setObjectName(_fromUtf8("ckDelimeter"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.ckDelimeter)
        self.ckQuoteChar = QtGui.QCheckBox(self.wVariableLength)
        self.ckQuoteChar.setChecked(True)
        self.ckQuoteChar.setObjectName(_fromUtf8("ckQuoteChar"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.ckQuoteChar)
        self.ckNullReplace = QtGui.QCheckBox(self.wVariableLength)
        self.ckNullReplace.setChecked(True)
        self.ckNullReplace.setObjectName(_fromUtf8("ckNullReplace"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.ckNullReplace)
        self.eDelimeter = QtGui.QLineEdit(self.wVariableLength)
        self.eDelimeter.setObjectName(_fromUtf8("eDelimeter"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.eDelimeter)
        self.eQuoteChar = QtGui.QLineEdit(self.wVariableLength)
        self.eQuoteChar.setObjectName(_fromUtf8("eQuoteChar"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.eQuoteChar)
        self.eNullReplace = QtGui.QLineEdit(self.wVariableLength)
        self.eNullReplace.setObjectName(_fromUtf8("eNullReplace"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.eNullReplace)
        self.verticalLayout_3.addWidget(self.wVariableLength)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.verticalLayout_4.setStretch(1, 1)
        self.toolBox.addItem(self.page, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 323, 263))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.formLayout_3 = QtGui.QFormLayout(self.page_2)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label = QtGui.QLabel(self.page_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.sIndent = QtGui.QSpinBox(self.page_2)
        self.sIndent.setMaximum(10)
        self.sIndent.setObjectName(_fromUtf8("sIndent"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.sIndent)
        self.ckColumnTypes = QtGui.QCheckBox(self.page_2)
        self.ckColumnTypes.setObjectName(_fromUtf8("ckColumnTypes"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.ckColumnTypes)
        self.toolBox.addItem(self.page_2, _fromUtf8(""))
        self.page_3 = QtGui.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 323, 263))
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.formLayout_4 = QtGui.QFormLayout(self.page_3)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.rbStructure = QtGui.QRadioButton(self.page_3)
        self.rbStructure.setObjectName(_fromUtf8("rbStructure"))
        self.buttonGroup_2 = QtGui.QButtonGroup(Dialog)
        self.buttonGroup_2.setObjectName(_fromUtf8("buttonGroup_2"))
        self.buttonGroup_2.addButton(self.rbStructure)
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.rbStructure)
        self.rbData = QtGui.QRadioButton(self.page_3)
        self.rbData.setObjectName(_fromUtf8("rbData"))
        self.buttonGroup_2.addButton(self.rbData)
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.rbData)
        self.rbStructureData = QtGui.QRadioButton(self.page_3)
        self.rbStructureData.setChecked(True)
        self.rbStructureData.setObjectName(_fromUtf8("rbStructureData"))
        self.buttonGroup_2.addButton(self.rbStructureData)
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.LabelRole, self.rbStructureData)
        self.toolBox.addItem(self.page_3, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.toolBox)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_2.addWidget(self.widget)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.toolBox.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Export Data", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Choose a format in which you want to export your data", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Save to file", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Select Field(s) To Export", None, QtGui.QApplication.UnicodeUTF8))
        self.bSelectAll.setText(QtGui.QApplication.translate("Dialog", "Select All", None, QtGui.QApplication.UnicodeUTF8))
        self.bDeselectAll.setText(QtGui.QApplication.translate("Dialog", "Deselect All", None, QtGui.QApplication.UnicodeUTF8))
        self.ckEscapeChar.setText(QtGui.QApplication.translate("Dialog", "Escaped by", None, QtGui.QApplication.UnicodeUTF8))
        self.eEscapeChar.setText(QtGui.QApplication.translate("Dialog", "\\\\", None, QtGui.QApplication.UnicodeUTF8))
        self.ckLineTerminator.setText(QtGui.QApplication.translate("Dialog", "Lines terminated by", None, QtGui.QApplication.UnicodeUTF8))
        self.eLineTerminator.setText(QtGui.QApplication.translate("Dialog", "\\r\\n", None, QtGui.QApplication.UnicodeUTF8))
        self.ckAddColumns.setText(QtGui.QApplication.translate("Dialog", "Add colum names on top", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "Fields", None, QtGui.QApplication.UnicodeUTF8))
        self.rbFixedLength.setText(QtGui.QApplication.translate("Dialog", "Fixed Length", None, QtGui.QApplication.UnicodeUTF8))
        self.rbVariableLength.setText(QtGui.QApplication.translate("Dialog", "Variable length", None, QtGui.QApplication.UnicodeUTF8))
        self.ckDelimeter.setText(QtGui.QApplication.translate("Dialog", "Fields terminated by", None, QtGui.QApplication.UnicodeUTF8))
        self.ckQuoteChar.setText(QtGui.QApplication.translate("Dialog", "Fields enclosed by", None, QtGui.QApplication.UnicodeUTF8))
        self.ckNullReplace.setText(QtGui.QApplication.translate("Dialog", "NULL value replaced by", None, QtGui.QApplication.UnicodeUTF8))
        self.eDelimeter.setText(QtGui.QApplication.translate("Dialog", ",", None, QtGui.QApplication.UnicodeUTF8))
        self.eQuoteChar.setText(QtGui.QApplication.translate("Dialog", "\"", None, QtGui.QApplication.UnicodeUTF8))
        self.eNullReplace.setText(QtGui.QApplication.translate("Dialog", "\\N", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QtGui.QApplication.translate("Dialog", "CSV", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Indent", None, QtGui.QApplication.UnicodeUTF8))
        self.ckColumnTypes.setText(QtGui.QApplication.translate("Dialog", "Include column names and types", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QtGui.QApplication.translate("Dialog", "JSON", None, QtGui.QApplication.UnicodeUTF8))
        self.rbStructure.setText(QtGui.QApplication.translate("Dialog", "Structure only", None, QtGui.QApplication.UnicodeUTF8))
        self.rbData.setText(QtGui.QApplication.translate("Dialog", "Data only", None, QtGui.QApplication.UnicodeUTF8))
        self.rbStructureData.setText(QtGui.QApplication.translate("Dialog", "Structure and Data", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QtGui.QApplication.translate("Dialog", "SQL", None, QtGui.QApplication.UnicodeUTF8))

import res_rc
