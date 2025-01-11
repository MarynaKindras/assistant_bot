# Decorator for handling input-related errors
from ..utils.utils import input_error
from .note import Note  # Note class for creating and managing notes

# Function to add a note to the notebook


@input_error
def add_note(notebook):
    """
    Prompts the user to enter a title, text, and optional tags to create a new note.
    Validates that the title and text are not empty. Tags are optional and can be 
    entered as comma-separated values.
    Adds the new note to the notebook.

    Args:
        notebook: The notebook object to which the note will be added.

    Returns:
        str: A success message after adding the note.
    """
    title = input("Enter the title of the note: ").strip()
    if not title:
        raise ValueError("Title cannot be empty.")
    text = input("Enter the text of the note: ").strip()
    if not text:
        raise ValueError("Text cannot be empty.")

    tags_input = input(
        "Would you like to add tags? (Enter tags separated by commas or press Enter to skip): ").strip()
    tags = tags_input.split(",") if tags_input else []

    note = Note(title, text, ", ".join(tags) if tags else None)
    notebook.add_note(note)

    return f"Note '{title}' added successfully!"


# Function to delete a note by its title
@input_error
def delete_note_by_title(notebook):
    """
    Prompts the user to enter the title of a note to delete.
    Validates that the title is not empty and checks if the note exists in the notebook.
    Deletes the note if found.

    Args:
        notebook: The notebook object from which the note will be deleted.

    Returns:
        str: A success or error message depending on whether the note was found and deleted.
    """
    title = input("Enter the title of the note to delete: ").strip()
    if not title:
        raise ValueError("Title cannot be empty.")

    if title in notebook.data:
        del notebook.data[title]
        return f"Note '{title}' deleted successfully."
    return f"Note '{title}' not found."

# Function to find notes interactively based on a search term


@input_error
def find_notes_interactive(notebook):
    """
    Prompts the user to search for notes by a specified term and location (title, text, tags, or all).
    Displays the matching notes and allows the user to take an action (edit, delete, or skip).
    Validates input at each step and handles invalid actions gracefully.

    Args:
        notebook: The notebook object in which the search is performed.

    Returns:
        str: A message indicating the result of the operation (e.g., no matches, action taken).
    """
    search_term = input("Enter the search term: ").strip()
    if not search_term:
        raise ValueError("Search term cannot be empty.")

    search_in = input(
        "Where do you want to search? (title, text, tags, all): ").strip().lower()
    if search_in not in {"title", "text", "tags", "all"}:
        raise ValueError(
            "Invalid search option. Choose from 'title', 'text', 'tags', or 'all'.")

    results = notebook.find_notes(search_term, search_in)

    if not results:
        return "No matching notes found."

    print(
        f"Found {len(results)} matching note{'s' if len(results) > 1 else ''}:\n")
    for idx, note in enumerate(results, start=1):
        print(f"{idx}. {note}\n")

    # Ask the user for the next action
    action = input(
        "Would you like to edit or delete a note? (edit/delete/skip): ").strip().lower()
    if action not in {"edit", "delete", "skip"}:
        return "Invalid action. Skipping."

    if action == "skip":
        return "No action taken."

    try:
        # Validate and retrieve the note to edit or delete
        index = int(
            input(f"Enter the note number (1-{len(results)}): ").strip())
        if index < 1 or index > len(results):
            raise ValueError
        note_to_edit = results[index - 1]
    except ValueError:
        return "Invalid note number. Skipping."

    if action == "delete":
        # Delete the selected note
        return delete_note_by_title(notebook)
    elif action == "edit":
        # Edit the selected note by deleting the old note and adding a new one
        del notebook.data[note_to_edit.title.value]
        add_note(notebook)
        return "Note edited successfully."
