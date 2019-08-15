#import unittest
from unittest import TestSuite as ts
from unittest import TextTestRunner as ttr
from test_module import test_module as tm

if __name__ == '__main__':
    #suite = unittest.TestSuite()
    suite = ts()
    #suite.addTest(test_module('test_LastBootUpTime'))

    #suite.addTest(test_module('test_GetMonthToDay'))
    suite.addTest(tm('test_GetMonthToDay'))
    #runner = unittest.TextTestRunner(verbosity=3)
    runner = ttr(verbosity=3)
    runner.run(suite)