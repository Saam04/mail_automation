import schedule
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()
email_address = os.getenv('EMAIL_ADDRESS')
email_password = os.getenv('EMAIL_PASSWORD')

#  Define mail_send function first
def mail_send(to_email, subject, body):
    
    msg = MIMEMultipart()
    msg["From"] = email_address
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email_address, email_password)
        server.sendmail(email_address, to_email, msg.as_string())
        server.quit()
        print(f" Email sent to {to_email}")
    except Exception as e:
        print(f"❌ Error: {e}")

#  Now, schedule the email correctly
schedule.every().day.at("09:00").do(mail_send, "sumitboddu0407@gmail.com", "Daily Update", "Hello! This is your daily email.")
schedule.every(1).minutes.do(mail_send, "saamluke@gmail.com", "Test Email", "This is a test email sent every minute.")

#  Keep the script running
while True:
    schedule.run_pending()
    print(" Waiting for the next scheduled task...")  # Debugging Output
    time.sleep(60)
