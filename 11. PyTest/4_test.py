from collections import namedtuple
import pytest
Dinner = namedtuple('Dinner',['food','cook','ready','id'])

def test_asdict():
    t_Dinner = Dinner(food='potatoes',cook='Bol',ready=True,id=344)
    t_dict = t_Dinner._asdict()
    expected = {'food': 'potatoes',
                'cook': 'Bol',
                'ready': True,
                'id': 344}
    assert t_dict == expected

@pytest.mark.run_first
def test_replace():
    t_before = Dinner(food='meat', cook='Sam', ready=False,id=455)
    t_after = t_before._replace(id=456, ready=True)
    t_expected = Dinner('meat', 'Sam', True, 456)
    assert t_after == t_expected