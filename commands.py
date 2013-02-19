from collections import OrderedDict
import sqlite3

from PyQt4 import QtGui, QtCore, QtSql

from constants import FIELD_TYPES
from sqlitedatabase import SQLiteDatabase, SQLiteQuery

def transaction(db, table, query):
    db.transaction()
    q = db.exec_(query)
    err = q.lastError()
    if err.isValid():
        self._db.rollback()
        
        return False, err.databaseText()
    
    return True, None

def newDatabase(name):
    sqlite3.connect(name)
    
    return True

def openDatabase(name=None):
    dbname = name if name is not None else ':memory:'
    qdb = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db = SQLiteDatabase(qdb)
    db.setDatabaseName(dbname)
    db.open()
    
    return db

def openMemoryDatabase():
    return openDatabase()
    
def getFieldTypes(db, table):
    """ Returns a dict of field names to field types
    
    :param db: Database object to check
    :type db: QSqlDatabase
    :param table: Database table to get values for
    :type table: str
    :returns: dict
    """
    data = OrderedDict()
    q = db.exec_("PRAGMA table_info(%s)" % table)
    hasmore = q.next()
    while hasmore:
        name = q.value(1)
        type_ = q.value(2)
        data[name] = type_
        hasmore = q.next()
    
    return data

def truncateTable(db, table):
    """Drops then creates the table
    
    :param db: Database to operate on
    :type db: QSqlDatabase
    :param table: Table to truncate
    :type table: str
    """
    fields = getFieldTypes(db, table)
    fieldstr = ','.join(['%s %s' % (k, v) for k, v in fields.iteritems()])
    drop = "DROP TABLE IF EXISTS %s" % table
    create = "CREATE TABLE IF NOT EXISTS {table} ({fields})".format(
        table=table,
        fields=fieldstr
    )
    
    res, msg = transaction(db, table, drop)
    if not res:
        return res, msg
    
    res, msg = transaction(db, table, create)
    if not res:
        return res, msg
    
    db.commit()
    
    return True, None

def dropTable(db, table):
    """Drops the table from the database"""
    fields = getFieldTypes(db, table)
    query = "DROP TABLE IF EXISTS {table}".format(
        table=table
    )
    if transaction(db, table, query)[0]:
        db.commit()

def emptyDatabase(db):
    """Drops all tables from database"""
    tables = db.tables()
    for table in tables:
        query = "DROP TABLE IF EXISTS {table}".format(
            table=table
        )
        res, msg = transaction(db, table, query)
        if not res:
            db.rollback()
            
            return res, msg
    
    db.commit()
    
    return True, None

def insertRow(db, table):
    """Inserts a new row into the table"""
    fields = getFieldTypes(db, table)
    query = "INSERT INTO {table} ({fields})".format(
        table=table,
        fields=','.join(fields.keys())
    )
    q = SQLiteQuery(db)
    q.exec_(query)
    db.appendQuery(q)
    

def deleteRows(db, table, rows):
    """Deletes rows from db.table"""
    pass

def duplicateRows(db, table, rows):
    """duplicates rows in db.table"""
    pass
