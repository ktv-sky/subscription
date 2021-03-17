from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'You finally subscribe!', # Subject
        'We will send you a lot of spam.', # Body
        'test_email@email.com', # From
        [user_email],
        fail_silently=False,
    )
