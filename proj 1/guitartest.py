import unittest

from guitar import Guitar

class GuitarTest(unittest.TestCase):

    def testDefaults(self):
        guitar = Guitar()
        self.assertEqual(guitar.stringCount, guitar.DEFAULT_STRING_COUNT)
        self.assertEqual(guitar.stringGauge, guitar.DEFAULT_STRING_GAUGE)
        self.assertEqual(guitar.tuning, guitar.DEFAULT_TUNING)
        self.assertEqual(guitar.volume, guitar.DEFAULT_VOLUME)

    def testSetters(self):
        guitar = Guitar()
        guitar.stringCount = 8
        self.assertEqual(guitar.stringCount, 8)
        guitar.stringCount = -1
        self.assertEqual(guitar.stringCount, 0)
        guitar.stringGauge = 2223
        self.assertEqual(guitar.stringGauge, 2223)
        guitar.volume = 5.6
        self.assertEqual(guitar.volume, 5.6)
        guitar.volume = -3.2
        self.assertEqual(guitar.volume, 0)
        guitar.volume = 12
        self.assertEqual(guitar.volume, 10)
        guitar.stringCount = 6
        guitar.tuning = "A# B C D Eb F"
        self.assertEqual(guitar.tuning, "A# B C D Eb F")
        guitar.tuning = "A B C"
        self.assertEqual(guitar.tuning, guitar.DEFAULT_TUNING)
        guitar.tuning = "Z Z Z Z Z Z"
        self.assertEqual(guitar.tuning, guitar.DEFAULT_TUNING)
        guitar.stringCount = 7
        guitar.tuning = "B E A D G B E"
        self.assertEqual(guitar.tuning, "B E A D G B E")


if __name__ == '__main__':
    unittest.main()