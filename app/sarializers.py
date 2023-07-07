from .models import BotUser, Feedback, Sms
from rest_framework.serializers import ModelSerializer


class BotUserSerializers(ModelSerializer):
    class Meta:
        model = BotUser
        fields = ("username", "name", "user_id", "created_at")


class FeedbackSerializers(ModelSerializer):
    class Meta:
        model = Feedback
        fields = ("user_id", "body", "created_at")


class OtvetSerialezrs(ModelSerializer):
    class Meta:
        model = Sms
        fields = ('user', 'body', 'created_at')
