"""Module that shows a use example of the Proxy Pattern."""


class Actor(object):
    """Class that actually performs the actions wanted by the client."""

    def __init__(self):
        """Initialize the Actor class."""
        self.isBusy = False

    def occupied(self):
        """Set the actor as occupied and print its name and status."""
        self.isBusy = True
        print(type(self).__name__, "is occupied with its current movie.")

    def available(self):
        """Set the actor as available and print its name and status."""
        self.isBusy = False
        print(type(self).__name__, "is free for the movie.")

    def getStatus(self):
        """Return the actor busy status."""
        return self.isBusy


class Agent(object):
    """Class that represents the Proxy."""

    def __init__(self):
        """Initialize the proxy class."""
        self.principal = None

    def work(self):
        """Access the subject class and act as a proxy to it."""
        self.actor = Actor()
        if self.actor.getStatus() is True:
            self.actor.occupied()
        else:
            self.actor.available()


if __name__ == '__main__':
    r = Agent()
    r.work()
