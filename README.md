# First Extra Homework for Yandex Intensive

## Установка проекта

Для установки Django, его зависимостей и библиотеки `python-decouple` (нужной для получения переменных среды) воспользуйтесь командой `pip3 install -r requirements.txt`, запущенной в терминале из внешней папки homework.

Вне папки homework создайте файл `.env` с переменными, необходимыми для корректной работы проекта:
```
SECRET_KEY="<Ваш_секретный_ключ_Django>"
DEBUG="True" (DEBUG="False")
ALLOWED_HOSTS="127.0.0.1|localhost" (разрешенные хосты, разделенные вертикальной чертой)
```

Для запуска проекта воспользуйтесь следующими командами, запущенными в терминале ищ внешней папки homework.

1. `cd homework`
2. `python3 manage.py runserver`