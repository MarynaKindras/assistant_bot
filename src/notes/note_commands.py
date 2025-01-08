from ..utils.utils import input_error
from .note import Note



@input_error
def add_note(args, notebook):
    # if len(args) < 2:
    title = input("Enter the title of the note: ").strip()
    if not title:
        raise ValueError("Title cannot be empty.")
    text = input("Enter the text of the note: ").strip()
    if not text:
        raise ValueError("Text cannot be empty.")
        
    tags_input = input("Would you like to add tags? (Enter tags separated by commas or press Enter to skip): ").strip()
    tags = tags_input.split(",") if tags_input else []

    # args = [title, text] + tags
    # title = args[0]
    # text = args[1]
    # tags = args[2:] if len(args) > 2 else None

    note = Note(title, text, ", ".join(tags) if tags else None)
    notebook.add_note(note)

    return f"Note '{title}' added successfully!"
