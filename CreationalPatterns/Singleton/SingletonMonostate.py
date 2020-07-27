#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 13:18:39 2020

@author: fuhr
"""

"""With singleton monostate, the state of all objects is store in the class."""

class Borg:
    __shared_state = {"1": "2"}
    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass
    
b = Borg()
b1 = Borg()
b.x = -2
b.f = 2

print("Borg Object 'b':", b)
print("Borg Object 'b1':", b1)

print("Object State 'b':", b.__dict__)
print("Object State 'b1':", b1.__dict__)
