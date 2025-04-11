from selenium import webdriver
from bs4 import BeautifulSoup
import os
import requests
import re
import aiohttp
async def photo_osn(url_osn,path_directory):
    # # Задаем URL
    # url = url_osn
    #
    # # Создаем экземпляр браузера
    # driver = webdriver.Chrome()
    #
    # # Открываем URL в браузере
    # driver.get(url)
    #
    # # Получаем HTML-код страницы
    # html = driver.page_source
    #
    # # Создаем объект BeautifulSoup
    # soup = BeautifulSoup(html, 'html.parser')
    #
    directory = path_directory
    # Создаем директорию, если она не существует
    directory_path = os.path.join(directory, 'photo_osn')
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)



    # file_path = os.path.join(directory, 'photo_osn/spisok_osn.txt')
    # if not os.path.exists(file_path):
    #     with open(file_path, 'w') as f:
    #         pass  # Создаем пустой файл
    #
    # # Сортируем ссылки по их href
    # # Находим все ссылки на странице
    # links = soup.find_all('a', href=True, attrs={'data-testid': 'mosaicAssetAnchor'})
    #
    # # Сортируем ссылки по их href
    # links = sorted(links, key=lambda x: x['href'])
    #
    # for link in links:
    #     full_url = "https://www.gettyimages.es" + link['href']
    #     driver.get(full_url)
    #     html = driver.page_source
    #     soup = BeautifulSoup(html, 'html.parser')
    #     sources = soup.find_all('source', srcset=re.compile('s=2048x204'), type="image/jpeg")
    #     for source in sources:
    #         if 'srcset' in source.attrs:
    #             with open(os.path.join(directory, 'photo_osn/spisok_osn.txt'), 'a') as f:
    #                 f.write(source['srcset'] + '\n')
    #
    # # Закрываем браузер
    # driver.quit()
    await file_path_save(directory_path)



async def file_path_save(directory_path):
    # Задаем директорию
    directory = directory_path
    # Создаем директорию Photo, если она не существует
    photo_directory = os.path.join(directory, 'Photo')
    if not os.path.exists(photo_directory):
        os.makedirs(photo_directory)
    # Открываем файл со ссылками на изображения
    with open(os.path.join(directory, 'spisok_osn.txt'), 'r') as f:
        # Читаем ссылки на изображения
        img_urls = f.read().splitlines()
    # Загружаем изображения по ссылкам
    async with aiohttp.ClientSession() as session:
        for img_url in img_urls:
            try:
                if not img_url.startswith('http'):
                    print(f"Ошибка при загрузке изображения: Некорректный URL")
                    continue
                async with session.get(img_url) as response:
                    if response.status == 200:
                        img_data = await response.read()
                        # Извлекаем имя файла из URL
                        img_name = img_url.split('https://media.gettyimages.com/id/')[1].split('/es/foto/')[0]
                        with open(os.path.join(photo_directory, f'{img_name}.jpg'), 'wb') as handler:
                            handler.write(img_data)
                    else:
                        print(f"Ошибка при загрузке изображения: HTTP {response.status}")
            except aiohttp.ClientError as e:
                # Игнорируем ошибку и переходим к следующей ссылке
                print(f"Ошибка при загрузке изображения: {e}")
                continue





# async def file_path_save(directory_path):
#     # Задаем директорию
#     directory = directory_path
#     # Создаем директорию Photo, если она не существует
#     photo_directory = os.path.join(directory, 'Photo')
#     if not os.path.exists(photo_directory):
#         os.makedirs(photo_directory)
#     # Открываем файл со ссылками на изображения
#     with open(os.path.join(directory, 'spisok_osn.txt'), 'r') as f:
#         # Читаем ссылки на изображения
#         img_urls = f.read().splitlines()
#     # Загружаем изображения по ссылкам
#     async with aiohttp.ClientSession() as session:
#         for i, img_url in enumerate(img_urls):
#             try:
#                 if not img_url.startswith('http'):
#                     print(f"Ошибка при загрузке изображения {i}: Некорректный URL")
#                     continue
#                 async with session.get(img_url) as response:
#                     if response.status == 200:
#                         img_data = await response.read()
#                         with open(os.path.join(photo_directory, f'image_{i}.jpg'), 'wb') as handler:
#                             handler.write(img_data)
#                     else:
#                         print(f"Ошибка при загрузке изображения {i}: HTTP {response.status}")
#             except aiohttp.ClientError as e:
#                 # Игнорируем ошибку и переходим к следующей ссылке
#                 print(f"Ошибка при загрузке изображения {i}: {e}")
#                 continue
