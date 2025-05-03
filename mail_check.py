import smtplib  
import imaplib  
import email  # No need to install
from email.mime.text import MIMEText  
from email.mime.multipart import MIMEMultipart  
from dotenv import load_dotenv 
import os
from email.header import decode_header

load_dotenv()

imap_server = os.getenv('IMAP_SERVER')
email_address = os.getenv('EMAIL_ADDRESS')
email_password = os.getenv('EMAIL_PASSWORD')
print("Part A Successfull")

def check_emails():
    try:
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(email_address, email_password)
        mail.select("inbox")

        # Search for unread emails
        status, messages = mail.search(None, 'UNSEEN')
        email_ids = messages[0].split()

        if not email_ids:
            print("No new emails.")
            return

        for email_id in email_ids:
            _, msg_data = mail.fetch(email_id, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes) and encoding:
                        subject = subject.decode(encoding)
                    sender = msg.get("From")

                    print(f"New Email from {sender}: {subject}")

                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            if content_type == "text/plain":
                                body = part.get_payload(decode=True).decode()
                                print(f"Message: {body}\n")
                    else:
                        body = msg.get_payload(decode=True).decode()
                        print(f"Message: {body}\n")

        mail.close()
        mail.logout()
    except Exception as e:
        print("Error:", e)

print("Part B Successfull")

# Example Usage
check_emails()
