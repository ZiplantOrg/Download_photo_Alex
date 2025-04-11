from selenium import webdriver
from bs4 import BeautifulSoup
import os
import requests

async def photo_preview(url_preview,path_directory):
    # Задаем URL
    url = url_preview

    # Создаем экземпляр браузера
    driver = webdriver.Chrome()

    # Открываем URL в браузере
    driver.get(url)

    # Получаем HTML-код страницы
    html = driver.page_source

    # Создаем объект BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Находим все элементы <img class="Xc8V0Fvh0qg0lUySLpoi" src="">
    img_tags = soup.find_all('img', class_='Xc8V0Fvh0qg0lUySLpoi')


    directory = path_directory
    # Создаем директорию, если она не существует
    directory_path = os.path.join(directory, 'photo_preview')
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    # Открываем файл для записи
    with open(os.path.join(directory, 'photo_preview/spisok_preview.txt'), 'w') as f:
        # Записываем значения src каждого элемента в файл
        for img in img_tags:
            f.write(img['src'] + '\n')

    # Закрываем браузер
    driver.quit()
    await file_path(directory_path)

async def file_path(directory_path):
    # Задаем директорию
    directory = directory_path

    # Создаем директорию Photo, если она не существует
    photo_directory = os.path.join(directory, 'Photo')
    if not os.path.exists(photo_directory):
        os.makedirs(photo_directory)

    # Открываем файл со ссылками на изображения
    with open(os.path.join(directory, 'spisok_preview.txt'), 'r') as f:
        # Читаем ссылки на изображения
        img_urls = f.read().splitlines()

    # Загружаем изображения по ссылкам
    for i, img_url in enumerate(img_urls):
        img_data = requests.get(img_url).content
        with open(os.path.join(photo_directory, f'image_{i}.jpg'), 'wb') as handler:
            handler.write(img_data)
