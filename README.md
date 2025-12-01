# Notification Service

A Django REST Framework service that sends notifications via Email, Telegram, and SMS.

## Features

- **Multi-channel notifications**: Email, Telegram, SMS
- **Telegram bot subscription**: Users can subscribe via Telegram bot
- **REST API**: Simple POST endpoint to send notifications
- **Admin interface**: Django admin for user management

## Quick Start with Docker

1. **Install dependencies**:
   ```bash
    git clone <your-repo>
    cd notification_service
    cp .env.example .env
   ```

2. **Configure environment**:<p>Edit .env with your actual values:</p>
    
   ```bash
    BOT_TOKEN=your_actual_token
    APP_PASSWORD=your_password
    FROM_EMAIL=your_email@gmail.com
   ```
     
3. **Run with Docker**:
    ```bash
    docker compose up --build
   ```
4. **Run migrations (first time)**:
    ```bash
    docker compose exec web python src/manage.py migrate
   ```

## API Usage
**Send notifications to all subscribed users**:
    
    POST /api/send/
    Content-Type: application/json
    {
        "message": "Your notification text here"
    }
    
    

## Using the Telegram Bot

1. Get a bot token from [BotFather](https://t.me/botfather)
2. Add it to `.env` as `BOT_TOKEN=your_token_here`
3. Find and start your bot on Telegram
4. Click "Subscribe" to add current chat id to user database

## Manual Setup (without Docker)
If you prefer running without Docker:

```bash
  pip install -r requirements.txt
  cd src
  python manage.py migrate
  python manage.py runserver
  # In another terminal:
  python manage.py run_bot
```

## Configuration
Set these environment variables:

- `BOT_TOKEN`: Your Telegram Bot Token

- Email settings (for email notifications)

