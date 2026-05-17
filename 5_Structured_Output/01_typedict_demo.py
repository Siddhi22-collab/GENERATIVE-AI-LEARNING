from typing import TypedDict
class Person(TypedDict):
    name: str
    age: int
person1: Person = {"name": "Siddhi", "age": 22}
print(person1)