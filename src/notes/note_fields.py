class NoteField:
    """
    Base class for all note fields such as title and text.
    
    Attributes:
        value: The value of the field.
    
    Methods:
        __str__(): Returns the string representation of the field.
    """
    def __init__(self, value):
        self.value = value  # Assign the value to the field

    def __str__(self):
        """
        Returns the string representation of the field.

        Returns:
            str: The field's value as a string.
        """
        return str(self.value)


class Title(NoteField):
    """
    Represents the title of a note.

    Inherits from NoteField and adds validation for the title.
    """
    def __init__(self, value):
        """
        Initializes the Title object with the given value.

        Args:
            value: The title of the note.

        Raises:
            ValueError: If the title is empty.
        """
        if not value:
            raise ValueError("Title is required.")  # Validate that title is not empty
        super().__init__(value)  # Initialize the parent class


class Text(NoteField):
    """
    Represents the text content of a note.

    Inherits from NoteField and adds validation for the text.
    """
    def __init__(self, value):
        """
        Initializes the Text object with the given value.

        Args:
            value: The text content of the note.

        Raises:
            ValueError: If the text content is empty.
        """
        self.validate(value)  # Validate the text content
        super().__init__(value)  # Initialize the parent class

    @staticmethod
    def validate(value):
        """
        Validates the text content of the note.

        Args:
            value: The text content to validate.

        Raises:
            ValueError: If the text content is empty.
        """
        if not value:
            raise ValueError("The note must contain at least one symbol.")


class Tags:
    """
    Represents the tags associated with a note.

    Attributes:
        tags: A list of tags associated with the note.

    Methods:
        add_tags_from_string(tags_string): Parses and adds tags from a comma-separated string.
        __str__(): Returns a comma-separated string representation of the tags.
    """
    def __init__(self, tags_string=None):
        """
        Initializes the Tags object. If a tags string is provided,
        parses and adds the tags to the tags list.

        Args:
            tags_string: A comma-separated string of tags (optional).
        """
        self.tags = []  # Initialize an empty list of tags
        if tags_string:
            self.add_tags_from_string(tags_string)  # Parse and add tags if provided

    def add_tags_from_string(self, tags_string):
        """
        Parses a comma-separated string and adds valid tags to the tags list.

        Args:
            tags_string: A comma-separated string of tags.
        """
        # Strip whitespace and ignore empty tags
        tag_list = [tag.strip() for tag in tags_string.split(",") if tag.strip()]
        self.tags.extend(tag_list)  # Add the parsed tags to the list

    def __str__(self):
        """
        Returns a string representation of the tags, joined by commas.

        Returns:
            str: A comma-separated string of tags.
        """
        return ', '.join(self.tags)
