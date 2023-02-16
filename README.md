# stripe_pay

![Workflow status](https://github.com/Beloborodova-Anastasiia/stripe_pay/actions/workflows/stripe_pay_workflow.yml/badge.svg)

### Server data 
[Link to the project on the server](http://84.201.133.140/) 


### Description

Test task for Rishat

The project goal is to integrate a simple Django project with the Stripe payment provider. The server creates payment forms for products by contacting Stripe.
The project is packaged in a docker container and launched on the Yandex Cloud server.

### Technologies
 
Python 3.8

Django 2.2.6

Django REST framework 3.12.4

Docker 20.10.17


### Local project run

Clone a repository and navigate to it on the command line:

```
git clone git@github.com:Beloborodova-Anastasiia/stripe_pay.git
```

```
cd stripe_pay
```

Create env-file with environment variables by template in the root of project (there is env_example in the root):

```
STRIPE_SECRET_KEY=YOUR_STRIPE_SECRET_KEY
STRIPE_PUBLIC_KEY=YOUR_STRIPE_PUBLIC_KEY
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=PASSWORD
DB_HOST=db
DB_PORT=5432
HOST=127.0.0.1

```

Build docker-container:

```
for Windows and Mac:
docker-compose up -d --build
```
```
for Linux:
sudo docker-compose up -d --build
```


### Available resources

Items list:
```
http://127.0.0.1/ - local
http://84.201.133.140/ - on server
```

Templates of items:
```
http://127.0.0.1/item/{id} - local
http://84.201.133.140/item/{id} - on server

id = [1, 2, 3]
```

The project administrator's website is available at:

```
http://127.0.0.1/admin - local
http://84.201.133.140/admin - on server
```

Administrator's data:
```
username = admin
password = 123
```

### Author

Anastasiia Beloborodova 

anastasiia.beloborodova@gmail.com
