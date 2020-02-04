import unittest
from adres.adressvalid import check_adress

class CheckAdressTests(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(check_adress('Dluga 2'))
    # def test_validate2(self):
    #      self.assertTrue(check_adress('Dluga'))


if __name__ == "__main__":
    unittest.main()
