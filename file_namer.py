def generate_filename(name, cert_id):

    clean_name = name.strip().replace(" ", "_")

    filename = f"{clean_name}_{cert_id}.png"

    return filename