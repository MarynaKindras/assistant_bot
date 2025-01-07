import pickle

def save_data(data, filename):
    with open(filename, "wb") as f:
        pickle.dump(data, f)

def load_data(filename, default_factory=None):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        if default_factory is not None:
            return default_factory()
        raise FileNotFoundError(f"The file '{filename}' was not found, and no default factory was provided.")