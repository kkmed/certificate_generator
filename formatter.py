def format_data(records):
    formatted = []

    for r in records:
        formatted.append({
            "Name": r["name"].strip().title(),
            "Age": int(r["age"]),
            "Email": r["email"].lower()
        })

    return formatted
