
# TODO Project setup
python -m venv myenv
myenv\Scripts\activate
pip install django   
python -m pip install --upgrade pip
django-admin startproject growupmore .
python manage.py startapp master


# TODO update setting.py
INSTALLED_APPS = [
    'master', 
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'girishinindia@gmail.com'
EMAIL_HOST_PASSWORD = 'your app password'


TEMPLATES = [
    {
        'DIRS': [BASE_DIR, 'templates'],
    },
]

# TODO Do migration
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
admin
admin@gmail.com
password
password
y
python manage.py runserver


# TODO master/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    to_email = forms.EmailField(label="Recipient's email")
    message = forms.CharField(widget=forms.Textarea)


# TODO master/views.py
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from .forms import ContactForm

def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            to_email = form.cleaned_data['to_email']
            message = form.cleaned_data['message']
            send_mail(
                f"Message from {name}",
                message,
                'girishinindia@gmail.com',  # Hardcoded sender's email
                [to_email],  # Recipient's email from the form
                fail_silently=False,
            )
            return HttpResponse('Email sent successfully')
    else:
        form = ContactForm()
    return render(request, 'email_form.html', {'form': form})


# TODO master/templates/email_form.html

<!DOCTYPE html>
<html>
<head>
    <title>Contact Form</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Send</button>
    </form>
</body>
</html>


# TODO master/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('send_email/', views.send_email, name='send_email'),
]


# TODO project/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emailer/', include('master.urls')),
]