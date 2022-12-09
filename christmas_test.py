import unittest
from ChristmasCarol import generateSingle


class ChristmasTest(unittest.TestCase):
    def test_first_werse(self):
        self.assertEqual(generateSingle(1),
                         "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree")

    def test_second_day(self):
        self.assertEqual(generateSingle(2),
                         "On the second day of Christmas my true love gave to me: two Turtle Doves, " +
                         "and a Partridge in a Pear Tree.")

    def test_third_day(self):
        self.assertEqual(generateSingle(3),
                         "On the third day of Christmas my true love gave to me: three French Hens, " +
                         "two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_fourth_day(self):
        self.assertEqual(generateSingle(4),
                         "On the fourth day of Christmas my true love gave to me: four Calling Birds," +
                         " three French Hens, " +
                         "two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_fifth_day(self):
        self.assertEqual(generateSingle(5),
                         "On the fifth day of Christmas my true love gave to me: five Gold Rings, " +
                         "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_eleven_day(self):
        self.assertEqual(generateSingle(11),
                         "On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping," +
                         " ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming," +
                         " six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens," +
                         " two Turtle Doves, and a Partridge in a Pear Tree.")
