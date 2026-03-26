import smtplib
import schedule
import time

# Function to send email
def send_email():
    with open("templates/email_template.txt", "r") as f:
        template = f.read()

    message = template.replace("{name}", "Swyam")

    sender_email = "enteryouremailaddress"
    receiver_email = "emailaddress"
    password = "vpdadadddbbjaadyofsyvshcbuog"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)

        server.sendmail(sender_email, receiver_email, message)
        print("Scheduled email sent")

        server.quit()

    except Exception as e:
        print("Error:", e)


# Schedule email (every 1 minute)
schedule.every(1).minutes.do(send_email)

print("Scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(1)