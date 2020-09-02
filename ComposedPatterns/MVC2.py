"""
MVC2.

This is another example of the MVC Design Pattern.
"""


class Model(object):
    """Model - Controls the logical structure of the application."""

    def logic(self):
        """Return the business logic."""
        print("Model: Crunching data as per business logic")


class View(object):
    """Model - Controls the logical structure of the application."""

    def list_services(self, services):
        """Return the business logic."""
        for svc in services:
            print(svc, ' ')

    def list_pricing(self, services):
        """Return the business logic."""
        for svc in services:
            print('For', Model.services[svc]['number'],
                  svc, "message you pay $",
                  Model.services[svc]['price'])


class Controller(object):
    """Controls the communication between the View and the Model."""

    def __init__(self):
        """Initialize the Controller."""
        self.model = Model()
        self.view = View()

    def get_services(self):
        """Get services."""
        services = self.model.services.keys()
        return(self.view.list_services(services))

    def get_pricing(self):
        """Get services prices."""
        services = self.model.services.keys()
        return (self.view.list_pricing(services))


class Client(object):
    """Client of the application."""

    controller = Controller()
    print("Services provided:")
    controller.get_services()
    print("Pricing for services:")
    controller.get_pricing()


client = Client()
