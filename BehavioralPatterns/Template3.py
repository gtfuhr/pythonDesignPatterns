"""
Template.

Here is complete example of the Template implementation.
"""

from abc import ABCMeta, abstractmethod


class Trip(metaclass=ABCMeta):
    """Abstract class."""

    def __init__(self):
        """Pass initialization."""
        pass

    @abstractmethod
    def setTransport(self):
        """Abstract step method for the template method."""
        pass

    @abstractmethod
    def day1(self):
        """Abstract step method for the template method."""
        pass

    @abstractmethod
    def day2(self):
        """Abstract step method for the template method."""
        pass

    @abstractmethod
    def day3(self):
        """Abstract step method for the template method."""
        pass

    @abstractmethod
    def returnHome(self):
        """Abstract step method for the template method."""
        pass

    def ititnerary(self):
        """Template method."""
        self.setTransport()
        self.day1()
        self.day2()
        self.day3()
        self.returnHome()


class VeniceTrip(Trip):
    """Concrete implementation of the Template Abstract Class."""

    def setTransport(self):
        """Concrete step method for the template method."""
        print("Take a boat and find your way in the Grand Canal")

    def day1(self):
        """Concrete step method for the template method."""
        print("Visit st Mark's Basilica...")

    def day2(self):
        """Concrete step method for the template method."""
        print("Appreciate Doge's Palace")

    def day3(self):
        """Concrete step method for the template method."""
        print("Enjoy the food near Rialto Bridge")

    def returnHome(self):
        """Concrete step method for the template method."""
        print("Get souvernirs for friends and get back.")


class MaldivesTrip(Trip):
    """Concrete implementation of the Template Abstract Class."""

    def setTransport(self):
        """Concrete step method for the template method."""
        print("On foot.")

    def day1(self):
        """Concrete step method for the template method."""
        print("Enjoy the marine.")

    def day2(self):
        """Concrete step method for the template method."""
        print("Go for the water sports.")

    def day3(self):
        """Concrete step method for the template method."""
        print("Relax on the beach and enjoy the sun.")

    def returnHome(self):
        """Concrete step method for the template method."""
        print("Dont feel like leaving the beach.")


class TravelAgency:
    """Client class of a concrete implementation of the Template algo."""

    def arrange_trip(self):
        """Call it on the main."""
        choice = int(input("""Select the travel by inserting its code number:
                       1 -> Historical
                       2 -> Beach\n"""))
        if choice == 1:
            self.trip = VeniceTrip()
            self.trip.ititnerary()
        elif choice == 2:
            self.trip = MaldivesTrip()
            self.trip.ititnerary()


TravelAgency().arrange_trip()
