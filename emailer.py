import smtplib

from email.message import EmailMessage


def send_email(receiver_email, receiver_name, certificate_path):

    sender_email = "savithareddy.rajidi@gmail.com"

    app_password = "wxbu wxhc ccpn lluh"


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
ABC University
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