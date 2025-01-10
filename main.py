from src.utils.persistence import save_data, load_data
from src.utils.utils import parse_input
from src.contacts.address_book import AddressBook
from src.notes.notebook import NoteBook
from src.contacts.commands import add_contact, change_contact,delete_contact, show_phone, add_birthday, show_birthday, birthdays
from src.features.help import print_help
from src.notes.note_commands import add_note, find_notes_interactive
contacts_file_name = "addressbook.pkl"
notes_file_name = "notebook.pkl"

def main():
    book = load_data(contacts_file_name, AddressBook)
    notebook = load_data(notes_file_name, NoteBook)
    print("Welcome to the assistant bot!")
    try:
        while True:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, book))
            elif command == "change":
                print(change_contact(args, book))
            elif command == "delete":
                print(delete_contact(args, book))
            elif command == "phone":
                print(show_phone(args, book))
            elif command == "all":
                book.display_all_contacts()
            elif command == "add-birthday":
                print(add_birthday(args, book))
            elif command == "show-birthday":
                print(show_birthday(args, book))
            elif command == "birthdays":
                print(birthdays(args, book))
            elif command == "add-note":
                print(add_note(args, notebook))
            elif command == "all-notes":
                notebook.display_all_notes()
            elif command == "find-notes":
                print(find_notes_interactive(args, notebook))
            elif command == "help":
                print_help()
            else:
                print("Invalid command.")
    finally:
        save_data(book, contacts_file_name)
        save_data(notebook, notes_file_name) 

if __name__ == "__main__":
    main()
