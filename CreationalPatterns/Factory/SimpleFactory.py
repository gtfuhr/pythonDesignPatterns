"""
Created on Mon Jul 27 13:12:14 2020.

@author: fuhr
"""

from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    """Abstract class for animals."""

    @abstractmethod
    def do_say(self):
        """Abstract method to print the animal sound."""
        pass


class Dog(Animal):
    """Class to define a dog."""

    def do_say(self):
        """Print the sound of a dog."""
        print("Au au!")


class Cat(Animal):
    """Class to define a cat."""

    def do_say(self):
        """Print the sound of a cat."""
        print("Miau miau!")


class ForestFactory(object):
    """Class to define a forest Simple Factory."""

    def make_sound(self, object_type):
        """Call the do_say method from the desired class."""
        return eval(object_type)().do_say()


# Client code
if __name__ == '__main__':
    ff = ForestFactory()
    animal = input("Which animal should make_sound Dog or Cat?")
    ff.make_sound(animal)
