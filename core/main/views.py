from django.shortcuts import render
import requests

API_BASE_URL = 'http://192.168.7.113:8000'

def index(request):
    # Получение списка файлов с API
    files = get_files()

    context = {
        'files': files
    }

    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        upload_file(uploaded_file)

    return render(request, 'main/index.html', context)


def get_files():
    try:
        response = requests.get(f'{API_BASE_URL}/files/')
        if response.status_code == 200:
            files = response.json()
            print(files)  # Выводим результат в консоль для отладки
            return files  # Предполагается, что это список словарей с полями 'name' и 'download_url'
    except requests.exceptions.RequestException:
        return []
    return []


def upload_file(file):
    # Загрузка файла на сервер через API
    files = {'file': file}
    try:
        response = requests.post(f'{API_BASE_URL}/files/upload/', files=files)
        print(response.status_code, response.text)  # Выводим статус и текст ответа для отладки
        return response.status_code == 201
    except requests.exceptions.RequestException as e:
        print(e)
        return False
