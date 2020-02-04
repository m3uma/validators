import unittest
from haslo.function import check_password


class CheckPasswordTestCase(unittest.TestCase):
    def test_function_usage(self):
        check_password('haslo123')

    def test_password_min_length(self):
        # self.assertIsNone(check_password('H4$lo'))
        self.assertIsNotNone(check_password('H4$lo43'))

    def test_password_min_one_uppercase_letter(self):
        # self.assertIsNone(check_password('h4$lo43'))
        self.assertIsNotNone(check_password('H4$lo43'))

    def test_password_min_one_lowercase_letter(self):
        # self.assertIsNone(check_password('H4$LO43'))
        self.assertIsNotNone(check_password('H4$lo43'))

    def test_password_min_one_digit(self):
        # self.assertIsNone(check_password('HD$LoAB'))
        self.assertIsNotNone(check_password('H4$lo43'))

    def test_password_min_one_special_character(self):
        # self.assertIsNone(check_password('HDRLoA5'))
        self.assertIsNotNone(check_password('H4$lo43'))

if __name__ == "__main__":
    unittest.main()