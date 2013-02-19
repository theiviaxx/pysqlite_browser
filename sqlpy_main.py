# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Dixon\Projects\pysqlite_browser\sqlpy.ui'
#
# Created: Mon Feb 18 22:49:52 2013
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(899, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8("#centralwidget, QSplitter {\n"
"background: #d2d9e2;\n"
"}\n"
"QTabWidget > QWidget {\n"
"background: #293955;\n"
"}"))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tbDatabases = QtGui.QTabWidget(self.centralwidget)
        self.tbDatabases.setStyleSheet(_fromUtf8("QTabWidge1t {\n"
"background: #293955;\n"
"}"))
        self.tbDatabases.setDocumentMode(True)
        self.tbDatabases.setTabsClosable(True)
        self.tbDatabases.setObjectName(_fromUtf8("tbDatabases"))
        self.verticalLayout.addWidget(self.tbDatabases)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 899, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuDatabase = QtGui.QMenu(self.menubar)
        self.menuDatabase.setObjectName(_fromUtf8("menuDatabase"))
        self.menuTable = QtGui.QMenu(self.menubar)
        self.menuTable.setObjectName(_fromUtf8("menuTable"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/database_edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionNew = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/database_add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon1)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionClose_All = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/cross.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose_All.setIcon(icon2)
        self.actionClose_All.setObjectName(_fromUtf8("actionClose_All"))
        self.actionExecute_Current_Query = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/script.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExecute_Current_Query.setIcon(icon3)
        self.actionExecute_Current_Query.setObjectName(_fromUtf8("actionExecute_Current_Query"))
        self.actionExecute_All_Queries = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/script_go.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExecute_All_Queries.setIcon(icon4)
        self.actionExecute_All_Queries.setObjectName(_fromUtf8("actionExecute_All_Queries"))
        self.actionRefresh = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/database_refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRefresh.setIcon(icon5)
        self.actionRefresh.setObjectName(_fromUtf8("actionRefresh"))
        self.actionBackup = QtGui.QAction(MainWindow)
        self.actionBackup.setObjectName(_fromUtf8("actionBackup"))
        self.actionExport_DB = QtGui.QAction(MainWindow)
        self.actionExport_DB.setObjectName(_fromUtf8("actionExport_DB"))
        self.actionTruncate_Table = QtGui.QAction(MainWindow)
        self.actionTruncate_Table.setObjectName(_fromUtf8("actionTruncate_Table"))
        self.actionNew_Query_Editor = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/script_add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_Query_Editor.setIcon(icon6)
        self.actionNew_Query_Editor.setObjectName(_fromUtf8("actionNew_Query_Editor"))
        self.actionNew_Memory_Database = QtGui.QAction(MainWindow)
        self.actionNew_Memory_Database.setObjectName(_fromUtf8("actionNew_Memory_Database"))
        self.actionTruncate_Database = QtGui.QAction(MainWindow)
        self.actionTruncate_Database.setObjectName(_fromUtf8("actionTruncate_Database"))
        self.actionEmpty_Database = QtGui.QAction(MainWindow)
        self.actionEmpty_Database.setObjectName(_fromUtf8("actionEmpty_Database"))
        self.actionExport = QtGui.QAction(MainWindow)
        self.actionExport.setObjectName(_fromUtf8("actionExport"))
        self.actionImport = QtGui.QAction(MainWindow)
        self.actionImport.setObjectName(_fromUtf8("actionImport"))
        self.actionCreate_Table = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/table_add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCreate_Table.setIcon(icon7)
        self.actionCreate_Table.setObjectName(_fromUtf8("actionCreate_Table"))
        self.actionDrop_Table = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/table_delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDrop_Table.setIcon(icon8)
        self.actionDrop_Table.setObjectName(_fromUtf8("actionDrop_Table"))
        self.actionRename_Table = QtGui.QAction(MainWindow)
        self.actionRename_Table.setObjectName(_fromUtf8("actionRename_Table"))
        self.actionReorder_Columns = QtGui.QAction(MainWindow)
        self.actionReorder_Columns.setObjectName(_fromUtf8("actionReorder_Columns"))
        self.actionExport_2 = QtGui.QAction(MainWindow)
        self.actionExport_2.setObjectName(_fromUtf8("actionExport_2"))
        self.actionImport_2 = QtGui.QAction(MainWindow)
        self.actionImport_2.setObjectName(_fromUtf8("actionImport_2"))
        self.actionExecute_Script = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/script_code_red.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExecute_Script.setIcon(icon9)
        self.actionExecute_Script.setObjectName(_fromUtf8("actionExecute_Script"))
        self.actionHistory = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/calendar_view_day.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHistory.setIcon(icon10)
        self.actionHistory.setObjectName(_fromUtf8("actionHistory"))
        self.actionInfo = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/bricks.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInfo.setIcon(icon11)
        self.actionInfo.setObjectName(_fromUtf8("actionInfo"))
        self.actionPreferences = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/cog.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreferences.setIcon(icon12)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.actionAbout = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/information.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon13)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionNew_Memory_Database)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNew_Query_Editor)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionClose_All)
        self.menuDatabase.addAction(self.actionCreate_Table)
        self.menuDatabase.addSeparator()
        self.menuDatabase.addAction(self.actionTruncate_Database)
        self.menuDatabase.addAction(self.actionEmpty_Database)
        self.menuTable.addAction(self.actionRename_Table)
        self.menuTable.addSeparator()
        self.menuTable.addAction(self.actionTruncate_Table)
        self.menuTable.addAction(self.actionDrop_Table)
        self.menuTools.addAction(self.actionExecute_Script)
        self.menuTools.addAction(self.actionHistory)
        self.menuTools.addAction(self.actionInfo)
        self.menuTools.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDatabase.menuAction())
        self.menubar.addAction(self.menuTable.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionRefresh)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExecute_All_Queries)

        self.retranslateUi(MainWindow)
        self.tbDatabases.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PySQLite Browser", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuDatabase.setTitle(QtGui.QApplication.translate("MainWindow", "Database", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTable.setTitle(QtGui.QApplication.translate("MainWindow", "Table", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTools.setTitle(QtGui.QApplication.translate("MainWindow", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open Database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "New Database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose_All.setText(QtGui.QApplication.translate("MainWindow", "Close All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExecute_Current_Query.setText(QtGui.QApplication.translate("MainWindow", "Execute Current Query", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExecute_Current_Query.setToolTip(QtGui.QApplication.translate("MainWindow", "Execute Current Query", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExecute_All_Queries.setText(QtGui.QApplication.translate("MainWindow", "Execute All Queries", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRefresh.setText(QtGui.QApplication.translate("MainWindow", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBackup.setText(QtGui.QApplication.translate("MainWindow", "Backup", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport_DB.setText(QtGui.QApplication.translate("MainWindow", "Export DB", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTruncate_Table.setText(QtGui.QApplication.translate("MainWindow", "Truncate Table", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Query_Editor.setText(QtGui.QApplication.translate("MainWindow", "New Query Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Memory_Database.setText(QtGui.QApplication.translate("MainWindow", "New In-Memory Database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTruncate_Database.setText(QtGui.QApplication.translate("MainWindow", "Truncate Database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEmpty_Database.setText(QtGui.QApplication.translate("MainWindow", "Empty Database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport.setText(QtGui.QApplication.translate("MainWindow", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport.setText(QtGui.QApplication.translate("MainWindow", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreate_Table.setText(QtGui.QApplication.translate("MainWindow", "Create Table", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDrop_Table.setText(QtGui.QApplication.translate("MainWindow", "Drop Table", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRename_Table.setText(QtGui.QApplication.translate("MainWindow", "Rename Table", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReorder_Columns.setText(QtGui.QApplication.translate("MainWindow", "Reorder Columns", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport_2.setText(QtGui.QApplication.translate("MainWindow", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport_2.setText(QtGui.QApplication.translate("MainWindow", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExecute_Script.setText(QtGui.QApplication.translate("MainWindow", "Execute Script", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHistory.setText(QtGui.QApplication.translate("MainWindow", "History", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInfo.setText(QtGui.QApplication.translate("MainWindow", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))

import res_rc
