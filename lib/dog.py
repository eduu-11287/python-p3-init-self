#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

    def bark(self):
        return "Woof!"
    
fido = Dog("fido")
fido.name
fido.breed