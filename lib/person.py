#!/usr/bin/env python3

class Person:
    # Class body goes here
    def __init__(self, name="Person", age=0):
        self.name = name
        self.age = age

    #Instance method definition
    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")
