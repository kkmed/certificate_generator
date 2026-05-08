REQUIRED_FIELDS = [
    "organization_name",
    "certificate_title",
    "recipient_name",
    "event_name"
]


def validate_data(data):

    for field in REQUIRED_FIELDS:

        if field not in data or not data[field].strip():
            print(f"Missing required field: {field}")
            return False

    return True
