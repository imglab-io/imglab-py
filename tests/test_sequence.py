import unittest
import doctest

from imglab import sequence


class TestSequence(unittest.TestCase):
    def test_default_size(self):
        self.assertEqual(sequence(100, 8192), [100, 134, 180, 241, 324, 434, 583, 781, 1048, 1406, 1886, 2530, 3394, 4553, 6107, 8192])
        self.assertEqual(sequence(8192, 100), [8192, 6107, 4553, 3394, 2530, 1886, 1406, 1048, 781, 583, 434, 324, 241, 180, 134, 100])

    def test_negative_size(self):
        self.assertEqual(sequence(100, 8192, -1), [])
        self.assertEqual(sequence(8192, 100, -1), [])

    def test_zero_size(self):
        self.assertEqual(sequence(100, 8192, 0), [])
        self.assertEqual(sequence(8192, 100, 0), [])

    def test_ascending_order_sequence(self):
        self.assertEqual(sequence(100, 8192, 1), [100])
        self.assertEqual(sequence(100, 8192, 2), [100, 8192])
        self.assertEqual(sequence(100, 8192, 3), [100, 905, 8192])
        self.assertEqual(sequence(100, 8192, 4), [100, 434, 1886, 8192])
        self.assertEqual(sequence(100, 8192, 16), [100, 134, 180, 241, 324, 434, 583, 781, 1048, 1406, 1886, 2530, 3394, 4553, 6107, 8192])
        self.assertEqual(sequence(100, 8192, 32), [100, 115, 133, 153, 177, 204, 235, 270, 312, 359, 414, 477, 550, 634, 731, 843, 972, 1120, 1291, 1488, 1716, 1978, 2280, 2628, 3029, 3492, 4025, 4640, 5348, 6165, 7107, 8192])

    def test_descending_order_sequence(self):
        self.assertEqual(sequence(8192, 100, 1), [8192])
        self.assertEqual(sequence(8192, 100, 2), [8192, 100])
        self.assertEqual(sequence(8192, 100, 3), [8192, 905, 100])
        self.assertEqual(sequence(8192, 100, 4), [8192, 1886, 434, 100])
        self.assertEqual(sequence(8192, 100, 16), [8192, 6107, 4553, 3394, 2530, 1886, 1406, 1048, 781, 583, 434, 324, 241, 180, 134, 100])
        self.assertEqual(sequence(8192, 100, 32), [8192, 7107, 6165, 5348, 4640, 4025, 3492, 3029, 2628, 2280, 1978, 1716, 1488, 1291, 1120, 972, 843, 731, 634, 550, 477, 414, 359, 312, 270, 235, 204, 177, 153, 133, 115, 100])


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite("imglab.sequence"))

    return tests


if __name__ == "__main__":
    unittest.main()
