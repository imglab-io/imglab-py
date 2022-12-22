import unittest
import doctest

from imglab.utils import srcset as utils


class TestSrcsetUtils(unittest.TestCase):
    def test_normalize_params(self):
        self.assertEqual(utils.normalize_params({}), {})
        self.assertEqual(utils.normalize_params({"dpr": []}), {})
        self.assertEqual(utils.normalize_params({"dpr": [], "width": []}), {})

        self.assertEqual(
            utils.normalize_params({"blur": 100, "dpr": [], "width": [], "format": "png"}),
            {"blur": 100, "format": "png"}
        )
        self.assertEqual(
            utils.normalize_params({"blur": 100, "dpr": 1, "width": 100, "format": "png"}),
            {"blur": 100, "dpr": 1, "width": 100, "format": "png"}
        )
        self.assertEqual(
            utils.normalize_params({"blur": 100, "dpr": [1, 2, 3], "width": [100, 200, 300], "format": "png"}),
            {"blur": 100, "dpr": [1, 2, 3], "width": [100, 200, 300], "format": "png"}
        )
        self.assertEqual(
            utils.normalize_params({"blur": 100, "dpr": range(1, 3), "width": range(100, 300), "format": "png"}),
            {"blur": 100, "dpr": range(1, 3), "width": range(100, 300), "format": "png"}
        )

    def test_split_params_dpr(self):
        self.assertEqual(
            utils.split_params_dpr({"width": 100, "dpr": [1, 2], "format": "png"}),
            [
                {"width": 100, "dpr": 1, "format": "png"},
                {"width": 100, "dpr": 2, "format": "png"}
            ]
        )
        self.assertEqual(
            utils.split_params_dpr({"width": 100, "dpr": [1, 2], "quality": [75], "format": "png"}),
            [
                {"width": 100, "dpr": 1, "quality": 75, "format": "png"},
                {"width": 100, "dpr": 2, "quality": None, "format": "png"}
            ]
        )
        self.assertEqual(
            utils.split_params_dpr({"width": 100, "dpr": [1, 2], "quality": [75, 40], "format": "png"}),
            [
                {"width": 100, "dpr": 1, "quality": 75, "format": "png"},
                {"width": 100, "dpr": 2, "quality": 40, "format": "png"}
            ]
        )
        self.assertEqual(
            utils.split_params_dpr({"width": 100, "dpr": range(1, 2), "format": "png"}),
            [
                {"width": 100, "dpr": 1, "format": "png"},
                {"width": 100, "dpr": 2, "format": "png"}
            ]
        )
        self.assertEqual(
            utils.split_params_dpr({"width": 100, "dpr": range(1, 2), "quality": [75], "format": "png"}),
            [
                {"width": 100, "dpr": 1, "quality": 75, "format": "png"},
                {"width": 100, "dpr": 2, "quality": None, "format": "png"}
            ]
        )
        self.assertEqual(
            utils.split_params_dpr({"width": 100, "dpr": range(1, 2), "quality": range(75, 40), "format": "png"}),
            [
                {"width": 100, "dpr": 1, "quality": 75, "format": "png"},
                {"width": 100, "dpr": 2, "quality": 40, "format": "png"}
            ]
        )

    def test_split_params_width(self):
        self.assertEqual(
            utils.split_params_width({"width": [100, 200], "format": "png"}),
            [
                {"width": 100, "format": "png"},
                {"width": 200, "format": "png"}
            ]
        )
        self.assertEqual(
            utils.split_params_width({"width": [100, 200], "height": [300], "quality": [75], "format": "png"}),
            [
                {"width": 100, "height": 300, "quality": 75, "format": "png"},
                {"width": 200, "height": None, "quality": None, "format": "png"}
            ]
        )
        self.assertEqual(
            utils.split_params_width({"width": range(100, 200), "format": "png"}),
            [
                {"width": 100, "format": "png"},
                {"width": 105, "format": "png"},
                {"width": 110, "format": "png"},
                {"width": 115, "format": "png"},
                {"width": 120, "format": "png"},
                {"width": 126, "format": "png"},
                {"width": 132, "format": "png"},
                {"width": 138, "format": "png"},
                {"width": 145, "format": "png"},
                {"width": 152, "format": "png"},
                {"width": 159, "format": "png"},
                {"width": 166, "format": "png"},
                {"width": 174, "format": "png"},
                {"width": 182, "format": "png"},
                {"width": 191, "format": "png"},
                {"width": 200, "format": "png"}
            ]
        )
        self.assertEqual(
            utils.split_params_width({"width": range(100, 200), "height": [300], "quality": [75], "format": "png"}),
            [
                {"width": 100, "height": 300, "quality": 75, "format": "png"},
                {"width": 105, "height": None, "quality": None, "format": "png"},
                {"width": 110, "height": None, "quality": None, "format": "png"},
                {"width": 115, "height": None, "quality": None, "format": "png"},
                {"width": 120, "height": None, "quality": None, "format": "png"},
                {"width": 126, "height": None, "quality": None, "format": "png"},
                {"width": 132, "height": None, "quality": None, "format": "png"},
                {"width": 138, "height": None, "quality": None, "format": "png"},
                {"width": 145, "height": None, "quality": None, "format": "png"},
                {"width": 152, "height": None, "quality": None, "format": "png"},
                {"width": 159, "height": None, "quality": None, "format": "png"},
                {"width": 166, "height": None, "quality": None, "format": "png"},
                {"width": 174, "height": None, "quality": None, "format": "png"},
                {"width": 182, "height": None, "quality": None, "format": "png"},
                {"width": 191, "height": None, "quality": None, "format": "png"},
                {"width": 200, "height": None, "quality": None, "format": "png"}
            ]
        )
        self.assertEqual(
            utils.split_params_width({"width": range(100, 200), "height": range(300, 500), "quality": range(75, 40), "format": "png"}),
            [
                {"width": 100, "height": 300, "quality": 75, "format": "png"},
                {"width": 105, "height": 310, "quality": 72, "format": "png"},
                {"width": 110, "height": 321, "quality": 69, "format": "png"},
                {"width": 115, "height": 332, "quality": 66, "format": "png"},
                {"width": 120, "height": 344, "quality": 63, "format": "png"},
                {"width": 126, "height": 356, "quality": 61, "format": "png"},
                {"width": 132, "height": 368, "quality": 58, "format": "png"},
                {"width": 138, "height": 381, "quality": 56, "format": "png"},
                {"width": 145, "height": 394, "quality": 54, "format": "png"},
                {"width": 152, "height": 408, "quality": 51, "format": "png"},
                {"width": 159, "height": 422, "quality": 49, "format": "png"},
                {"width": 166, "height": 436, "quality": 47, "format": "png"},
                {"width": 174, "height": 451, "quality": 45, "format": "png"},
                {"width": 182, "height": 467, "quality": 43, "format": "png"},
                {"width": 191, "height": 483, "quality": 42, "format": "png"},
                {"width": 200, "height": 500, "quality": 40, "format": "png"}
            ]
        )


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite("imglab.utils.srcset"))

    return tests


if __name__ == "__main__":
    unittest.main()
