from unittest.mock import patch
from unittest import TestCase
import unittest
import sys
import io

from gradescope_utils.autograder_utils.decorators import weight

class Test(TestCase):
    @patch('builtins.input', return_value="1")
    @weight(10)
    def test_lion(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            import main
            try:
                lines = mock_stdout.getvalue().split("\n")
                self.assertEqual(lines[7], "The lion (Panthera leo) is a large mammal of the Felidae (cat) family. Some large males weigh over 250 kg (550 lb). Today, wild lions live in sub-Saharan Africa and in Asia. Lions are adapted for life in grasslands and mixed areas with trees and grass. The relatively small females are fast runners over short distances, and coordinate their hunting of herd animals.")
            finally:
                sys.modules.pop('main')

    @patch('builtins.input', return_value="5")
    @weight(10)
    def test_buffalo(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            import main
            try:
                lines = mock_stdout.getvalue().split("\n")
                self.assertEqual(lines[7], 
  "The African buffalo (Syncerus caffer) is a large sub-Saharan African bovine. Syncerus caffer caffer, the Cape buffalo, is the typical subspecies, and the largest one, found in Southern and East Africa. S. c. nanus (the forest buffalo) is the smallest subspecies, common in forest areas of Central and West Africa, while S. c. brachyceros is in West Africa and S. c. aequinoctialis is in the savannas of East Africa. The adult African buffalo's horns are its characteristic feature: they have fused bases, forming a continuous bone shield across the top of the head referred to as a 'boss'. It is widely regarded as one of the most dangerous animals on the African continent, and according to some estimates it gores, tramples, and kills over 200 people every year.")
            finally:
                sys.modules.pop('main')

    @patch('builtins.input', return_value="3")
    @weight(10)
    def test_leopard(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            import main
            try:
                lines = mock_stdout.getvalue().split("\n")
                self.assertEqual(lines[7], 
  "The African leopard (Panthera pardus pardus) is the nominate subspecies of the leopard, native to many countries in Africa. It is widely distributed in most of sub-Saharan Africa, but the historical range has been fragmented in the course of habitat conversion. Leopards have also been recorded in North Africa as well.")
            finally:
                sys.modules.pop('main')


if __name__ == '__main__':
    unittest.main()
