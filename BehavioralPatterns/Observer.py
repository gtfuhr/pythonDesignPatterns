"""
Observer module.

The Observer module is capable of modelling data relationships such as the
e-mail or push-notification service of a blog or app.
The observer Design Patter defines this one-to-many relationship of
subject->observers (news blog -> interested readers).
"""


class Subject:
    """Subject class."""

    def __init__(self):
        """Initialize an empty subscription list in the subject class."""
        self.__observers = []

    def register(self, observer):
        """Register a new observer in the subscription list."""
        self.__observers.append(observer)

    def notifyAll(self, *args, **kwargs):
        """Notify every observer in the subscription list."""
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)


class Observer1:
    """First Observer class."""

    def __init__(self, subject):
        """Register itself in the subscription list of the Subject."""
        subject.register(self)

    def notify(self, subject, *args):
        """Notify the Observer with news from the Subject."""
        print(type(self).__name__, ':: Got', args, ' From ', subject)


class Observer2:
    """Second Observer class."""

    def __init__(self, subject):
        """Register itself in the subscription list of the Subject."""
        subject.register(self)

    def notify(self, subject, *args):
        """Notify the Observer with news from the Subject."""
        print(type(self).__name__, ':: Got', args, ' From ', subject)


subject = Subject()
observer1 = Observer1(subject)
observer2 = Observer2(subject)
subject.notifyAll("New post!")
