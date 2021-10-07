import pytest 
import sys

def test_strjoin():
    s1 = 'python, pytest and automation'
    l1 = ['python, pytest', 'and', 'automation']
    l2 = ['python', 'pytest and automation']
    assert ' '.join(l1) == s1

#si el assert geenra un error se levanata como XFAIL
# @pytest.mark.xfail(reason = "error conocido")
@pytest.mark.xfail(raises=IndexError, reason = "error conocido")
def test_str04():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[100]

@pytest.mark.xfail(sys.platform=='win32', reason = 'solo en linux')
def test_str05():
    letters = 'abcd'
    num = 1234
    assert letters + num == 'abcd1234'