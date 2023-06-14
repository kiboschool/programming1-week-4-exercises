from unittest.mock import patch
from unittest import TestCase
import unittest
import sys
import io

from gradescope_utils.autograder_utils.decorators import weight

class Test(TestCase):
    @patch('builtins.print')
    @weight(1)
    def test_output(self, mock_print):
        import main
        self.assertAlmostEqual(mock_print.call_args[0][0], 39.903, 3)
        sys.modules.pop('main')

if __name__ == '__main__':
    unittest.main()
