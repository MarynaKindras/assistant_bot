"""
This is the main file of the assistant bot. It is responsible for the interaction with the user.
"""
from src.utils.promt_session import get_promt_session
from src.utils.command_completer import CommandCompleter
from src.constants.controls import COMMANDS
from src.constants.file_names import CONTACTS_FILE_NAME, NOTES_FILE_NAME
from src.notes.note_commands import add_note, find_notes_interactive
from src.features.help import print_help
from src.utils.persistence import save_data, load_data
from src.utils.utils import parse_input
from src.contacts.address_book import AddressBook
from src.notes.notebook import NoteBook
from src.contacts.commands import add_contact, change_contact, delete_contact, show_contact, add_birthday, show_birthday, birthdays


def main():
    """
    The main function to run the assistant bot.
    """
    # Load data from files
    book = load_data(CONTACTS_FILE_NAME, AddressBook)
    notebook = load_data(NOTES_FILE_NAME, NoteBook)
    print("Welcome to the assistant bot!")

    # Initialize the PromptSession with the CommandCompleter
    command_completer = CommandCompleter(COMMANDS.values())
    session = get_promt_session(command_completer)

    try:
        while True:
            try:
                # Get user input
                user_input = session.prompt("Enter a command: ", default="")
                command, *args = parse_input(user_input)

                # Check the command and execute the corresponding function
                if command in COMMANDS.values():
                    if command == COMMANDS['hello']:
                        print("How can I help you?")
                    elif command == COMMANDS['add_contact']:
                        print(add_contact(args, book))
                    elif command == COMMANDS['change_contact']:
                        print(change_contact(args, book))
                    elif command == COMMANDS['delete_contact']:
                        print(delete_contact(args, book))
                    elif command == COMMANDS['show_contact']:
                        print(show_contact(args, book))
                    elif command == COMMANDS['all_contacts']:
                        book.display_all_contacts()
                    elif command == COMMANDS['add_birthday']:
                        print(add_birthday(args, book))
                    elif command == COMMANDS['show_birthday']:
                        print(show_birthday(args, book))
                    elif command == COMMANDS['birthdays']:
                        print(birthdays(args, book))
                    elif command == COMMANDS['add_note']:
                        print(add_note(args, notebook))
                    elif command == COMMANDS['all_notes']:
                        notebook.display_all_notes()
                    elif command == COMMANDS['find_notes']:
                        print(find_notes_interactive(args, notebook))
                    elif command == COMMANDS['help']:
                        print_help()
                    elif command in [COMMANDS['close'], COMMANDS['exit']]:
                        print("Good bye!")
                        break
                    else:
                        print("Invalid command.")
                else:
                    print("Invalid command.")
            except KeyboardInterrupt:
                print("\nUse 'close' or 'exit' to quit.")
    finally:
        # Save data to files before exiting
        save_data(book, CONTACTS_FILE_NAME)
        save_data(notebook, NOTES_FILE_NAME)


if __name__ == "__main__":
    main()
