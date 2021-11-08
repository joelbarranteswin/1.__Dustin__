from dataclasses import dataclass, field

@dataclass(order=True,frozen=False) #congela los valores  y no se les puede asignar mas
# @dataclass(order=True)
class Person:
    # sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
    strength: int = 100

    def __post_init__(self):
        # self.sort_index = self.age
        object.__setattr__(self, 'sort_index', self.strength)

    # def __str__(self):
    #     return f'{self.name}, {self.job} ({self.age})'


person1 = Person("Geralt", "Witcher", 30, 38)
person2 = Person("Yennefer", "Sorceress", 25)
person3 = Person("Yennefer", "Sorceress", 25)
# person1.age = 5 #si se usa el frozen no se puede cambiar los valores

print(person1)
print(id(person2))
print(id(person3))
print(person3 > person2) #solo se puede mayor o menor si se usa un orden
# print(person1 > person2)