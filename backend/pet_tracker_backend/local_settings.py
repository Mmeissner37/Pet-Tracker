# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1f1gaxy)9)mszh0!3&6x-i-tnx2#r103=lx!uj7htlxfdqo_3s'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pet_tracker_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password',
    }
}
