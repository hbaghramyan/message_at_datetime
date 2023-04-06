import unittest
from functions import *

strd = "%d.%m.%Y" # string variable for date formate
strt = "%H:%M:%S" # string variable for time formate

cases_valid = [["23:10:55", strt, True], ["23:10:5", strt, False], 
               ["23:10:55", strd, False], ["04.08.2022", strd, True],
               ["04.08.202", strd, False], ["04.08.202", strt, False]]

class TestValid(unittest.TestCase):

    def test_valid(self):
        for cases_v in cases_valid:
            self.assertEqual(validate(cases_v[0], cases_v[1]), cases_v[2], f"Should be {cases_v[2]}")

if __name__ == '__main__':
    unittest.main()