import json

def load_file(path):
    with path.open("r") as file:
        data = json.load(file)
        return data

def save_file(path, data):
    with path.open("w") as file:
        json.dump(data, file, indent=2)