import unittest
from unittest import mock
from test_combination1 import append_list_10, append_sample

class test_module(unittest.TestCase):
    """description of class"""
    def test_append_list_10(self):
        self.assertEqual(append_list_10([],10), True)
        self.assertEqual(append_list_10([],11), False)
    
    @mock.patch('test_combination1.append_list_10')
    def test_append_sample(self, mock_append_list_10):
        mock_append_list_10.return_value = True
        self.assertEqual(append_sample([],[1,2],1,1,1), [[1,2]])
        mock_append_list_10.return_value = False
        self.assertEqual(append_sample([],[1,2],1,1,1), [])

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=3).run(unittest.TestLoader().loadTestsFromTestCase(test_module))


