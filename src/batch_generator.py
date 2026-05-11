from reader import read_csv_file
from validator import validate_data
from formatter import format_data

from id_generator import generate_certificate_id
from folder_manager import create_output_folder
from file_namer import generate_filename

from generator import generate_certificate, TEMPLATE_CONFIGS
from emailer import send_email
import json

def run_batch_generation(cert_data, template_id, generate_certs=True, send_emails=True):
    # STEP 1 → READ CSV
    records = read_csv_file("data/students.csv")

    # STEP 2 → VALIDATE DATA
    valid_records = validate_data(records)

    # STEP 3 → FORMAT DATA
    formatted_records = format_data(valid_records)

    # STEP 4 → CREATE OUTPUT FOLDER
    output_folder = create_output_folder()

    # GET TEMPLATE DETAILS
    template_config = TEMPLATE_CONFIGS.get(str(template_id))
    if not template_config:
        print(f"Error: Invalid template ID '{template_id}'.")
        return

    image_path = template_config["image_path"]
    layout = template_config.get("layout", {})
    style = template_config.get("style", {})

    # STEP 5 → LOOP THROUGH STUDENTS
    for index, student in enumerate(formatted_records, start=1):

        # GENERATE CERTIFICATE ID
        cert_id = generate_certificate_id(index)

        # GENERATE FILE NAME
        filename = generate_filename(student["Name"], cert_id)

        output_path = f"{output_folder}/{filename}"

        # CERTIFICATE DATA
        student_cert_data = cert_data.copy()
        student_cert_data["recipient_name"] = student["Name"]
        student_cert_data["cert_id_value"] = cert_id

        # GENERATE CERTIFICATE
        if generate_certs:
            generate_certificate(
                student_cert_data,
                image_path,
                output_path,
                style=style,
                layout=layout
            )
            print(f"\nCertificate generated for {student['Name']}")

        # SEND EMAIL
        with open("data/config.json","r") as file:
            data = json.load(file)
        if send_emails:
            send_email(
                student["Email"],
                student["Name"],
                data["organization_name"],
                output_path
            )