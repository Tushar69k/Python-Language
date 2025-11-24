# Define Inheritance, write the types of inheritance and write the program for multilevel inheritance


# Multilevel Inheritance Example

class Animal:         # Parent class
    def sound(self):
        print("Animals make different sounds.")

class Dog(Animal):    # Child class of Animal
    def bark(self):
        print("Dog barks: Woof Woof!")

class Puppy(Dog):     # Child class of Dog (multilevel)
    def weep(self):
        print("Puppy weeps: Mee Mee!")

# Creating object of Puppy
p = Puppy()

p.sound()   # From Animal
p.bark()    # From Dog
p.weep()    # From Puppy
