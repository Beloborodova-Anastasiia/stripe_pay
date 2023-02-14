# stripe_pay

![Workflow status](https://github.com/Beloborodova-Anastasiia/stripe_pay/actions/workflows/foodgram_workflow.yml/badge.svg
)
### Server data (Данные сервера)
```
[Link to the project on the server](http://84.201.133.140/) (Ссылка на проект, запущенный на сервере)
```


### Description (Описание)

Test task for Rishat (Тестовое задание для ООО Ришат)

Project for implemention connection to the Stripe payment system. The server creates payment forms for products by contacting Stripe (Проект реализации обращения к платежной системе Stripe. Сервевер создает платежные формы для товаров, обращаясь к Stripe)

### Technologies (Технологии)
 
Python 3.8

Django 2.2.6

Django REST framework 3.12.4

Docker 20.10.17


### Local project run (Запуск проекта локально):

Clone a repository and navigate to it on the command line (Клонировать репозиторий в командной строке):

```
git clone git@github.com:Beloborodova-Anastasiia/stripe_pay.git
```

```
cd stripe_pay
```

Create env-file with environment variables by template (Создать env-файл с переменными окружения по образцу):

```
STRIPE_SECRET_KEY=YOUR_STRIPE_SECRET_KEY
STRIPE_PUBLIC_KEY=YOUR_STRIPE_PUBLIC_KEY
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=PASSWORD
DB_HOST=db
DB_PORT=5432
HOST=127.0.0.1:8000

```

Run build docker-container (Запустить сборку докер-контейнера):

```
for Windows and Mac:
docker-compose up -d --build
```
```
for Linux:
sudo docker-compose up -d --build
```


### Available resources (Доступные ресурсы)

The project administrator's website is available at (Панель администратора Django доступна по адресу):

```
http://127.0.0.1/admin - local
http://84.201.133.140/admin - on server
```

Administrator's data (Данные администратора):
```
username = admin
password = 123
```

Templates of items (Страницы товаров):
```
http://127.0.0.1/item/{id} - local
http://84.201.133.140/item/{id} - on server

id = [1, 2, 3]
```


### Author (Автор)

Anastasiia Beloborodova 

anastasiia.beloborodova@gmail.com
