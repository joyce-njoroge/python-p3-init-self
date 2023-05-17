#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed='Mutt'):
        self.name = name
        self.breed = breed

my_dog = Dog('Max', 'Labrador')
print(my_dog.name)   
print(my_dog.breed) 

another_dog = Dog('Buddy')
print(another_dog.name)   
print(another_dog.breed)     