def format_data(records):

    formatted = []

    for r in records:

        formatted.append({

            "Name": r.get("name", "").strip().title(),

            "Email": r.get("email", "").strip().lower()

        })

    return formatted