"""Module that shows another use example of the Proxy Pattern."""

from abc import ABCMeta, abstractmethod


class You:
    """Client class that initialize the Proxy."""

    def __init__(self):
        """Call the Proxy and instantiate it."""
        print("You:: Lets buy the Denim shirt")
        self.debitCard = DebitCard()
        self.isPurchased = None

    def make_payment(self):
        """Make the payment."""
        self.isPurchased = self.debitCard.do_pay()

    def __del__(self):
        """Make the payment."""
        if self.isPurchased:
            print("You:: Wow! Denim shirt is mine :-) ")
        else:
            print("You:: I should earn more :-( ")


class Payment(metaclass=ABCMeta):
    """Subject Abstract class, to be implemented by Proxy and RealSubject."""

    @abstractmethod
    def do_pay(self):
        """Abstract method."""
        pass


class Bank(Payment):
    """Real Subject class."""

    def __init__(self):
        """Initialize the real subject class."""
        self.card = None
        self.account = None

    def __getAccount(self):
        # The number of the account is equal to the number of the card.
        self.account = self.card
        return self.account

    def __hasFunds(self):
        print("Bank:: Checking if Account", self.__getAccount(),
              "has enough funds")
        return True

    def setCard(self, card):
        """Receives the card and set it internally."""
        self.card = card

    def do_pay(self):
        """Real implementation of the abstract method from the Subject."""
        if self.__hasFunds():
            print("Bank:: Paying the merchant.")
            return True
        else:
            print("Bank:: Sorry, not enough funds.")
            return False


class DebitCard(Payment):
    """Proxy class."""

    def __init__(self):
        """Initialize the RealSubject class."""
        self.bank = Bank()

    def do_pay(self):
        """Proxy implementation of the abstract method from the Subject."""
        card = input("Proxy:: Punch in Card Number: ")
        self.bank.setCard(card)
        return self.bank.do_pay()


you = You()
you.make_payment()
del you
