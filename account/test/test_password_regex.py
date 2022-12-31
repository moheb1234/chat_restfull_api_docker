from django.test import TestCase
from rest_framework.exceptions import ValidationError

from account.password_regex import password_re


class TestPasswordRegex(TestCase):
    def test_short_password(self):
        with self.assertRaises(ValidationError) as error:
            password_re('Pass12!')
        self.assertEqual(error.exception.args[0], 'password must be at least 8 characters')

    def test_password_not_include_uppercase(self):
        with self.assertRaises(ValidationError) as error:
            password_re('pass12!31')
        self.assertEqual(error.exception.args[0], 'password must be contains at least one uppercase')

    def test_password_not_include_lowercase(self):
        with self.assertRaises(ValidationError) as error:
            password_re('PASS12!31')
        self.assertEqual(error.exception.args[0], 'password must be contains at least one lowercase')

    def test_password_not_contains_digits(self):
        with self.assertRaises(ValidationError) as error:
            password_re('Password@')
        self.assertEqual(error.exception.args[0], 'password must be contains at least one digit')

    def test_password_not_contains_special_character(self):
        with self.assertRaises(ValidationError) as error:
            password_re('Password12')
        self.assertEqual(error.exception.args[0], 'password must be contains at least one special character')

    def test_password_contains_space(self):
        with self.assertRaises(ValidationError) as error:
            password_re('Pass word23@')
        self.assertEqual(error.exception.args[0], 'password must not be contains space')

    def test_valid_password(self):
        password = password_re('Password@56')
        self.assertEqual(password, 'Password@56')
