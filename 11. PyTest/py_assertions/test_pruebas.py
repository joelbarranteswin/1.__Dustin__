def test_a1():
    assert 4 != 3

def test_a2():
    assert 1

def test_a3():
    assert "abcd" == 'abcd'

def test_a4():
    assert ((3-1)*4/2) == 4.0

def test_5a():
    assert 1 in divmod(9,5)
    assert 'put' not in 'this is pytest'
    assert 2 in [1,2,4]

def test_6a():
    a = 2
    b = 4
    assert 2 == 4/2

