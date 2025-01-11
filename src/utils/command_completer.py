"""This module contains the CommandCompleter class."""

from prompt_toolkit.completion import Completer, Completion


class CommandCompleter(Completer):
    """The class to provide command completions."""

    def __init__(self, commands):
        self.commands = commands

    def get_completions(self, document, complete_event):
        if document.cursor_position == 0 or " " not in document.text_before_cursor:
            word_before_cursor = document.get_word_before_cursor()
            for command in self.commands:
                if command.startswith(word_before_cursor):
                    yield Completion(command, start_position=-len(word_before_cursor))
