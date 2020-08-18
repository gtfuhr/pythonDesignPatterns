"""
Command.

The command Design Pattern has the objective of requesting something for the
client from a selected objected. The parameters of the request are chosen
by the client and then passed from the Command to the object.

Here is a example of the use of Command in a program installation Wizard.
"""


class Wizard:
    """Command class."""

    def __init__(self, rootdir, src):
        """Initialize the installation wizard."""
        self.choices = []
        self.rootdir = rootdir
        self.src = src

    def preferences(self, command):
        """Set any preference."""
        self.choices.append(command)

    def execute(self):
        """Execute the installation with the setted preferences."""
        for choice in self.choices:
            if list(choice.values())[0]:
                print("Copying binaries --", self.src, "to ", self.rootdir)
            else:
                print("No operations")


if __name__ == '__main__':
    # Código do cliente
    wizard = Wizard('python3.5.gzip', '/usr/bin/')
    # Os usuários escolhem instalar somente Python
    wizard.preferences({'python': True})
    wizard.preferences({'java': False})
    wizard.execute()
