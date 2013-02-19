import time
import re

from PyQt4 import QtGui, QtCore, QtSql
from query_main import Ui_Form

from tabledatawidget import TableDataWidget
from resultdatawidget import ResultDataWidget
from sqlitedatabase import SQLiteQuery
from constants import KEYWORDS

QUERY = "SELECT * FROM {table} WHERE rowid > {first} ORDER BY {column} {order} LIMIT {limit}"
MESSAGE_HEAD = "{queries} queries executed, {success} success, {errors} errors\n"
MESSAGE_SELECT = """
Query: {query}

{numrows} row(s) returned

Time: {time}
--------------------------------------------------

"""

MESSAGE_UPDATE = """
Query: {query}

{numrows} row(s) affected

Time: {time}
--------------------------------------------------

"""
MESSAGE_ERROR = """
Query: {query}

{error}

Time: {time}
--------------------------------------------------

"""


class QueryWidget(QtGui.QWidget):
    def __init__(self, db, parent=None):
        super(QueryWidget, self).__init__(parent)
        
        self._table = ''
        self._db = db
        self._resulticon = QtGui.QIcon(QtGui.QPixmap(":/icons/table_lightning.png"))
        
        self._ui = Ui_Form()
        self._ui.setupUi(self)
        self._ui.tdTable.setDatabase(db)
        self._ui.tdTable.setQuery(self)
        
        self.bindEvents()
    
    def bindEvents(self):
        self._ui.tQuery.keyReleaseEvent = self.keyup
    
    def table(self):
        return self._table
    
    def setTable(self, table):
        self._table = table
        self._ui.tdTable.setTable(table)
    
    def keyup(self, event):
        pos = self._ui.tQuery.textCursor().position()
        text = self._ui.tQuery.document().toPlainText().lower()
        for i in iter(KEYWORDS):
            text = re.sub(r'\b%s\b' % i.lower(), i, text)
        self._ui.tQuery.setPlainText(text)
        cur = self._ui.tQuery.textCursor()
        cur.setPosition(pos)
        self._ui.tQuery.setTextCursor(cur)
    
    def executeInput(self):
        queries = filter(None, self._ui.tQuery.toPlainText().split(';'))
        self.execute(queries)
    
    def execute(self, queries):
        errors = 0
        success = 0
        text = ''
        self._ui.tMessages.clear()
        self.__clearQueryTabs()
        for query in queries:
            q = SQLiteQuery()
            res = q.exec_(query)
            if res:
                success += 1
            else:
                errors += 1
            self._db.appendQuery(q)
            err = q.lastError()
            if err.isValid():
                text += MESSAGE_ERROR.format(
                    query=q.lastQuery(),
                    error=err.databaseText(),
                    time=q.time(),
                )
            else:
                if q.isSelect():
                    i = 0
                    while q.next():
                        i += 1
                    q.seek(-1)
                    widget = ResultDataWidget()
                    widget.setDatabase(self._db)
                    widget.setData(q)
                    self._ui.twTabs.insertTab(0, widget, self._resulticon, 'Results')
                    text += MESSAGE_SELECT.format(
                        query=q.lastQuery(),
                        numrows=i,
                        time=q.time(),
                    )
                else:
                    text += MESSAGE_UPDATE.format(
                        query=q.lastQuery(),
                        numrows=q.numRowsAffected(),
                        time=q.time(),
                    )
        
        self._ui.tMessages.insertPlainText(
            MESSAGE_HEAD.format(queries=len(queries), success=success, errors=errors)
        )
        self._ui.tMessages.insertPlainText(text)
        
        if errors:
            self._ui.twTabs.setCurrentWidget(self._ui.tabMessages)
    
    def __clearQueryTabs(self):
        widget = self._ui.twTabs.widget(0)
        while isinstance(widget, ResultDataWidget):
            widget.deleteLater()
            self._ui.twTabs.removeTab(0)
            widget = self._ui.twTabs.widget(0)
