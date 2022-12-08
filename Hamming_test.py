import unittest

from Hamming import hamming


class HammingTest(unittest.TestCase):
    def test_empty_strands(self):
        self.assertEqual(self.hamming.distance("", ""), 0)

    def test_single_letter_identical_strands(self):
        self.assertEqual(self.hamming.distance("A", "A"), 0)

    def test_single_letter_different_strands(self):
        self.assertEqual(self.hamming.distance("G", "T"), 1)


    def test_long_identical_strands(self):
        self.assertEqual(self.hamming.distance("GGACTGAAATCTG", "GGACTGAAATCTG"), 0)

    def test_long_different_strands(self):
        self.assertEqual(self.hamming.distance("GGACGGATTCTG", "AGGACGGATTCT"), 9)

    @unittest.skip
    def test_disallow_first_strand_longer(self):
        with self.assertRaisesWithMessage(ValueError):
            self.hamming.distance("AATG", "AAA")

    @unittest.skip
    def test_disallow_second_strand_longer(self):
        with self.assertRaisesWithMessage(ValueError):
            self.hamming.distance("ATA", "AGTG")

    @unittest.skip
    def test_disallow_left_empty_strand(self):
        with self.assertRaisesWithMessage(ValueError):
            self.hamming.distance("", "G")

    @unittest.skip
    def test_disallow_right_empty_strand(self):
        with self.assertRaisesWithMessage(ValueError):
            self.hamming.distance("G", "")

    # Utility functions
    def setUp(self):
        self.hamming = hamming()
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")
