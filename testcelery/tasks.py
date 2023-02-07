import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
from celery import Celery
import smtplib
from email.mime.text import MIMEText

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def send_email(email, subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = 'sender@example.com'
    msg['To'] = email
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()