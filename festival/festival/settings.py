from pathlib import Path
import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Configuration des fichiers statiques (CSS, JS, images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'monsite/static',  # Assurez-vous que ce dossier existe pour les fichiers statiques
]

# Configuration des fichiers médias (images, vidéos, etc.)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # Le répertoire où les fichiers médias seront stockés

# Sécurité du projet
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')  # La clé est récupérée de l'environnement

# Autres paramètres
DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'

# Ajouter les hôtes autorisés depuis les variables d'environnement
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# Configuration des applications installées
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'monsite',  # Assurez-vous que cette application existe dans votre projet
]

# Configuration du middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuration des URLs de base
ROOT_URLCONF = 'festival.urls'

# Application WSGI
WSGI_APPLICATION = 'festival.wsgi.application'

# Base de données (SQLite pour le développement)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Utilisation de SQLite
        'NAME': BASE_DIR / 'db.sqlite3',         # Le fichier SQLite se trouvera à la racine du projet
    }
}

# Validation des mots de passe
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Paramètres de localisation
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_TZ = True

# Paramètres de gestion des templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Répertoire des templates supplémentaires
        'APP_DIRS': True,  # Cherche les templates dans les répertoires 'templates' de chaque application
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Paramètre pour la clé primaire par défaut
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
