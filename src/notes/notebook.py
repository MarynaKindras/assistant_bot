from collections import UserDict
from datetime import datetime, timedelta

class NoteBook(UserDict):
    def add_note(self, note):
        if note.title.value in self.data:
            raise ValueError("Note with this title already exists.")
        self.data[note.title.value] = note
    
    def display_all_notes(self):
        if not self.data:
            print("The notebook book is empty.")
        print("All notes:")
        for note in self.data.values():
                print(note)
                print()

    
   
        
    