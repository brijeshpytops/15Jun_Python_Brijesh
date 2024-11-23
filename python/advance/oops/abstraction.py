from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def voice(self):
        pass

class Dog(Animal):
    def voice(self, sound):
        print(sound)

class Cat(Animal):
    def voice(self, sound):
        print(sound)

# obj = Animal() # TypeError: Can't instantiate abstract class Animal without an implementation for abstract method 'voice'

dog = Dog()
dog.voice("Woof!")

cat = Cat()
cat.voice("Meow!")
