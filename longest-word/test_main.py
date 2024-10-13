from unittest.mock import patch
from unittest import TestCase
import unittest
import sys
import io

class Test(TestCase):
    @patch('builtins.input', side_effect=["a", "bb", "ccc", "dddd", "eeeee"])
    @patch('builtins.print')
    def test_output(self, mock_print, mock_input):
        import main
        try:
            mock_print.assert_called_with("eeeee")
        finally:
            sys.modules.pop('main')

    @patch('builtins.input', side_effect=["bb", "eeeee", "dddd", "ffffff", "a"])
    @patch('builtins.print')
    def test_shuffled_order(self, mock_print, mock_input):
        import main
        try:
            mock_print.assert_called_with("ffffff")
        finally:
            sys.modules.pop('main')

    @patch('builtins.input', side_effect=["Giraffe", "Hippo", "Lion", "Dog", "Cat"])
    @patch('builtins.print')
    def test_animals(self, mock_print, mock_input):
        import main
        try:
            mock_print.assert_called_with("Giraffe")
        finally:
            sys.modules.pop('main')

if __name__ == '__main__':
    unittest.main()
