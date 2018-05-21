# -*- coding: utf-8 -*-

class Curves:
    def __init__(self,name):
	''' Constructor for this class. '''
        self.curves = [name,`1`]

    def printCurves(self):
        for curve in self.curves:
            print('%s' % curve)