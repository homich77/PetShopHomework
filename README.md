# PetShopHomework

# Installation
* clone the repo
* create virtualenv
* pip install -r requirements.txt 
* python manage.py migrate

# Настройки БД
```
DATABASES = { 
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'petshop_db2', 
        'USER': 'petshop_admin1', 
        'PASSWORD': 'password', 
        'HOST': '127.0.0.1', 
        'PORT': '5432', 
    } 
} 
```

