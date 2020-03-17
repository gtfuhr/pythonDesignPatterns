import unittest


class TestAnimal(unittest.TestCase):
    """Class that tests the Animal Class with an animal of name
Rex, weight 20 and sound bark"""

    def setUp(self):
        self.animal = Animal(name="Rex", weight=20, sound="bark")

    def tearDown(self):
        del self.animal

    def test_animal_name(self):
        self.assertEqual(self.animal.get_name(), "Rex")

    def test_animal_sound(self):
        self.assertEqual(self.animal.get_sound(), "bark")

    def test_animal_weight(self):
        self.assertEqual(self.animal.get_weight(), 20)

    def test_animal_weight_error(self):
        with self.assertRaises(AttributeError) as context_manager:
            self.animal.set_weight(-2)
        exception = context_manager.exception
        self.assertEqual(str(exception), "Negative animal weight.")


class Animal:
    """This class defines an animal that has a name, weight and sound"""
    __version__ = "0.1"

    def __init__(self, name, weight, sound):
        self.set_name(name)
        self.set_sound(sound)
        self.set_weight(weight)

    def set_name(self, name):
        if type(name) == str:
            self.name = name

    def get_name(self):
        return self.name

    def set_sound(self, sound):
        if type(sound) == str:
            self.sound = sound

    def get_sound(self):
        return self.sound

    def set_weight(self, new_weight):
        if new_weight > 0:
            self.weight = new_weight
        else:
            raise AttributeError("Negative animal weight.")

    def get_weight(self):
        return self.weight
