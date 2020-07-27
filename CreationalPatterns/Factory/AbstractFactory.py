"""
Created on Mon Jul 27 14:24:59 2020.

@author: fuhr
"""

from abc import ABCMeta, abstractmethod


class PizzaFactory(metaclass=ABCMeta):
    """Abstract class defining a Pizza factory."""

    @abstractmethod
    def createVegPizza(self):
        """Abstract method to create a veg pizza."""
        pass

    @abstractmethod
    def createNonVegPizza(self):
        """Abstract method to create a non veg pizza."""
        pass


class IndianPizzaFactory(PizzaFactory):
    """Definition of an Indian Pizza Factory."""

    def createVegPizza(self):
        """Definition of a veggie pizza."""
        return DeluxVeggiePizza()

    def createNonVegPizza(self):
        """Definition of a nonveggie pizza."""
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):
    """Definition of an US Pizza Factory."""

    def createVegPizza(self):
        """Definition of a veggie pizza."""
        return MexicanVegPizza()

    def createNonVegPizza(self):
        """Definition of a nonveggie pizza."""
        return HamPizza()


class VegPizza(metaclass=ABCMeta):
    """Abstract definition of a veggie pizza."""

    @abstractmethod
    def prepare(self, VegPizza):
        """Definition of a abstract method for veggie pizzas."""
        pass


class NonVegPizza(metaclass=ABCMeta):
    """Abstract definition for nonveggie pizzas."""

    @abstractmethod
    def serve(self, VegPizza):
        """Definition of a abstract method for nonveggie pizzas."""
        pass


class DeluxVeggiePizza(VegPizza):
    """Specific definition of a veg pizza class."""

    def prepare(self):
        """Specific implementation of a veg pizza preparation process."""
        print("Prepare", type(self).__name__)


class ChickenPizza(NonVegPizza):
    """Specific implementation of a nonveg pizza class."""

    def serve(self, VegPizza):
        """Specific implementation of a nonveg pizza serving process."""
        print(type(self).__name__, " is served with chicken on ",
              type(VegPizza).__name__)


class MexicanVegPizza(VegPizza):
    """Specific implementation of a veg pizza class."""

    def prepare(self):
        """Specific implementation of a veg pizza preparation process."""
        print("Prepare", type(self).__name__)


class HamPizza(NonVegPizza):
    """Specific implementation of a nonveg pizza class."""

    def serve(self, VegPizza):
        """Specific implementation of a nonveg pizza serving process."""
        print(type(self).__name__, " is served with chicken on ",
              type(VegPizza).__name__)


class PizzaStore:
    """Implementation of an Abstract Factory."""

    def makePizzas(self):
        """Start the Abstract factory production."""
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.NonVegPizza = self.factory.createNonVegPizza()
            self.VegPizza = self.factory.createVegPizza()
            self.VegPizza.prepare()
            self.NonVegPizza.serve(self.VegPizza)


pizza = PizzaStore()
pizza.makePizzas()
