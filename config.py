class Config:
    SECRET_KEY = 'hk(9buz7m&2xzhf9z(3k)t(vtrf03q68z!_tkf=wpk4v5dh=kw'


class DevelopmentConfig(Config):
    ALLOWED_HOSTS = []

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'HOST': 'db',
            'PORT': 5432
        },
        'sqlite3': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3'
        }
    }