# Django imports
from django.conf import settings
from django.core.management.base import BaseCommand
from asgiref.sync import sync_to_async

# Telegram imports
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    CommandHandler,
    ApplicationBuilder,
    ContextTypes,
    CallbackQueryHandler
)

# Local application imports
from notifications.models import User

class Command(BaseCommand):
    help = 'Bot for subscribing users to notification service through Telegram'

    BOT_TOKEN = settings.BOT_TOKEN

    async def add_subscriber(self, chat_id: int):
        user, created = await sync_to_async(User.objects.get_or_create)(
            chat_id=chat_id)
        return created

    async def start_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /start command - show subscription button."""
        # Create inline keyboard with subscribe button
        keyboard = [[InlineKeyboardButton("Subscribe", callback_data="subscribe")]]
        # This makes the button appear below the message text
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text("Click to subscribe:",
                                        reply_markup=reply_markup)

    async def callback_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle subscription button clicks."""
        query = update.callback_query
        # to stop button loading
        await query.answer()

        chat_id = update.effective_chat.id
        added = await self.add_subscriber(chat_id)

        if added:
            # if new subscriber was created
            await query.edit_message_text("✅ Subscribed!")
        else:
            await query.edit_message_text("ℹ️ Already subscribed.")

    def handle(self, *args, **options):
        """Main entry point - setup and start the bot."""
        application = ApplicationBuilder().token(self.BOT_TOKEN).build()
        application.add_handler(CommandHandler("start", self.start_handler))
        application.add_handler(CallbackQueryHandler(self.callback_handler, pattern="^subscribe$"))

        self.stdout.write(
            self.style.SUCCESS("🤖 Bot is running...\n"
                               "Send /start to your bot to test subscription.")
        )
        application.run_polling()