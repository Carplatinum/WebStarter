﻿# WebStarter
## Описание
Это минимальный веб-сервер на Python, который на любой GET-запрос возвращает HTML-страницу «Контакты».
HTML-страница хранится в отдельном файле contacts.html и загружается из него при каждом запросе.

## Файлы проекта  
catalog.html — HTML-код страницы «Каталог»  
category.html — HTML-код страницы «Категория 1»  
contacts.html — HTML-код страницы «Контакты»  
home.html — HTML-код страницы «Главная»  
server.py — скрипт Python для запуска веб-сервера  

## Требования
Python 3.x (рекомендуется 3.6 и выше)

## Запуск сервера
Скопируйте оба файла (contacts.html и server.py) в одну папку.

Откройте терминал (командную строку) и перейдите в эту папку.

Запустите сервер командой:

python server.py
В браузере откройте адрес:

http://localhost:8000
Вы увидите страницу «Контакты».

Остановка сервера
Нажмите Ctrl+C в терминале, где запущен сервер.

Особенности
Все запросы возвращают одну и ту же страницу.

Подключение CSS и JS происходит через CDN (удалённые репозитории).
