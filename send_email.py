# import smtplib
# from email.message import EmailMessage

# # Set up email details
# sender_email = "karanagg1001@gmail.com"
# sender_password = "tjlldxzkqfxybtgz"  # Generate from Google App Passwords
# recipient_email = "karanagg2002@gmail.com"

# msg = EmailMessage()
# msg["Subject"] = "Test Email"
# msg["From"] = sender_email
# msg["To"] = recipient_email
# msg.set_content("This is a test email sent via Gmail SMTP.")

# # Connect to Gmail SMTP server
# with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
#     server.login(sender_email, sender_password)
#     server.send_message(msg)

# print("Email sent successfully!")


# import smtplib
# from email.message import EmailMessage

# SMTP_SERVER = "smtp.gmail.com"
# SMTP_PORT = 587
# EMAIL_ADDRESS = "karanagg1001@gmail.com"
# EMAIL_PASSWORD = "tjlldxzkqfxybtgz"

# def send_email(subject, body):
#     to_emails = ["karanagg2002@gmail.com"]
#     cc_emails = ["kanikaagg2001@gmail.com","rushilagarwal08@gmail.com"]

#     msg = EmailMessage()
#     msg["From"] = EMAIL_ADDRESS
#     msg["To"] = ", ".join(to_emails)
#     msg["Cc"] = ", ".join(cc_emails)
#     msg["Subject"] = subject
#     msg.set_content(body)

#     with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
#         server.starttls()
#         server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#         all_recipients = to_emails + cc_emails
#         server.send_message(msg, to_addrs=all_recipients)

#     print("Email sent successfully!")




import smtplib
import os
from email.message import EmailMessage

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")  # Fetch from environment
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")  # Fetch from environment

def send_email(subject, body):
    to_emails = ["karanagg2002@gmail.com"]
    cc_emails = ["kanikaagg2001@gmail.com", "rushilagarwal08@gmail.com"]

    msg = EmailMessage()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = ", ".join(to_emails)
    msg["Cc"] = ", ".join(cc_emails)
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        all_recipients = to_emails + cc_emails
        server.send_message(msg, to_addrs=all_recipients)

    print("Email sent successfully!")
