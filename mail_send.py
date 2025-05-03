import smtplib  
from email.mime.text import MIMEText  
from email.mime.multipart import MIMEMultipart  
import schedule
import time
from dotenv import load_dotenv
import os

load_dotenv()

email_address = os.getenv('EMAIL_ADDRESS')
email_password = os.getev('EMAIL_PASSWORD')

def send_email(to_email, bcc_emails, subject, body):
    msg = MIMEMultipart()
    msg["From"] = email_address
    msg["To"] = to_email  # Primary recipient (visible)
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email_address, email_password)
        
        #  Send email with BCC (recipients are hidden)
        server.sendmail(email_address, [to_email] + bcc_emails, msg.as_string())  
        server.quit()
        
        print(f" Email sent to {to_email} (Primary) and {len(bcc_emails)} BCC recipients.")
    except Exception as e:
        print(f"❌ Error: {e}")

# Example Recipients
to_email = "saloniraghavaran@gmail.com"  # Visible recipient
bcc_list = ["sumitboddu04@gmail.com", "ronak.boddu@gmail.com", "sumitboddu4@gmail.com"]  # Hidden recipients

# Step 2: Automate Sending with BCC
schedule.every().day.at("09:00").do(send_email, to_email, bcc_list, "Daily Update", "Hello! This is your daily email.")
schedule.every(1).minutes.do(send_email, to_email, bcc_list, "Test Email", "This is a test email sent every minute.")


while True:
    schedule.run_pending()
    print(" Waiting for the next scheduled task...")
    time.sleep(60)  # Checks every 60 seconds
