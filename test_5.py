import csv
import unittest
import Project_02 as cli
import requests

class TestMethods(unittest.TestCase):

    def test_cli(self):
        self.assertEqual(cli.no_flags("text_1"),{'a': 2, 'b': 2, 'c': 2, 'd': 2})
        self.assertEqual(cli.alpha("text_1"), {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0})
        self.assertEqual(cli.capital_letters("text_1"), {'A': 2, 'b': 2, 'C': 1, 'c': 1, 'd': 1, 'D': 1})

if __name__ == '__main__':
    unittest.main()
