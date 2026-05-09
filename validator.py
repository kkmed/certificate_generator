def validate_data(records):
    valid_data = []

    for record in records:
        if not record["name"]:
            continue
        if not str(record["age"]).isdigit():
            continue
        if "@" not in record["email"]:
            continue

        valid_data.append(record)

    return valid_data
