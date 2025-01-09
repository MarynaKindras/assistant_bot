from collections import UserDict

class NoteBook(UserDict):
    def add_note(self, note):
        if note.title.value in self.data:
            raise ValueError("Note with this title already exists.")
        self.data[note.title.value] = note

    def display_all_notes(self):
        if not self.data:
            print("The notebook is empty.")
            return
        print("All notes:")
        for note in self.data.values():
            print(note)
            print()

    def find_notes(self, search_term, search_in):
        """
        Загальний метод для пошуку нотаток.
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
                    any(search_term.lower() in tag.lower() for tag in note.tags.tags)
            ]
        else:
            raise ValueError("Invalid search field.")