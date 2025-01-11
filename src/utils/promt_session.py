"""This module contains the function to create a prompt session with a custom style."""

from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style


custom_style = Style.from_dict({
    'prompt': '#00FFFF',
})


def get_promt_session(completer):
    """Return a PromptSession with the custom style and the provided completer."""
    return PromptSession(completer=completer, style=custom_style)
