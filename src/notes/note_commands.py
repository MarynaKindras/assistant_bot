from ..utils.utils import input_error
from .note import Note

@input_error
def add_note(args, notebook):
    title = input("Enter the title of the note: ").strip()
    if not title:
        raise ValueError("Title cannot be empty.")
    text = input("Enter the text of the note: ").strip()
    if not text:
        raise ValueError("Text cannot be empty.")
        
    tags_input = input("Would you like to add tags? (Enter tags separated by commas or press Enter to skip): ").strip()
    tags = tags_input.split(",") if tags_input else []

    note = Note(title, text, ", ".join(tags) if tags else None)
    notebook.add_note(note)

    return f"Note '{title}' added successfully!"

@input_error
def delete_note_by_title(args, notebook):
    title = input("Enter the title of the note to delete: ").strip()
    if not title:
        raise ValueError("Title cannot be empty.")

    if title in notebook.data:
        del notebook.data[title]
        return f"Note '{title}' deleted successfully."
    return f"Note '{title}' not found."

@input_error
def find_notes_interactive(args, notebook):
    search_term = input("Enter the search term: ").strip()
    if not search_term:
        raise ValueError("Search term cannot be empty.")

    search_in = input("Where do you want to search? (title, text, tags, all): ").strip().lower()
    if search_in not in {"title", "text", "tags", "all"}:
        raise ValueError("Invalid search option. Choose from 'title', 'text', 'tags', or 'all'.")

    results = notebook.find_notes(search_term, search_in)

    if not results:
        return "No matching notes found."

    print(f"Found {len(results)} matching note{'s' if len(results) > 1 else ''}:\n")
    for idx, note in enumerate(results, start=1):
        print(f"{idx}. {note}\n")

    action = input("Would you like to edit or delete a note? (edit/delete/skip): ").strip().lower()
    if action not in {"edit", "delete", "skip"}:
        return "Invalid action. Skipping."

    if action == "skip":
        return "No action taken."

    try:
        index = int(input(f"Enter the note number (1-{len(results)}): ").strip())
        if index < 1 or index > len(results):
            raise ValueError
        note_to_edit = results[index - 1]
    except ValueError:
        return "Invalid note number. Skipping."

    if action == "delete":
        return delete_note_by_title([note_to_edit.title.value], notebook)
    elif action == "edit":
        del notebook.data[note_to_edit.title.value]
        add_note([], notebook)
        return "Note edited successfully."
