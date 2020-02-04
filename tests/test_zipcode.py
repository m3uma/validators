import unittest
from adres.zipvalid import check_zipcode

class CheckZipcodeMailTests(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(check_zipcode('33-100'))
    # def test_validate2(self):
    #     self.assertTrue(check_zipcode('33100'))

if __name__ == "__main__":
    unittest.main()