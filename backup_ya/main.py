import os
import yadisk
import zipfile

from TOKEN import TOKEN
from datetime import datetime


"""
Архивируетм все в нужной папке и сохраняем на уровень выше
"""

where_files = 'C:/Users/Гоша/Documents/test/' # место, где хранятся файлы
where_save = 'C:/Users/Гоша/Documents/'		  # место, где будет архив

#where_files = input("Введите путь до папки, откда хотите сохранить информацию:")
#where_save = input("Введите путь до папки, где буде сохранен архив:")

z = zipfile.ZipFile(where_save + 'spam.zip', 'w') # Создание нового архива
for root, dirs, files in os.walk(where_files): # Список всех файлов и папок в директории 
	for file in files:
		z.write(os.path.join(root,file), compress_type=zipfile.ZIP_DEFLATED) # Создание относительных путей и запись файлов в архив

z.close()


"""
Потом код ниже закидывает архив на яндекс диск
"""

#токен спрятан в отдельный файл
x = yadisk.YaDisk(token = TOKEN)

# Check if the token is valid - проверить, что работает
print(x.check_token())

# Get disk information - проверить, что хватает места
print(x.get_disk_info())

date = datetime.strftime(datetime.now(), "%d.%m.%Y-%H.%M") 
x.mkdir(f'/test/{date}')


folder = []
for i in os.walk('C:/Users/Гоша/Documents/test'): #откуда копировать
    folder.append(i)
for address, dirs, files in folder:
# for address, dirs, files in folder:
    # for dir in dirs:
    #     x.mkdir(f'/zoom_save/{date}/{dir}')
    #     print(f'Папка {dir} создана')
    for file in files:
        x.upload(f'{address}/{file}', f'/test/{date}/{file}')
        print(f'Файл {file} загружен')


"""
Удаление директорий
С помощью функции os.rmdir() можно удалить указанную папку:

# удалить папку
os.rmdir("folder")
Для удаления каталогов рекурсивно необходимо использовать os.removedirs():

# удалить вложенные папки
os.removedirs("nested1/nested2/nested3")
Это удалит только пустые каталоги.
"""