from django.core.mail import send_mail
from subscription.celery import app

from .service import send
from .models import Contact


@app.task
def send_spam_email(user_email):
    send(user_email)


@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
            'You finally subscribe!',
            'We will send you a lot of spam every 5 minutes',
            'test_email@email.com',
            [contact.email],
            fail_silently=False,
        )
