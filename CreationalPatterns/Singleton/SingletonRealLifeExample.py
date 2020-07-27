#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 13:39:06 2020

@author: fuhr
"""

import sqlite3

# class MetaSingleton(type):
#     _instances = {}
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(MetaSingleton,
#                                         cls).__call__(*args, **kwargs)
#             return cls._instances[cls]

class Singleton(object):
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

class Database(Singleton):
    connection = None
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj
    

db1 = Database().connect()
db2 = Database().connect()

print("Database object DB1: ", db1)
print("Database object DB2: ", db2)