#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 13:27:32 2020

@author: fuhr
"""

# class MyInt(type):
#     def __call__(cls, *args, **kwds):
#         print("********* Here's My int", args)
#         print("Now do whatever you want with those objects...")
#         return type.__call__(cls, *args, **kwds)
    
# class int(metaclass=MyInt):
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#         self.lol = "a"
    
# i = int(4, 5)
# a = int(4, 5)
# print(hasattr(i, "lol"))
# print(hasattr(i, "__x"))
#print(i.__x + a.__y)

class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton,
                                        cls).__call__(*args, **kwargs)
            return cls._instances[cls]
        
class Logger(metaclass=MetaSingleton):
    pass

logger1 = Logger()
logger2 = Logger()
print(logger1, logger2)