import unittest
import doctest
from urllib.parse import urlencode

from imglab import signature, Source


class TestSignature(unittest.TestCase):
    SECURE_KEY = "ixUd9is/LDGBw6NPfLCGLjO/WraJlHdytC1+xiIFj22mXAWs/6R6ws4gxSXbDcUHMHv0G+oiTgyfMVsRS2b3"
    SECURE_SALT = "c9G9eYKCeWen7vkEyV1cnr4MZkfLI/yo6j72JItzKHjMGDNZKqPFzRtup//qiT51HKGJrAha6Gv2huSFLwJr"

    def setUp(self):
        self.source = Source("assets", secure_key=self.SECURE_KEY, secure_salt=self.SECURE_SALT)

    def test_generate_with_encoded_params(self):
        sig = signature.generate(self.source, "example.jpeg", urlencode({"width": 200, "height": 300, "format": "png"}))

        self.assertEqual(sig, "VJ159IlBl_AlN59QWvyJov5SlQXlrZNpXgDJLJgzP8g")

    def test_generate_without_encoded_params(self):
        sig = signature.generate(self.source, "example.jpeg")

        self.assertEqual(sig, "aRgmnJ-7b2A0QLxXpR3cqrHVYmCfpRCOglL-nsp7SdQ")


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite("imglab.signature"))

    return tests


if __name__ == "__main__":
    unittest.main()
