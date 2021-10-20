import pytest 

@pytest.fixture(params=[(3,4),[3,5]], ids=['tuple','list'])
def fixture01(request):
    return request.param

@pytest.fixture(params=['access', 'slice'])
def fixture02(request):
    return request.param

 

def test_fix_param01(fixture01):
    assert (type(fixture01)) in [tuple, list]

def test_fix_param01(fixture01, fixture02):
    if (fixture02 == 'access'):
        assert (fixture01[0])
    elif (fixture02 == 'slice'):
        assert fixture01[::-1]
   
    