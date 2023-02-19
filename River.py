# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:04:03 2023

@author: Maria Fernanda Ortega
"""
from Creatures import Bear
from Creatures import Fish

import random

class River:

    def __init__(self, n_room):
        self._n_room = n_room
        self._eco = []
        for i in range(self._n_room):
            n_value = random.randint(1, 3)
            if n_value == 1:
                self._eco.append(Bear())
            elif n_value == 2:
                self._eco.append(Fish())
            else:
                self._eco.append(None)

    def __len__(self):
        return self._n_room


    def count_none(self):
        return self._eco.count(None)

    def add_random(self, Creature):
        if self.count_none() > 0:
            choices = [i for i, x in enumerate(self._eco) if x == None]
            index = random.choice(choices)
            self._eco[index] = Creature

    def update_cell(self, i):
        if self._eco[i] != None:
            move = random.randint(-1, 1)
            if move != 0 and 0 <= i + move < self._n_room:
                if self._eco[i + move] == None:
                    self._eco[i + move] = self._eco[i]
                    self._eco[i] = None
                elif type(self._eco[i]) == type(self._eco[i + move]):
                        if type(self._eco[i]) == Bear:
                            self.add_random(Bear())
                        else:
                            self.add_random(Fish())
                else:
                    if type(self._eco[i]) == Bear:
                        self._eco[i + move] = self._eco[i]
                    self._eco[i] = None

    def update_river(self):
        for i in range(len(self._eco)):
            self.update_cell(i)

    def display(self):
        s = '|'
        for x in self._eco:
            if x:
                if type(x) == Bear:
                    s += 'B'
                elif type(x) == Fish:
                    s += 'F'
            else:
                s += 'N'
            s += '|'
        print(s)

river = River(5)
river.display()
river.update_river()




