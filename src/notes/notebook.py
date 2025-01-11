from collections import UserDict


class NoteBook(UserDict):
    """
    A class to manage a collection of notes. Inherits from UserDict for dictionary-like behavior.
    """

    def add_note(self, note):
        """
        Adds a note to the notebook. Ensures that the title of the note is unique.

        Args:
            note: The Note object to be added to the notebook.

        Raises:
            ValueError: If a note with the same title already exists.
        """
        if note.title.value in self.data:
            raise ValueError("Note with this title already exists.")
        self.data[note.title.value] = note

    def display_all_notes(self):
        """
        Displays all notes in the notebook. If the notebook is empty, it notifies the user.
        """
        if not self.data:
            print("The notebook is empty.")
            return
        print("All notes:")
        for note in self.data.values():
            print(note)
            print()

    def find_notes(self, search_term, search_in):
        """
        Searches for notes based on a search term and a specified field.

        Args:
            search_term: The term to search for.
            search_in: The field to search in ('title', 'text', 'tags', or 'all').

        Returns:
            list: A list of Note objects that match the search criteria.

        Raises:
            ValueError: If an invalid search field is provided.
        """
        if search_in == "title":
            return [note for note in self.data.values() if search_term.lower() in note.title.value.lower()]
        elif search_in == "text":
            return [note for note in self.data.values() if search_term.lower() in note.text.value.lower()]
        elif search_in == "tags":
            return [note for note in self.data.values() if any(search_term.lower() in tag.lower() for tag in note.tags.tags)]
        elif search_in == "all":
            return [
                note for note in self.data.values()
                if search_term.lower() in note.title.value.lower() or
                search_term.lower() in note.text.value.lower() or
                any(search_term.lower() in tag.lower()
                    for tag in note.tags.tags)
            ]
        else:
            raise ValueError("Invalid search field.")
