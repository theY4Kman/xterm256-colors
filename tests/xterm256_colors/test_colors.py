from pytest_lambda import lambda_fixture
from pytest_lambda.impl import LambdaFixture

from xterm256_colors import Back256, Fore256, XtermCodes


class DescribeXtermCodes:
    codes: LambdaFixture[XtermCodes] = lambda_fixture(params=[
        Fore256,
        Back256,
    ])

    def it_allows_getattr_lookup_by_name(self, codes):
        assert codes.BLACK

    def it_allows_getitem_lookup_by_name(self, codes):
        assert codes['BLACK']

    def it_allows_getitem_lookup_by_code(self, codes):
        assert codes[1]
