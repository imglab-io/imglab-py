import unittest
import doctest

from time import gmtime
from datetime import datetime

import imglab


class TestUrlWithSourceName(unittest.TestCase):
    def test_url_without_params(self):
        url = imglab.url("assets", "example.jpeg")

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg")

    def test_url_with_params(self):
        url = imglab.url("assets", "example.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&format=png")

    def test_url_with_none_params(self):
        url = imglab.url("assets", "example.jpeg", width=200, download=None)

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&download=")

    def test_url_with_params_using_string_path(self):
        url = imglab.url("assets", "example.jpeg", width=200, height=300, watermark="example.svg", format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&watermark=example.svg&format=png")

    def test_url_with_params_using_string_path_with_inline_params(self):
        url = imglab.url("assets", "example.jpeg", width=200, height=300, watermark="example.svg?width=100&format=png", format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&watermark=example.svg%3Fwidth%3D100%26format%3Dpng&format=png")

    def test_url_with_params_using_rgb_color(self):
        url = imglab.url("assets", "example.jpeg", width=200, height=300, background_color=imglab.color(255, 128, 122))

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&background-color=255%2C128%2C122")

    def test_url_with_params_using_rgba_color(self):
        url = imglab.url("assets", "example.jpeg", width=200, height=300, background_color=imglab.color(255, 128, 122, 128))

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&background-color=255%2C128%2C122%2C128")

    def test_url_with_params_using_named_color(self):
        url = imglab.url("assets", "example.jpeg", width=200, height=300, background_color=imglab.color("blue"))

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&background-color=blue")

    def test_url_with_params_using_horizontal_and_vertical_position(self):
        url = imglab.url("assets", "example.jpeg", width=200, height=300, mode="crop", crop=imglab.position("left", "bottom"))

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&mode=crop&crop=left%2Cbottom")

    def test_url_with_params_using_vertical_and_horizontal_position(self):
        url = imglab.url("assets", "example.jpeg", width=200, height=300, mode="crop", crop=imglab.position("bottom", "left"))

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&mode=crop&crop=bottom%2Cleft")

    def test_url_with_params_using_position(self):
        url = imglab.url("assets", "example.jpeg", width=200, height=300, mode="crop", crop=imglab.position("left"))

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&mode=crop&crop=left")

    def test_url_with_params_using_url_with_source(self):
        source = imglab.Source("assets")

        url = imglab.url(
            "assets",
            "example.jpeg",
            width=200,
            height=300,
            watermark=imglab.url(source, "example.svg", width=100, format="png"),
            format="png",
        )

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&watermark=https%3A%2F%2Fassets.imglab-cdn.net%2Fexample.svg%3Fwidth%3D100%26format%3Dpng&format=png")

    def test_url_with_params_using_url_with_source_name(self):
        url = imglab.url(
            "assets",
            "example.jpeg",
            width=200,
            height=300,
            watermark=imglab.url("assets", "example.svg", width=100, format="png"),
            format="png",
        )

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&watermark=https%3A%2F%2Fassets.imglab-cdn.net%2Fexample.svg%3Fwidth%3D100%26format%3Dpng&format=png")

    def test_url_with_params_using_names_with_underscores(self):
        url = imglab.url("assets", "example.jpeg", trim="color", trim_color="orange")

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?trim=color&trim-color=orange")

    def test_url_with_params_using_dict(self):
        url = imglab.url("assets", "example.jpeg", **{"width": 200, "height": 300, "format": "png"})

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&format=png")

    def test_url_with_params_using_dict_keys_with_underscores(self):
        url = imglab.url("assets", "example.jpeg", **{"trim": "color", "trim_color": "orange"})

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?trim=color&trim-color=orange")

    def test_url_with_params_using_dict_keys_with_hyphens(self):
        url = imglab.url("assets", "example.jpeg", **{"trim": "color", "trim-color": "orange"})

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?trim=color&trim-color=orange")

    def test_url_with_expires_param_using_a_struct_time(self):
        url = imglab.url("assets", "example.jpeg", width=200, height=300, expires=gmtime(1464096368))

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&expires=1464096368")

    def test_url_with_expires_param_using_a_datetime(self):
        url = imglab.url("assets", "example.jpeg", width=200, height=300, expires=datetime.fromtimestamp(1464096368))

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&expires=1464096368")

    def test_url_with_path_starting_with_slash(self):
        url = imglab.url("assets", "/example.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&format=png")

    def test_url_with_path_starting_with_slash_using_reserved_characters(self):
        url = imglab.url("assets", "/example image%2C01%2C02.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/example%20image%252C01%252C02.jpeg?width=200&height=300&format=png")

    def test_url_with_path_starting_and_ending_with_slash(self):
        url = imglab.url("assets", "/example.jpeg/", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&format=png")

    def test_url_with_path_starting_and_ending_with_slash_using_reserved_characters(self):
        url = imglab.url("assets", "/example image%2C01%2C02.jpeg/", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/example%20image%252C01%252C02.jpeg?width=200&height=300&format=png")

    def test_url_with_subfolder_path_starting_with_slash(self):
        url = imglab.url("assets", "/subfolder/example.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/subfolder/example.jpeg?width=200&height=300&format=png")

    def test_url_with_subfolder_path_starting_with_slash_using_reserved_characters(self):
        url = imglab.url("assets", "/subfolder images/example image%2C01%2C02.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/subfolder%20images/example%20image%252C01%252C02.jpeg?width=200&height=300&format=png")

    def test_url_with_subfolder_path_starting_and_ending_with_slash(self):
        url = imglab.url("assets", "/subfolder/example.jpeg/", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/subfolder/example.jpeg?width=200&height=300&format=png")

    def test_url_with_subfolder_path_starting_and_ending_with_slash_using_reserved_characters(self):
        url = imglab.url("assets", "/subfolder images/example image%2C01%2C02.jpeg/", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/subfolder%20images/example%20image%252C01%252C02.jpeg?width=200&height=300&format=png")

    def test_url_with_path_using_http_url(self):
        url = imglab.url("assets", "http://assets.com/subfolder/example.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/http%3A%2F%2Fassets.com%2Fsubfolder%2Fexample.jpeg?width=200&height=300&format=png")

    def test_url_with_path_using_http_url_with_reserved_characters(self):
        url = imglab.url("assets", "http://assets.com/subfolder/example%2C01%2C02.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/http%3A%2F%2Fassets.com%2Fsubfolder%2Fexample%252C01%252C02.jpeg?width=200&height=300&format=png")

    def test_url_with_path_using_https_url(self):
        url = imglab.url("assets", "https://assets.com/subfolder/example.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/https%3A%2F%2Fassets.com%2Fsubfolder%2Fexample.jpeg?width=200&height=300&format=png")

    def test_url_with_path_using_https_url_with_reserver_characters(self):
        url = imglab.url("assets", "https://assets.com/subfolder/example%2C01%2C02.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/https%3A%2F%2Fassets.com%2Fsubfolder%2Fexample%252C01%252C02.jpeg?width=200&height=300&format=png")


class TestUrlWithSource(unittest.TestCase):
    def setUp(self):
        self.source = imglab.Source("assets")

    def test_url_without_params(self):
        url = imglab.url(self.source, "example.jpeg")

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg")

    def test_url_with_params(self):
        url = imglab.url(self.source, "example.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&format=png")

    def test_url_with_none_params(self):
        url = imglab.url(self.source, "example.jpeg", width=200, download=None)

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&download=")

    def test_url_with_params_using_string_path(self):
        url = imglab.url(self.source, "example.jpeg", width=200, height=300, watermark="example.svg", format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&watermark=example.svg&format=png")

    def test_url_with_params_using_string_path_with_inline_params(self):
        url = imglab.url(
            self.source,
            "example.jpeg",
            width=200,
            height=300,
            watermark="example.svg?width=100&format=png",
            format="png",
        )

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&watermark=example.svg%3Fwidth%3D100%26format%3Dpng&format=png")

    def test_url_with_params_using_url_with_source(self):
        url = imglab.url(
            self.source,
            "example.jpeg",
            width=200,
            height=300,
            watermark=imglab.url(self.source, "example.svg", width=100, format="png"),
            format="png",
        )

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&watermark=https%3A%2F%2Fassets.imglab-cdn.net%2Fexample.svg%3Fwidth%3D100%26format%3Dpng&format=png")

    def test_url_with_params_using_url_with_source_name(self):
        url = imglab.url(
            self.source,
            "example.jpeg",
            width=200,
            height=300,
            watermark=imglab.url("assets", "example.svg", width=100, format="png"),
            format="png",
        )

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&watermark=https%3A%2F%2Fassets.imglab-cdn.net%2Fexample.svg%3Fwidth%3D100%26format%3Dpng&format=png")

    def test_url_with_params_using_names_with_underscores(self):
        url = imglab.url(self.source, "example.jpeg", trim="color", trim_color="orange")

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?trim=color&trim-color=orange")

    def test_url_with_params_using_dict(self):
        url = imglab.url(self.source, "example.jpeg", **{"width": 200, "height": 300, "format": "png"})

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&format=png")

    def test_url_with_params_using_dict_keys_with_underscores(self):
        url = imglab.url(self.source, "example.jpeg", **{"trim": "color", "trim_color": "orange"})

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?trim=color&trim-color=orange")

    def test_url_with_params_using_dict_keys_with_hyphens(self):
        url = imglab.url(self.source, "example.jpeg", **{"trim": "color", "trim-color": "orange"})

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?trim=color&trim-color=orange")

    def test_url_with_expires_param_using_a_struct_time(self):
        url = imglab.url(self.source, "example.jpeg", width=200, height=300, expires=gmtime(1464096368))

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&expires=1464096368")

    def test_url_with_expires_param_using_a_datetime(self):
        url = imglab.url(self.source, "example.jpeg", width=200, height=300, expires=datetime.fromtimestamp(1464096368))

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&expires=1464096368")

    def test_url_with_disabled_subdomains(self):
        url = imglab.url(imglab.Source("assets", subdomains=False), "example.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "https://imglab-cdn.net/assets/example.jpeg?width=200&height=300&format=png")

    def test_url_with_disabled_https(self):
        url = imglab.url(imglab.Source("assets", https=False), "example.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "http://assets.imglab-cdn.net/example.jpeg?width=200&height=300&format=png")

    def test_url_with_host(self):
        url = imglab.url(imglab.Source("assets", host="imglab.net"), "example.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab.net/example.jpeg?width=200&height=300&format=png")

    def test_url_with_port(self):
        url = imglab.url(imglab.Source("assets", port=8080), "example.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net:8080/example.jpeg?width=200&height=300&format=png")

    def test_url_with_disabled_subdomains_disabled_https_host_and_port(self):
        url = imglab.url(
            imglab.Source("assets", subdomains=False, https=False, host="imglab.net", port=8080),
            "example.jpeg",
            width=200,
            height=300,
            format="png",
        )

        self.assertEqual(url, "http://imglab.net:8080/assets/example.jpeg?width=200&height=300&format=png")

    def test_url_with_path_starting_with_slash(self):
        url = imglab.url(self.source, "/example.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&format=png")

    def test_url_with_path_starting_with_slash_using_reserved_characters(self):
        url = imglab.url(self.source, "/example image%2C01%2C02.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/example%20image%252C01%252C02.jpeg?width=200&height=300&format=png")

    def test_url_with_path_starting_and_ending_with_slash(self):
        url = imglab.url(self.source, "/example.jpeg/", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&format=png")

    def test_url_with_path_starting_and_ending_with_slash_using_reserved_characters(self):
        url = imglab.url(self.source, "/example image%2C01%2C02.jpeg/", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/example%20image%252C01%252C02.jpeg?width=200&height=300&format=png")

    def test_url_with_subfolder_path_starting_with_slash(self):
        url = imglab.url(self.source, "/subfolder/example.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/subfolder/example.jpeg?width=200&height=300&format=png")

    def test_url_with_subfolder_path_starting_with_slash_using_reserved_characters(self):
        url = imglab.url(self.source, "/subfolder images/example image%2C01%2C02.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/subfolder%20images/example%20image%252C01%252C02.jpeg?width=200&height=300&format=png")

    def test_url_with_subfolder_path_starting_and_ending_with_slash(self):
        url = imglab.url(self.source, "/subfolder/example.jpeg/", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/subfolder/example.jpeg?width=200&height=300&format=png")

    def test_url_with_subfolder_path_starting_and_ending_with_slash_using_reserved_characters(self):
        url = imglab.url(self.source, "/subfolder images/example image%2C01%2C02.jpeg/", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/subfolder%20images/example%20image%252C01%252C02.jpeg?width=200&height=300&format=png")

    def test_url_with_path_using_http_url(self):
        url = imglab.url(self.source, "http://assets.com/subfolder/example.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/http%3A%2F%2Fassets.com%2Fsubfolder%2Fexample.jpeg?width=200&height=300&format=png")

    def test_url_with_path_using_http_url_with_reserved_characters(self):
        url = imglab.url(self.source, "http://assets.com/subfolder/example%2C01%2C02.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/http%3A%2F%2Fassets.com%2Fsubfolder%2Fexample%252C01%252C02.jpeg?width=200&height=300&format=png")

    def test_url_with_path_using_https_url(self):
        url = imglab.url(self.source, "https://assets.com/subfolder/example.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/https%3A%2F%2Fassets.com%2Fsubfolder%2Fexample.jpeg?width=200&height=300&format=png")

    def test_url_with_path_using_https_url_with_reserved_characters(self):
        url = imglab.url(self.source, "https://assets.com/subfolder/example%2C01%2C02.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/https%3A%2F%2Fassets.com%2Fsubfolder%2Fexample%252C01%252C02.jpeg?width=200&height=300&format=png")


class TestUrlWithSecureSource(unittest.TestCase):
    SECURE_KEY = "ixUd9is/LDGBw6NPfLCGLjO/WraJlHdytC1+xiIFj22mXAWs/6R6ws4gxSXbDcUHMHv0G+oiTgyfMVsRS2b3"
    SECURE_SALT = "c9G9eYKCeWen7vkEyV1cnr4MZkfLI/yo6j72JItzKHjMGDNZKqPFzRtup//qiT51HKGJrAha6Gv2huSFLwJr"

    def setUp(self):
        self.source = imglab.Source("assets", secure_key=self.SECURE_KEY, secure_salt=self.SECURE_SALT)

    def test_url_without_params(self):
        url = imglab.url(self.source, "example.jpeg")

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?signature=aRgmnJ-7b2A0QLxXpR3cqrHVYmCfpRCOglL-nsp7SdQ")

    def test_url_with_params(self):
        url = imglab.url(self.source, "example.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&format=png&signature=VJ159IlBl_AlN59QWvyJov5SlQXlrZNpXgDJLJgzP8g")

    def test_url_with_none_params(self):
        url = imglab.url(self.source, "example.jpeg", width=200, download=None)

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&download=&signature=ljL9HNRaxVrk7jfQaf6FPYFZn4RJzQPCW-aVNJoIQI8")

    def test_url_with_params_using_string_path(self):
        url = imglab.url(self.source, "example.jpeg", width=200, height=300, watermark="example.svg", format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&watermark=example.svg&format=png&signature=xrwElVGVPyOrcTCNFnZiAa-tzkUp1ISrjnvEShSVsAg")

    def test_url_with_params_using_string_path_inline_params(self):
        url = imglab.url(
            self.source,
            "example.jpeg",
            width=200,
            height=300,
            watermark="example.svg?width=100&format=png",
            format="png",
        )

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&watermark=example.svg%3Fwidth%3D100%26format%3Dpng&format=png&signature=0yhBOktmTTVC-ANSxMuGK_LakyjCOlnGTSN3I13B188")

    def test_url_with_params_using_url_with_source(self):
        url = imglab.url(
            self.source,
            "example.jpeg",
            width=200,
            height=300,
            watermark=imglab.url(self.source, "example.svg", width=100, format="png"),
            format="png",
        )

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&watermark=https%3A%2F%2Fassets.imglab-cdn.net%2Fexample.svg%3Fwidth%3D100%26format%3Dpng%26signature%3DiKKUBWG4kZBv6CVxwaWGPpHd9LLTfuj9CBWamNYtWaI&format=png&signature=ZMT8l8i9hKs4aYiIUXpGcMSzOGHS8xjUlQeTrvE8ESA")

    def test_url_with_params_using_url_with_source_name(self):
        url = imglab.url(
            self.source,
            "example.jpeg",
            width=200,
            height=300,
            watermark=imglab.url(imglab.Source("fixtures"), "example.svg", width=100, format="png"),
            format="png",
        )

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&watermark=https%3A%2F%2Ffixtures.imglab-cdn.net%2Fexample.svg%3Fwidth%3D100%26format%3Dpng&format=png&signature=6BowGGEXe9wUmGa4xkhoscfPkqrLGumkIglhPQEkNuo")

    def test_url_with_params_using_names_with_underscores(self):
        url = imglab.url(self.source, "example.jpeg", trim="color", trim_color="orange")

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?trim=color&trim-color=orange&signature=cfYzBKvaWJhg_4ArtL5IafGYU6FEgRb_5ZADIgvviWw")

    def test_url_with_params_using_dict(self):
        url = imglab.url(self.source, "example.jpeg", **{"width": 200, "height": 300, "format": "png"})

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&format=png&signature=VJ159IlBl_AlN59QWvyJov5SlQXlrZNpXgDJLJgzP8g")

    def test_url_with_params_using_dict_keys_with_underscores(self):
        url = imglab.url(self.source, "example.jpeg", **{"trim": "color", "trim_color": "orange"})

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?trim=color&trim-color=orange&signature=cfYzBKvaWJhg_4ArtL5IafGYU6FEgRb_5ZADIgvviWw")

    def test_url_with_params_using_dict_keys_with_hyphens(self):
        url = imglab.url(self.source, "example.jpeg", **{"trim": "color", "trim-color": "orange"})

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?trim=color&trim-color=orange&signature=cfYzBKvaWJhg_4ArtL5IafGYU6FEgRb_5ZADIgvviWw")

    def test_url_with_expires_param_using_a_struct_time(self):
        url = imglab.url(self.source, "example.jpeg", width=200, height=300, expires=gmtime(1464096368))

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&expires=1464096368&signature=DpkRMiecDlOaQAQM5IQ8Cd4ek8nGvfPxV6XmCN0GbAU")

    def test_url_with_expires_param_using_a_datetime(self):
        url = imglab.url(self.source, "example.jpeg", width=200, height=300, expires=datetime.fromtimestamp(1464096368))

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&expires=1464096368&signature=DpkRMiecDlOaQAQM5IQ8Cd4ek8nGvfPxV6XmCN0GbAU")

    def test_url_with_disabled_subdomains(self):
        url = imglab.url(
            imglab.Source("assets", secure_key=self.SECURE_KEY, secure_salt=self.SECURE_SALT, subdomains=False),
            "example.jpeg",
            width=200,
            height=300,
            format="png",
        )

        self.assertEqual(url, "https://imglab-cdn.net/assets/example.jpeg?width=200&height=300&format=png&signature=VJ159IlBl_AlN59QWvyJov5SlQXlrZNpXgDJLJgzP8g")

    def test_url_with_disabled_https(self):
        url = imglab.url(
            imglab.Source("assets", secure_key=self.SECURE_KEY, secure_salt=self.SECURE_SALT, https=False),
            "example.jpeg",
            width=200,
            height=300,
            format="png",
        )

        self.assertEqual(url, "http://assets.imglab-cdn.net/example.jpeg?width=200&height=300&format=png&signature=VJ159IlBl_AlN59QWvyJov5SlQXlrZNpXgDJLJgzP8g")

    def test_url_with_host(self):
        url = imglab.url(
            imglab.Source("assets", secure_key=self.SECURE_KEY, secure_salt=self.SECURE_SALT, host="imglab.net"),
            "example.jpeg",
            width=200,
            height=300,
            format="png",
        )

        self.assertEqual(url, "https://assets.imglab.net/example.jpeg?width=200&height=300&format=png&signature=VJ159IlBl_AlN59QWvyJov5SlQXlrZNpXgDJLJgzP8g")

    def test_url_with_port(self):
        url = imglab.url(
            imglab.Source("assets", secure_key=self.SECURE_KEY, secure_salt=self.SECURE_SALT, port=8080),
            "example.jpeg",
            width=200,
            height=300,
            format="png",
        )

        self.assertEqual(url, "https://assets.imglab-cdn.net:8080/example.jpeg?width=200&height=300&format=png&signature=VJ159IlBl_AlN59QWvyJov5SlQXlrZNpXgDJLJgzP8g")

    def test_url_with_disabled_subdomains_disabled_https_host_and_port(self):
        source = imglab.Source(
            "assets",
            secure_key=self.SECURE_KEY,
            secure_salt=self.SECURE_SALT,
            subdomains=False,
            https=False,
            host="imglab.net",
            port=8080,
        )

        url = imglab.url(source, "example.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "http://imglab.net:8080/assets/example.jpeg?width=200&height=300&format=png&signature=VJ159IlBl_AlN59QWvyJov5SlQXlrZNpXgDJLJgzP8g")

    def test_url_with_path_starting_with_slash(self):
        url = imglab.url(self.source, "/example.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&format=png&signature=VJ159IlBl_AlN59QWvyJov5SlQXlrZNpXgDJLJgzP8g")

    def test_url_with_path_starting_with_slash_using_reserved_characters(self):
        url = imglab.url(self.source, "/example image%2C01%2C02.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/example%20image%252C01%252C02.jpeg?width=200&height=300&format=png&signature=yZcUhTCB9VB3qzjyIJCCX_pfJ76Gb6kHe7KwusAPl-w")

    def test_url_with_path_starting_and_ending_with_slash(self):
        url = imglab.url(self.source, "/example.jpeg/", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/example.jpeg?width=200&height=300&format=png&signature=VJ159IlBl_AlN59QWvyJov5SlQXlrZNpXgDJLJgzP8g")

    def test_url_with_path_starting_and_ending_with_slash_using_reserved_characters(self):
        url = imglab.url(self.source, "/example image%2C01%2C02.jpeg/", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/example%20image%252C01%252C02.jpeg?width=200&height=300&format=png&signature=yZcUhTCB9VB3qzjyIJCCX_pfJ76Gb6kHe7KwusAPl-w")

    def test_url_with_subfolder_path_starting_with_slash(self):
        url = imglab.url(self.source, "/subfolder/example.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/subfolder/example.jpeg?width=200&height=300&format=png&signature=3jydAIXhF8Nn_LXKhog2flf7FsACzISi_sXCKmASkOs")

    def test_url_with_subfolder_path_starting_with_slash_using_reserved_characters(self):
        url = imglab.url(self.source, "/subfolder images/example image%2C01%2C02.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/subfolder%20images/example%20image%252C01%252C02.jpeg?width=200&height=300&format=png&signature=2oAmYelI7UEnvqSSPCfUA25TmS7na1FRVTaxfe5ADyY")

    def test_url_with_subfolder_path_starting_and_ending_with_slash(self):
        url = imglab.url(self.source, "/subfolder/example.jpeg/", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/subfolder/example.jpeg?width=200&height=300&format=png&signature=3jydAIXhF8Nn_LXKhog2flf7FsACzISi_sXCKmASkOs")

    def test_url_with_subfolder_path_starting_and_ending_with_slash_using_reserved_characters(self):
        url = imglab.url(self.source, "/subfolder images/example image%2C01%2C02.jpeg/", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/subfolder%20images/example%20image%252C01%252C02.jpeg?width=200&height=300&format=png&signature=2oAmYelI7UEnvqSSPCfUA25TmS7na1FRVTaxfe5ADyY")

    def test_url_with_path_using_http_url(self):
        url = imglab.url(self.source, "http://assets.com/subfolder/example.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/http%3A%2F%2Fassets.com%2Fsubfolder%2Fexample.jpeg?width=200&height=300&format=png&signature=MuzfKbHDJY6lzeFQGRcsCS8DzxgL4nCpIowOMFLR1kA")

    def test_url_with_path_using_http_url_with_reserved_characters(self):
        url = imglab.url(self.source, "http://assets.com/subfolder/example%2C01%2C02.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/http%3A%2F%2Fassets.com%2Fsubfolder%2Fexample%252C01%252C02.jpeg?width=200&height=300&format=png&signature=78e-ysfcy3d0e0rj70QJQ3wpuwI_hAl9ZYxIUVRw62I")

    def test_url_with_path_using_https_url(self):
        url = imglab.url(self.source, "https://assets.com/subfolder/example.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/https%3A%2F%2Fassets.com%2Fsubfolder%2Fexample.jpeg?width=200&height=300&format=png&signature=7Dp8Q01u_5YmpmH-j_y4P5vzOn_9EGvh77B3fi2Ke-s")

    def test_url_with_path_using_https_url_with_reserved_characters(self):
        url = imglab.url(self.source, "https://assets.com/subfolder/example%2C01%2C02.jpeg", width=200, height=300, format="png")

        self.assertEqual(url, "https://assets.imglab-cdn.net/https%3A%2F%2Fassets.com%2Fsubfolder%2Fexample%252C01%252C02.jpeg?width=200&height=300&format=png&signature=-zvh2hWXP8bHkoJVh8AdJFe9Kqdd1HpP1c2UmuQcYFQ")


class TestUrlWithInvalidSource(unittest.TestCase):
    def test_url_with_none_as_source(self):
        with self.assertRaises(ValueError):
            imglab.url(None, "example.jpeg")

    def test_url_with_dict_as_source(self):
        with self.assertRaises(ValueError):
            imglab.url({}, "example.jpeg")

    def test_url_with_integer_as_source(self):
        with self.assertRaises(ValueError):
            imglab.url(10, "example.jpeg")


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite("imglab.url"))

    return tests


if __name__ == "__main__":
    unittest.main()
