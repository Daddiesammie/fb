from django.conf import settings
from .models import EmailConfiguration

def get_email_settings():
    config = EmailConfiguration.objects.filter(active=True).first()
    if config:
        return {
            'EMAIL_HOST_USER': config.email,
            'EMAIL_HOST_PASSWORD': config.password,
        }
    return {
        'EMAIL_HOST_USER': settings.EMAIL_HOST_USER,
        'EMAIL_HOST_PASSWORD': settings.EMAIL_HOST_PASSWORD,
    }
