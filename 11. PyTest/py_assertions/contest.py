import pytest
import os

def pytest_configure():
    pytest.weekdays1 = [ 'mon', 'tue', 'wed']
    pytest.weekdays2 = [ 'fri', 'sat', 'sun']


@pytest.fixture(scope='module')
def setup01():
    wk = pytest.weekdays1.copy()
    wk.append('thur')
    yield wk
    print("\n Fixture setup01 closing")

@pytest.fixture()
def setup02():
    wk2 = pytest.weekdays2.copy()
    wk2.insert(0, 'thur')
    yield wk2

@pytest.fixture()
def setup04(request):
    print("\n in fixture setup04")
    print("\n in fixture scope: " + str(request.scope))
    print("\n calling function: " + str(request.function.__name__))
    print("\n calling function: " + str(request.module.__name__))