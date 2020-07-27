#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 13:10:03 2020

@author: fuhr
"""

class Singleton(object):
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
    
s = Singleton()
print("Obj created", s)

s1 = Singleton()
print("Obj created", s1)        