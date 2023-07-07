from django.db import models


class BotUser(models.Model):
    user_id = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    username = models.CharField(max_length=120, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    user_id = models.CharField(max_length=120)
    body = models.CharField(max_length=1200)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id


class Sms(models.Model):
    user = models.ForeignKey(BotUser, on_delete=models.CASCADE, null=True)
    body = models.CharField(max_length=1200)

    created_at = models.DateTimeField(auto_now_add=True)
