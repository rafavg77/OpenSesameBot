import os
import json

def load_config():
    root_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(root_path, "config.json")

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"[!] File {config_path} not found!!")

    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    return config