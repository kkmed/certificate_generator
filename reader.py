import csv


# -------------------------------
# MANUAL INPUT
# -------------------------------
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


# -------------------------------
# READ CSV FILE
# -------------------------------
def read_csv_file(file_path):

    try:

        with open(file_path, mode="r") as file:

            reader = csv.DictReader(file)

            for row in reader:
                return row

    except Exception as e:
        print("Error reading CSV:", e)

    return {}
