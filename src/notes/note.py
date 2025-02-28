"""
This module defines the Note class and its associated fields for managing notes.

The Note class provides functionality to:
- Store and validate a note's title, text, and tags.
- Represent the note as a formatted string.

Classes:
    Note: Represents a single note with a title, text, and optional tags.

Dependencies:
    Title, Text, Tags: Classes for validating and handling specific fields of a note.
"""

from src.notes.note_fields import Title, Text, Tags
# Importing Title, Text, and Tags classes for handling note fields (titles, text, tags)


class Note:
    """
    A class representing a single note with a title, text, and optional tags.

    Attributes:
        title: The title of the note, stored as a Title object.
        text: The text content of the note, stored as a Text object.
        tags: The tags associated with the note, stored as a Tags object.

    Methods:
        __str__(): Returns a formatted string representation of the note.
    """

    def __init__(self, title, text, tags=None):
        """
        Initializes a Note object with the given title, text, and optional tags.
        Validates the title and text using their respective classes.

        Args:
            title: The title of the note as a string.
            text: The text content of the note as a string.
            tags: A comma-separated string of tags (optional).
        """
        self.title = Title(title)  # Validates and sets the note's title
        self.text = Text(text)  # Validates and sets the note's text
        # Creates a Tags object if tags are provided, otherwise initializes an empty Tags object
        self.tags = Tags(tags) if tags else Tags()

    def __str__(self):
        """
        Returns a formatted string representation of the note, including title, text, and tags.

        Returns:
            str: A string representation of the note.
        """
        tags = str(self.tags) if self.tags.tags else "No tags"
        return f"Title: {self.title.value}\nText: {self.text.value}\nTags: {tags}"
