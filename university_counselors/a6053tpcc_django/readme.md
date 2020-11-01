1. 修改自己的postgresql的用户名，密码，数据库名字

at django_line folder 's settings.py  line 85:
DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'TPCC',

        'USER': 'postgres',

        'PASSWORD': 'postgres',

        'HOST': '127.0.0.1',

        'PORT': '5432',

    }

}