# -*- coding: utf-8 -*-
'''
Created on 2012-12-01

@author: Krzysztof Langner
'''
def lm(data):
    xy = 0
    x = 0
    y = 0
    x2 = 0
    for sample in data:
        xy += sample['x']*sample['y']
        y += sample['y']
        x += sample['x']
        x2 += sample['x']**2
    slope = (6.0*xy-x*y)/(6.0*x2-x*x)
    return slope
