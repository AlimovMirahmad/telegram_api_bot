from django.urls import path
from .views import BotUserView, FeedbacksApiView, home_view, filter_view, page, otvet

urlpatterns = [
    path('bot-users/', BotUserView.as_view(), name='bot-users/'),
    path('bot-feedbacks/', FeedbacksApiView.as_view(), name='bot-feedbacks/'),
    path('', home_view),
    path('feedbacks/', filter_view),
    path('feedbacks/<int:pk>/', otvet),
    ]


