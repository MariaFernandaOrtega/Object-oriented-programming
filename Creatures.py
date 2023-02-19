# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:02:49 2023

@author: Maria Fernanda Ortega
"""

from abc import ABCMeta, abstractmethod
import random

class Creature(metaclass=ABCMeta):
    def method(self):
        return 'This object is a  ' + self
  
        
class Bear(Creature):
    def method(self):
        return 'This object is a  ' + self

        
class Fish(Creature):
    def method(self):
        return 'This object is a  ' + self

