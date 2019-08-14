import unittest
from test_module import test_module

if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTest(test_module('test_LastBootUpTime'))

    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite)