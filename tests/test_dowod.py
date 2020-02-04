import unittest
from id.id_card import check_id,get_letter_value

class CkeckIdTests(unittest.TestCase):
    def test_validate(self):
        self.assertTrue(check_id('LOC768734'))

if __name__ == "__main__":
    unittest.main()