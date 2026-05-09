def format_data(data):

    formatted = {}

    for key, value in data.items():

        formatted[key] = value.strip()

    # special formatting
    formatted["recipient_name"] = formatted["recipient_name"].title()
    formatted["organization_name"] = formatted["organization_name"].title()

    return formatted
