from src.notes.note_fields import Title, Text, Tags

class Note:
    def __init__(self, title, text, tags=None):
        self.title = Title(title)
        self.text = Text(text)
        self.tags = Tags(tags) if tags else Tags()

    def __str__(self):
        tags = str(self.tags) if self.tags.tags else "No tags"
        return f"Title: {self.title.value}\nText: {self.text.value}\nTags: {tags}"

 