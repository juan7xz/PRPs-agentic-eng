import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

class EmailService:
    def __init__(self):
        self.sendgrid_client = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))

    def send_email(self, to_email, from_email, subject, html_content):
        message = Mail(
            from_email=from_email,
            to_emails=to_email,
            subject=subject,
            html_content=html_content)
        try:
            response = self.sendgrid_client.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)
