from collections import namedtuple
import pytest
Dinner = namedtuple('Dinner', ['food','cook','ready','id'])


def test_deafults():
    t1 = Dinner(food='bread',cook='Soup',ready=True,id=455)
    t2 = Dinner(food='bread',cook='Soup',ready=True,id=455)
    assert t1 == t2

@pytest.mark.run_first
def test_num_access():
    t = Dinner('potatoes', 'Sam',False, 455)
    assert t.food == 'potatoes'
    assert t.cook == 'Sam'
    assert (t.ready, t.id) == (False, 455)
