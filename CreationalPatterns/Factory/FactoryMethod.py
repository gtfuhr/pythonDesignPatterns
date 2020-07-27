"""
Created on Mon Jul 27 13:28:11 2020.

@author: fuhr
"""

from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):
    """Abstract class to define the section of a profile."""

    @abstractmethod
    def describe(self):
        """Abstract method for the Section class."""
        pass


class PersonalSection(Section):
    """Section containing personal information."""

    def describe(self):
        """Show personal information."""
        print("Personal Section")


class AlbumSection(Section):
    """Section containing photo album data."""

    def describe(self):
        """Show photo album data."""
        print("Album Section")


class PatentSection(Section):
    """Section containing patents information."""

    def describe(self):
        """Show patenting information."""
        print("Patent Section")


class PublicationSection(Section):
    """Section containing publication information."""

    def describe(self):
        """Show publication information."""
        print("Publication Section")


class Profile(metaclass=ABCMeta):
    """Abstract Creator class."""

    def __init__(self):
        """Creator init."""
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        """Abstract method to be implemented."""
        pass

    def getSections(self):
        """Get the profile sections."""
        return self.sections

    def addSections(self, section):
        """Add a section to the profile sections."""
        self.sections.append(section)


class linkedin(Profile):
    """Concrete linkedin profile creator class."""

    def createProfile(self):
        """Concrete method to add actual sections to a lk profile."""
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())


class facebook(Profile):
    """Concrete facebook profile creator class."""

    def createProfile(self):
        """Concrete method to add actual sections to a fb profile."""
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())


if __name__ == '__main__':
    profile_type = input("Which Profile you'd like to create?\
                         [LinkedIn or Facebook]")
    profile = eval(profile_type.lower())()
    print("Creating Profile..", type(profile).__name__)
    print("Profile has section --", profile.getSections())
    