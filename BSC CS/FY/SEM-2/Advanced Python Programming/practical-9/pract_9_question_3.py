# The __str__() Function

class Person:
  
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"Name is {self.name} and age is ({self.age})"

p1 = Person("Varaliya", 20)

print(p1)