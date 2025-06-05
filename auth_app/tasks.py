from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.mail import EmailMultiAlternatives

app = Celery('tasks', broker='pyamqp://guest@localhost//')

def send_email(subject,EMAIL_HOST_USER,recipient_list,html_message=None):
    email = EmailMultiAlternatives(
        subject=subject,
        # body=message,
        from_email=EMAIL_HOST_USER,
        to=recipient_list
    )
    if html_message:
        email.attach_alternative(html_message,"text/html")
    return email.send(fail_silently=False)

logger = get_task_logger(__name__)

@shared_task(name="send_email_task")
def send_email_task(subject, EMAIL_HOST_USER, recipient_list, html_message = None):
    logger.info("Mail Sent!")
    return send_email(subject, EMAIL_HOST_USER, recipient_list, html_message)