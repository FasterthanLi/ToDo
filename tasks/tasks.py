from celery import shared_task
from django.core.mail import send_mail

@shared_task(bind=True)
def send_email_task(subject, message, from_email, recipient_list, fail_silently):
    if not isinstance(recipient_list, (list, tuple)):
        recipient_list = [recipient_list]

    send_mail(subject, message, from_email, recipient_list, fail_silently)
    return "Done"