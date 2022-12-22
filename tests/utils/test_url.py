import unittest
import doctest

from time import gmtime
from datetime import datetime

from imglab.utils import url as utils


class TestUrlUtils(unittest.TestCase):
    def test_normalize_path(self):
        self.assertEqual(utils.normalize_path(""), "")
        self.assertEqual(utils.normalize_path("example.jpeg"), "example.jpeg")
        self.assertEqual(utils.normalize_path("/example.jpeg"), "example.jpeg")
        self.assertEqual(utils.normalize_path("//example.jpeg"), "example.jpeg")
        self.assertEqual(utils.normalize_path("example.jpeg/"), "example.jpeg")
        self.assertEqual(utils.normalize_path("example.jpeg//"), "example.jpeg")
        self.assertEqual(utils.normalize_path("/example.jpeg/"), "example.jpeg")
        self.assertEqual(utils.normalize_path("//example.jpeg//"), "example.jpeg")
        self.assertEqual(utils.normalize_path("subfolder/example.jpeg"), "subfolder/example.jpeg")
        self.assertEqual(utils.normalize_path("/subfolder/example.jpeg"), "subfolder/example.jpeg")
        self.assertEqual(utils.normalize_path("//subfolder/example.jpeg"), "subfolder/example.jpeg")
        self.assertEqual(utils.normalize_path("subfolder/example.jpeg/"), "subfolder/example.jpeg")
        self.assertEqual(utils.normalize_path("subfolder/example.jpeg//"), "subfolder/example.jpeg")
        self.assertEqual(utils.normalize_path("/subfolder/example.jpeg/"), "subfolder/example.jpeg")
        self.assertEqual(utils.normalize_path("//subfolder/example.jpeg//"), "subfolder/example.jpeg")

    def test_normalize_params(self):
        self.assertEqual(utils.normalize_params({}), {})
        self.assertEqual(utils.normalize_params({"width": 200, "height": 300}), {"width": 200, "height": 300})
        self.assertEqual(
            utils.normalize_params({"width": 200, "height": 300, "download": None}),
            {"width": 200, "height": 300, "download": ""}
        )
        self.assertEqual(
            utils.normalize_params({"trim": "color", "trim_color": "orange"}),
            {"trim": "color", "trim-color": "orange"},
        )
        self.assertEqual(
            utils.normalize_params({"trim": "color", "trim-color": "orange"}),
            {"trim": "color", "trim-color": "orange"},
        )
        self.assertEqual(
            utils.normalize_params({"width": 200, "expires": 1464096368}),
            {"width": 200, "expires": 1464096368},
        )
        self.assertEqual(
            utils.normalize_params({"width": 200, "expires": "1464096368"}),
            {"width": 200, "expires": "1464096368"},
        )
        self.assertEqual(
            utils.normalize_params({"width": 200, "expires": gmtime(1464096368)}),
            {"width": 200, "expires": 1464096368},
        )
        self.assertEqual(
            utils.normalize_params({"width": 200, "expires": datetime.fromtimestamp(1464096368)}),
            {"width": 200, "expires": 1464096368},
        )

    def test_is_web_uri(self):
        self.assertEqual(utils.is_web_uri("https://assets.com/example.jpeg"), True)
        self.assertEqual(utils.is_web_uri("http://assets.com/example.jpeg"), True)
        self.assertEqual(utils.is_web_uri("HTTPS://assets.com/example.jpeg"), True)
        self.assertEqual(utils.is_web_uri("HTTP://assets.com/example.jpeg"), True)

        self.assertEqual(utils.is_web_uri(""), False)
        self.assertEqual(utils.is_web_uri("example.jpeg"), False)
        self.assertEqual(utils.is_web_uri("/example.jpeg"), False)
        self.assertEqual(utils.is_web_uri("https/example.jpeg"), False)
        self.assertEqual(utils.is_web_uri("http/example.jpeg"), False)
        self.assertEqual(utils.is_web_uri("/https/example.jpeg"), False)
        self.assertEqual(utils.is_web_uri("/http/example.jpeg"), False)


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite("imglab.utils.url"))

    return tests


if __name__ == "__main__":
    unittest.main()
