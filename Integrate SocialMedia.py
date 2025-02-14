
# TODO Project setup
python -m venv myenv
myenv\Scripts\activate
pip install django   
python -m pip install --upgrade pip
django-admin startproject growupmore .
python manage.py startapp master


# TODO install packages
pip install django-allauth


# TODO update setting.py
INSTALLED_APPS = [
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'master',
]


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# index of site which is added in admin
SITE_ID = 1

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


MIDDLEWARE = [
    'allauth.account.middleware.AccountMiddleware',
]


TEMPLATES = [
    {
        'DIRS': [BASE_DIR, 'templates'],
    },
]


# TODO project/urls.py
from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name = "login/index.html")),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]


# TODO Configure Google OAuth2 
Visit the Google Developer Console. https://console.cloud.google.com/
Create a new project.
Go to "Credentials", click "Create Credentials", and choose "OAuth client ID".
Configure the consent screen as required.
set javascript url to "http://localhost:8000"
Set the authorized redirect URIs. For development, it will be something like "http://localhost:8000/accounts/google/login/callback/"
Note down the Client ID and Client Secret.


# TODO Add Social Application in Django Admin
Run your Django server:
python manage.py runserver

Open http://127.0.0.1:8000/admin and log in with your superuser account.

Navigate to "Social applications" under "SOCIALACCOUNT".
Add a new social application:
Provider: Google
Name: Google
Client id: [Your Client ID from Google Console]
Secret key: [Your Client Secret from Google Console]
Sites: choose your site (localhost for development)

# TODO master/templates/login/index.html

{% load socialaccount %}
{% providers_media_js %}

<html>
  <body>
    {{user}}
    <a href="{% provider_login_url 'google' %}">Google Connect</a>
  </body>
</html>
