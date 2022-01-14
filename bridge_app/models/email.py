import os
from sendgrid import SendGridAPIClient

from bridge_app.models.reservation import Reservation

SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
RESERVATION_EMAIL_LIST = os.getenv('RESERVATION_EMAIL_LIST', '').split(",")
RESERVATION_EMAIL_TEMPLATE_ID = os.getenv('RESERVATION_EMAIL_TEMPLATE_ID')

class ReservationEmail():

    def __init__(self, reservation: Reservation):
        self.reservation = reservation
        self.response = None
        self.api_key = SENDGRID_API_KEY
        self.email_list = RESERVATION_EMAIL_LIST
        self.template_id = RESERVATION_EMAIL_TEMPLATE_ID

    def send(self):
        sg = SendGridAPIClient(api_key=self.api_key)
        data = {
            'from': {
                'email': 'noreply@palmsparkbridge.com'
            },
            'template_id': self.template_id,
            'personalizations': [
                {
                    'to': [{'email': email} for email in self.email_list],
                    'dynamic_template_data': {
                        'reservation': vars(self.reservation)
                    }
                }
            ]
        }
        self.response = sg.client.mail.send.post(request_body=data)
