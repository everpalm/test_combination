#import unittest
from unittest import TestSuite as ts
from unittest import TextTestRunner as ttr
from test_module import test_module as tm

if __name__ == '__main__':
    suite = ts()
    #suite.addTest(tm('test_GetMonthToDay'))
    suite.addTest(tm('test_reverse'))
    suite.addTest(tm('test_reverse_minus'))

    runner = ttr(verbosity=3)
    runner.run(suite)