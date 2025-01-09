from colorama import Fore, Style, init
from tabulate import tabulate

init(autoreset=True)

def print_help():
    help_data = [
        ("hello", "", "Greet the assistant."),
        ("add", "<name> <phone>", "Add a new contact with the given name and phone number."),
        ("change", "<name> <phone>", "Change the phone number for an existing contact."),
        ("phone", "<name>", "Show the phone numbers for the given contact."),
        ("all", "", "Display all contacts in the address book."),
        ("add-birthday", "<name> <date>", "Add a birthday for the given contact (format: DD.MM.YYYY)."),
        ("show-birthday", "<name>", "Show the birthday of the given contact."),
        ("birthdays", "<days>", "Show contacts with birthdays in the next given number of days."),
        ("add-note", "", "Add a new note. You will be prompted to enter the title, text, and tags."),
        ("all-notes", "", "Display all notes in the notebook."),
        ("find-notes", "", "Search notes by title, text, or tags. Then select a note to edit or delete."),
        ("help", "", "Show this help message."),
        ("close, exit", "", "Exit the assistant bot.")
    ]
    
    color_data = [
      (f"{Fore.CYAN}{command}", f"{Fore.GREEN}{parameters}", f"{Fore.LIGHTBLACK_EX}{description}")
      for command, parameters, description in help_data
]

    headers = [f"{Fore.CYAN}Available commands:", f"{Fore.CYAN}Parameters:", f"{Fore.CYAN}Description"]
    
    table = tabulate(color_data, headers=headers, tablefmt="firstrow")
    
    print(table)
    print(Style.RESET_ALL)



