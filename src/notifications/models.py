from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.TextField(default='')
    phone_number = models.TextField(default='')
    chat_id = models.TextField(default='')
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'notifications'


