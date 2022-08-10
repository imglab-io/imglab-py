import unittest
import doctest

from imglab import Source


class TestSource(unittest.TestCase):
    def test_source_instance_with_default_values(self):
        source = Source("assets")

        self.assertEqual(source.host, "assets.%s" % Source.DEFAULT_HOST)
        self.assertEqual(source.https, Source.DEFAULT_HTTPS)
        self.assertEqual(source.name, "assets")
        self.assertEqual(source.port, None)
        self.assertEqual(source.secure_key, None)
        self.assertEqual(source.secure_salt, None)
        self.assertEqual(source.subdomains, Source.DEFAULT_SUBDOMAINS)

    def test_source_instance_with_expected_optional_values(self):
        self.assertEqual(Source("assets", host="imglab.net").host, "assets.imglab.net")
        self.assertEqual(Source("assets", https=False).https, False)
        self.assertEqual(Source("assets", port=8080).port, 8080)
        self.assertEqual(Source("assets", secure_key="secure-key").secure_key, "secure-key")
        self.assertEqual(Source("assets", secure_salt="secure-salt").secure_salt, "secure-salt")
        self.assertEqual(Source("assets", subdomains=False).subdomains, False)

    def test_scheme(self):
        self.assertEqual(Source("assets").scheme(), "https")
        self.assertEqual(Source("assets", https=True).scheme(), "https")
        self.assertEqual(Source("assets", https=False).scheme(), "http")

    def test_host(self):
        self.assertEqual(Source("assets").host, "assets.imglab-cdn.net")
        self.assertEqual(Source("assets", subdomains=False).host, "imglab-cdn.net")
        self.assertEqual(Source("assets", subdomains=False, host="imglab.net").host, "imglab.net")
        self.assertEqual(Source("assets", subdomains=True).host, "assets.imglab-cdn.net")
        self.assertEqual(Source("assets", subdomains=True, host="imglab.net").host, "assets.imglab.net")

    def test_path(self):
        self.assertEqual(Source("assets").path("example.jpeg"), "example.jpeg")
        self.assertEqual(Source("assets").path("subfolder/example.jpeg"), "subfolder/example.jpeg")
        self.assertEqual(Source("assets", subdomains=False).path("example.jpeg"), "assets/example.jpeg")
        self.assertEqual(Source("assets", subdomains=False).path("subfolder/example.jpeg"), "assets/subfolder/example.jpeg")
        self.assertEqual(Source("assets", subdomains=True).path("example.jpeg"), "example.jpeg")
        self.assertEqual(Source("assets", subdomains=True).path("subfolder/example.jpeg"), "subfolder/example.jpeg")

    def test_is_secure(self):
        self.assertEqual(Source("assets").is_secure(), False)
        self.assertEqual(Source("assets", secure_key="secure-key").is_secure(), False)
        self.assertEqual(Source("assets", secure_salt="secure-salt").is_secure(), False)
        self.assertEqual(Source("assets", secure_key="secure-key", secure_salt="secure-salt").is_secure(), True)


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite("imglab.source"))

    return tests


if __name__ == "__main__":
    unittest.main()
