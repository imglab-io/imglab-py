import unittest
import doctest

from imglab import color


class TestColor(unittest.TestCase):
    def test_rgb_colors(self):
        self.assertEqual(color(255, 0, 0), "255,0,0")
        self.assertEqual(color(0, 255, 0), "0,255,0")
        self.assertEqual(color(0, 0, 255), "0,0,255")

        self.assertEqual(color(0, 255, 255), "0,255,255")
        self.assertEqual(color(255, 0, 255), "255,0,255")
        self.assertEqual(color(255, 255, 0), "255,255,0")

        self.assertEqual(color(0, 0, 0), "0,0,0")
        self.assertEqual(color(255, 255, 255), "255,255,255")
        self.assertEqual(color(1, 2, 3), "1,2,3")

    def test_rgba_colors(self):
        self.assertEqual(color(255, 0, 0, 0), "255,0,0,0")
        self.assertEqual(color(0, 255, 0, 0), "0,255,0,0")
        self.assertEqual(color(0, 0, 255, 0), "0,0,255,0")
        self.assertEqual(color(0, 0, 0, 255), "0,0,0,255")

        self.assertEqual(color(0, 255, 255, 255), "0,255,255,255")
        self.assertEqual(color(255, 0, 255, 255), "255,0,255,255")
        self.assertEqual(color(255, 255, 0, 255), "255,255,0,255")
        self.assertEqual(color(255, 255, 255, 0), "255,255,255,0")

        self.assertEqual(color(0, 0, 0, 0), "0,0,0,0")
        self.assertEqual(color(255, 255, 255, 255), "255,255,255,255")
        self.assertEqual(color(1, 2, 3, 4), "1,2,3,4")

    def test_named_colors(self):
        self.assertEqual(color("blue"), "blue")
        self.assertEqual(color("black"), "black")
        self.assertEqual(color("white"), "white")

    def test_invalid_rgb_colors(self):
        with self.assertRaises(ValueError):
            color(-1, 255, 255)
        with self.assertRaises(ValueError):
            color(255, -1, 255)
        with self.assertRaises(ValueError):
            color(255, 255, -1)

        with self.assertRaises(ValueError):
            color(256, 255, 255)
        with self.assertRaises(ValueError):
            color(255, 256, 255)
        with self.assertRaises(ValueError):
            color(255, 255, 256)

        with self.assertRaises(ValueError):
            color("255", 255, 255)
        with self.assertRaises(ValueError):
            color(255, "255", 255)
        with self.assertRaises(ValueError):
            color(255, 255, "255")

    def test_invalid_rgba_colors(self):
        with self.assertRaises(ValueError):
            color(-1, 255, 255, 255)
        with self.assertRaises(ValueError):
            color(255, -1, 255, 255)
        with self.assertRaises(ValueError):
            color(255, 255, -1, 255)
        with self.assertRaises(ValueError):
            color(255, 255, 255, -1)

        with self.assertRaises(ValueError):
            color(256, 255, 255, 255)
        with self.assertRaises(ValueError):
            color(255, 256, 255, 255)
        with self.assertRaises(ValueError):
            color(255, 255, 256, 255)
        with self.assertRaises(ValueError):
            color(255, 255, 255, 256)

        with self.assertRaises(ValueError):
            color("255", 255, 255, 255)
        with self.assertRaises(ValueError):
            color(255, "255", 255, 255)
        with self.assertRaises(ValueError):
            color(255, 255, "255", 255)
        with self.assertRaises(ValueError):
            color(255, 255, 255, "255")

    def test_invalid_named_colors(self):
        with self.assertRaises(ValueError):
            color("Blue")
        with self.assertRaises(ValueError):
            color("Red")
        with self.assertRaises(ValueError):
            color("blues")
        with self.assertRaises(ValueError):
            color("reds")


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite("imglab.color"))

    return tests


if __name__ == "__main__":
    unittest.main()
