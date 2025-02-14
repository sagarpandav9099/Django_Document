 
# TODO Project setup
python -m venv myenv
myenv\Scripts\activate
pip install django   
python -m pip install --upgrade pip
django-admin startproject growupmore .
python manage.py startapp master


# TODO inatsall package
pip install requests


# TODO update setting.py
INSTALLED_APPS = [
    'master', 
]


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

class PostForm(forms.Form):
    userId = forms.IntegerField(widget=forms.HiddenInput(), initial=1)  # Assuming a default user
    title = forms.CharField(max_length=200)
    body = forms.CharField(widget=forms.Textarea)



# TODO master/views.py
from django.shortcuts import render, redirect
from .forms import PostForm
import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"

def list_posts(request):
    response = requests.get(API_URL)
    posts = response.json()
    return render(request, 'myapp/list.html', {'posts': posts})

def detail_post(request, pk):
    response = requests.get(f"{API_URL}/{pk}")
    post = response.json()
    return render(request, 'myapp/detail.html', {'post': post})

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            requests.post(API_URL, data=form.cleaned_data)
            return redirect('list_posts')
    else:
        form = PostForm()
    return render(request, 'myapp/create.html', {'form': form})

def update_post(request, pk):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            requests.put(f"{API_URL}/{pk}", data=form.cleaned_data)
            return redirect('list_posts')
    else:
        response = requests.get(f"{API_URL}/{pk}")
        post = response.json()
        form = PostForm(initial=post)
    return render(request, 'myapp/update.html', {'form': form, 'post_id': pk})

def delete_post(request, pk):
    requests.delete(f"{API_URL}/{pk}")
    return redirect('list_posts')



# TODO master/templates/myapp/list.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Posts List</title>
</head>
<body>
    <h1>List of Posts</h1>
    <a href="{% url 'create_post' %}">Create New Post</a>
    <ul>
        {% for post in posts %}
            <li>
                <h3>{{ post.title }}</h3>
                <p>{{ post.body }}</p>
                <a href="{% url 'detail_post' post.id %}">View Details</a> |
                <a href="{% url 'update_post' post.id %}">Edit</a> |
                <a href="{% url 'delete_post' post.id %}">Delete</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>




# TODO master/templates/myapp/detail.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Post Detail</title>
</head>
<body>
    <h1>Post Detail</h1>
    <h2>{{ post.title }}</h2>
    <p>{{ post.body }}</p>
    <a href="{% url 'list_posts' %}">Back to List</a>
</body>
</html>



# TODO master/templates/myapp/create.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Create Post</title>
</head>
<body>
    <h1>Create a New Post</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>
    <a href="{% url 'list_posts' %}">Back to List</a>
</body>
</html>


# TODO master/templates/myapp/update.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Edit Post</title>
</head>
<body>
    <h1>Edit Post</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Update</button>
    </form>
    <a href="{% url 'detail_post' post_id %}">Cancel</a>
</body>
</html>



# TODO master/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_posts, name='list_posts'),
    path('post/<int:pk>/', views.detail_post, name='detail_post'),
    path('post/new/', views.create_post, name='create_post'),
    path('post/<int:pk>/edit/', views.update_post, name='update_post'),
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),
]





# TODO project/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('master.urls')),
]

