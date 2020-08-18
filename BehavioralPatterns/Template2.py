"""
Template.

Here is a more simple and generic example of the Template implementation.
"""

from abc import ABCMeta, abstractmethod


class AbstractClass(metaclass=ABCMeta):
    """Abstract class."""

    def __init__(self):
        """Pass initialization."""
        pass

    @abstractmethod
    def operation1(self):
        """Abstract step method for the template method."""
        pass

    @abstractmethod
    def operation2(self):
        """Abstract step method for the template method."""
        pass

    def template_method(self):
        """Template method."""
        print("Defining the Algorithm. Operation1 follows Operation2.")
        self.operation2()
        self.operation1()


class ConcreteClass(AbstractClass):
    """Concrete implementation of the Template Abstract Class."""

    def operation1(self):
        """Concrete step method for the template method."""
        print("My concrete operation 1")

    def operation2(self):
        """Concrete step method for the template method."""
        print("Operation 2 remains the same")


class Client:
    """Client class of a concrete implementation of the Template algo."""

    def main(self):
        """Call it on the main."""
        self.concrete = ConcreteClass()
        self.concrete.template_method()


client = Client()
client.main()
