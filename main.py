import asyncio
from photo_osn import photo_osn
from photo_preview import photo_preview

async def main():
    url = input("Введите URL: ")
    path_directory = input("Введите путь к директории: ")
    #

    # url = "https://www.gettyimages.es/search/2/image?family=editorial&phrase=1993%20julia%20roberts%20Audrey%20Hepburn&sort=best"
    # path_directory = "/home/vlad/Документы/Vlad/Alex_Photo"

    url_preview = url
    url_osn = url



    await photo_osn(url_osn,path_directory)
    # await photo_preview(url_preview,path_directory)

asyncio.run(main())