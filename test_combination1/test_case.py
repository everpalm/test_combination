from unittest import TestLoader as tl
from unittest import TextTestRunner as ttr
from unittest import TestCase as tc
from unittest import mock

from leetcode import Solution as sl
import subprocess

#class test_module(unittest.TestCase):
class test_two_sum(tc):
    """description of class"""
    # This is test version
    # 7 elements stnad for 7 items of different price, choose two of them from these 7 items with 10 dollars

    def test_brute_force(self):
        self.assertEqual(sl().TwoSumBrute([1,3,5,7], 10), [1,3])
    
    def test_two_sum_improve(self):
        self.assertEqual(sl().TwoSumImprove([1,3,5,7], 10), [1,3])

    #@mock.patch('test_combination1.append_list_10')
    #def test_append_sample(self, mock_append_list_10):
     #   mock_append_list_10.return_value = True
     #   self.assertEqual(append_sample([],[1,2],1,1), [[1,2]])
     #   mock_append_list_10.return_value = False
     #   self.assertEqual(append_sample([],[1,2],1,1), [])

class test_call_windows_bat(tc):
    def test_call_windows_bat(self):
        self.assertEqual(sl().CallWindowsBat(), 1)

    def test_call_windows_bat1(self):
        self.assertEqual(sl().CallWindowsBat1(), 0)

    def test_LastBootUpTime(self):
        self.assertEqual(subprocess.call(["LastBootUpTime.bat","0"]),0)

    def test_GetMonthToDay(self):
        self.assertEqual(subprocess.call(['GetMonthToday.bat','2019','8','0']),0)

class test_reverse(tc):
    def test_positive(self):
        self.assertEqual(sl().reverse(123), 321)

    def test_minus(self):
        self.assertEqual(sl().reverse(-123), -321)

    def test_overflow(self):
        self.assertEqual(sl().reverse(2**31), 0)
        self.assertEqual(sl().reverse(-2**31+1), 0)

class test_reverseInPlace(tc):
    def test_positive(self):
        self.assertEqual(sl().reverseInPlace(123), 321)

    def test_minus(self):
        self.assertEqual(sl().reverseInPlace(-123), -321)

    def test_overflow(self):
        self.assertEqual(sl().reverseInPlace(2**31), 0)
        self.assertEqual(sl().reverseInPlace(-2**31+1), 0)

if __name__ == "__main__":
    #unittest.TextTestRunner(verbosity=3).run(unittest.TestLoader().loadTestsFromTestCase(test_module))
    runner = ttr(verbosity=3)
    runner.run(tl().loadTestsFromTestCase(test_reverseInPlace))

