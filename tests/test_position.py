import unittest
import doctest

from imglab import position


class TestPosition(unittest.TestCase):
    def test_single_position(self):
        self.assertEqual(position("left"), "left")
        self.assertEqual(position("center"), "center")
        self.assertEqual(position("right"), "right")

        self.assertEqual(position("top"), "top")
        self.assertEqual(position("middle"), "middle")
        self.assertEqual(position("bottom"), "bottom")

    def test_horizontal_vertical_position(self):
        self.assertEqual(position("left", "top"), "left,top")
        self.assertEqual(position("left", "middle"), "left,middle")
        self.assertEqual(position("left", "bottom"), "left,bottom")

        self.assertEqual(position("center", "top"), "center,top")
        self.assertEqual(position("center", "middle"), "center,middle")
        self.assertEqual(position("center", "bottom"), "center,bottom")

        self.assertEqual(position("right", "top"), "right,top")
        self.assertEqual(position("right", "middle"), "right,middle")
        self.assertEqual(position("right", "bottom"), "right,bottom")

    def test_vertical_horizontal_position(self):
        self.assertEqual(position("top", "left"), "top,left")
        self.assertEqual(position("top", "center"), "top,center")
        self.assertEqual(position("top", "right"), "top,right")

        self.assertEqual(position("middle", "left"), "middle,left")
        self.assertEqual(position("middle", "center"), "middle,center")
        self.assertEqual(position("middle", "right"), "middle,right")

        self.assertEqual(position("bottom", "left"), "bottom,left")
        self.assertEqual(position("bottom", "center"), "bottom,center")
        self.assertEqual(position("bottom", "right"), "bottom,right")

    def test_invalid_single_position(self):
        with self.assertRaises(ValueError):
            position("lefts")
        with self.assertRaises(ValueError):
            position("rights")

    def test_invalid_horizontal_vertical_position(self):
        with self.assertRaises(ValueError):
            position("left", "left")
        with self.assertRaises(ValueError):
            position("left", "center")
        with self.assertRaises(ValueError):
            position("left", "right")

        with self.assertRaises(ValueError):
            position("center", "center")
        with self.assertRaises(ValueError):
            position("center", "left")
        with self.assertRaises(ValueError):
            position("center", "right")

        with self.assertRaises(ValueError):
            position("right", "right")
        with self.assertRaises(ValueError):
            position("right", "left")
        with self.assertRaises(ValueError):
            position("right", "center")

        with self.assertRaises(ValueError):
            position("top", "top")
        with self.assertRaises(ValueError):
            position("top", "middle")
        with self.assertRaises(ValueError):
            position("top", "bottom")

        with self.assertRaises(ValueError):
            position("middle", "middle")
        with self.assertRaises(ValueError):
            position("middle", "top")
        with self.assertRaises(ValueError):
            position("middle", "bottom")

        with self.assertRaises(ValueError):
            position("bottom", "bottom")
        with self.assertRaises(ValueError):
            position("bottom", "top")
        with self.assertRaises(ValueError):
            position("bottom", "middle")


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite("imglab.position"))

    return tests


if __name__ == "__main__":
    unittest.main()
