DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'resume_db',
        'USER': 'your_mysql_user',
        'PASSWORD': 'Siddhant@27',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

INSTALLED_APPS = [
    # Django default apps...
    'rest_framework',
    'resume',  # our resume app
]
