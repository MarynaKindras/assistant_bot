"""The module with the utility functions."""


def input_error(func):
    """The decorator to handle exceptions in the functions."""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError as e:
            return str(e)
        except IndexError:
            return "Invalid number of arguments."
    return inner


def parse_input(user_input):
    """The function to parse the user input."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
