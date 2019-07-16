import unittest
from test_combination1 import append_list_10

class test_module(unittest.TestCase):
    """description of class"""
    def test_append_list_10(self):
        self.assertEqual(append_list_10([],10), True)
        self.assertEqual(append_list_10([],11), False)

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=3).run(unittest.TestLoader().loadTestsFromTestCase(test_module))


