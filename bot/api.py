import requests
import json

BASE_URL = 'http://127.0.0.1:8000/api/v1'


def create_user(username, name, user_id):
    url = f'{BASE_URL}/bot-users/'
    response = requests.get(url=url).text
    data = json.loads(response)
    user_exist = False
    for i in data:
        if i['user_id'] == str(user_id):
            user_exist = True
            break
    if user_exist == False:
        requests.post(url=url, data={'username': username, 'name': name, 'user_id': user_id})
        return "foydalanuvchi yaratildi."
    else:
        return "foydalanuvchi mavjud"


def feedback_create(user_id, body):
    url = f'{BASE_URL}/bot-feedbacks/'
    if body and user_id:
        post = requests.post(url=url, data={
            'user_id': user_id,
            'body': body
        })
        return 'xabar adminga yuborildi'
    else:
        return 'amal oxiriga yetmadi'


def otvet(user, body):
    url = f'{BASE_URL}/hele/'
    if user and body:
        post = requests.post(url=url, data={
            'user': user,
            'body': body
        })
