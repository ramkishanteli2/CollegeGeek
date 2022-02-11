import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'CollegeGeek',

        'USER': 'postgres',

        'PASSWORD': 'admin',

        'HOST': 'localhost',
    }
}
