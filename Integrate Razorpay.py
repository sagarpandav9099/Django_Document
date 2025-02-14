
# TODO Project setup
python -m venv myenv
myenv\Scripts\activate
pip install django   
python -m pip install --upgrade pip
django-admin startproject growupmore .
python manage.py startapp master


# TODO inatsall package
pip install razorpay
pip install setuptools


# TODO update setting.py
INSTALLED_APPS = [
    'master', 
]


# Razorpay settings https://dashboard.razorpay.com/app/website-app-settings/api-keys
RAZORPAY_KEY_ID = 'your_key_id'
RAZORPAY_KEY_SECRET = 'your_key_secret'

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
    order_id = models.CharField(max_length=100, unique=True)
    payment_id = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_id



# TODO Do migration
python manage.py makemigrations master
python manage.py migrate master


# TODO master/forms.py
from django import forms

class PaymentForm(forms.Form):
    amount = forms.DecimalField(decimal_places=2, max_digits=10)



# TODO master/views.py
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import PaymentForm
from .models import Payment
import razorpay
from django.views.decorators.csrf import csrf_exempt

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

def payment_process(request):
    form = PaymentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        amount = int(form.cleaned_data['amount'] * 100)  # Razorpay accepts amount in paise
        currency = 'INR'
        razorpay_order = client.order.create(dict(amount=amount, currency=currency, payment_capture='1'))
        order_id = razorpay_order['id']

        # Save order to the database
        payment_instance = Payment(
            order_id=order_id,
            amount=form.cleaned_data['amount'],
            status='created'
        )
        payment_instance.save()

        # context to send to the form
        context = {
            'form': form,
            'order_id': order_id,
            'amount': amount,
            'razorpay_key_id': settings.RAZORPAY_KEY_ID,
        }
        return render(request, 'payments/payment_form.html', context)

    return render(request, 'payments/payment_form.html', {'form': form})

@csrf_exempt
def payment_success(request):
    if request.method == "POST":
        payment_id = request.POST.get('razorpay_payment_id')
        order_id = request.POST.get('razorpay_order_id')
        signature = request.POST.get('razorpay_signature')

        # Verify the payment (optional)
        params_dict = {
            'razorpay_order_id': order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }
        result = client.utility.verify_payment_signature(params_dict)
        if result is None:
            payment_instance = Payment.objects.get(order_id=order_id)
            payment_instance.payment_id = payment_id
            payment_instance.status = 'paid'
            payment_instance.save()
            return render(request, 'payments/payment_success.html')
        else:
            return render(request, 'payments/payment_failure.html')

    return redirect('payment_process')



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


# TODO master/urls.py
from django.urls import path
from .views import payment_process, payment_success

urlpatterns = [
    path('process/', payment_process, name='payment_process'),
    path('success/', payment_success, name='payment_success'),
]




# TODO project/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payment/', include('master.urls')),
]
