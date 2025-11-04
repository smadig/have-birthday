print("=== Person Class ===")

class Person:
  """Represents a person with name and age"""

  def __init__(self, name, age):
    """Initialize a new person"""
    self.name = name
    self.age = age

  def introduce(self):
    """Return an introduction string"""
    return f"Hi, I'm {self.name} and I'm {self.age} years old"

  def have_birthday(self):
    """Celebrate a birthday (increase age by 1)"""
    self.age += 1
    return f"Happy birthday, {self.name}! Now {self.age} years old."

if __name__ == "__main__":

    person1 = Person("Alice", 25)
    person2 = Person("Bob", 30)

    print(person1.introduce())
    print(person2.introduce())

    # Have birthay

    print(person1.have_birthday())
    print(person2.have_birthday())

    # Access attributes directly
    print(f"\n{person1.name}'s age: {person1.age}")
    print(f"{person2.name}'s age: {person2.age}")