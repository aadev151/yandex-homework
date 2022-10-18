# Yandex.Homework

## Этот проект сделан на Django

В данном файле описана подробная инструкция по запуску проекта.

1. Скачайте проект с Гитхаба. Для этого нажмите зеленую кнопку `Code` и выберите опцию `Download ZIP`

![Скачивание кода](https://aadev151.tech/static/for_other_projects/download_gh_proj.png)

Чтобы запустить проект, воспользуйтесь следующей последовательностью команд, запущенных в терминале из внешней папки (`yandex-homework-main`):

### Для Linux и MacOS
1. `python3 -m venv venv` для создания виртуального окружения (чтобы версии установленных модулей в данном проекте и других проектах на Вашем компьютере не конфликтовали)
2. `source venv/bin/activate` для активации виртуального окружения
3. `pip3 install -r requirements.txt` для установки необходимых в проекте модулей
4. `cd homework` для перехода в основную папку проекта
5. `python3 manage.py runserver` для запуска проекта

### Для Windows
1. `pip install virtualenv` для установки модуля, создающего виртуальное окружение
2. Перейдите в папку проекта (`yandex-homework-main`) и запустите командную строку из неё. [Подробнее](https://comp-security.net/как-открыть-командную-строку-в-папке/)
3. `virtualenv venv` в папке проекта (`yandex-homework-main`), для создания виртуального окружения
4. `venv\Scripts\activate` из той же папки, для активации вирутального окружения
5. `pip3 install -r requirements.txt` для установки необходимых в проекте модулей
6. `cd homework` для перехода в основную папку проекта
7. `python3 manage.py runserver` для запуска проекта

После этого Вы получите сообщение в терминале:
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
September 24, 2022 - 11:04:56
Django version 4.1.1, using settings 'myportfolio.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Чтобы открыть сайт, посетите http://127.0.0.1:8000. Чтобы прекратить выполнение программы, нажмите Control+C.

