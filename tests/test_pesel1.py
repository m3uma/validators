import unittest
from pesel.functions import analyze_pesel
import datetime

class AnalyzePeselTests(unittest.TestCase):
    def test_validate(self):
        self.assertTrue(analyze_pesel('03211949001')['valid'])
    def test_valid(self):
        self.assertTrue(analyze_pesel('04302142693')['valid'])
    def test_valid_female(self):
        self.assertEqual(analyze_pesel('03211949001')['gender'], 'female')
    def test_valid_male(self):
        self.assertEqual(analyze_pesel('04302142693')['gender'], 'male')
    def test_pesel1(self):
        self.assertEqual(analyze_pesel('03211949001')['pesel'], '03211949001')
    def test_pesel2(self):
        self.assertEqual(analyze_pesel('04302142693')['pesel'], '04302142693')
    def test_validate_birth_date(self):
        self.assertEqual(analyze_pesel('04302142693')['birth_date'], datetime.datetime(2004, 10, 21))

if __name__ == "__main__":
    unittest.main()