#import unittest
from unittest import TestSuite as ts
from unittest import TextTestRunner as ttr
from test_case import test_reverse as tr

if __name__ == '__main__':
    suite = ts()
    suite.addTest(tr('test_positive'))
    suite.addTest(tr('test_minus'))
    suite.addTest(tr('test_overflow'))

    runner = ttr(verbosity=3)
    runner.run(suite)