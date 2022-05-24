from dataclasses import dataclass, field


@dataclass(order=True, frozen=True)
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
    strength: int = 100

    def __post_init__(self):
        object.__setattr__(self, 'sort_index', self.strength)

    def __str__(self):
        return f'{self.name} {self.job}: {self.age}'

    def __repr__(self):
        return f'Person("{self.name}", "{self.job}", {self.age}, {self.strength})'

# before
# class Person:
#     def __init__(self, name, job, age):
#         self.name = name
#         self.job = job
#         self.age = age

person1 = Person('Gerald', 'Witcher', 40)
person2 = Person('Ciri', 'Witcher', 20)
person3 = Person('Jennyfer', 'Sorceress', 25)
person4 = Person('Jennyfer', 'Sorceress', 25)

print(id(person1))
print(id(person2))
print(person1)

print(person3 == person4)
