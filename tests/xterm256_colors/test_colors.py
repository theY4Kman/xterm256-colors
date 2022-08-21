import pytest
from colormath.color_objects import LabColor, sRGBColor  # type: ignore[import]
from pytest_assert_utils import util  # type: ignore[import]
from pytest_lambda import lambda_fixture, static_fixture
from pytest_lambda.impl import LambdaFixture

from xterm256_colors import Back256, Fore256, XtermCodes
from xterm256_colors.colors import _XtermColorSwatch


class DescribeXtermCodes:
    codes: LambdaFixture[XtermCodes] = lambda_fixture(params=[
        pytest.param(Fore256, id='Fore256'),
        pytest.param(Back256, id='Back256'),
    ])

    def it_allows_getattr_lookup_by_name(self, codes):
        assert codes.BLACK

    def it_allows_getitem_lookup_by_name(self, codes):
        assert codes['BLACK']

    def it_allows_getitem_lookup_by_code(self, codes):
        assert codes[1]


class DescribeXtermColor:
    # NOTE: INDIANRED1_1 chosen because each of its RGB components are different (#ff5f87)
    color = static_fixture(Fore256.INDIANRED1_1)

    # Because most of these tests deal with essentially arbitrary colours, the intent is
    # not to test the *information* in the returned values, but to ensure their execution
    # paths are error-free and return the expected types.

    def it_returns_swatch(self, color):
        expected = _XtermColorSwatch(color)
        actual = color.swatch
        assert expected == actual

    def it_returns_r_g_b_byte_components(self, color):
        expected = (0xff, 0x5f, 0x87)
        actual = (color.r, color.g, color.b)
        assert expected == actual

    def it_returns_red_green_blue_float_components(self, color):
        expected = (1.0, 0.37254901960784315, 0.5294117647058824)
        actual = (color.red, color.green, color.blue)
        assert expected == actual

    def it_returns_hsv(self, color):
        expected = (0.9583333333333334, 0.6274509803921569, 1.0)
        actual = color.hsv
        assert expected == actual

    def it_returns_is_greyscale(self, color):
        expected = False
        actual = color.is_greyscale
        assert expected == actual

    def it_returns_perceived_brightness(self, color):
        expected = 0.6422016149650706
        actual = color.perceived_brightness
        assert expected == actual

    def it_returns_is_bright_and_is_dark(self, color):
        expected = (True, False)
        actual = (color.is_bright, color.is_dark)
        assert expected == actual

    def it_returns_srgb_color(self, color):
        expected = util.Any(sRGBColor)
        actual = color.as_srgb_color
        assert expected == actual

    def it_returns_lab_color(self, color):
        expected = util.Any(LabColor)
        actual = color.as_lab_color
        assert expected == actual

    def it_is_string(self, color):
        assert isinstance(color, str)

    def it_returns_string_value_when_called_with_no_arguments(self, color):
        expected = str(color)
        actual = color()
        assert expected == actual
