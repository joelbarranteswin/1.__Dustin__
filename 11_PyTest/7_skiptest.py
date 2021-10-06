import pytest
import sys

#si es verdadero, entonces salta los testing
pytestmark = pytest.mark.skipif(sys.platform != 'win32',
                        reason = "will run only windows")

const = 9/5
def cent_to_fah(cent=0):
    fah = (cent * const) + 32
    return fah

# print(cent_to_fah())

@pytest.mark.skip(reason="saltando por una rason especifica")
def test_case01():
    assert type(const) == float

# @pytest.mark.skipif(sys.version_info < (3,8), reason = "no menor de 3.8")
# @pytest.mark.skipif(cent_to_fah()==32, reason="default value test, so skipping")
def test_case02():
    assert cent_to_fah() == 32


@pytest.mark.skipif(pytest.__version__ < '6.2.0', reason = 'pytest version is menor')
def test_case03():
    assert cent_to_fah(38) == 100.4

