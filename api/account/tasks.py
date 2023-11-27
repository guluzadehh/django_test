from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_email_signup_success(email: str, username: str):
    subject = f"Успешная регистрация"
    txt = f"Регистрация прошла успешна!\nВаше имя пользователя: {username}"
    return send_mail(subject, txt, settings.EMAIL_HOST_USER, [email])
