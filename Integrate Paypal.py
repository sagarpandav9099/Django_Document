
# TODO Project setup
python -m venv myenv
myenv\Scripts\activate
pip install django   
python -m pip install --upgrade pip
django-admin startproject growupmore .
python manage.py startapp master


# TODO inatsall package
pip install paypalrestsdk


# TODO update setting.py
INSTALLED_APPS = [
    'master', 
]


# PayPal settings  from https://developer.paypal.com/dashboard/accounts/
PAYPAL_CLIENT_ID = 'your-client-id'
PAYPAL_CLIENT_SECRET = 'your-client-secret'
PAYPAL_MODE = 'sandbox'  # change to 'live' for production

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

class Payment(models.Model):
    payment_id = models.CharField(max_length=100, blank=True)
    payment_status = models.CharField(max_length=20, blank=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_id


# TODO Do migration
python manage.py makemigrations master
python manage.py migrate master


# TODO master/forms.py
from django import forms

class PaymentForm(forms.Form):
    amount = forms.DecimalField(decimal_places=2, max_digits=6)


# TODO master/views.py
import paypalrestsdk
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import PaymentForm
from .models import Payment

paypalrestsdk.configure({
    "mode": settings.PAYPAL_MODE,
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET,
})

def payment_process(request):
    form = PaymentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "transactions": [{
                "amount": {
                    "total": str(form.cleaned_data['amount']),
                    "currency": "USD"
                },
                "description": "Payment transaction description."
            }],
            "redirect_urls": {
                "return_url": request.build_absolute_uri('/payment/done/'),
                "cancel_url": request.build_absolute_uri('/payment/canceled/'),
            }
        })

        if payment.create():
            for link in payment.links:
                if link.rel == "approval_url":
                    payment_instance = Payment(
                        payment_id=payment.id,
                        amount=form.cleaned_data['amount'],
                        payment_status=payment.state
                    )
                    payment_instance.save()
                    return redirect(link.href)
        else:
            print(payment.error)

    return render(request, 'payments/payment_form.html', {'form': form})

def payment_done(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')
    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        payment_instance = Payment.objects.get(payment_id=payment_id)
        payment_instance.payment_status = payment.state
        payment_instance.save()
        return render(request, 'payments/payment_done.html')
    else:
        return render(request, 'payments/payment_error.html')

def payment_canceled(request):
    return render(request, 'payments/payment_canceled.html')



# TODO master/templates/payments/payment_form.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Payment Form</title>
</head>
<body>
    <h1>Pay with PayPal</h1>
    <form method="post">
        {% csrf_token %}
        <label for="amount">Enter Amount:</label>
        {{ form.amount }}
        <button type="submit">Submit</button>
    </form>
</body>
</html>


# TODO master/templates/payments/payment_error.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Payment Error</title>
</head>
<body>
    <h1>Payment Error</h1>
    <p>There was an error processing your payment. Please try again later.</p>
    <a href="/">Return Home</a>
</body>
</html>


# TODO master/templates/payments/payment_done.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Payment Successful</title>
</head>
<body>
    <h1>Payment Successful!</h1>
    <p>Thank you for your payment.</p>
    <a href="/">Return Home</a>
</body>
</html>


# TODO master/templates/payments/payment_cancelled.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Payment Canceled</title>
</head>
<body>
    <h1>Payment Canceled</h1>
    <p>You have canceled the payment process.</p>
    <a href="/">Return Home</a>
</body>
</html>


# TODO master/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('process/', views.payment_process, name='payment_process'),
    path('done/', views.payment_done, name='payment_done'),
    path('canceled/', views.payment_canceled, name='payment_canceled'),
]



# TODO project/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payment/', include('master.urls')),
]
