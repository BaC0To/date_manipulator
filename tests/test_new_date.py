import unittest
from date_modify import offset_date_with_days, is_date_correct
import random


class TestNewIsoDate(unittest.TestCase):

    def test_if_date_valid(self):
        #2023-09-13
        offset = random.randint(-999, 999)
        print(f"Random offset to be used: {offset}")
        test_date = offset_date_with_days(offset)
        self.assertTrue(is_date_correct(test_date))

    def test_if_date_invalid(self):
        #2023-02-33
        test_date = "2023-02-33" 
        self.assertFalse(is_date_correct(test_date))



if __name__ == '__main__':
    unittest.main()