"""
Facade Module.

The facade module creates a facade that will create an interface for the Client
to request for complex services from multiple subsystems in a simple manner.
"""


class EventManager(object):
    """This is the Facade, it will interact with all of the subsystems."""

    def __init__(self):
        """Init of the Facade class."""
        print("Event Manager:: Let me talk to the folks\n")

    def arrange(self):
        """
        Arrange.

        Method used to attend a complex request from the client and hide
        its execution complexity.
        """
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()

        self.florist = Florist()
        self.florist.setFlowerRequirements()

        self.caterer = Caterer()
        self.caterer.setCuisine()

        self.musician = Musician()
        self.musician.setMusicType()


class Hotelier(object):
    """Hotel subsystem."""

    def __init__(self):
        """Initialize the Hotel subsystem."""
        print("Arranging the Hotel for Marriage? --")

    def __isAvailable(self):
        print("Is the Hotel free for the event on given day?")
        return True

    def bookHotel(self):
        """Perform the main function of subsystem."""
        if self.__isAvailable():
            print("Registered the booking.")


class Florist(object):
    """Florist subsystem."""

    def __init__(self):
        """Initialize the Florist subsystem."""
        print("Flower Decorations for the Event? --")

    def setFlowerRequirements(self):
        """Perform the main function of subsystem."""
        print("""Carnations, Roses and Lillies
              would be used for decorations.\n\n""")


class Caterer(object):
    """Caterer subsystem."""

    def __init__(self):
        """Initialize the Caterer subsystem."""
        print("Food Arrangements for the Event --")

    def setCuisine(self):
        """Perform the main function of subsystem."""
        print("Chinese & Continental Cuisine to be served.\n\n")


class Musician(object):
    """Musician subsystem."""

    def __init__(self):
        """Initialize the Musician subsystem."""
        print("Music Arrangements for the Marriage --")

    def setMusicType(self):
        """Perform the main function of subsystem."""
        print("Jazz and Classical will be played.\n\n")


class You(object):
    """Client class that will use the Facade."""

    def __init__(self):
        """Initialize the Client class."""
        print("You:: Whoa! Marriage Arrangements?!!")

    def askEventManager(self):
        """Instantiate, use and delete the Facade."""
        print("You:: Let's contact the Event Manager\n\n")
        em = EventManager()
        em.arrange()

    def __del__(self):
        """Upon deletion of the You object, say thanks to the Event Manager."""
        print("""You:: Thanks to the Event Manager,
              all preparations are done! Phew!""")


you = You()
you.askEventManager()
del you
