from datetime import datetime
import re

class NoteField:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Title(NoteField):
    def __init__(self, value):
        if not value:
            raise ValueError("Title is required.")
        super().__init__(value)

class Text(NoteField):
    def __init__(self, value):
        self.validate(value)
        super().__init__(value)

    @staticmethod
    def validate(value):
        if not value:
            raise ValueError("The note must contain at least one symbol.")
        
class Tags:
    def __init__(self, tags_string=None):
       
        self.tags = []
        if tags_string:
            self.add_tags_from_string(tags_string)

    def add_tags_from_string(self, tags_string):
        tag_list = [tag.strip() for tag in tags_string.split(",") if tag.strip()]
        self.tags.extend(tag_list)

    def __str__(self):
        return ', '.join(self.tags)
        
