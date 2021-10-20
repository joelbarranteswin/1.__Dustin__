import pytest

QA_config = 'qa.prop'
prod_config = 'prod.prop'

def pytest_addptions(parser):
    parser.addoption("--cmdopt", default='QA')

@pytest.fixture()
def CmdOpt(pytestconfig):
    opt = pytestconfig.getoption('cmdopt') 
    if opt == 'QA':
        f = open(prod_config, 'r')
    else:
        f = open(QA_config, 'r')
    yield f
    