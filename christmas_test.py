import unittest
from ChristmasCarol import generateSingle


class ChristmasTest(unittest.TestCase):
    def test_first_werse(self):
        self.assertEqual(generateSingle(1), "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree")