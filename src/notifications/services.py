from django.core.mail import send_mail
from django.conf import settings
from .models import User
from telegram import Bot
from telegram.error import BadRequest, TelegramError
import asyncio


async def send_telegram(user: User, text):
    bot = Bot(token=settings.BOT_TOKEN)
    try:
        chat_id = user.chat_id
        if not chat_id:
            return False
        await bot.send_message(chat_id=chat_id, text=text)
        return True
    except (BadRequest, TelegramError):
        return False


def send_email(user: User, text, subject="Notification"):
    try:
        email = user.email
        if not email:
            return False

        send_mail(subject=subject,
                  message=text,
                  from_email=None,
                  recipient_list=[email],
                  fail_silently=False,
                  )
        return True
    except Exception:
        return False


def send_sms(user: User, text):
    """Заглушка для SMS"""
    return True

def deliver_notification(user: User, text: str):
    if send_email(user, text):
        return "email"
    if asyncio.run(send_telegram(user, text)):
        return "telegram"
    if send_sms(user, text):
        return "sms"
    return "failed"


