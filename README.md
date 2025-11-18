# Notification Service

A Django REST Framework service that sends notifications via Email, Telegram, and SMS.

## Features

- **Multi-channel notifications**: Email, Telegram, SMS
- **Telegram bot subscription**: Users can subscribe via Telegram bot
- **REST API**: Simple POST endpoint to send notifications
- **Admin interface**: Django admin for user management

## Quick Start

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

2. **Setup database**:
    ```bash
    python manage.py migrate
     
3. **Run server**:
    ```bash
    python manage.py runserver
4. **Start Telegram bot (in separate terminal)**:
    ```bash
    python manage.py run_bot

## API Usage
**Send notifications to all subscribed users**:
    ```http
    POST /api/send/
    Content-Type: application/json

    {
        "message": "Your notification text here"
    }

## Configuration
Set these environment variables:

- `BOT_TOKEN`: Your Telegram Bot Token

- Email settings (for email notifications)

## Project Structure
- `src/notifications/` - Main application

- `src/config/` - Django settings

- `src/notifications/management/commands/run_bot.py` - Telegram bot

- `src/notifications/services.py` - Notification delivery logic