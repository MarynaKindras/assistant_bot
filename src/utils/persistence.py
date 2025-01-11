"""This module provides functions for saving and loading data using the pickle module."""

import pickle


def save_data(data, filename):
    """Save the data to a file using the pickle module."""
    with open(filename, "wb") as f:
        pickle.dump(data, f)


def load_data(filename, default_factory=None):
    """Load the data from a file using the pickle module."""
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError as exc:
        if default_factory is not None:
            return default_factory()
        raise FileNotFoundError(
            f"The file '{filename}' was not found, and no default factory was provided.") from exc
