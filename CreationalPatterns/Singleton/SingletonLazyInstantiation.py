#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 13:12:59 2020

@author: fuhr
"""

"""This singleton class should be used for modules."""

class Singleton:
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print("__init__ method called")
        else:
            print("Instance already created:", self.getInstance())
    
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

s = Singleton()
print("Object created", Singleton.getInstance())
s1 = Singleton()