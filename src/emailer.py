import smtplib
import os

from email.message import EmailMessage


def send_email(receiver_email, receiver_name, organization_name, certificate_path):

    sender_email = os.environ.get("EMAIL_SENDER")

    app_password = os.environ.get("EMAIL_PASSWORD")
    
    if not sender_email or not app_password:
        print("Error: EMAIL_SENDER and EMAIL_PASSWORD must be set in the .env file. Could not send email.")
        return

    # CREATE EMAIL
    msg = EmailMessage()

    msg["Subject"] = "Your Certificate"

    msg["From"] = sender_email

    msg["To"] = receiver_email


    # EMAIL BODY
    msg.set_content(
        f"""
Hello {receiver_name},

Congratulations!

Please find your certificate attached with this email.

Regards,
{organization_name}
"""
    )


    # ATTACH CERTIFICATE
    with open(certificate_path, "rb") as file:

        file_data = file.read()

        file_name = file.name


    msg.add_attachment(
        file_data,
        maintype="image",
        subtype="png",
        filename=file_name
    )


    # CONNECT TO GMAIL SERVER
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

        smtp.login(sender_email, app_password)

        smtp.send_message(msg)


    print(f"Email sent to {receiver_name}")