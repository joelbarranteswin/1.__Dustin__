
import pytest

@pytest.fixture()
def setup_list():
    print("\n in fixture.. \n")
    city = ['new york', 'london', 'riyadh', 'singapore', 'munbai']
    return city

def test_getItem(setup_list):
    print(setup_list[1:3])
    assert setup_list[0] == 'new york'
    assert setup_list[::2] == ['new york', 'riyadh', 'munbai']

def myReverse(lst):
    lst.reverse()
    return lst

def test_revereList(setup_list):
    assert setup_list[::-2] == ['munbai', 'riyadh', 'new york']
    assert setup_list[::-1] == myReverse(setup_list)

@pytest.mark.xfail(reason="known issue: usefixture cannot use the fixture's return value ")
@pytest.mark.usefixture("setup_list")
def test_usefixturedemo():
    assert 1 == 1
    assert setup_list[0]