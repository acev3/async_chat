# Асинхронный чат-клиент

Заготовка под проект асинхронного чата.


## Как установить

Для работы микросервиса нужен Python версии не ниже 3.7.

```bash
pip install -r requirements.txt
```

## Как запустить

```bash
python listener.py
```
Код подключиться к анонимному чату в режиме чтения.

Аргументы:
```
 -h, --help         show this help message and exit
  --host HOST        Set host
  --port PORT        Set port
  --history HISTORY  Set history path
```
```bash
python sender.py <MESSAGE>, MESSAGE - обзательный аргумент.
```
Код отправит сообщение в чат.
```
 -h, --help           show this help message and exit
  --host HOST          Set host
  --port PORT          Set port
  --token TOKEN        Set token
  --username USERNAME  Set username
  --message MESSAGE    Set message
```
Чтобы зарегистрировать пользователя
```bash
python sender.py --message <MESSAGE> --username <USERNAME>
```
В результате будет выведен ответ вида:
```bash
INFO:SENDER:Your username: <Username> ; your hash: <hash>
```
Эти параметры можно передать для отправки сообщения или поместить в .env файл.

# Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).