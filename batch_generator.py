from reader import read_csv_file
from validator import validate_data
from formatter import format_data

from id_generator import generate_certificate_id
from folder_manager import create_output_folder
from file_namer import generate_filename

from generator import generate_certificate
from emailer import send_email


# STEP 1 → READ CSV
records = read_csv_file("students.csv")


# STEP 2 → VALIDATE DATA
valid_records = validate_data(records)


# STEP 3 → FORMAT DATA
formatted_records = format_data(valid_records)


# STEP 4 → CREATE OUTPUT FOLDER
output_folder = create_output_folder()


# STEP 5 → LOOP THROUGH STUDENTS
for index, student in enumerate(formatted_records, start=1):

    # GENERATE CERTIFICATE ID
    cert_id = generate_certificate_id(index)

    # GENERATE FILE NAME
    filename = generate_filename(student["Name"], cert_id)

    output_path = f"{output_folder}/{filename}"


    # CERTIFICATE DATA
    certificate_data = {

        # HEADER
        "organization_name": "ABC University",
        "organization_tagline": "Excellence in Education",

        # TITLE
        "certificate_title": "Certificate of Participation",
        "subtitle": "This certificate is proudly presented to",

        # STUDENT NAME
        "recipient_name": student["Name"],

        # BODY
        "body_line": "for participating successfully in",
        "event_name": "Python Workshop 2026",
        "organized_by": "organized by ABC University",

        # DETAILS
        "date_label": "Date",
        "date_value": "May 2026",

        "venue_label": "Venue",
        "venue_value": "Hyderabad",

        "cert_id_label": "Certificate No.",
        "cert_id_value": cert_id,

        # SIGNATURES
        "dignitary_1_name": "Dr. Rao",
        "dignitary_1_title": "Director",

        "dignitary_2_name": "Prof. Sharma",
        "dignitary_2_title": "Dean",

        "dignitary_3_name": "Ms. Iyer",
        "dignitary_3_title": "Coordinator",

        # FOOTER
        "footer_text": "abc@university.com · www.abcuniversity.com"
    }


    # GENERATE CERTIFICATE
    generate_certificate(
        certificate_data,
        "classic",
        output_path
    )

    print(f"\nCertificate generated for {student['Name']}")


    # SEND EMAIL
    send_email(
        student["Email"],
        student["Name"],
        output_path
    )

    