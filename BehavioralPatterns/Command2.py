"""
Command.

The command Design Pattern has the objective of requesting something for the
client from a selected objected. The parameters of the request are chosen
by the client and then passed from the Command to the object.

Here is another example of the use of Command in a program installation Wizard.
"""


from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    """Metaclass made to be inherited by the concrete Command."""

    @abstractmethod
    def __init__(self, recv):
        """Initialize the Command Class."""
        self.recv = recv

    @abstractmethod
    def execute(self):
        """Abstract execute method."""
        pass


class ConcreteCommand(Command):
    """Command class."""

    def __init__(self, recv):
        """Initialize the ConcreteCommand Class."""
        self.recv = recv

    def execute(self):
        """Execute method."""
        self.recv.action()


class Receiver:
    """Receiver class."""

    def action(self):
        """Make some action in the receiver."""
        print("Receiver Action")


class Invoker:
    """Invoker class."""

    def command(self, cmd):
        """Make some command."""
        self.cmd = cmd

    def execute(self):
        """Execute the command action."""
        self.cmd.execute()


if __name__ == '__main__':
    recv = Receiver()
    cmd = ConcreteCommand(recv)
    invoker = Invoker()
    invoker.command(cmd)
    invoker.execute()
