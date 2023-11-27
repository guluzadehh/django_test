from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_email_signup_success(email: str):
    subject = f"Успешная регистрация"
    txt = "Регистрация прошла успешна!"
    return send_mail(subject, txt, settings.EMAIL_HOST_USER, [email])
