import unittest
from unittest import mock
from test_combination1 import Solution as sl

class test_module(unittest.TestCase):
    """description of class"""
    # This is test version
    # 7 elements stnad for 7 items of different price, choose two of them from these 7 items with 10 dollars

    def test_two_sum(self):
        self.assertEqual(sl().TwoSumBrute([1,3,5,7], 10), [1,3])
    
    def test_two_sum_improve(self):
        self.assertEqual(sl().TwoSumImprove([1,3,5,7], 10), [1,3])
    #@mock.patch('test_combination1.append_list_10')
    #def test_append_sample(self, mock_append_list_10):
     #   mock_append_list_10.return_value = True
     #   self.assertEqual(append_sample([],[1,2],1,1), [[1,2]])
     #   mock_append_list_10.return_value = False
     #   self.assertEqual(append_sample([],[1,2],1,1), [])

    def test_call_windows_bat(self):
        self.assertEqual(sl().CallWindowsBat(), 1)

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=3).run(unittest.TestLoader().loadTestsFromTestCase(test_module))


