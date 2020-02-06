import unittest

from guitar import Guitar

class GuitarTest(unittest.TestCase):

    def testDefaults(self):
        guitar = Guitar('Gibson', 'Les Paul')
        self.assertEqual(guitar.pickups, guitar.DEFAULT_PICKUPS)
        self.assertEqual(guitar.stringCount, guitar.DEFAULT_STRING_COUNT)
        self.assertEqual(guitar.stringGauge, guitar.DEFAULT_STRING_GAUGE)
        self.assertEqual(guitar.tuning, guitar.DEFAULT_TUNING)
