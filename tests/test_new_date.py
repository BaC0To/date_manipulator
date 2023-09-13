import unittest
from date_modify import is_date_iso_format, offset_date_with_days

offset = 2


class TestNewIsoDate(unittest.TestCase):

    def test_if_date_iso_formatted(self):
        #2023-09-13
        test_date = offset_date_with_days(offset)
        self.assertTrue(is_date_iso_format(test_date))


if __name__ == '__main__':
    unittest.main()