# Welcome to Personal Assistant Bot: Your Digital Organizer

The Personal Assistant is a versatile application designed to simplify your life by managing your contacts and notes.

## Key Features:

**Contact Management:** Add, edit, and delete contacts with detailed information including name, address, phone number, email, and birthday. Search for contacts by name or birthday. Ensure data accuracy with built-in validation for phone numbers and email addresses.

**Note Management:** Create, edit, and delete text-based notes. Easily search for specific notes.

## Get Started:

### :cd: Installation:

1. Clone the repository:

   ```bash
   git clone https://github.com/MarynaKindras/assistant_bot
   cd assistant_bot
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/Scripts/activate
   ```

3. Before running the bot, install the necessary dependencies using the following command:

   ```bash
   pip install -r requirements.txt
   ```

### :arrow_forward: Usage:

Run the main script to start the application:

```bash
python main.py
```

## Commands list:

### :computer: Main commands:

| Available commands: | Parameters: | Description:            |
| ------------------- | ----------- | ----------------------- |
| hello               |             | Greet the assistant.    |
| help                |             | Show this help message. |
| close or exit       |             | Exit the assistant bot. |

### :calling: Contacts commands:

| Available commands: | Parameters:                                   | Description:                                                                                                                                      |
| ------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| add-contact         | < name > < phone >                            | Add a new contact with the given name (multi-word) and phone number. You will be prompted to enter the address (multi-words), birthday, and email.|
| change-contact      | < name > < phone > < old_phone > < new_value >| Change the phone number for an existing contact.                                                                                                  |
| change-contact      | < name > < field > < new_value >              | Change field: address (multi-words), birthday, or email for the existing contact.                                                                 |
| delete-contact      | < name >                                      | Delete existing contact.                                                                                                                          |
| show-contact        | < name > or < email >                         | Show the full contact information.                                                                                                                |
| all-contacts        |                                               | Display all contacts in the address book.                                                                                                         |

### :calendar: Birthday commands:

| Available commands: | Parameters:       | Description:                                                   |
| ------------------- | ----------------- | -------------------------------------------------------------- |
| add-birthday        | < name > < date > | Add a birthday for the given contact (format: DD.MM.YYYY).     |
| show-birthday       | < name >          | Show the birthday of the given contact.                        |
| birthdays           | < days >          | Show contacts with birthdays in the next given number of days. |

### :label: Notes commands:

| Available commands: | Parameters: | Description:                                                                |
| ------------------- | ----------- | --------------------------------------------------------------------------- |
| add-note            |             | Add a new note. You will be prompted to enter the title, text, and tags.    |
| all-notes           |             | Display all notes in the notebook.                                          |
| find-notes          |             | Search notes by title, text, or tags. Then select a note to edit or delete. |

## Usage example:

![Usage](./assets/Usage_example_01.png)

## Technologies:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Development Team:

- [Kindras Maryna](https://github.com/MarynaKindras)
- [Chernous Vitaliy](https://github.com/vitalii-kyiv)
- [Tytenko Dima](https://github.com/dimatytenko)
- [Sabinina Iryna](https://github.com/IrynaSabinina)
