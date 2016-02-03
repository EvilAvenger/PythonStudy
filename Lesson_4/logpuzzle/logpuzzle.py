#!/usr/bin/python3

import os
import re
import sys
import urllib.request
import urllib.parse

""" Logpuzzle
На сервере лежит 9 изображений, являющихся частями одного изображения 
(фото дикой природы).

Дан лог файл веб-сервера, в котором среди прочих запросов содеражатся запросы
к этим изображениям. Нужно вытащить из файла url всех изображений и скачать их.
Затем создать файл index.html и собрать с его помощью все изображения в одну
картинку.

Вот что из себя представляет строка лога:
101.237.66.11 - - [05/Jun/2013:10:44:02 +0400] "GET /images/animals_07.jpg HTTP/1.1" 200 13632 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"

Замечание: для создания html файла можно использовать самую простую разметку:
<html>
<body>
<img src="img0.jpg"><img src="img1.jpg">...
</body>
</html>

Подсказка: скачать файлы можно двумя способами:

1. Воспользоваться функцией, сохраняющей url по заданному пути file_name:
urllib.request.urlretrieve(url, file_name)

2. Скачать url и сохранить в файле:
import urllib.request
import shutil
...
with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

"""


def read_urls(filename):
    imgRegex = re.compile(r"(?<=GET\s)(/images/animals_\d\d.jpg)")
    urlRegex = r'http://[^/]+'
    fileText = open(filename, 'r', encoding="UTF-8").read()
    match = re.search(urlRegex, fileText)
    urls = []
    if match:
        match = match.group()
        urls = sorted((map(lambda x: ''.join((match, x)),
                           set(re.findall(imgRegex, fileText)))))
    return urls


def download_images(img_urls, dest_dir):
    """
    Получает уже отсортированный спискок url, скачивает каждое изображение
    в директорию dest_dir. Переименовывает изображения в img0.jpg, img1.jpg и тд.
    Создает файл index.html в заданной директории с тегами img, чтобы 
    отобразить картинку в сборе. Создает директорию, если это необходимо.
    """
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    filePath = os.path.abspath(os.path.join(dest_dir, "index.html"))
    file = open(filePath, 'w', encoding="UTF-8")
    file.write("<html><body>")
    i = 0
    for url in img_urls:
        imgName = "img{0}.jpg".format(i)
        fileName = os.path.abspath(os.path.join(dest_dir, imgName))
        urllib.request.urlretrieve(url, fileName)
        file.write('<img src="{0}">'.format(imgName))
        i += 1
    file.write("</body></html>")
    file.close()
    return


def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))

if __name__ == '__main__':
    main()
