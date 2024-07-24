
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
import sendgrid
#from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


message = Mail(
    from_email='dicampok@comcast.net',
    to_emails='dicampok@comcast.net',
    subject='Sending with Twilio SendGrid is Fun!',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    #sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    sg = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    #sg = sendgrid.SendGridAPIClient('put a key here')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(f'Function x gave error {e}')
    #print(e.message)