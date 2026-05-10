def validate_data(records):

    valid_data = []

    for record in records:

        if not record.get("name"):
            continue

        if "@" not in record.get("email", ""):
            continue

        valid_data.append(record)

    return valid_data