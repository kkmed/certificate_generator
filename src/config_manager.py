import json
import os

CONFIG_FILE = "data/config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        except Exception as e:
            print("Could not load config:", e)
    return {}

def save_config(config_data):
    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump(config_data, f, indent=4)
        return True
    except Exception as e:
        print("Could not save config:", e)
        return False
