import schedule
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ✅ Define mail_send function first
def mail_send(to_email, subject, body):
    EMAIL_ADDRESS = "sumitboddu0407@gmail.com"
    EMAIL_PASSWORD = "ttxe iitp dxnr kdfa"  # Use an App Password if 2FA is enabled

    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
        server.quit()
        print(f"✅ Email sent to {to_email}")
    except Exception as e:
        print(f"❌ Error: {e}")

# ✅ Now, schedule the email correctly
schedule.every().day.at("09:00").do(mail_send, "sumitboddu0407@gmail.com", "Daily Update", "Hello! This is your daily email.")
# schedule.every(1).minutes.do(mail_send, "sumitboddu0407@gmail.com", "Test Email", "This is a test email sent every minute.")

# ✅ Keep the script running
while True:
    schedule.run_pending()
    print("✅ Waiting for the next scheduled task...")  # Debugging Output
    time.sleep(60)
