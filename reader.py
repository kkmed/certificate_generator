import json


def read_manual_input():
    return {
        "organization_name": input("Organization Name: "),
        "organization_tagline": input("Tagline: "),
        "certificate_title": input("Certificate Title: "),
        "subtitle": input("Subtitle: "),
        "recipient_name": input("Recipient Name: "),
        "body_line": input("Body Line: "),
        "event_name": input("Event Name: "),
        "organized_by": input("Organized By: ")
    }


def read_json_file(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except Exception as e:
        print("Error reading JSON:", e)
        return {}
