"""
Template.

The Template method is quite useful and can be used in multiple scenarios.
It is primarily composed of two classes and one template method.

Abstract Class: Declares an Interface to define the steps of the algorithm.
Example: Beverage

Concrete Class: Define steps specific to the subclass
Example: PrepareTea, PrepareCofffe

template_method(): Defines the algorithm calling the specific methods for each
step.
"""

from abc import ABCMeta, abstractmethod


class Compiler(metaclass=ABCMeta):
    """Abstract class."""

    @abstractmethod
    def collectSource(self):
        """Abstract step method for the template method."""
        pass

    @abstractmethod
    def compileToObject(self):
        """Abstract step method for the template method."""
        pass

    @abstractmethod
    def run(self):
        """Abstract step method for the template method."""
        pass

    def compileAndRun(self):
        """Template method."""
        self.collectSource()
        self.compileToObject()
        self.run()


class iOSCompiler(Compiler):
    """Concrete implementation of the Template Compiler."""

    def collectSource(self):
        """Concrete step method for the template method."""
        print("Collecting Swift Source Code")

    def compileToObject(self):
        """Concrete step method for the template method."""
        print("Compiling Swift code to LLVM bticode")

    def run(self):
        """Concrete step method for the template method."""
        print("Program running on runtime environment")


iOS = iOSCompiler()
iOS.compileAndRun()
