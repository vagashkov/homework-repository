﻿import os
import sqlite3


class TableData(dict):
    """ storage wrapper for simple sqlite database"""
    def __init__(self, db_name, table_name):
        self.conn = sqlite3.connect(os.getcwd() + db_name)
        self.conn.row_factory = sqlite3.Row
        self.table = table_name

    def __len__(self):
        """ checking for table row number """
        cursor = self.conn.cursor()
        data = cursor.execute(f"SELECT count(*) from {self.table}").fetchall()
        return data[0][0]

    def __getitem__(self, key):
        """ getting the single record (name should be unique) """
        cursor = self.conn.cursor()
        query = f"SELECT * from {self.table} where name='{key}'"
        data = cursor.execute(query).fetchall()
        return data[0]

    def __contains__(self, key):
        """ checking in value exists in column """
        cursor = self.conn.cursor()
        query = f"SELECT * from {self.table} where name='{key}'"
        data = cursor.execute(query).fetchall()
        return bool(data)

    def __iter__(self):
        """ returning iterator object for request result (cursor itself) """
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * from {self.table}")
        return cursor

    def __setitem__(self, key, value):
        """ insert (update) record """
        cursor = self.conn.cursor()
        query = f"SELECT count(*) from {self.table} where name='{key}'"
        data = cursor.execute(query).fetchall()
        if not bool(data[0][0]):
            # inserting new record
            query = f"INSERT INTO {self.table} VALUES(?,?,?)"
            values = (key, ) + value
            cursor.execute(query, values)
            self.conn.commit()
        else:
            # updating an existing record
            query = f"UPDATE {self.table} SET age = ?, country = ?"
            query += "WHERE name = ?"
            values = value + (key, )
            cursor.execute(query, values)
            self.conn.commit()

    def __delattr__(self, key):
        """ 'delete' attribute from dict """
        cursor = self.conn.cursor()
        query = f"DELETE from {self.table} where name='{key}'"
        cursor.execute(query)
        self.conn.commit()
