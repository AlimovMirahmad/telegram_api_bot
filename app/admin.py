from django.contrib import admin
from .models import BotUser, Feedback, Sms

admin.site.register(BotUser)
admin.site.register(Feedback)
admin.site.register(Sms)
