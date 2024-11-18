import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email_without_auth(smtp_server, port, from_address, to_address, subject, body):
    try:
        # Set up the server connection
        server = smtplib.SMTP(smtp_server, port)
        #server.starttls()  # Upgrade the connection to secure if STARTTLS is supported

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = from_address
        msg['To'] = to_address
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Send the email without authentication
        server.sendmail(from_address, to_address, msg.as_string())

        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()

# Example usage
smtp_server = "smtp.yourmailserver.com"  # Replace with  SMTP server
port = 25  # Use the appropriate port (25, 465, 587); 25 is common for unauthenticated SMTP
from_address = "sender@domain.com"  # Sender email address
to_address = "recipient@example.com"  # Recipient's email address
subject = "Testing Unauthenticated Email"
body = "This is a test to see if the server allows sending emails without authentication."

send_email_without_auth(smtp_server, port, from_address, to_address, subject, body)
