import unittest
from pesel.functions import analyze_pesel

class AnalyzePeselTests(unittest.TestCase):

    def test_validate_pesel(self):
        self.assertTrue(analyze_pesel('03211949001')['valid']), {
        "pesel": "03211949001",
        "valid": True,
        "gender": 'female',
        #"birth_date": datetime.datetime(2003, 01,19)
}

class AnalyzePeselTests2(unittest.TestCase): # wynik: FAILED, gdyż pesel jest błędny
    def test_validate_pesel(self):
        self.assertEqual(analyze_pesel('03211949001'), {
        "pesel": "03211949001",
        "valid": True,
        "gender": 'female',
    })

if __name__ == "__main__":
    unittest.main()