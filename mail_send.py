import smtplib  
from email.mime.text import MIMEText  
from email.mime.multipart import MIMEMultipart  
import schedule
import time

EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"  # Use App Password if 2FA is enabled

def send_email(to_email, bcc_emails, subject, body):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email  # Primary recipient (visible)
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        
        # ✅ Send email with BCC (recipients are hidden)
        server.sendmail(EMAIL_ADDRESS, [to_email] + bcc_emails, msg.as_string())  
        server.quit()
        
        print(f"✅ Email sent to {to_email} (Primary) and {len(bcc_emails)} BCC recipients.")
    except Exception as e:
        print(f"❌ Error: {e}")

# Example Recipients
to_email = "primary@example.com"  # Visible recipient
bcc_list = ["user1@example.com", "user2@example.com", "user3@example.com"]  # Hidden recipients

# ✅ Step 2: Automate Sending with BCC
schedule.every().day.at("09:00").do(send_email, to_email, bcc_list, "Daily Update", "Hello! This is your daily email.")

while True:
    schedule.run_pending()
    print("✅ Waiting for the next scheduled task...")
    time.sleep(60)  # Checks every 60 seconds
