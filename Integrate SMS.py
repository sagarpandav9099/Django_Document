
# TODO Project setup
python -m venv myenv
myenv\Scripts\activate
pip install django   
python -m pip install --upgrade pip
django-admin startproject growupmore .
python manage.py startapp master


# TODO inatsall package
pip install twilio


# TODO update setting.py
INSTALLED_APPS = [
    'master', 
]

H1FP5GLVULVQQEHZ5SJKWMVZ
# Twilio settings https://console.twilio.com/us1/account/keys-credentials/api-keys
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'  # SMS-capable Twilio phone number
TWILIO_WHATSAPP_NUMBER = 'whatsapp:your_twilio_whatsapp_number'  # WhatsApp-capable number, prefixed with "whatsapp:"


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


# TODO master/models.py
from django.db import models

class MessageLog(models.Model):
    to = models.CharField(max_length=100)
    body = models.TextField()
    direction = models.CharField(max_length=20)  # 'SMS' or 'WhatsApp'
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.direction} to {self.to} on {self.date_sent}"



# TODO Do migration
python manage.py makemigrations master
python manage.py migrate master


# TODO master/forms.py
from django import forms

class SendMessageForm(forms.Form):
    to = forms.CharField(label='To', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)
    send_via = forms.ChoiceField(label='Send Via', choices=[('sms', 'SMS'), ('whatsapp', 'WhatsApp')])



# TODO master/views.py
from django.shortcuts import render
from django.conf import settings
from twilio.rest import Client
from .forms import SendMessageForm
from .models import MessageLog

def send_message(request):
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            to = form.cleaned_data['to']
            body = form.cleaned_data['message']
            send_via = form.cleaned_data['send_via']

            if send_via == 'whatsapp':
                to = f"whatsapp:{to}"  # Prefix to number with whatsapp: for WhatsApp messages
                from_ = settings.TWILIO_WHATSAPP_NUMBER
            else:
                from_ = settings.TWILIO_PHONE_NUMBER

            message = client.messages.create(
                body=body,
                from_=from_,
                to=to
            )

            # Optionally save the message to the database
            MessageLog.objects.create(to=to, body=body, direction=send_via)

            return render(request, 'communication/message_sent.html', {'message': message.sid})
    else:
        form = SendMessageForm()

    return render(request, 'communication/send_message.html', {'form': form})




# TODO master/templates/communication/send_message.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Send Message</title>
</head>
<body>
    <h1>Send Message</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Send</button>
    </form>
</body>
</html>



# TODO master/templates/communication/message_sent.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Message Sent</title>
</head>
<body>
    <h1>Message Sent Successfully!</h1>
    <p>Your message ID: {{ message }}</p>
    <a href="{% url 'send_message' %}">Send Another Message</a>
</body>
</html>



# TODO master/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('send/', views.send_message, name='send_message'),
]




# TODO project/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('communication/', include('master.urls')),
]

