from .sarializers import BotUserSerializers, FeedbackSerializers
from rest_framework.generics import ListCreateAPIView
from django.shortcuts import render, redirect
from .models import Feedback, BotUser, Sms
from rest_framework.decorators import api_view

import requests


class BotUserView(ListCreateAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializers


class FeedbacksApiView(ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializers


def home_view(request):
    return render(request, 'navbr.html')


def filter_view(request):
    user = BotUser.objects.all()
    context = {
        'user': user
    }
    return render(request, 'filter_1.html', context)


def page(request, pk):
    feed = Feedback.objects.filter(user_id=pk)
    sms = Sms.objects.all()
    context = {
        'feed': feed,
        'sms': sms
    }
    if request.method == 'POST':
        data = request.POST
        body = data.get('body')
        obj = Sms.objects.create(body=body)
        obj.save()
        return redirect(f'/feedbacksi/{pk}')

    return render(request, 'detal.html', context)


def otvet(request, pk):
    user = BotUser.objects.get(user_id=str(pk))
    if request.method == 'POST':
        data = request.POST
        body = data.get('body')
        obj = Sms.objects.create(body=body, user=user)
        obj.save()

        token = '6248365823:AAHl_dzLapBh9OzlgUzvj7Zf2znnBdLguk4'
        text = request.POST.get('body')
        url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id='
        requests.get(url + str(pk) + '&text=' + text)

        return redirect(f'/feedbacks/{pk}')
    feed = Feedback.objects.filter(user_id=pk).order_by('-created_at')
    sms = Sms.objects.filter(user=user).order_by('-created_at')
    context = {
        'feed': feed,
        'sms': sms
    }
    return render(request, 'detal.html', context)


