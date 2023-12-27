#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed='Mutt'):
        self.name = name
        self.breed = breed
        #print(self)

# a = Dog('Ana')
# a = Dog('Stuart', 'Poodle')
# print(a.name)
# print(a.breed)

        
# the function inside the class, in this case __init__, is called instance method. The self keyword is the object itself, a variable name you can choose. The attributes of the Dog class are name and breed.
