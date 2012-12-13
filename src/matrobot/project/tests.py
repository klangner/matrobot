'''
Created on 13-12-2012

@author: klangner
'''
from matrobot.project.utils import lm
import unittest


class Test(unittest.TestCase):


    def testTrend(self):
        data = []
        data.append({'x': 1, 'y':1})
        data.append({'x': 2, 'y':2})
        data.append({'x': 3, 'y':3})
        data.append({'x': 4, 'y':4})
        data.append({'x': 5, 'y':5})
        data.append({'x': 6, 'y':6})
        trends = lm(data)
        self.assertEquals(1, trends) 


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()