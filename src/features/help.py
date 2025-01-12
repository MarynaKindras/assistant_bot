"""This module contains the function to display the help message."""

from colorama import Fore, Style, init
from tabulate import tabulate
from src.constants.controls import COMMANDS

init(autoreset=True)


def print_help():
    """
    This function prints a help message listing available commands,
    their parameters, and descriptions. It also applies colors to the output
    using the `colorama` library and formats the data into a table using
    the `tabulate` library.
    """
    help_data = [
        (COMMANDS['hello'], "", "Greet the assistant."),
        (COMMANDS['add_contact'], "<name> <phone>",
         "Add a new contact with the given name and phone number."),
        (COMMANDS['change_contact'], "<name>",
         "Change any field for the existing contact."),
        (COMMANDS['delete_contact'], "<name>", "Delete existing contact."),
        (COMMANDS['show_contact'], "<name>",
         "Show the phone numbers for the given contact."),
        (COMMANDS['all_contacts'], "",
         "Display all contacts in the address book."),
        (COMMANDS['add_birthday'], "<name> <date>",
         "Add a birthday for the given contact (format: DD.MM.YYYY)."),
        (COMMANDS['show_birthday'], "<name>",
         "Show the birthday of the given contact."),
        (COMMANDS['birthdays'], "<days>",
         "Show contacts with birthdays in the next given number of days."),
        (COMMANDS['add_note'], "",
         "Add a new note. You will be prompted to enter the title, text, and tags."),
        (COMMANDS['all_notes'], "", "Display all notes in the notebook."),
        (COMMANDS['find_notes'], "",
         "Search notes by title, text, or tags. Then select a note to edit or delete."),
        (COMMANDS['help'], "", "Show this help message."),
        (f"{COMMANDS['close']}, {COMMANDS['exit']}",
         "", "Exit the assistant bot.")
    ]

    color_data = [
        (f"{Fore.CYAN}{command}", f"{Fore.GREEN}{parameters}",
         f"{Fore.LIGHTBLACK_EX}{description}")
        for command, parameters, description in help_data
    ]

    headers = [f"{Fore.CYAN}Available commands:",
               f"{Fore.CYAN}Parameters:", f"{Fore.CYAN}Description"]

    table = tabulate(color_data, headers=headers, tablefmt="firstrow")

    print(table)
    print(Style.RESET_ALL)
