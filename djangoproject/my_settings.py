import pymysql  
pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_test',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

SECRET_KEY = 'django-insecure-l2qqkec!o4h7q=01_b!=y7hnn#i(12jiixzr+pp^)x-a!own2g'