"""
Observer module.

The Observer module is capable of modelling data relationships such as the
e-mail or push-notification service of a blog or app.
The observer Design Patter defines this one-to-many relationship of
subject->observers (news blog -> interested readers).

This module provides a more complete example of the Observer design pattern.
"""


from abc import ABCMeta, abstractmethod


class NewsPublisher:
    """Subject class."""

    def __init__(self):
        """
        News Publisher.

        Initialize an subscription list and latest news in the subject class.
        """
        self.__subscribers = []
        self.__latestNews = None

    def attach(self, subscriber):
        """Register a new subscriber in the subscription list."""
        self.__subscribers.append(subscriber)

    def detach(self):
        """Delete a subscriber from the subscription list."""
        return self.__subscribers.pop()

    def subscribers(self):
        """Return the subscribers names from the subscription list."""
        return [type(x).__name__ for x in self.__subscribers]

    def notifySubscribers(self, *args, **kwargs):
        """Notify every subscriber in the subscription list."""
        for sub in self.__subscribers:
            sub.update()

    def addNews(self, news):
        """Assign news to the latest news variable."""
        self.__latestNews = news

    def getNews(self):
        """Return a string with the latest news."""
        return "Got news: " + str(self.__latestNews)


class Subscriber(metaclass=ABCMeta):
    """Observer Abstract class."""

    @abstractmethod
    def update(self):
        """Abstract method."""
        pass


class SMSSubscriber:
    """SMS Subscriber class."""

    def __init__(self, publisher):
        """Register itself in the subscription list of the NewsPublisher."""
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        """Notify the Subscriber with news from the NewsPublisher."""
        print(type(self).__name__, self.publisher.getNews())


class EmailSubscriber:
    """E-mail Subscriber class."""

    def __init__(self, publisher):
        """Register itself in the subscription list of the NewsPublisher."""
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        """Notify the Subscriber with news from the NewsPublisher."""
        print(type(self).__name__, self.publisher.getNews())


class AnyOtherSubscriber:
    """Any other Subscriber class."""

    def __init__(self, publisher):
        """Register itself in the subscription list of the NewsPublisher."""
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        """Notify the Subscriber with news from the NewsPublisher."""
        print(type(self).__name__, self.publisher.getNews())


if __name__ == '__main__':
    news_publisher = NewsPublisher()

    for Subscribers in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        Subscribers(news_publisher)
    print("\nSubscribers:", news_publisher.subscribers())

    news_publisher.addNews("Hello World, here I come with the news!")
    news_publisher.notifySubscribers()

    print("\nDetached:", type(news_publisher.detach()).__name__)
    print("\nSubscribers: ", news_publisher.subscribers())

    news_publisher.addNews("My second news!")
    news_publisher.notifySubscribers()
