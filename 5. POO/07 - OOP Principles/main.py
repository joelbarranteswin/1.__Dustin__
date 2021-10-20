from item import Item
from phone import Phone
from keyboard import Keyboard


# item1 = Keyboard("jscKeyboard", 1000, 3)
# item1 = Item("MyItem", 750)
# item1.price = -900

# item1.apply_increment(0.2)
# item1.apply_discount()
# print(item1.price)


#ABSTRACTION
# item1 = Item("MyItem", 750)
# print(item1.send_email())

#INHERITANCE
# item1 = Phone("MyPhone", 1000, 3)
# item1.apply_increment(0.2)
# print(item1.price)

#POLYMORPHISM
item1 = Keyboard("jscKeyboard", 1000, 3)
item1.apply_discount()
print(item1.price)


