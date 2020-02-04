import unittest
from mail.mailvalid import validate_mail

class ValidateMailTests(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(validate_mail('ania@hotmail.com'))
    # def test_validate2(self):
    #     self.assertTrue(validate_mail('aniahotmail.com'))
    # def test_validate3(self):
    #     self.assertTrue(validate_mail('ania@hotmailcom'))

if __name__ == "__main__":
    unittest.main()
