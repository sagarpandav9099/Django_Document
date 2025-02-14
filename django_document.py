
# ///////////////////////////
#  13 - How To Use Variables
# ///////////////////////////
# todo add templet in

<h1>hello,my name is {{name}}</h1>

# todo add in view
def home(request):
    return render(request,'home.html',{'name':'sagar pandav'})

# //////////////////////////
# 14 - Use Direct variables 
# ////////////////////////
# todo templets in add
{% with firstname='sagar pandav' %}
<h2>my name is {{firstname}}</h2>
{% endwith %}

# ///////////////////////
# 21 - Generate & Install Packages From Requirement Files
# ////////////////////////////
# ! pip freeze

# todo current file
# ! pip freeze > requirment.txt

# todo requirment file paste in new project
# ! pip install -r requirment.txt

# ////////////////////////////////
# 26 - Collect or backup Static Files
# ////////////////////////////////

# todo project setting in add
STATIC_ROOT = BASE_DIR / 'staticfiles'

# //////////////////////////////////
# 27 - create class based views
# ///////////////////////////////
# todo app views
from django.db.models.query import QuerySet
from . import TemplateViews
class homeview(TemplateViews):
    template_name = 'home.html'

# todo app url
from django.urls import path
from django.views import homeview_as_view

path('',homeview_as_view(),name='ecomerce home page')

# /////////////////////////////////
# 28 - genret documentetion
# ///////////////////////////////
# todo project url
from django.urls import path,include 
path('admin/doc/', include('django.contrib.admindocs.urls')),

# todo instal pip
# ! pip install docutils

# //////////////////////////////////
#  31- change title of admin page
# ///////////////////////////////
# todo add project url

admin.site.site_header = 'E-Fast Administration'
admin.site.site_title = 'ECommerce admin site'
admin.site.index_title = 'ECommerce Admin'

# /////////////////////////////
# 34- queryset and default database
# //////////////////////////////
from myapps.services.models import Student
x = Student.objects.all()
print(x)
print(type(x))    # query.queryset

# ////////////////////////////////////
# 38- migration withput delating database
# ////////////////////////////////////
# todo open python shell

from myapps.services.models import Product
Product.objects.all().delete()
# ----------
from django.db import connection
with connection.cursor() as cursor:
    cursor.execute("drop table homepage_product")
# ///////////////////////////////////
# 39 - fielded option
# ///////////////////////////////////
# todo create model
class Product(models.Model):
    Name = models.CharField(verbose_name="Name:",max_length=40,default="No Name",help_text="Enter Product Name")
    Qty = models.IntegerField(verbose_name="Quentity:",default=0,help_text="Enter Qunty of Product")
    Price = models.DecimalField(verbose_name="Price:", max_digits=5, decimal_places=2, default=0.0)
    Date_Added = models.DateField(verbose_name="Registred Date:",auto_now_add=True,)
    Date_Updated = models.DateField(verbose_name="Updated Date:",auto_now=True)
    Is_Active = models.BooleanField(verbose_name="Active:",default=True)
    URL = models.SlugField(verbose_name="Slug URL:")
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.Name}"
# //////////////////////////////
# 40 -primary key 
# ///////////////////////////
# todo Create your models.
class Department(models.Model):
    Dept_Id = models.AutoField(primary_key=True)
    DeptName = models.CharField(max_length=40)

# todo makemigrations
# ! python manage.py makemigrations
# ! python manage.py migrate
# //////////////////////////////////
# 41 - foregin key in model
# ////////////////////////////////

# todo create model
class Category(models.Model):
    Name = models.CharField(max_length=40)

    def __str__(self):
        return self.Name

class Product(models.Model):
    Name = models.CharField(max_length=40)
    Qty = models.IntegerField()
    Price = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    Date_Added = models.DateField(auto_now_add=True,)
    Date_Updated = models.DateField(auto_now=True)
    Is_Active = models.BooleanField()
    URL = models.SlugField()
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.Name}"

# todo make migration
#! python manage.py makemigrations
#! python manage.py migrate

# todo add admin in resister model
from django.contrib import admin
from myapps.services.models import Category,Product
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)

# /////////////////////////////////
# 42-sqlite plugins
# /////////////////////////////////

# todo pluging
# sqlite3

# ////////////////////////////////
# 43 - solve migration issues
# /////////////////////////////
# todo drop user table
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute('DROP TABLE table_name')

# todo reset migration 
# ! python manage.py makemigrations --empty services
# ! python manage.py makemigrations services
# ! python manage.py migrate

# ////////////////////////////////////
# 44-manage migration issues
# ///////////////////////////////////
# todo migration
# ! python manage.py makemigrations services
# ! python manage.py migrate

# todo reset migration
# ! python manage.py makemigrations --empty services

# todo chenge in 0001.py
dependencies = [
    ('services','previous_migration')
]

opretions = [
    # migrations.RUNSQL('DROP TABLE Department')
]

# todo migrations
# ! python manage.py migrate services

# todo create migrate without reset it
# ! python manage.py makemigrations services
# ! python manage.py migrate services

# ///////////////////////////////////
# 45-- Check Table is Create or Not
# /////////////////////////////////

# --------------------------
#todo add in views
# --------------------------
from typing import Any
from django.db import connection
from django.http import HttpResponse

table_name = "homepage_department"
def checktable(request):
   if is_table_created(table_name):
      result = (f"the table '{table_name}' exists")
   else:
      result = (f"the table '{table_name}' does not exist")
   return HttpResponse(result)

def is_table_created(table_name):
   with connection.cursor()as cursor:
      table_exists = table_name in connection.introspection.table_names()
   return table_exists

# ///////////////////////////////////////////////////
#  46-- fields options of models
# /////////////////////////////////////////////////

# --------------------------
# todo content_type alredy exist
# ---------------------------

#  ! python manage.py migrate --fake-initial

# -----------------------------------
# todo  Employee models
# ---------------------------------
from django.db import models
from django.core.validators import MinLengthValidator,RegexValidator,MinValueValidator

class Employee(models.Model):
    name = models.CharField(
        db_column = 'EName',
        null = False,
        max_length=40,
        validators=[
            MinValueValidator(2),
            RegexValidator(r'^[A-Za-z]+$','only alphabetic characters are allowed.')
        ]
    )
    birthdate = models.DateField(
        db_column = 'EBirthDate',
        null=False,
        max_length=60,
        validators=[
            RegexValidator(
                    r'^[\w.%+-]+[A-Za-z]{2,4}$','invalid email format.'
            )
        ]
    )

    phone= models.CharField(
        db_column='EPhone',
        null = False,
        max_length=10,
        default='0000000000',
        validators=[
            RegexValidator(r'^\d{10}$','phone number must be 10 digits')
        ]
    
    )
    hiredate = models.DateField(
        db_column='EHireDate',
        null = False
    )

    salary = models.DecimalField(
        db_column = 'Esalary',
        null = False,
        max_digits=7,
        decimal_places=2,
        default=0,
        validators=[MinLengthValidator(0)],
        help_text='salary must not be negative and shoud a maximum of 5 digit with two decimal place',
        error_messages={
            'min_value':'salary must not be less than zero',
            'max_digit' : 'salary shoud have a maximum of 5 digit',
            'max_decimal_places' : 'salary should have a maximum of decimal places'
        }
    )

# //////////////////////////////////////////
#  47-- Meta options
# ////////////////////////////////////////


class Customer(models.Model):
    name = models.CharField(max_length=40)
    birth_date = models.DateField()
    email = models.CharField(max_length=60)
    phone = models.IntegerField()

    class Meta:
        db_table = 'Customers'
        verbose_name_plural = 'Customers'
        ordering = ['name']
        unique_together = ['email','phone']

# ///////////////////////////
# 48 --  Upgrade Models
# /////////////////////////

# ---------------------
#  todo Rename Column Name
# --------------------
cname = models.CharField(max_length=40)

class Meta:
    ordering = ['cname']
       

# /////////////////////////////////////
#  49 -- Impliment One To One Reletionship
# ///////////////////////////////////////

# --------------------
# todo Add in models
# ---------------------

class Employee(models.Model):
    name = models.CharField(max_length=40)
    birth_date = models.DateField()
    email = models.CharField(max_length=60)
    phone = models.IntegerField()
    hiredate = models.DateTimeField()
    salary = models.FloatField()

class EmployeeDetails(models.Model):
    empid = models.OneToOneField(Employee,on_delete=models.CASCADE,primary_key=True)
    passport = models.CharField(max_length=10)

class EmployeeQualification(models.Model):
    empid = models.ForeignKey(Employee,on_delete=models.CASCADE)
    qualification = models.CharField(max_length=10)

# -------------------------
#  todo Diffrent Between Forenkey And One_To_One 
# ------------------------------
# ? with a foreign key, you can have multiple entris in the refrecing (employee details) table pointing to the same entry in the refrence table
# ? with one to one reletionship,each entry in the refrecing table is assosiated with exactly one entry in the refrecing table.

# ? the foregin key is   nullable be default,meaning it can be null,indicating an optional relationship.
# ? the one to one fiels is typicle set as the primary key of the refrencing table,indicate a unique relationship.

# ? you can access related objects in a both directions(e.g ,you can access the 'Employeedetailse' from "Employee" and 'vice versa ).


# ////////////////////////////////
#  50 Implement Many to Many Relationship
# /////////////////////////////////////

# --------------------------
#  Add In models
# ------------------------------

#  todo without using manytomany

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40,unique=True)
    price = models.FloatField()
    desc = models.CharField(max_length=100,default='N/A')

class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    orddate = models.DateTimeField()

class OrderProduct(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

# todo with manualy primary key and third table with foregian fields

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40,unique=True)
    price = models.FloatField()
    desc = models.CharField(max_length=100,default='N/A')

class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    orddate = models.DateTimeField()



# /////////////////////////////////////////////////
#  51 Query Execute or Reset 
# ////////////////////////////////////////////////

# --------------------------------
# create department model
# -----------------------------
class Department(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=30)

    from myapps.services.models import Department

    Department.objects.all()
    Department.objects.all().delete()
    Department.objects.create(id = 101,name = 'Account',location = 'india')

    # todo To Show Sql Queries
    from django.db import connection,reset_queries

    # todo show all the previously executed
    connection.queries

    # todo reset/eares previously executed
    reset_queries()
    connection.queries

    Department.objects.all()
    connection.queries

    Department.objects.all().delete()
    connection.queries

# ////////////////////////////////////////
#  52 Pretty Print Query
# ////////////////////////////////////////

# ?pygments - for highlighing syntex
# ?rsplpase - splitting and formatting sql statements

# ! pip install pygments
# ! pip install sqlparse

from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format
from myapps.services.models import Department

Department.objects.all()
Department.objects.all().delete()
Department.objects.create(id=102,name="Sales",location = "USA")
Department.objects.create(id=103,name="IT",location = "india")
x = Department.objects.filter(location = "india")
x = Department.objects.all()

sqlformatted = format(str(x.query),reindent = True)
print(highlight(sqlformatted,PostgresLexer(),TerminalFormatter()))

# /////////////////////////////////////////////////////
#53 - Insert Data Into Single Table Using Create()
# //////////////////////////////////////////////////////
# todo create a new view
def addnew(request):
    Department.objects.create(id=104,name='RGB',location = 'UK')
    return HttpResponse("Record is saved!")

# todo go to shell to run from shell
#! python manage.py shell
#! curl http://127.0.0.1:8000/new

# todo handle exception for unique constraint issue
from django.db import IntegrityError

def new(request):
    try:
        Department.objects.create(id=104,name='RGB',location='UK')
        return HttpResponse("record is saved!")
    except IntegrityError:
        return HttpResponse("sorry we cannot add!")
    
# todo go to shell to run from shell
# !python manage.py shell
#! curl http:.0.1:8000/new

# //////////////////////////////////
#  54 --Insert Data Using Save() Method
# ///////////////////////////////
# todo Create a new veiws
def save(request):
    try:
        Department(id=107,name='Dance',location='USA').save()
        return HttpResponse("record is saved!")
    except IntegrityError:
        return HttpResponse("sorry we cannot add!")
      
# todo go to shell to run from shell
#! python manage.py shell
# ! curl http://127.0.0.1:8000/save
    
# //////////////////////////////////////////////
#  55 - Difference Between Create() and Save()
# ////////////////////////////////////////////   

# todo It WillCreate a Record If ID is not exists or give error
Department.objects.create(id=101,name='AC',location = 'india')

# todo reset/erase previously executed
from django.db import connection,reset_queries
reset_queries()
connection.queries

# todo it will also create a record id is not exists or update if id is existed
Department(id=5001,name='A/C',location='india').save()

# todo reset/erase  previously executed
reset_queries()
connection.queries

# //////////////////////////////////
# 56 - Insert Record with Foreign key
# ////////////////////////////////////

# todo create models
class Course(models.Model):
    name=models.CharField(max_length=20)

class Student(models.model):
    name = models.CharField(max_length=20)
    courseid = models.ForeignKey(Course,on_delete=models.CASCADE)

# todo - Do Migration
# !python manage.py makemigration
#! python manage.py migrate

# todo -go to python shell but in different terminal
# ?project must be rnning
# ! python manage.py shell

# todo -add records into Course
Course.objects.create(name="Python Develoepmnt")
Course.objects.create(name="Web Designing")
Course.objects.create(name="Designing")

# todo - add records into Student with Foreign key
Student.objects.create(name='pandav sagar',courseid=Course.objects.get(id=1))
Student.objects.create(name='Dev Joshi',courseid=Course.objects.get(id=2))
Student.objects.create(name='Susmita Sen',courseid=Course.objects.get(id=1))

# ////////////////////////////////
# 57  Insert Record with DateTime Field
# ///////////////////////////////////
# todo see all data
# ! python manage.py shell
# ! SampleModel.objects.all()

# todo Create sample model
class SampleModel(models.Model):
    data_field = models.DateField()
    time_field = models.TimeField()
    datatime_field = models.DateTimeField()

# todo Do Migrations
# ! python manage.py makemigrations
# !python manage.py migrate

# todo way-1 using create()
from myapps.services.models import SampleModel
from datetime import date,time,datetime

sample = SampleModel.objects.create(
    date_field = date(2023,7,1),
    time_field = time(10,30),
    datetime_field = datetime(2023,7,1,10,30)

)

# OR

# todo way-2 -using cursor
from django.db import connection

sql = "insert into services_samplemodel(date_field,time_field,datetime_field) values(%s,%s,%s)"
params = [date(2023,7,2).isoformat(),time(12,0).isoformat(),datetime(2023,7,2,12,0).isoformat()]

with connection.cursor() as cursor:
    cursor.execute(sql,params)

# OR

# todo way 3 - with current date and time
from myapps.services.models import SampleModel
from datetime import date,time,datetime

current_date = date.today()
current_time = datetime.now().time()
current_datetime = datetime.now()

sample = SampleModel.objects.create(
    date_field = current_date,
    time_field = current_time,
    datetime_field = current_datetime
)

# OR
# todo way-4 - with current date and time with cursor
from django.db import connection
from datetime import date,time,datetime

current_date = date.today()
current_time = datetime.now().time()
current_datetime = datetime.now()

sql = "insert into services_SampleModel(date_field,time_field,datetime_field)values (%s,%s,%s)"
params = [current_date,current_time,current_datetime]

with connection.cursor() as cursor:
    cursor.execute(sql,params)

# Or
# todo way 5 - with date and time in string
from myapps.services.models import SampleModel
from datetime import datetime

date_string = "2023-07-01"
time_string = "10:30:00"
datetime_string = "2023-07-01 10:30:00"

date_obj = datetime.strptime(date_string,"%Y-%M-%D").date()
time_obj = datetime.strptime(time_string,"%H-%M-%S").time()
datetime_obj = datetime.strptime(datetime_string,"%Y-%M-%D %H:%M:%S")

sample = SampleModel.objects.create(
    date_field = date_obj,
    time_field = time_obj,
    datetime_field = datetime_obj
)

# OR
# todo way 6 -with date and time in string using cursor

from django.db import connection
from datetime import datetime

date_string = "2023-07-02"
time_string = "12:00:00"
datetime_string = "2023-07-02 12:00:00"

date_obj = datetime.strprime(date_string,"%Y-%M-%D").date()
time_obj = datetime.strprime(time_string,"%H-%M-%S").time()
datetime_obj = datetime.strptime(datetime_string,"%Y-%M-%D %H:%M:%S")

sql = "insert into services_samplemodel(date_field,time_field,datetime_field) values (%s,%s,%s)"
params = [date_obj,time_obj,datetime_obj]

with connection.cursor()as cursor:
    cursor.execute(sql.params)

# OR
# todo way 7 -with direct date and time in string
from myapps.services.models import SampleModel

date_string = "2023-07-02"
time_string = "12:00:00"
datetime_string = "2023-07-02 12:00:00"

sample = SampleModel.objects.create(
    date_field = date_string,
    time_field = time_string,
    datetime_field = datetime_string
)

# //////////////////////////////////////////////
#  58 --insert data with manytomany relationship
# /////////////////////////////////////////////
# todo create sample models
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name
    
# todo Do Migration
# ! python manage.py makemigrations
# !python manage.py migrate

# todo insert records
from myapps.services.models import Student,Course

# create students
student1 = Student.objects.create(name='john')
student2 = Student.objects.create(name='jane')

# create courses
course1 = Course.objects.create(name='math')
course2= Course.objects.create(name='science')
course3 = Course.objects.create(name='history')

# add courses to students
student1.courses.add(course1,course2)
student2.courses.add(course1,course2,course3)

# todo Retrieve all student
students = Student.objects.all()

for student in students:
    print(f"Student:{student.name}")
    print("courses:")
    for course in student.courses.all():
        print(f'-{course.name}')
    print()

# todo create models with extra files
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField('course', through='Enrollment')

    def __str__(self):
        return self.name
    
class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    courses = models.ForeignKey(Course,on_delete=models.CASCADE)
    fees = models.DecimalField(max_digits=8,decimal_places=2)
    discount = models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self):
        return f'{self.name} - {self.course.name}' 

# todo do migration
# ! python manage.py makemigration
# ! python manage.py migrate

# todo insert records
from myapps.services.models import Student,Course,Enrollment

# create student
student1 = Student.objects.create(name='john')
student2 = Student.objects.create(name='jane')

# create courses
course1 = Course.objects.create(name='math')
course2= Course.objects.create(name='science')
course3 = Course.objects.create(name='history')

# create enrollment with extra fields
enrollment1 = Enrollment.objects.create(student=student1,courses = course1,fees=100.00,discount=10.00)
enrollment2 = Enrollment.objects.create(student=student1,courses = course2,fees=100.00,discount=20.00)
enrollment3 = Enrollment.objects.create(student=student2,courses = course2,fees=100.00,discount=25.00)
enrollment4 = Enrollment.objects.create(student=student2,courses = course3,fees=100.00,discount=15.00)

# todo retrieve all enrollment
enrollments = Enrollment.objects.all()
for enrollment in enrollments:
    print(f'student:{enrollment.student.name}')
    print(f'course:{enrollment.courses.name}')
    print(f'fees:{enrollment.fees}')
    print(f'discount: {enrollment.discount}')
    print()

# ///////////////////////////////
# 59 -insert data with one to one relationship
# /////////////////////////////////////
# todo import in models

from django.db import models
class Person(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    bio = models.TextField()

    def __str__(self):
        return self.name

class PersonDetail(models.Model):
    person_profile = models.OneToOneField(Person,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name
    
# todo do migration
# !python manage.py makemigrations
# !python manage.py migrate

# todo insert records into one-to-one relationship
# create a userprofile object
person =Person.objects.create(name='john',email='john@example.com',bio='i am developer')

# create a userprofiledetails objects and associate it with the userprofile
person_details=PersonDetail.objects.create(
    person_profile = person,
    full_name = 'john doe',
    date_of_birth = '1990-01-01',
    address = '123 main st'
)

# //////////////////////////////////////////
# 60 - insert into multiples table using Atomic operations
# ////////////////////////////////////////////////
# todo create model

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
# todo python do migrations
# ! python manage.py makemigrations
# ! python manage.py migrate

# todo function to add value
from django.db import transaction
 
def create_author_and_book(author_name,book_title):
    with transaction.atomic():
        author = Author.objects.create(name=author_name)
        book = Book.objects.create(title=book_title,author = author)

# todo use above function
from django.db import transaction
from myapps.services.models import Author,Book

create_author_and_book('iron man','the avengers')

# ////////////////////////////////////////////////////////////
# 61-insert bulk records into single table
# ///////////////////////////////////////////////////////////

# todo create model
class piple(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

# todo do migrations
# ! python manage.py makemigrations
# !python manage.py migrate

# todo insert records
from myapps.services.models import piple

# create a list of objects
person = [
    piple(name = 'Alice',age = 25),
    piple(name = 'Bob',age = 30),
    piple(name = 'Charlia',age = 35)
]

# insert the objects into the table using bulk_create
piple.objects.bulk_create(person)

# todo another exemple

from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField() 

# todo do migrations
# !python manage.py makemigrations
# !python manage.py miograte

# todo insert records
from datetime import date
from myapps.services.models import Books

# create list of objects
books = [
    Books(title = 'Book 1',author = 'Author1',published_date = date(2020,1,1)),
    Books(title = 'Book 2',author = 'Author2',published_date = date(2021,2,2)),
    Books(title = 'Book 3',author = 'Author3',published_date = date(2022,3,3)),
]

# insert the objects into the table using bulk_create
Books.objects.bulk_create(books)

# //////////////////////////////////////////
# 62-bulk create vs create performance Analysis
# ////////////////////////////////////////////

# todo create model
from django.db import models

class ExampleModel(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()

# todo do migration
# !python manage.py makemigrations
# !python manage.py migrate

# todo test of create()
import time
start_time = time.time()

# create multiple instances using create()
for i in range(1000):
    ExampleModel.objects.create(name=f'Example {i}', value=i)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time for create(): {execution_time} seconds")

# todo test of bulk_create()
import time
start_time = time.time()

# create multiple instances using bulk_create()
examples = []
for i in range(1000):
    example = ExampleModel(name=f"Example {i}", value=i)
    examples.append(example)

ExampleModel.objects.bulk_create(examples)

end_time =time.time()
execution_time = end_time - start_time
print(f"Execution time for bulk_create(): {execution_time} seconds")

# //////////////////////////////////////////////
# 63 - generate dump or json data from table
# /////////////////////////////////////////////

# todo create model
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    hero = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Actor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name 

# todo add some records
Movie.objects.create(title="The Avengers",hero="Iroman")
Movie.objects.create(title="Thor:Ragnarok",hero="Thor")
Movie.objects.create(title="Captain America",hero="Steve Rojar")

Actor.objects.create(name="Disha Patani",age=27)
Actor.objects.create(name="pooja Hegde",age=26)
Actor.objects.create(name="Rashmika mandana",age=24)
Actor.objects.create(name="Mnuhal Thakur",age=29)

# todo Generate Dump/json data file
# todo create jsondata directory first on root
# ?--indent 2 meanes two spech instead of defaul tab with 4 or 8 spaces
#! python manage.py dumpdata services.Movies -- indent 2 > jsondata/movies.json
#! python manage.py dumpdata services.Actore -- indent 2 > jsondata/actore.json  

# todo Backup data using python modual, it will create jsondata directory automatically at root level
# todo file name is "backup_data.py"

import subprocess
import os

# create Directory
def create_folder_if_not_exists(folder_name):
    root_directory = os.path.dirname(os.path.abspath(__file__))
    folder_path  =  os.path.join(root_directory,folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    else:
        pass

# usage example
folder_name = "jsondata"
create_folder_if_not_exists(folder_name)

models = [
    'services.Movie',
    'services.Actor',
]

files = [
    'movies.json',
    'actors.json',
]

i = 0
for file in files:
    command = f'python manage.py dumpdata {models[i]} --indent 2 > {folder_name}/{file}'
    subprocess.run(command,shell=True)
    i=+1

# todo call above file form command
# ! python backup_data.py

# //////////////////////////////////////
# 64 - Load Dump /Json Data Into Table
# /////////////////////////////////////////

# todo load data using command
#! python manage.py loaddata jsondata/movies.json
#! python manage.py loaddata jsondata/actors.json

# todo Load data using python module
# todo create file on root named "load_data.py"
from django.core.management import call_command
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE",'ELearning.settings')
django.setup()

files = [
    'movies.json',
    'actors.json',
]

for file in files:
    fixture_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),f"jsondata/{file}")
    call_command('loaddate',fixture_path)

# todo call above file from command
#! python load_data.py

# todo Auto load  file names
from django.core.management import call_command
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE",'ELearning.settings')
django.setup()

jsondata_folder = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'jsondata')
files = os.listdir(jsondata_folder)

for file in files:
    if file.endswith('.json'):
        fixture_path = os.path.join(jsondata_folder,file)
        call_command('loaddata',fixture_path)

# todo call above file from command
#! python load_data.py

# //////////////////////////////////////
# 65 - Backup Fixture Automatically
# //////////////////////////////////////

import subprocess
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','ELearning.settings')
django.setup()

# todo create Directory
def create_folder_if_not_exists(folder_name):
    # root_directory = D:\Sagar\Django\MyProject
    root_directory = os.path.dirname(os.path.abspath(__file__))

    # folder_path = D:\Sagar\Django\MyProject\jsondata
    folder_path = os.path.join(root_directory,folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    else:
        pass

# using example
folder_name = 'jsondata'
create_folder_if_not_exists(folder_name)

app_name = "services"

#todo  Retrieve models from the app's models.py file
models = []
app_models = django.apps.apps.get_app_config(app_name).get_models()
for model in app_models:
    models.append(f'{model._meta.app_label}.{model.__name__}')

files = []
for model in models:
    app_label,model_name = model.split('.')            # services.Actor
    file_name = f'{model_name.lower()}s.json'          # actor.json
    files.append(file_name)

i = 0
for file in files:
    command = f'python manage.py dumpdata {models[i]} --indent 2 > {folder_name}/{file}'
    subprocess.run(command,shell=True)
    i +=1

# //////////////////////////////////////////////
# 66 - Retrieve Data in a Diffrent Way
# ///////////////////////////////////////////
# -----------------------------------
# todo object way
# ----------------------------------

from myapps.services.models import Movie,Actor

# todo Method 1:Queryset all()
all_movies = Movie.objects.all()
all_actors = Actor.objects.all()

# todo Iterate over the records
for movie in all_movies:
    title = movie.title
    hero = movie.hero
    print(title)
    print(hero)

for actor in all_actors:
    name = actor.name
    age = actor.age
    print(name)
    print(age)

# todo Method 2:Queryset values()
all_movies = Movie.objects.values()
all_actors = Actor.objects.values()

# todo Method 3:Queryset values_list()
all_movies = Movie.objects.values_list()
all_actors = Actor.objects.values_list()

# todo Method 4: Queryset only() (to retrieve specific fields)
all_movies = Movie.objects.only('title','hero')
all_actors = Actor.objects.only('name','age')

# todo Retrieve specific column values() or value_list
movie_titles = Movie.objects.values_list('title',flat=True)
actor_names = Actor.objects.values_list('name',flat=True)

# -----------------------------------------
# todo SQL way
# -----------------------------------------

from django.db import connection

# todo raw SQL Query to retrieve all records from movie model
movie_query = "SELECT * FROM services_movie"
with connection.cursor() as cursor:
    cursor.execute(movie_query)
    all_movies = cursor.fetchall()

# todo Raw SQL query to retrieve all records from Actor model
actor_query ="SELECT * FROM services_actor"
with connection.cursor() as cursor:
    cursor.execute(actor_query)
    all_actors = cursor.fetchall()

# todo Raw SQL query to retrieve specific column from Movie model
movie_query = "SELECT title FROM services_movie"
with connection.cursor() as cursor:
    cursor.execute(movie_query)
    movie_title = cursor.fetchall()

# todo Raw SQL query to retrieve specific column from actor model
actor_query = "SELECT name FROM services_actor"
with connection.cursor() as cursor:
    cursor.execute(actor_query)
    actor_names = cursor.fetchall()
    
# todo iterate over the records
for movie in all_movies:
    # Access individual fields of the movie
    title = movie[1]  #Assuming title is second field
    hero = movie[2]   #Assuming hero is the third field
    print(title)
    print(hero)

for actor in all_actors:
    name = actor[1]   #Assuming name is the second field
    age = actor[2]    #Assuming age is the third field
    print(name)
    print(age)

# /////////////////////////////////////////
# 67 Retrieve Single  Records in a Different Way
# ///////////////////////////////////////////

# -------------------------------
# todo object way
# ------------------------------
from myapps.services.models import Movie,Actor

# todo Retrive a single record by pk using get() method
movie = Movie.objects.get(pk=1)     #or (id=1)
actor = Actor.objects.get(pk=1)     #or (id=1)

# todo Access the fields of the record
movie_title = movie.title
actor_name = actor.name

# --------------------------------------
# todo sql way
# ------------------------------------
from django.db import connection

# todo Raw Sql query to retrive a single records by pk from movie model
movie_query = "SELECT * FROM services_movie where id = %s"
with connection.cursor()as cursor:
    cursor.execute(movie_query,[1]) #Reple 1 with the desired primery key value
    movie_record = cursor.fetchone()

# todo Raw SQl query to  retrieve a singel records by pk from Actor model
actor_query = "SELECT * FROM services_actor WHERE id = %s"
with connection.cursor() as cursor:
    cursor.execute(actor_query,[1]) #replace 1 with the  desired primary key value
    actor_record = cursor.fetchone()

# todo Access the fields of the records
movie_title = movie_record[1]    # Assuming title is the second fields
actor_name = actor_record[1]     # Assuming name is theseconds fields

# //////////////////////////////////////
# 68 - Filtering Records in a Diffrent Way
# //////////////////////////////////////

# ---------------------------------
# todo object way
# ---------------------------------

from myapps.services.models import Movie,Actor
# todo Method 1:filter using filter() method
movies = Movie.objects.filter(title__contains = 'Avengers')
actors = Actor.objects.filter(age__gte=25)

# todo Method 2:filter using exclude() method
movies = Movie.objects.exclude(hero='Iroman')
actors = Actor.objects.exclude(name='Disha patani')

# todo Metho 3:filter using Q object for complex queries
from django.db.models import Q 
movies = Movie.objects.filter(Q(hero = 'Ironman') | Q(hero='Thor'))

# todo Iterate over filtered records
for movie in movies:
    #Access individual fields of the movie
    title = movie.title
    hero = movie.hero

for actor in actors:
    #Access individual fields of the  actor
    name = actor.name
    age = actor.age
    print(name)
    print(age)

# ---------------------------------
# todo sql way
# -------------------------------
from django.db import connection

# todo Raw SQL query to filter records from Movie model
movie_query = "SELECT * FROM services_movie WHERE title LIKE %s"
with connection.cursor() as cursor:
    cursor.execute(movie_query, ['%Avengers%'])
    movie_records = cursor.fetchall()

# todo Raw SQL query to filter records from Actor model
actor_query = "SELECT * FROM services_actor where age >= %s"
with connection.cursor() as cursor:
    cursor.execute(actor_query,[25])
    actor_records = cursor.fetchall()

# todo iterate over the filtered records
for movie in movie_records:
    # Access individual fields of the movie
    title = movie[1]  #assuming title is the second field
    hero = movie[2]   #Assuming hero is the third field 

for actor in actor_records:
    # Access individual fields of the actor
    name = actor[1] 
    age = actor[2]

# ////////////////////////////////////////////
# 69 - filtering records with 'And' and 'OR' 
# //////////////////////////////////////.

# ------------------------
# todo object way
# ----------------------------
from myapps.services.models import Movie,Actor
from django.db.models  import Q 

# todo Method 1:using multiple filter conditions
movie = Movie.objects.filter(title__contains='Avengers',hero='Iroman')
actor = Actor.objects.filter(name='Disha Patani',age__gte=25)

# todo Method 2: using Q objects for complex queries
movies = Movie.objects.filter(Q(title__contains='Avengers') | Q(hero='Iroman'))  #one ture
actor = Actor.objects.filter(Q(name='Disha Patani') & Q(age__gte=25))   # both condition are true

# todo iterate over the filtered records
for movie in movies:
    # Access individual of the movie
    title = movie.title
    hero = movie.hero

for actor in actors:
    # Access individual of the actor
    name = actor.name
    age = actor.age
    print(name)
    print(age)

# ---------------------
# todo sql way
# -----------------

from django.db import connection

# todo Raw sql query to filter records using And operator
movie_query = "SELECT * FROM services_movie WHERE title LIKE %s AND hero = %s"
with connection .cursor() as cursor:
    cursor.execute(movie_query,['%Avengers%','Iroman'])
    movie_reccords = cursor.fetchall()

# todo Raw SQL query to filter records using OR operetor
actor_query = "SELECT * FROM services_movie WHERE  name= %s OR age >=%s"
with connection.cursor() as cursor:
    cursor.execute(actor_query,['Disha Patani',25])
    actor_records = cursor.fetchall()

# todo iterate over the filtered records
for movie in movie_records:
    title = movie[1]
    hero = movie[2]

for actor in actor_records:
    name = actor[1]
    age = actor[2]

# //////////////////////////////
# 70 - Retrive objects from one to one Relationship table
# ////////////////////////////////////////

# ---------------------------
# todo object way
# ---------------------------
from django.db import models

class UserProfile(models.Model):
    name = models.charfield(max_lenth=100)

class User(models.Model):
    username = models.charfield(max_lenth =100)
    profile = models.OneToOneField(UserProfile,on_delete=models.CASCADE)

# todo Add some records
# create userprofiles
user_profile1 = UserProfile.objects.create(name='john doe')
user_profile2 = UserProfile.objects.create(name='jane smith')

# create user with associated userprofile
user1 = User.objects.create(username='johnd',profile=user_profile1)
user2 = User.objects.create(username='janes',profile=user_profile2)

# todo retrive userprofile and related users
user_profiles = UserProfile.objects.all()

for user_profile in user_profiles:
    print(f"user profile name: {user_profile.name}")

    # Access assciated user fields
    user = user_profile.user
    print(f"username: {user.username}")

    print()

# -------------------------------
# todo sql way
# ---------------------------------

# todo add some records
from django.db import connection

# todo add some records
with connection.cursor() as cursor:
    cursor.execute("INSERT INTO services_userprofiles (name) values ('john doe')")
    cursor.execute("INSERT INTO services_userprofiles (name) values ('jane smith')")

# todo retrive userprofiles and related users
with connection.cursor() as cursor:
    query = """
    SELECT services_userprofile.name,services_user.username
    FROM services_userprofile
    INNER JOIN services_user ON services_userprofile.id = services_user.profile_id
    """
    cursor.execute(query)
    records = cursor.fetchall()

for record in records:
    user_profile_name = record[0]
    print(f"user profile name:{user_profile_name}")

    username = record[1]
    print(f"username:{username}")
    print()

# ///////////////////////////////////
# 71 - Retrive object from one to many Relationship tables
# ///////////////////////////////////////

# ----------------------------
# todo object way
# ------------------------------
class Category(models.Model):
    name = models.CharField(max_length=100)

class product(models.Model):
    name = models.CharField(max_length=100)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)

# todo add some records
# create category
category1 = Category.objects.create(name='Electronics')
category2 = Category.objects.create(name='Clothing')

# create product
product1 = product.objects.create(name='Laptop',Category=category1)
product2 = product.objects.create(name='T-Shirt',Category=category2)
product3 = product.objects.create(name='Smartphone',Category=category1)

# todo retrive userprofile and related user
categories = Category.objects.all()

for category in categories:
    print(f'category name:{category.name}')

    products = category.product_set.all()

    for product in products:
        print(f'product name: {product.name}')
    print()

# -----------------------------
# todo sql way
# ----------------------------

from django.db import connection

# todo add some records

with connection.cursor() as cursor:
    # create category
    cursor.execute("INSERT INTO services_category (name) VAlUES  ('Electronics')")
    cursor.execute("INSERT INTO services_category (name) VAlUES  ('Clothing')")

    # create product with associated category
    cursor.execute("INSERT INTO services_category (name,category_id) VALUES ('Laptop',LAST_INSERT_ID())")
    cursor.execute("INSERT INTO services_category (name,category_id) VALUES ('T-Shirt',LAST_INSERT_ID())")
    cursor.execute("INSERT INTO services_category (name,category_id) VALUES ('smartphone',LAST_INSERT_ID())")

# todo retrieve Category and releted products
with connection.cursor() as cursor:
    # retrive Categories and related products using join
    query="""
        select services_category.name,services_product.name
        FROM services_category
        INNER JOIN services_product on services_category.id = services_product.category_id
    """ 

    cursor.execute(query)
    records = cursor.fetchall()

    for record in records:
        category_name = record[0]
        print(f"category name: {category_name}")

        # associate product name
        product_name = record[1]
        print(f"product name: {product_name}")

        print()

# ///////////////////////////////////////
# 72 - retrive object from many to many reletionship
# ////////////////////////////////////////

# ------------------------------
# todo object way
# --------------------------

from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)

class Product2(models.Model):
    name = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)

# todo add some records
# create tags
tag1 = Tag.objects.create(name='Electronics')
tag2 = Tag.objects.create(name='Clothing')

# create product or associat tag
product1 = Product2.objects.create(name='Laptop')
product1.tags.add(tag1,tag2)

product2 = Product2.objects.create(name='T-Shirt')
product2.tags.add(tag1)

product3 = Product2.objects.create(name='Smartphone')
product3.tags.add(tag2)

# todo retrive userprofile and related user
# retrive products and related tag
products = Product2.objects.all()

for product in products:
    # access product fields
    print(f"product name: {product.name}")

    # access asociated tag
    tags = product.tags.all()

    for tag in tags:
        print(f"tag name: {tag.name}")
    
    print()

# ---------------------------
# todo sql way
# ------------------------------

from django.db import connection

# todo add some records
with connection.cursor() as cursor:
    # create tag
    cursor.execute("INSERT INTO services_tag (name) values ('Electronics')")
    cursor.execute("INSERT INTO services_tag (name) values ('Clothing')")

    # create product
    cursor.execute("INSERT INTO services_tag (name) VALUES ('Laptop')")
    cursor.execute("INSERT INTO services_tag (name) VALUES ('T-Shirt')")
    cursor.execute("INSERT INTO services_tag (name) VALUES ('Smartphone')")

    # associated tag with intermidiat table
    cursor.execute("INSERT INTO services_product_tags (product_id,Tag_id) VALUES (LAST_INSERT_ID(),1)")
    cursor.execute("INSERT INTO services_product_tags (product_id,Tag_id) VALUES (LAST_INSERT_ID(),2)")
    cursor.execute("INSERT INTO services_product_tags (product_id,Tag_id) VALUES (LAST_INSERT_ID(),2)")
    cursor.execute("INSERT INTO services_product_tags (product_id,Tag_id) VALUES (LAST_INSERT_ID(),1)")

# todo retrive products and related tag
with connection.cursor() as cursor:
    # retrive product and related tags join and intermediate table
    query = """
    SELECT services_product2.name,services_tag.name
    FROM services_product2
    INNER JOIN services_product2_tags on services_product2.id = services_product2_tags.product2_id
    INNER JOIN services_tag on services_product2_tags.tag_id = services_tag.id
    """
    cursor.execute(query)
    records = cursor.fetchall()

    for record in records:
        # access product name
        product_name = record[0]
        print(f"product name:{product_name}")
        tag_name = record[1]
        print(f"tag name: {tag_name}")
        print()

# ///////////////////////////////////////////
# 73 - Modify existing data for a specified record in a table
# //////////////////////////////////////////////

# ---------------------------
# todo object way
# ----------------------------

class User2(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

user1 = User2.objects.create(name='john Doe',age=25)
user2 = User2.objects.create(name='jane smith',age=30)

# todo Modify Existing record
user = User2.objects.get(name='john Doe')

# Modify the record
user.age = 27
user.save()

# ------------------------
# todo sql way
# -----------------------
from django.db import connection

# Execute raw sql queries to create the  table and add sample records
with connection.cursor() as cursor:
    cursor.execute("""
    CREATE TABLE services_user2(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT
    )
    """)

# todo Modify EXsiting Records
    # insert sample records
    cursor.execute("""
        INSERT INTO services_user2(name,age) VALUES
        ('john Doe',25),
        ('jane smith',30)
""")
    
# todo Update existing record
with connection.cursor() as cursor:
    query = """
        Update services_user2
        SET age = 30
        where name LIKE 'john Doe';
    """
    cursor.execute(query)

# //////////////////////////////
# 74 - Implementing Update or create
# ///////////////////////////////

# -------------------------------
# todo object way
# ---------------------------
# todo Update existing records or create a new one
user,created = User2.objects.update_or_create(
    name='john Doe',
    defaults={'age':27}
    
)

user,created = User2.objects.update_or_create(
    name='sagar pandav',
    defaults={'age':22}
)
# todo check if a new recor was created
if created:
    print('New records created.')
else:
    print('Exisisting records update')

# ------------------
# todo sql way
# ---------------------

# todo update existing records or create a new one
with connection.cursor() as cursor:
    cursor.execute("SELECT id FROM services_user2 WHERE name = 'john Doe'")
    result = cursor.fetchone()

    if result:
        # update existing record
        cursor.execute("UPDATE services_user2 SET age = 20 WHERE name = 'john Doe'")
    else:
        cursor.execute("INSERT INTO services_user2 (name,age) VALUES ('john Doe',27)")


# ////////////////////////////////////
# 75 - bulkupdate records in a single table 
# ////////////////////////////////////

# ------------------
# todo object way
# ------------------

# todo add sample records
User2.objects.bulk_create([
    User2(name='john Doe',age=25),
    User2(name='jane smith',age=30),
    User2(name='Bob johnson',age=35),
]) 

# todo Retrive the records you want to update
users = User2.objects.filter(name__startswith='j')

# todo perform bulk update
users.update(age=25)

# ------------------
# todo sql way
# --------------------

# todo Execute a raw sql query to perform bulk update
with connection.cursor() as cursor:
    cursor.execute("UPDATE services_user2 SET age=32 WHERE name LIKE 'j%'")

# ///////////////////////////////////
# 76 - Delete single and multiple objects
# /////////////////////////////////////

# ------------------
# todo object way
# ----------------

# todo Delete a single object
user = User2.objects.get(id=1)
user.delete()

# todo Delete multiple objects
users = User2.objects.filter(age__gte=30)
users.delete()

# -----------------------------
# todo sql way
# -----------------

# todo execute raw sql query to delete objects

with connection.cursor() as cursor:
    # todo Delete a single objects
    cursor.execute("DELETE FROM services_user2  WHERE id=1")

    # todo Delete multiple objects
    cursor.execute("DELETE FROM services_user2 WHERE age>=30")

# ///////////////////////////////
# 77 - Create custom field -part 1
# ///////////////////////////////
# todo create 'custom_fields.py' file in director

from django.db import models
from django.core.exceptions import ValidationError
import re

class AutoIDField(models.CharField):
    def __init__(self,prefix="", start=1,incrementby=1, *args,**kwargs):
        self.prefix = prefix
        self.start = start
        self.incrementby = incrementby
        kwargs.setdefault('max_length',10)
        kwargs.setdefault('editable',False)
        kwargs.setdefault('primary_key',True)
        super().__init__(*args, **kwargs)

    # ?pre_save() is overridden.it is called before saving the field value to the database.
    def pre_save(self,model_instance,add):
        value = getattr(model_instance,self.attname)
        if not value:
            last_instance = model_instance.__class__.objects.last()
            last_id = last_instance.pk if last_instance else self.prefix + \
                str(self.start - self.incrementby)
            last_id = int(last_id.replace(self.prefix, ""))

            while True:
                last_id += self.incrementby
                generated_id = self.prefix + str(last_id)
                if not model_instance.__class__.objects.filter(pk=generated_id).exists():
                    value = generated_id
                    break

        setattr(model_instance,self.attname,value)
        return value
    
class NameField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length',20)
        kwargs.setdefault('help_text','Enter a name (2-20 characters)')
        kwargs.setdefault('validators',[self.validate_name])
        super().__init__(*args, **kwargs)

    def validate_name(self,value):
        if len(value)<2 or len(value)>20:
            raise ValidationError('name must be between 2 and 20 charecters')
        if not re.match(r'[a-zA-Z]+$',value):
            raise ValidationError('name can only contain alphabets')
        if ' ' in value:
            raise ValidationError('name cannot contain spaces')
        
    # ?pre_save() is overridden.it is called before saving the field value to the database.
    def pre_save(self,model_instance,add):
        value = getattr(model_instance,self.attname)
        self.validate_name(value)
        if value:
            value = value.capitalize()
            setattr(model_instance,self.attname,value)
        return value

class MobileField(models.IntegerField):
    def __init__(self,*args, **kwargs):
        kwargs.setdefault('validators', [self.validate_mobile])
        kwargs.setdefault('default', 0)
        super().__init__(*args, **kwargs)

    def validate_mobile(self,value):
        if value < 1000000000 or value < 9999999999:
            raise ValidationError('mobile number must be 10 digit number')

    def pre_save(self,model_instance,add):
        value = getattr(model_instance,self.attname)
        if value is None or value =="":
            value = self.get_default()
        if value !=0:
            self.validate_mobile(value)
        setattr(model_instance,self.attname,value)
        return value 
    
class EmailField(models.EmailField):
    def __init__(self,*args, **kwargs):
        kwargs.setdefault('max_length',60)
        kwargs.setdefault('help_text','Enter valid email address')
        kwargs.setdefault('validators', [self.validate_email])
        super().__init__(*args, **kwargs)

    def validate_email(self,value):
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$',value):
            raise ValidationError('Enter a valid Email Address')
        
    def pre_save(self,model_instance,add):
        value = getattr(model_instance,self.attname)
        if value:
            self.validate_email(value)
            value = value.lower()
            setattr(model_instance,self.attname,value)
        return value
    
class DescriptionField(models.CharField):
    def __init__(self,*args, **kwargs):
        kwargs.setdefault('max_length',100)
        kwargs.setdefault('default','N/A')
        kwargs.setdefault('help_text','Enter a Description (2-100 charecter)')
        super().__init__(*args, **kwargs)

    def validate_description(self,value):
            if len(value)< 2 or len(value) >100:
                raise ValidationError('Description must be 2 to 100 charecter')
            
    def pre_save(self,model_instance,add):
        value = getattr(model_instance,self.attname)
        self.validate_description(value)
        setattr(model_instance,self.attname,value)
        return value
    
class CreatedDateField(models.DataTimeFile):
    def __init__(self,*args, **kwargs):
        kwargs.setdefault('auto_now_add',True)
        super().__init__(*args, **kwargs)

class UpdatedDateField(models.DateTimeField):
    def __init__(self,*args, **kwargs):
        kwargs.setdefault('auto_now',True)
        super().__init__(*args, **kwargs)

# todo create model
from django.db import models
from myapps.services.custom_fields import AutoIDField,NameField,MobileField,EmailField,DescriptionField,CreatedDateField,UpdatedDateField

class Person2(models.Model):
    id = AutoIDField(perfix='P',start=10,incrementby=10)
    name = NameField()
    email = EmailField()
    mobile = MobileField()
    description = DescriptionField()
    created_at = CreatedDateField()
    updated_at = UpdatedDateField()

    def __str__(self):
        return self.name

# todo add data using save method
#! python manage.py shell
from myapps.services.models import Person2

p1 = Person2(name='dhruvi',email='dhruvi@example.com',mobile = 1234567890,description='knowledge is anocean')
p1.save()

# /////////////////////////////
# 79 - django single
# //////////////////////////////

# todo create simple models
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
    
# todo create files "signals.py" in your app directory
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User 
from django.core.mail import send_mail
# from  .models import BlogPost


@receiver(post_save,sender=BlogPost)
def send_notification(sender,instance,created,**kwargs):
    if created:
        subject = 'New Blog Post published'
        message = f"A new blog post title '{instance.title}' has been published."
        recipients = User.objects.filter(is_staff=True).value_list('username',flat=True)
        print(f"Subject:{subject}")
        print(f"Message: {message}")
        print(f"Recipients: {recipients}")

# todo import the signal receiver function in your django app's apps.py
from django.apps import AppConfig

def ready(self):
    import myapps.services.signals

# todo add view
from myapps.services.models import BlogPost
def create_blog_post(request):
    post = BlogPost(title='new Blog post',content='Lorem ipsum dolor sit amet.')
    post.save()

# ///////////////////////////////////
# 80 - add user in deffrent way
# //////////////////////////////////////

# todo add new users to default 'user' table 
from django.contrib.auth.models import User

# add single users
user = User.objects.create_user('user1','user1@gmail.com','password')
user = User.objects.create_user('user2','user2@gmail.com','password')
user = User.objects.create_user('user3','user1@gmail.com','password')
admin = User.objects.create_superuser('admin3','admin@gmail.com','password')

# add More paramteres
user = User.objects.create(
    username='user4',
    password = 'password',
    first_name = 'Sahaj',
    last_name = 'savaliya',
    email = 'sahaj@example.com',
    is_staff = 1,
)

# add multiple users
user_data = [
    {'username':'user5','password':'password'},
    {'username':'user6','password':'password'},
    {'username':'user7','password':'password'},

]

for data in user_data:
    User.objects.create_user(username=data['username'],password=data['password'])

# add multiple users without data
user_data = [
    {'username':'user8','password':'password'},
    {'username':'user9','password':'password'},
    {'username':'user10','password':'password'},

]

for data in user_data:
    User.objects.create_user(username='username',password='password')

#todo  form baedcreate view
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect

def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print('user is created')
    else:
        form = UserCreationForm()

    return render(request,'create_user.html',{'form':form})

# todo create html page
# <form method='post'>
#     {% csrf_token %}
#     {{form.as_p}}
#     <button type = 'submit'>create</button>

# todo set url
# path('create-user/',views.create_user,name='create_user'),

# ///////////////////////////////////
# 81 - user model proxi
# //////////////////////////////////
# todo create default "user" table proxi
# ? create a proxi model called customer by subclassing the user models
# ? by setting proxi = True,we inicate that this model is a proxi model and does not create a new database table 

from django.contrib.auth.models import User as AuthUser
# ? if you have created user model manualy also than it will refer to your model even if you import above
# ? but if you went to acess in-built  user model than you can rename it as below...
from django.contrib.auth.models import User as AuthUser

class CustomUser(User):
    class Meta:
        proxi = True

# todo get all user 
from myapps.services.models import CustomUser
#! CustomUSer.objects.all()


# ///////////////////////////////////
# 82 - user model beheviar with model manager
# /////////////////////////////////

from django.contrib.auth.models import User

class PersonMangerinactive(models.Manager):
    def get_queryset(self):
        return super(PersonMangerinactive, self).get_queryset().filter(is_active=False)

class PersonMangeractive(models.Manager):
    def get_queryset(self):
        return super(PersonMangeractive, self).get_queryset().filter(is_active=True)

class CustomUser(AuthUser):
    inactive = PersonMangerinactive()
    active = PersonMangeractive()
    class Meta:
        proxy = True
        ordering = ('first_name',)

    def __str__(self):
        return self.first_name
    
# todo check all users
#! CustomUSer.inactive.all()
#! CustomUSer.inactive.all().count()

#! CustomUSer.active.all()
#! CustomUSer.active.all().count()

# /////////////////////////////////////
# 83 - user model beheviar with class method
# /////////////////////////////////////

# reference 82

# todo updated portion
# ? classmethod is used to call method directoly,without the need to create an instance
# ? if you went to count only the active objects,you can pass states=True
@classmethod
def count_all(cls,status=None):
    return cls.objects.filter(is_active=True).count()

# ? this method need objects to call this nethod
def check_active(self):
    if self.is_active == True:
        return "you are active"
    else:
        return "you are not active"


# todo count all user
x= CustomUser.count_all()
print(x)

x= CustomUser.count_all(status=True)
print(x)

# todo check whether user is active or not
# todo make any user inactive or check both

from myapps.services.models import CustomUser
x = CustomUser.objects.get(id=1) 
x.check_active()

# ///////////////////////////////////////
# 84 - store extra informetion of user using one to one relationship
# ///////////////////////////////////////
# todo store more informetion about user

from django.db import models
from django.contrib.auth.models import User

class InUserProfile(models.Model):
    user = models.OneToOneField(AuthUser,on_delete=models.CASCADE)
    age = models.IntegerField(null=True,blank=True)
    nickname = models.CharField(max_length = 100,null=True,blank=True)

    def __str__(self):
        return self.user.username
    
# todo create new user
from django.contrib.auth.models import User
from myapps.services.models import UserProfile

# create a new user
user = User.objects.create_user(username='john',password = 'password')

# create user profile instance for the user 
profile = UserProfile.objects.create(user=user,age=30,nickname='janey')

# todo add details for existing user

from django.contrib.auth.models import User
from myapps.services.models import UserProfile

# get the user instance
user = User.objects.get(username='john')

# create a userprofile instance and assoiate it with the user
profile = InUserProfile.objects.create(user = user,age = 25,nickname = 'johny')


# //////////////////////////////////////
# 85 - add user data automaticaly using signal and one to one relationship
# //////////////////////////////////////////

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.IntegerField(null=True,blank=True)
    nickname = models.CharField(max_length = 100,null=True,blank=True)

    def __str__(self):
        return self.user.username

# ? for singal file
# todo create reciaver to do auto opretions
@receiver(post_save,sender=AuthUser) 
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        # it create new user data autometicaly into userprofile table using table instance
        # but not age and nickname
        InUserProfile.objects.create(user=instance)

# todo create new user from shell
#! python manage.py createsuperuser

# //////////////////////////////////////
# 86 - add extra fields on user admin form
# //////////////////////////////////////
#? in "admin.py"
# todo create model to store more informatin about user

from myapps.Enquiry.models import InUserProfile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

class UserProfileInline(admin.StackedInline):
    model = InUserProfile 
    # which means that when editing a user in the django admin interface
    # the associated Userprofile instace cannot be deleted directly from the inline display
    can_delete = False

# todo it will show all extra fields while creating new user as well as update existing user
class UserAdmin(AuthUserAdmin):
    inlines = [UserProfileInline]

# or
# todo it will show all no extra fields while creating new user but will show while update exsiting user
# class UserAdmin(AuthUserAdmin):
#   def add_view(self,*args,**kwargs):
    #     self.inlines=[]
    #     return super(userAdmin,self).add_view(*args,**kwargs)

    # def change_view(self,*args,**kwargs):
    #     self.inlines = [UserProfileInline]
    #     return super(UserAdmin,self).change_view(*args,**kwargs)
    
# todo unregister old user admin - to removew all setting
admin.site.unregister(User)

# todo register new user admin - to apply new setting
admin.site.register(User,UserAdmin)

# ////////////////////////////////////
# 87 - add Extra user using html view
# /////////////////////////////////////

#? for views.py
#todo add extra fields of user and profile after login only
from django.shortcuts import render,redirect
from django.contrib.auth.models import User as AuthUser
from django import forms
from myapps.Enquiry.models import InUserProfile
from django.contrib.auth.decorators import login_required
from django.db import transction

# ?for views.py
# todo it is for in-buit user odel
class UserForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ("first_name","last_name")

# todo it is for user defined user-profile model
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = InUserProfile
        fields = ("age","nickname")

# ? login is required means you can change detail only after login
@login_required
# ?it is for adding records in multiple  tables at a same time
@transaction.atomic
def update_profile(request):
    if request.method == "POST":
        pass

    # or
    # todo practical
        # user_form = UserForm(request.POST,instance=request.user)
        # user_profile_form = UserProfileForm(request.POST, instance=request.user.inuserprofile)
        # if user_form.is_valid() and user_profile_form.is_valid():
        #     user_form.save()
        #     user_profile_form.save()
        #     print("data has been added")  #or return redirect("user:profile")
    else:
        user_form = UserForm(instance=request.user)
        user_profile_form  = UserProfileForm(instance=request.user.inuserprofile)
    return render(request,"profile.html",{"u_form":user_form, "p_form": user_profile_form})

# ? for url.py
# todo add url to urls.py
from myapps.Enquiry import views 
urlpatterns = [
    path("profile/",views.update_profile,name="profile")
] 

# ?for profile.html
# todo add form to html page
# <form method="POST">
#     {% csrf_token %}
#     {{u_form.as_p}}
#     {{p_form.as_p}}
#     <button type="submit">submit</button>
# </fom>

# ///////////////////////////
# 88 - inherit & add Extra fiels to user by abstrec
# //////////////////////////////////

# todo setup new projects
#! python -m venv myvenv
#! myvenv\scripts\activate
#! pip install django
#! python -m pip install --upgrade pip
#! django-admin startproject ELerning .
#! python manage.py startapp front 

# todo add model for abstrecting exsisting user model before migrate 
from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    age = models.IntegerField(null=True,blank=True)
    nickname = models.CharField(max_length=100,null=True,blank=True)

# todo do migrate to install default packages
# ! python manage.py migrate front

# it will error because of permission that django
# ?Add setting.py
# todo to add for permission
AUTH_USER_MODEL = 'front.MyUser'

# todo do migrate again
# !python manage.py migrate front

# todo add admin
from front.models import MyUser
admin.site.register(MyUser)

# ///////////////////////////////////
# 89 - add custom user fields on admin page
# /////////////////////////////////////
# ? add app's admin.py 
# todo to add custom field at admin page

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import NewUser

# class CustomUserAdmin(UserAdmin):
# fieldsets = (
#     *UserAdmin.fieldsets,
#     (
#         'New Fields',
#         {
#             'fields':(
#                 'age',
#                 'nickname'
#             ),
#         },
#     ),
# )
# admin.site.register(NewUser,CustomUserAdmin)

# or
# todo change position of fields
from django.contrib.auth.admin import UserAdmin
fields = list(UserAdmin.fieldsets)
fields[0] =(None, {'fields':('username','email','password')})
fields[1] = ('Personal info',{'fields':('first_name','last_name','age','nickname')})
fields[2] = ('Permissions',{'fields':('is_active','is_staff','is_superuser','groups','user_permision')})
fields[3] = ('Important dates',{'fields':('last_login','date_joined')})

UserAdmin.fieldsets = tuple(fields)
admin.site.register(NewUser,UserAdmin)

# todo check admin page for user

# ///////////////////////////////////
# 90 - Auto genrete records with 
# /////////////////////////////
# todo create models
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
# todo install package first
pip install django-faker
pip install factory_boy

# todo if error than cmd
pip install wheel setuptools pip --upgrade
pip3 install wheel setuptools pip --upgrade

# todo create factory method for creating fake recors
# ?for factories.py

import factory
from faker import Faker
from .models import Customer

Fake = Faker()
class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model  = Customer

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.LazyAttribute(lambda obj : f"{obj.first_name.lower()}.{obj.last_name.lower()}@example.com")
    age = factory.Faker('random_int',min=18,max=100)

# todo Generate records in python shell or with file nmame "fill_records.py"

from front.factories import CustomerFactory

# create a single random customer using the CustomerFactory
random_Customer = CustomerFactory()

# create a list of 10 random customer using the customerfactory
random_Customer_list = CustomerFactory.create_batch(10)

# you can access the fields of genreted customers like this
for customer in random_Customer_list:
    print(customer.first_name,customer.last_name,customer.email,customer.age)

# /////////////////////////////////
# 91 - Auto genrate records for one to one relationship
# //////////////////////////////////////

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class PersonProfile(models.Model):
    person = models.OneToOneField(Person,on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    address = models.TextField()

    def __str__(self):
        return f"profile of {self.person}"
    
# ?for factory.py
from front.models import Person,PersonProfile

class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")

class PersonProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PersonProfile

    person = factory.subFactory(PersonFactory)
    age = factory.Faker('random_int',min=18,max=99)
    address = factory.Facker('address')

# todo generate records in python shell or with file name 'fill_records.py'
# import the models and factories
from front.models import Person,PersonProfile
from front.factories import PersonFactory,PersonProfileFactory

# create a single person and ther profile using the factories
person1 = PersonFactory()
profile1 = PersonProfileFactory(person=person1)

# create a list of 5 person and profile using factories with multiple instance
person_list = PersonFactory.create_batch(5)
profile_list = [PersonProfileFactory(person=person) for person in person_list]

# print the detailse of a redonly genrated and ther profile
print(person1.first_name,person1.last_name,person1.email)
print(profile1.age,profile1.address)

# /////////////////////////////////
# 92 - auto generate records for one to many relationship
# ///////////////////////////////////////

# todo create model
class Branch(models.model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
# ? for factory.py
from .models import Branch,Employee

class BranchFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Branch

    name = factory.Faker('company')
    location = factory.Faker('address')

class EmployeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Employee

    branch = factory.SubFactory(BranchFactory)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    position = factory.Faker('job')

# todo genrete records in python shell with file name fill_records.py
from front.models import Branch,Employee
from front.factories import BranchFactory,EmployeeFactory

# create single branch and it employee using the factories
branch1 = BranchFactory()
employee1 = EmployeeFactory(branch=branch1)
employee2 = EmployeeFactory(branch=branch1)

# create list of 3 branch and their employee using the factories with multiple instance
branches_list = BranchFactory.create_batch(3)
employees_list = [EmployeeFactory(branch=branch) for branch in branches_list]

# print the detailse of a readonly genreted branch and its emplyee
print(branch1.name,branch1.location)
for employee in branch1.employee_set.all():
    print(employee.first_name,employee.last_name,employee.position)

# ///////////////////////////////////
# 93 - Auto generate records for many to many relationship
# ///////////////////////////////////////////
# todo create model
class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    first_name= models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
# todo create factori.py
from front.models import Course,Student

class CourseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Course

    name = factory.Faker('sentence',nb_words=3)
    code = factory.Faker('text',max_nb_chars=10)

class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Student

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    age = factory.Faker('random_int',min=18,max=30)

    @factory.post_generation
    def Courses(self,create,extracted,**kwargs):
        if not create or not extracted:
            return
        self.Courses.add(*extracted)

# todo import the models and factories for factories.py
from front.models import Course,Student
from front.factories import CourseFactory,StudentFactory

# create a single courses using the coursefactory
course1 = CourseFactory()

# create a list of 5 courses using coursefactory with multiple instances
courses_list = CourseFactory.create_batch(5)

# create a single student using studentfactory with specific courses
specific_courses = CourseFactory.create_batch(3)
student1 = StudentFactory(courses=specific_courses)

# create a list of 10 student using the studentfactory with multiple instances and random courses
students_list = StudentFactory.create_batch(10,courses=CourseFactory.create_batch(2))

# ///////////////////////////////////////////
# 94 - Auto genret records for many to many reletionship with extra fields
# ///////////////////////////////////////////////////////
# todo create model
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    order_number = models.CharField(max_length=20)
    date_created = models.DateField(auto_now_add=True)
    products = models.ManyToManyField(Product,through='OrderItem')

    def __str__(self):
        return self.order_number
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quntity = models.PositiveIntegerField()
    discount = models.DecimalField(max_digits=5,decimal_places=2,default=0.0)

# todo creat in fctories.py
from front.models import Product,Order,OrderItem

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
    
    name = factory.Faker('sentence',nb_words=3)
    price = factory.Faker('pydecimal',rigth_digits=2,positive=True,max_value=100)

class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    order_number = factory.Faker('uuid4')

    # define a relationship to create OrderItem instance for each order
    @factory.post_generation
    def orderitem_set(self,create,extracted,**kwargs):
        if not create:
            return
        if extracted:
            self.orderitem_set.add(*extracted)
        else:
            order_item = OrderItemFactory(order=self)
            self.orderitem_set.add(order_item)

class OrderItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OrderItem

    order = factory.SubFactory(OrderFactory)
    product = factory.SubFactory(ProductFactory)
    quntity  = factory.Faker('random_int',min=1,max=10)
    discount = factory.Faker('pydecimal',right_digits=2,max_value=10,positive=True)

# todo create records in shell
from front.models import Product,Order,OrderItem
from front.factories import ProductFactory,OrderFactory,OrderItemFactory

# create a single  product using the productfactory
product1 = ProductFactory()

# create a list of 5 product using the productfactory with multiple instances
products_list = ProductFactory.create_batch(5)

# create a single order using the orderfactory with order item
order1 = OrderFactory()
order_items = OrderItemFactory.create_batch(3,order=order1)

# create a list of 10 order with random order item using orderfactory and orderitemfactory with multiple instance
order_list = OrderFactory.create_batch(10)


# //////////////////////////////////////
# 95 - Model Meneger naming
# ////////////////////////////////////
# * need to remember while defining model class
# 1.All database fields
# 2.custom manager attributes
# 3.class Meta
# 4.def __str__(Self)
# 5. def save()
# 6.def get_absolute_url()
# 7.any custom method

# todo create model with custom model manager
class Worker(models.Model):
    firstname = models.CharField(max_length=100)
    age = models.IntegerField()

    something = models.Manager()

    
    
# todo add some records
# todo Access the records as below
from front.models import Worker
Worker.objects.all()
Worker.something.all()

# todo add class to implement more functionality before worker model
# todo add manager keyword at the end of class name

class WorkerFilterManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(firstname='sagar')
    
# todo modify model buy no need migrate
class Worker(models.Model):
    firstname = models.CharField(max_length=100)
    age = models.IntegerField()

    something = models.Manager()
    # ?update line
    custom_manager = WorkerFilterManager()

    def __str__(self):
        return self.firstname
    
# todo add some records
# todo access the record as below
from front.models import Worker
Worker.something.all()
Worker.custom_manager.all()

# ////////////////////////////////////////
# 96 - model manager extra method
# //////////////////////////////////////
# todo create extra method in model class
from django.db.models import Case,When,Value

class AgeCheckManager(models.Manager):
    # ?table level functionality
    def countall(self):
        return self.count()
    
    # ?table level funstionality
    def student_age(self):
        return self.annotate(
            classification=Case(
            When(age__gt=17, then= Value('Adult')),
            default = Value('Child')
            )
        )
    
# todo update existing student model
class Student(models.Model):
    firstname = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.ManyToManyField(Course,related_name='course')

    objects = AgeCheckManager()

    def __str__(self):
        return self.firstname
    
    # todo update below code
    # ?objects level functionality
    def age_check(self):
        if self.age:
            if self.age<18:
                return 'Child'
            else:
                return 'Adult'
        else:
            return 'no age defained'
        
# todo now try in python shell
# ?for objects level functional
x= Student.objects.all()
x[0].age_check()

# ?for table level functionality
Student.objects.count()
Student.objects.countall()
x = Student.objects.student_age()
x[0].age
x[0].classification

# //////////////////////////////
# 97 - modify inisial queryset
# //////////////////////////////
# todo update the code
class ActiveFilter(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)
    
    # todo update the ode
    def active_filter(self):
        return self.filter(active=True)
    
#* todo update existing  Student
class Student(models.Model):
    firstname = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.ManyToManyField(Course,related_name='course')
    active = models.BooleanField(default=True)  # ! default records with inisial records

    objects = AgeCheckManager()
    # objects = models.Manager()           #todo update to default manager 
    studentfilter = ActiveFilter()         #todo update record to code migrations

    def __str__(self):
        return self.firstname
    
    def age_check(self):
        if self.age:
            if self.age<18:
                return 'Child'
            else:
                return 'Adult'
        else:
            return 'no age defained'

# todo migration because we are adding new filds
# ! python manage.py makemigrations front
# ! python manage.py migrate front

# todo create extra method in model class
#*from django.db.models import Case,When,Value

# * class AgeCheckManager(models.Manager):
    # ?table level functionality
    #* def countall(self):
    #*    return self.count()
    
     # ?table level funstionality
    #*def student_age(self):
    #*     return self.annotate(
    #*          classification=Case(
    #*          When(age__gt=17, then= Value('Adult')),
    #*          default = Value('Child')
    #*    )
    #* )

    
# todo execute a following query
from front.models import Student

# make a one student inactive
x = Student.objects.get(id=1)
x.active = False
x.save(update_fields = ['active'])

# will return non active student
Student.objects.filter(active=False)

# show active students and count it
Student.objects.active_filter()
Student.objects.active_filter().count()

# use of active filter
Student.studentfilter.all()
Student.studentfilter.count()

# ////////////////////////////////
# 98 - using multiple model files
# //////////////////////////////
# todo setup new projects
#! python -m venv myvenv
#! myvenv\scripts\activate
#! pip install django
#! python -m pip install --upgrade pip
#! django-admin startproject ELerning .
#! python manage.py startapp front 

# todo create 'models' Directory under your app
# todo create '__init__.py' file under 'model' directory
# todo create 'person.py' model under 'models' directory

from django.db import models
class Person(models.Model):
    name = models.CharField(max_length=100)

# todo create 'book.py' model under 'models' directory

from django.db import models
class Book(models.model):
    title = models.CharField(max_length=150)
    content = models.TextField()

# todo update '__init__.py' file under 'models' directory
from .person import Person
from .book import Book

# front is a name of your app
# "FrontConfig" is a name of class in apps.py
default_app_config = 'front.apps.FrontConfig'

# todo do migration
# ! python manage.py makemigrations front
# ! python manage.py migrate front

# ////////////////////////////////
# 99 - using multiple view file
# ////////////////////////////

# todo create 'views.py' directory your app
# todo create '__init__.py' file under 'views' directory
# todo create 'person.py' model under 'views' directory

from django.shortcuts import render
from django.http import HttpResponse

def select_person(request):
    return HttpResponse('this is person view')

# todo create book.py model under 'views' directory
from django.shortcuts import render
from django.http import HttpResponse

def select_book(request):
    return HttpResponse('this is book view')

# todo update "__init__.py" file under 'model' derctory
default_app_config = 'front.apps.FrontConfig'

# todo add urls.py into apps
from django.urls import include,path
from .views import person,book

urlpatterns = [
    path('person/',person.select_person,name='Select Person'),
    path('book/',book.select_book,name='Select Book'),
]

# todo run server and check views
#! python manage.py runserver

# ///////////////////////////////////
# 100 - configuring mysql with django
# ///////////////////////////////////
# todo install package
# ! pip install mysqlclient

# todo change database setting
DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME':'testdb',
        'USER':'root',
        'PASSWORD':'password',
        'HOST':'localhost',
        'PORT':'3306'
    }
}

# ///////////////////////////////
# 101 - configuring postgresql with django
# /////////////////////////////////
# todo install package
# ! pip install psycopg2

# todo change database setting
DATABASES = {
     'default':{
        'ENGINE':'django.db.backends.postgresql',
        'NAME':'testdb',
        'USER':'postgres',
        'PASSWORD':'password',
        'HOST':'localhost',
        'PORT':'5432'
    }

}

# ///////////////////////////////////////////
# 102 - passing Object to HTML page
# ////////////////////////////////////////
# todo create Model
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name
    
# todo add some records
# !python manage.py shell

from back.models import Product
Product.objects.create(name='Product1',price=19.99,description='description of product1')
Product.objects.create(name='Product2',price=29.99,description='description of product2')
Product.objects.create(name='Product3',price=39.99,description='description of product3')
Product.objects.create(name='Product4',price=49.99,description='description of product4')
Product.objects.create(name='Product5',price=59.99,description='description of product5')

# todo create view
from django.shortcuts import render
from django.http import HttpResponse
from front.models.product import Product

def product_list(request):
    products = Product.objects.all()
    return render(request,'product_list.html',{'products':products})

# todo add url patterns in urls.py
path('products/',product.product_list,name='product_list'),

# ////////////////////////////////////
# 103 - looping throgh objects
# ////////////////////////////////////

# ? for product_list.html
# todo create html template and show objects data

# <!DOCTYPE html>
# <html>
# <head>
   
#     <title>Product List</title>
    
# </head>
# <body>
#     <h1>Product List</h1>
#     <ul>
#         {% for product in products %}
#         <li>
#             <strong>{{product.name}}</strong><br>
#             Price : ${{product.price}}<br>
#             Description : {{product.description}}
#         </li>
#         {% endfor %}
#     </ul>    
# </body>
# </html>

# ///////////////////////////////////
# 104 - Details Views
# ///////////////////////////////////
# todo create view
from django.shortcuts import render,get_object_or_404
from back.models import Product

def product_detail(request,pk):
    # retrive the product using get_objects_or_404 to handle if the product doesn't exist
    product = get_object_or_404(Product,pk=pk)
    return render(request,'product_detailse.html',{'product':product})

# todo create url pathpath('products/<int:pk>/',p
# add this pattern for details view
path('products/<int:pk>/',product.product_detail,name='product_detail'),

# ?for product_detail.html
# todo create html page

# <!DOCTYPE html>
# <html>
# <head>
   
#     <title>{{product.name}}</title>
    
# </head>
# <body>
#     <h1>{{product.name}}</h1>
      # <p> Price : ${{product.price}}</p>
#      <p>Description : {{product.description}}</p>
#          
# </body>
# </html>

# //////////////////////////////////
# 105 - create link for detailse view
# /////////////////////////////////
# todo updete product_list.html
# <!DOCTYPE html>
# <html>
# <head>
   
#     <title>Product List</title>
    
# </head>
# <body>
#     <h1>Product List</h1>
#     <ul>
#         {% for product in products %}
#         <li>
#             <strong><a href="/products/{{product.id}}/">{{product.name}}</a></strong><br>
#             Price : ${{product.price}}<br>
#             Description : {{product.description}}
#         </li>
#         {% endfor %}
#     </ul>    
# </body>
# </html>

# ////////////////////////////
# 106 - removing hardcoded URLs
# ////////////////////////////////

# todo update product_list.html
# <!DOCTYPE html>
# <html>
# <head>
   
#     <title>Product List</title>
    
# </head>
# <body>
#     <h1>Product List</h1>
#     <ul>
#         {% for product in products %}
#         <li>
#             <strong><a href="{% url 'product_detail' product.id %}">{{product.name}}</a></strong><br>
#             Price : ${{product.price}}<br>
#             Description : {{product.description}}
#         </li>
#         {% endfor %}
#     </ul>    
# </body>
# </html>

# ////////////////////////////////
# 107 - namespecing urls
# ///////////////////////////////
# todo update url.py 
# ? namespecing help prevent conflicts multiple have url patterns with the name
app_name = 'front'
urlpatterns = [
    path('products/',views.product_list,name='product_list'),
    path('products/<int:pk>/',views.product_detail,name='product_detail'),
]

# todo update product_list.html
# <strong><a href="{% url 'back:product_detail' product.id %}">{{product.name}}</a></strong><br>

# //////////////////////////////////
# 108 - add image field to model
# /////////////////////////////////
# todo install package
# ! pip install Pillow

# todo update model
image = models.ImageField(upload_to='product_images/',blank=True,null=True)

# todo make migrations
# ! python manage.py makemigrations
# ! python manage.py migrate

# todo update project setting.py
# path where media is stored
MEDIA_ROOT = BASE_DIR / 'media'

# Base url to serve media files
MEDIA_URL = '/media/'

# todo update projects urls.py
from django.conf import settings
from django.conf.urls.static import static

# serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# or
# media files will be served using the django development server,both in debug and producttion modes
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

# /////////////////////////////////////////
# 109 - add styling to objects
# ////////////////////////////////////////
# <html>
# <head>
#     <title>Product List</title>
#      <link href="http://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet">

# </head>
# <body>
    
#     <div class= "container">
#         <h1 class="mt-4 mb-4">Product List</h1>
#         <ul class="list-group">
#             {% for product in products %}
#             <li class="list-group-item">
#                 <div class= "d-flex justify-content-between align-items-center">
#                     <strong><a href="{% url 'front:product_detail' product.id %}">{{product.name}}</a></strong><br>
#                     <span class="badge bg-primary">${{product.price}}</span>
#                 </div>
#                 <p class="mt-2">{{product.description}}</p>
#             </li>
#             {% endfor %}
#         </ul>
#     </div>

# </body>
# </html>

# /////////////////////////////////////////////
# 110 - add styling to detailsview
# ///////////////////////////////////////////
# todo for product_detail.html
# <html>
# <head>
#     <title>Product List</title>
#      <link href="http://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet">

# </head>
# <body>
#         <div class="container">
#         <h1 class="mt-4">{{product.name}}</h1>
#             <div class ="row mt-3">
#                 <div class="col-md-6">
#                     <img src="{{product.image.url}}" class="img-fluid" alt="{{product.name}}">
#                 </div>
#                 <div class="col-md-6">
#                     <p>Price:${{product.price}}</p>
#                     <p>Description:{{product.description}}</p>
#                 </div>
#             </div>
#     </div>
# </body>
# </html>

# ///////////////////////////////////////////
# 111 - CURD creating form part-1
# //////////////////////////////////////////
# todo creating view
from django.shortcuts import render,get_object_or_404,redirect
from django import forms
from front.models import Product

def product_create(request):
    class ProductForm(forms.ModelForm):
        class Meta:
            model = Product
            fields = ('name','price','image','description')

    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('front:product_list')
        
    else:
        form = ProductForm()
    return render(request,'product_form.html',{'form':form})
    
# todo create add url 
path('create/',product.product_create,name='product_create')

# ? for product_form.html for add and update both
# todo create a form
# <body>
#     <h1>{% if form.instance.pk %}Edit Product{% else%}Create Product{%endif %}</h1>
#     <form method="post" enctype="multipart/form-data">
#         {% csrf_token %}
#         {{form.as_p}}
#         <input type="submit" value="Save">
#     </form>
#     <a href="{% url 'front:product_list' %}">Cancel</a>
# </body>

# /////////////////////////////////////////
# 112 -  CURD creating form part-2
# //////////////////////////////////////////
# todo create a form
# <html>
# <head>
#     <title>Product List</title>
#      <link href="http://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet">

# </head>
# <body>
#         <div class="container mt-5">
#         <h1>{% if form.instance.pk %}Edit Product {% else %}Create Product{% endif %}</h1>
#            <form method='post' enctype='multipart/form-data'>
#             {% csrf_token %}
#             <div class="form-group">
#                 <label for="{{form.name.id_for_label }}">Name:</label>
#                 {{form.name}}
#             </div>
#             <div class="form-group">
#                 <label for="{{form.price.id_for_label}}">price:</label>
#                 {{form.price}}
#             </div>
#             <div class="form-group">
#                 <label for="{{form.image.id_for_label}}">Image:</label>
#                 {{form.image}}
#             </div>
#             <div class="form-group">
#                 <label for="{{form.description.id_for_label}}">Description:</label>
#                 {{form.description}}
#             </div>
#             <input type="submit" value="save" class="btn btn-primary">
#         </form>
#         <a href="{% url 'froontproduct_list' %}" class="btn btn-secondary mt-3">Cencel</a>
#     </div>
# </body>
# </html>


# todo update product list.html
# <table class="table table-striped">
# <thead>
#     <tr>
#            <table class="table table-striped">
#         <thead>
#             <tr>
#                 <th>Image</th>
#                 <th>Name</th>
#                 <th>Price</th>
#                 <th>Description</th>
#                 <th>Actions</th>
#             </tr>
#         </thead>
#         <tbody>
#             {% for product in products %}
#             <tr>
#                 <td>
#                     <img src="{{product.image.url}}" alt="{{product.name}}" style="max-width:100;max-height:100;">
#                 </td>
#                 <td>{{product.name}}</td>
#                 <td>{{product.price}}</td>
#                 <td>{{product.description}}</td>
#                 <td>
#                     <a href="{% url 'product_detail' product.pk %}" class="btn btn-sm btn-info">
#                         <i class="bi bi-eye"></i>View</a>
#                     <a href="{% url 'product_update' product.pk %}" class="btn btn-sm btn-warning">
#                         <i class="bi bi-pencil"></i>Edit</a>
#                     <a href="{% url 'product_delate' product.pk %}" class="btn btn-sm btn-danger">
#                         <i class="bi bi-trash"></i>Delate</a>
#                     </td>
#                 </tr>
#                 {% endfor %}
#             </tbody>
#         </table>

# ////////////////////////////////
# 113 - crud update data part-1
# /////////////////////////////
# todo for views
def product_update(request,pk):
    class ProductForm(forms.ModelForm):
        class Meta:
            model=Product
            fields =('name','price','image','description')

    product = get_object_or_404(Product,pk=pk)
    if request.method =='POST':
        form = ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('back:product_list')
    else:
        form = ProductForm(instance=product)
    return render(request,'product_form.html',{'form':form})

# ////////////////////////////////////
# 114 -crud update data part-2
# //////////////////////////////////
<input type="text" name="name" maxlength="100" required id="id_name" class="form-control input-lg mt-1" value="{{form.instance.name}}">

# /////////////////////////////////////
# 115 - crud update data part-3
# ////////////////////////////////////
# todo install tweaks package
# ! pip install django-widget-tweaks

# todo install in appcv
INSTALL_APPS += ['widget_tweaks',]

# todo load twiks on html page
{% load widget_tweaks %}

# todo product_form.html
{{form.name|attr:"class:form-control input-lg" |attr:"maxlength:100"|attr:"required"}}

# /////////////////////////////////////
# 116 - crud delate data
# ////////////////////////////////////
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('front:product_list')
    return render(request,'product_confirm_delete.html', {'product':product})

# todo create template "product_confirm_delete.html"
# <html>
# <head>
#     <title>Product List</title>
#      <link href="http://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet">

# </head>
# <body>
#         <div class="container mt-5">
#         <h1>Delete {{product.name}}</h1>
#             <p>Are you went to delete this product?</p>
#             <form method="post">
#                   {% csrf_token %}
#                   <input type="submit" value="yes,delete" class="btn btn-danger">
#               </form>
#               <a href="{% url 'product_list' %}" class="btn btn-secondary mt-3">Cencel</a>
#           </div>

# </body>
# </html>

# todo add url
path('delete/<int:pk>/',product.product_delete,name='product_delete'),


# ///////////////////////////////////////
# 117 - populate dropdown
# /////////////////////////////////////
# todo create model
class Branch(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
# resister model in init.py
from .branch import Branch
    
# todo migration
# ! python manage.py makemigrations front 
# ! python manage.py migrate front

# todo add records
# ! python manage.py shell
from front.models.branch import Branch

Branch.objects.create(name='Pune',location='Chinchwad')
Branch.objects.create(name='Surat',location='Katargam')
Branch.objects.create(name='Mumbai',location='Dadar')

# todo create views
from front.models.branch import Branch

def branch_list(request):
    branches = Branch.objects.all()
    return render(request, 'branch_list.html',{'branches':branches})

# todo add urls patterns to apps url.py
path('branches/',branch.branch_list,name='branch_list'),

# todo add some records
# todo create branch_list.html
<html>
<head>
    <title>Branch List</title>
</head>
<body>
    <h1>Branches:</h1>
    <select>
        {% for branch in branches %}
            <option value="{{branch.id}}">{{branch.name}} - {{branch.location}}</option>
        {% endfor %}
    </select>
</body>
</html>

# ///////////////////////////////////
# 118 - populate multiple dropdowns
# //////////////////////////////////
# todo create model
class Country(model.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(Self):
        return self.name
    
# todo migration
# ! python manage.py makemigrations front
# ! python manage.py migrate front

# todo add some records
from front.models.country import Country
from front.models.state import State
from front.models.city import City

c1 = Country.objects.create(name="India")
c2 = Country.objects.create(name="USA")
c3 = Country.objects.create(name="Australia")

s1 = State.objects.create(name="Gujrat",country=c1)
s2 = State.objects.create(name="Maharastra",country=c1)
s3 = State.objects.create(name="Rajeshthan",country=c1)
s4 = State.objects.create(name="Albama",country=c2)
s5 = State.objects.create(name="Alaska",country=c2)
s6 = State.objects.create(name="Queensland",country=c3)
s7 = State.objects.create(name="Tasmania",country=c3)
s8 = State.objects.create(name="Victoria",country=c3)

City.objects.create(name="surat",state=s1)
City.objects.create(name="Ahemdabad",state=s1)
City.objects.create(name="Baroda",state=s1)
City.objects.create(name="Pune",state=s2)
City.objects.create(name="Mumbai",state=s2)
City.objects.create(name="Jaipur",state=s3)
City.objects.create(name="Udaipur",state=s3)
City.objects.create(name="Auburn",state=s4)
City.objects.create(name="Bessemer",state=s4)
City.objects.create(name="Birmingham",state=s4)
City.objects.create(name="Chickasaw",state=s4)
City.objects.create(name="Clanton",state=s4)
City.objects.create(name="Cordova",state=s5)
City.objects.create(name="Juneau",state=s5)
City.objects.create(name="Gympie",state=s6)
City.objects.create(name="Hervey Bay",state=s6)
City.objects.create(name="Ipswich",state=s6)
City.objects.create(name="Burnine",state=s7)
City.objects.create(name="Devonport",state=s7)
City.objects.create(name="Ararat",state=s8)
City.objects.create(name="Geelong",state=s8)
City.objects.create(name="Mildura",state=s8)

# todo create views
from .models import Country,State,City

def load_contries(request):
    countries = Country.objects.all()
    states = State.objects.filter(country=countries.first())
    cities = City.objects.filter(state=states.first())
    return render(request, 'country.html', {'contries':countries, 'states':states,'cities':cities})

def load_states(request):
    contry_id = request.GET.get('country_id')
    states = State.objects.filter(contry_id=contry_id)
    return render(request,'state_dropdown_list_options.html',{'states':states})


def load_cities(request):
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(state_id=state_id)
    return render(request,'city_dropdown_list_options.html', {'cities':cities})

# todo add urls patterns
    path('countries/',country.load_countries,name='load_countries'),
    path('states/',state.load_states,name='load_states'),
    path('cities/',city.load_cities,name='load_cities'),

# todo create country.html
<html>
<head>
    <title>Country,State,City Dropdown</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <h1>Select Country</h1>
    <select id="countrySelect">
        {% for country in countries %}
            <option value="{{country.id}}">{{country.name}}</option>
        {% endfor %}
    </select>

     <h1>Select State:</h1>
    <select id="stateSelect">
        {% for state in states %}
            <option value="{{state.id}}">{{state.name}}</option>
        {% endfor %}
    </select>

    <h1>Select City:</h1>
    <select id="citySelect">
        {% for city in cities %}
            <option value="{{city.id}}">{{city.name}}</option>
        {% endfor %}
    </select>

    <script>
        $(document).ready(function () {
            $("#countrySelect").change(function () {
                var countryId = $(this).val();
                $("#stateSelect").empty();
                $("#citySelect").empty();

                $.ajex({
                    url:"{% url 'front:load_states' %}",
                    data:{
                        'country_id':countryId
                    },
                    success:function (data){
                        $("#stateSelect").html(data);
                        var stateId = $("#stateSelect").val();
                        $.ajex({
                            url: "{% url 'front:load_cities' %}",
                            data:{
                                'state_id':stateId
                            },
                            success:function (data){
                                $("#citySelect").html(data);
                            }
                        });
                    }
                });
            });
            $("#stateSelect").chenge(function(){
                var stateId = $(this).val();
                $("#citySelect").empty();

                $.ajex({
                    url:"{% url 'front:load_cities' %}",
                    data:{
                        'state_id':stateId
                    }
                });
            });
        });
    </script>
</body>
</html>

# todo for state_dropdown_list_options.html
{% for state in states %}
    <option value="{{state.id}}">{{state.name}}</option>
{% endfor %}

# todo city_dropdown_list_options.html
{% for city in cities %}
    <option value="{{city.id}}">{{city.name}}</option>
{% endfor %}


# ///////////////////////////////////
# 119 - Master Details Data - part 1
#  120 - Master Detailse Data - part 2
# ///////////////////////////////////
Create Category Model with name and description fields
Create View for the Category model for category_list,category_update,category_delete
Create HTML template for Category with CURD opretion with bootstrap 5.3
    make templates as below
    - category_list.html -> to show all categories with update and delete button with model conformetion
    -category_form.html -> to insert or update category

add some 3 to 4 records into category
create Food model with name,price,image,description, Category and foreign_key with category model
create html template for food with CURD opretion with bootstrap 5.3
    make templates as below
    -food_list.html -> to show all foods with card vew and 4 cards view in one row with update and delete button with model
    -food_form.html -> to insert or update food to insert  or update category,must use html select 
    -food_detail.html -> to show each products details on detail page with image

Add some 8 to 10 records into food

# todo create category Model:
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
# todo migration
# ! python manage.py makemigrations front 
# ! python manage.py migrete front

# todo create forms for category:
# ?for forms.py
from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','description']

# create views for CURD opretions
from django.shortcuts import render,redirect,get_object_or_404
from .forms import CategoryForm

def category_list(request):
    categories = Category.objects.all()
    return render(request,'category_list.html',{'categories':categories})

def category_add(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('front:category_list')
        
    else:
        form = CategoryForm()
    return render(request, 'category_form.html',{'form':form})

def category_update(request,pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('front:category_list')
    else:
        form = CategoryForm(instance = category)
    return render(request,'category_form.html',{'form:form'})

def category_delete(request,pk):
    category = get_object_or_404(Category,pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('front:category_list')
    return render(request,'category_list.html',{'category':category})

# todo add url
path('category/',category.category_list,name='category_list'),
path('category/add/',category.category_add,name='category_add'),
path('category/update/<int:pk>/',category.category_update,name='category_update'),
path('category/delete/<int:pk>/',category.category_delete,name='category_delete'),

# todo create category_list.html
# <html>
# <head>
#     <title>Category List</title>
#      <link href="http://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet">

# </head>
# <body>
#       <h1>Category List</h1>
#         <ul>
#             {% for category in categories %}
#             <li>{{category.name}} - {{category.description}}
#                 <a href="{% url 'front:category_update' category.pk %}">update</a>
#                 <form method="post" action="{% url 'category_delete' category.pk %}" style="display:inline;">
#                 {% csrf_token %}
#                 <button type="submit" onlick="return confirm('Are you sure you want to delete this category?')"Delete</button>
#                 </form>
#             </li>
#         {% endfor %}
#     </ul>
#     <a href="{% url 'front:category_add' %}"Add Category</a>
# </body>
# </html>

# </body>
# </html>


# todo create category_form.html
<body>
#     <h1>{% if form.instance.pk %}Update Category{% else%}Add Category{%endif %}</h1>
#     <form method="post" >
#         {% csrf_token %}
#         {{form.as_p}}
#         <button type="submit">{% if form.instance.pk %}Update{% else %}Add{% endif %}</button>
#     </form>
#     <a href="{% url 'front:category_list' %}">Cancel</a>
# </body


#? ////////////////////////////////////
# todo create Food Model
class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_degits=10,decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
# todo migration
# ! python manage.py makemigrations front
# ! python manage.py migrate front

# todo  add code into forms.py

from .models import Food
class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name','price','description','category']

    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['category'].widget = forms.Select(choices=Category.objects.all().values_list('id','name'))

# todo create view
from django.shortcuts import render,redirect,get_list_or_404
from .models import Food
from .forms import FoodForm

def food_list(request):
    foods = Food.objects.all()
    return render(request,'food_list.html',{'foods':foods})
    
def food_add(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('front:food_list')
            
    else:
        form = FoodForm()
    return render(request, 'food_form.html',{'form':form})
    
def food_update(request,pk):
    food = get_objects_or_404(Food,pk=pk)
    if request.method == 'POST':
        form = FoodForm(request.POST,instance=food)
        if form.is_valid():
            form.save()
            return redirect('front:food_list')
    else:
        form = FoodForm(instance=food)
    return render(request,'food_form.html',{'form':form})

def food_delete(request,pk):
    food = get_object_or_404(Food,pk=pk)
    if request.method == 'POST':
        food.delete()
        return redirect('food_list')
    return render(request,'food_list.html',{'food':food})


# todo create food_list.html
<html>
# <head>
#     <title>Category List</title>
#      <link href="http://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet">

# </head>
# <body>
#   <h1>food List</h1>
    <div class="row">
        {% for food in foods %}
        <div class="col-md-3">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">{{food.name}}</h5>
                    <p class="card-text">Price:${{food.price}}</p>
                    <p class="card-text">Category:{{food.category.name}}</p>
                    <p class="card-text">{{food.description}}</p>
                    <a href="{% url 'front:food_update' food.pk %}" class="btn btn-primary">Update</a>
                    <form method="post" action="{% url 'front:food_delete' food.pk %}" style="display:inline;">
                        {% csrf_token %}
                        <button type="submit" class="btn btn-danger" onclik="return confirm("Are you sure you want to delete this food?)"Delete</button>
                    </form>
                </div>
            </div>
            {% endfor %}
        </div>
        <a href="{% url 'front:food_add' %}" class="btn btn-success">Add Food</a>
    </body>
</html>




# todo create food.form
<html>
# <head>
#     <title>{% if form.instance.pk %}Update Food{% endif %}</title>
#      <link href="http://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet">

# </head>
# <body>
#        
#         <h1>>{% if form.instance.pk %}Update Food{% endif %}</h1>
#            
#             <form method="post">
#                   {% csrf_token %}
                    {{form.as_p}}
#                   <button type="submit" class="btn btn-primary">{% if form.instance.pk %}Update{% else %}Add{% endif %}</button>
#               </form>
#               <a href="{% url 'front:food_list' %}" class="btn btn-secondary mt-3">Cencel</a>
#           

# </body>
# </html>

# todo add urls
path('food/',food.food_list,name='food_list'),
path('food/add/',food.food_add,name='food_add'),
path('food/update/<int:pk>/',food.food_update,name='food_update'),
path('food/delete/<int:pk>/',food.food_delete,name='food_delete'),


# /////////////////////////////
# 121 - Update only selected fields
# ///////////////////////////////
# ? when i want show name while create new records but
# ? when i update name fields should be there but not editable

# todo update form code
from django import forms
from .models import Food

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name','price','description','category']
        exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        instance = kwargs.get('instance')
        if instance:
            # disable the 'name' fields during update
            self.fields['name'].disabled = True
        else:
            # enable the 'name' fields during create
            self.fields['name'].disabled = False

        self.fields['category'].widget = forms.Select(choices=Category.objects.all().values_list('id','name'))


# /////////////////////////////
# 122 - pagination 
# //////////////////////////
# todo create model
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# todo migrations
# ! python manage.py makemigrations front
# ! python manage.py migrate front

# todo create views
from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage
from .models import Customer

def add_customers():
    customers = [
        {'name':'john Doe','email':'john@example.com','phone':'1234567890'}
        {'name':'jane smith','email':'jane@example.com','phone':'0987654321'}
        {'name':'Bob johnson','email':'bob@example.com','phone':'1234509876'}
        {'name':'Alice johnson','email':'alice@example.com','phone':'9012345678'}
        {'name':'michel smith','email':'michel@example.com','phone':'0123456789'}
        {'name':'Emily smith','email':'emily@example.com','phone':'3456789012'}
        {'name':'sophim devis','email':'sophim@example.com','phone':'5678901234'}
        {'name':'olivia clear','email':'olivia@example.com','phone':'4321098765'}
        {'name':'ethan hall','email':'ethan@example.com','phone':'8469327014'}
        {'name':'nohn lewis','email':'nohn@example.com','phone':'9099302436'}
        {'name':'isabela gariies','email':'isabela@example.com','phone':'9099095440'}
        {'name':'jayesh','email':'jayesh@example.com','phone':'7069404057'}
        {'name':'suresh','email':'suresh@example.com','phone':'3456712890'}
        {'name':'ramesh','email':'ramesh@example.com','phone':'8563523478'}
        {'name':'mohan mell','email':'mohan@example.com','phone':'9876554322'}
        {'name':'sany devel','email':'sany@example.com','phone':'3456712908'}
        {'name':'amitabh bachan','email':'amitabh@example.com','phone':'12334576846'}
        {'name':'chardh kapur','email':'chardh@example.com','phone':'1234567890'}
        {'name':'allu arjun','email':'allu@example.com','phone':'1234678903'}
        {'name':'mahesh babu','email':'mahesh@example.com','phone':'8765903214'}
        {'name':'magan kalu','email':'magan@example.com','phone':'59687364899'}
        {'name':'mohan tripathi','email':'mohan@example.com','phone':'59883784756'}
        {'name':'axsey rave','email':'axsey@example.com','phone':'33567899976'}
        {'name':'kalu kaliy ','email':'kalu@example.com','phone':'8448596958'}
        {'name':'tilu mehata','email':'tilu@example.com','phone':'4485896988'}
        {'name':'jetha gada','email':'jetha@example.com','phone':'498687774785'}
        {'name':'tapu jatha','email':'tapu@example.com','phone':'5987647654'}
        {'name':'sonu bhide','email':'sonu@example.com','phone':'49875674674'}
        {'name':'ramu rakhan','email':'ramu@example.com','phone':'44989874765'}
        {'name':'sita ram','email':'sita@example.com','phone':'55787576476'}
        {'name':'raju kamal','email':'raju@example.com','phone':'59875756465'}
        {'name':'mariya mohan','email':'mariya@example.com','phone':'4898736647'}
        {'name':'megha mule','email':'megha@example.com','phone':'5877576757'}
    ]

    for customer_data in customers:
        Customer.objects.create(**customer_data)

def show_customers(request):
    # function to show customer with pagination

    # check if customer records are added ,if not add some dummy records
    if not Customer.objects.exists():
        add_customers()

    # get the page number from the request,default to 1 if not present
    page_number = request.GET.get('page',1)

    # number of records to display per page
    records_per_page = 10

    # query all customer from the database
    all_customers = Customer.objects.all()

    # create a paginator objects
    paginator = Paginator(all_customers,records_per_page)

    try:
        # get the desired page from the paginator
        current_page = paginator.page(page_number)
    except EmptyPage:
        # if the request page number is out of ranges
        current_page = paginator.page(paginator.num_pages)

    return render(request,'customer_list.html',{'current_page':current_page})

# todo set url
path('customers/',customer.show_customers,name='show_customers')


# todo create customer_list.html
<html>
# <head>
#     <title>Category List</title>
#      <link href="http://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet">

# </head>
# <body>
    <div class="container mt-4">
    <h1 class="mb-3">Customer List</h1>

    <div class="list-group">
        {% for customer in current_page %}
            <a href="#" class="list-group-item list-group-item-action">
            <h5 class="mb-1">{{customer.name}}</h5>
            <p class="mb-1">Email:{{customer.email}}</p>    
             <p class="mb-1">Phone:{{customer.phone}}</p>
            </a>
        {% endfor %}
    </div>

    <nav aria-label="page navigation">
        <ul class="pagination mt-3">
            {% if current_page.has_previous %}
                <li class="page-item">
                    <a class="page-link" href="?page=1">&lanquo; first</a>
                </li>
                <li class="page-item">
                    <a class="page-link" href="?page={{current_page.previous_page_number}}">previous</a>
                </li>
            {% endif %}
            <li class="page-item disabled">
                <span class="page-link">
                    page {{current_page.number}} of {{current_page.paginator.num_pages}}
                </span>
            </li>

            {% if current_page.has_next %}
                <li class="page-item">
                    <a class="page-link" href="?page={{ current_page.next_page_number}}"next</a>
                </li>
                <li class="page-item">
                    <a class="page-link" href="?page={{current_page.paginator.num_pages}}"last &raquo;</a>
                </li>
            {% endif %}
        </ul>
    </nav>
</div>
 <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
   

</body>
</html>


# ///////////////////////////////////
# 123 - get radio and checkbox value from database
# ///////////////////////////////////
# todo create model
class Teacher(models.Model):
    GENDER_CHOICES = (
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),
    )

    name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
# todo makemigration
# ! python manage.py makemigrations front
# ! python manage.py migrate front

# todo create forms.py
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields =['name','salary','gender','is_active']
        widgets = {
            'gender':forms.RadioSelect(),
            'is_active':forms.CheckboxInput(),
        }

# todo create views
from django.shortcuts import render,get_object_or_404,redirect
from .models import Teacher
from .forms import TeacherForm

def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('front:teacher_list')
    else:
        form = TeacherForm
    return render(request,'add_teacher.html',{'form':form})
    
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request,'teachers.html',{'teachers':teachers})

def update_teacher(request,pk):
    teacher = get_object_or_404(Teacher,pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST,instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('front:teacher_list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request,'update_teacher.html',{'form':form, 'teacher':teacher})

def delete_teacher(request,pk):
    teacher = get_object_or_404(Teacher,pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('front:teacher_list')
    return render(request,'delete_teacher.html',{'teacher':teacher})

# todo add urls
from .views import teacher
path('teachers/add/',teacher.add_teacher,name='add_teacher'),
path('teachers/',teacher.teacher_list,name='teacher_list'),
path('teachers/update/<int:pk>/',teacher.update_teacher,name='update_teacher'),
path('teachers/delete/<int:pk>/',teacher.delete_teacher,name='delete_teacher'),

# todo create teacher.html
<html>
    <head>
        <title>Teacher management</title>
    </head>
<body>
    <h1>Teacher List</h1>
<table>
    <tr>
        <th>Name</th>
        <th>Salary</th>
        <th>Gender</th>
        <th>Is Active</th>
        <th>Actions</th>
    </tr>
    {% for teacher in teachers %}
    <tr>
        <td>{{teacher.name}}</td>
        <td>{{teacher.salary}}</td>
        <td>{{teacher.get_gender_display}}</td>
        <td>{{teacher.is_active}}</td>
        <td>
            <a href="{% url 'front:update_teacher' teacher.pk %}">update</a>
            <a href="{% url 'front:delete_teacher' teacher.pk %}">Delete</a>

        </td>
    </tr>
    {% endfor %}
</table>
<hr>
<a href="{% url 'front:add_teacher' %}">Add Teacher</a>
</body>
</html>

# todo create add_teacher.html
<html>
<head>
    <title>Teacher Management</title>
</head>
<body>
    <h1>Add Teacher</h1>
    <form method="post">
        {% csrf_token %}
        {{%form.as_p}}
        <button type="submit">Save</button>
    </form>
<hr>
<a href="{% url 'front:teacher_list' %}">back to Teacher</a>
</body>
</html>

# todo create update_teacher.html
<html>
<head>
    <title>Teacher Management</title>
</head>
<body>
    <h1>UpdateTeacher</h1>
    <form method="post">
        {% csrf_token %}
        {{%form.as_p}}
        <button type="submit">Save Changes</button>
    </form>
<hr>
<a href="{% url 'front:teacher_list' %}">Back to Teacher List</a>
</body>
</html>

# todo create delete_teacher.html
<html>
<head>
    <title>Teacher Management</title>
</head>
<body>
    <h1>Delete Teacher</h1>
    <p>Are you sure you want to delete "{{teacher.name}}"?</p>
    <form method="post">
        {% csrf_token %}
      
        <button type="submit">Confirm Delete</button>
    </form>
<hr>
<a href="{% url 'front:teacher_list' %}">Cancel</a>
</body>
</html>


# /////////////////////////////////////////
# 124 - create simple form
# ////////////////////////////////////////
# todo create model
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
# todo migration
# ! python manage.py makemigrations front 
# ! python manage.py migrate front

# todo create forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email']

# todo create views
from django.shortcuts import render,redirect
from .forms import ContactForm

def contact_add(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    
    else:
        form = ContactForm()

    return render(request, 'contact_form.html',{'form':form})

def success_view(request):
    return render(request,'success.html')

# todo create contact_form.html
<html>
<head>
    <title>Contact Form</title>
</head>
<body>
    <h1>Contact Form</h1>
    <form method='post'>
        {% csrf_token %}
        {{form.as_p}}
        <button type="submit">Submit</button>
    </form>
</body>
</html>

# todo html input control
<html>
<head>
    <title>Contact Form</title>
</head>
<body>
    <h1>Contact Form</h1>
    <form method='post'>
        {% csrf_token %}
        <label for="{{form.name_id_for_label}}">Name:</label>
        <input type="text" name="{{form.name.html_name}}" id="{{form.name.auto_id}}" value="{{form.name.value}}">
        <br>
        <label for="{{form.email_id_for_label}}">Email:</label>
        <input type="email" name="{{form.email.html_name}}" id="{{form.email.auto_id}}" value="{{form.email.value}}">
        <br>
        
        <button type="submit">Submit</button>
    </form>
</body>
</html>
# todo create success.html
<html>
<head>
    <title>Success Form</title>
</head>
<body>
    <h1>Form Submited Successfully!</h1>
    <p>Thank you for submited the form</p>
</body>
</html>

# todo create urls
path('contact/',views.contact_add,name='contact'),
path('success/',views.success_view,name='success'),

# /////////////////////////////////
# 125 - custom name of form control
# /////////////////////////////////
# todo update forms.py
widgets = {
    'name':forms.TextInput(attrs={'id':'texID','name':'texID'}),
    'email':forms.EmailInput(attrs={'id':'texEmail','name':'texEmail'}),
}

# //////////////////////////////
# 126- Aplay class atribute
# ///////////////////////////////
# todo update forms.py
widgets = {
            'name':forms.TextInput(attrs={'class':'form-control input-lg'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }

# todo contact_form.html
# add bootsrep link

# ///////////////////////////////
# 127- customizingform widgets
# ///////////////////////////////

# todo create model
class Friend(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name
    
# ! python manage.py makemigrations front
# ! python manage.py migrate front

# todo create form
from .models import Friend

from django import forms


class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name','age','email']
        widgets = {
            'name':forms.TextInput(attrs={'placeholder':'Enter your friend\'s name'}),
            'age':forms.NumberInput(attrs={'min':0}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter your friend\'s email'}),
        }

# todo create view
from .forms import FriendForm

def add_friend(request):
    if request.method == 'POST':
        form = FriendForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    
    else:
        form = FriendForm()

    return render(request, 'add_friend.html',{'form':form})

# todo create url
path('friend/',views.add_friend,name='add_friend'),

# todo create add_friend.html
<html>
<head>
    <title>Add Friend</title>
   
</head>
<body>
    <h1>Add a New Friend</h1>
    <form method='post'>
        {% csrf_token %}
        {{form.as_p}}
        <button type="submit">Add Friend</button>
    </form>
</body>
</html>

# /////////////////////////////////
# 128 - more form attributes
# ////////////////////////////////////
# todo create model
class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    birth_date = models.DateField()
    appoiment_time = models.TimeField()
    about_me = models.TextField()
    gender = models.CharField(max_length=1)
    interests = models.CharField(max_length=255)
    agree_terms = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pics/',null=True,blank=True)
    secret_code = models.CharField(max_length=10,default='ABC123')

    def __str__(self):
        return self.username
    
    gender_choices = [
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),
    ]

    interests_choices = [
        ('sports','Sports'),
        ('music','Music'),
        ('movie','Movie'), 
    ]

# todo create form
from .models import UserProfile

class userRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        widget = {
            'username':forms.TextInput(attrs={'placeholder':'Enter username'}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter email'}),
            'password':forms.PasswordInput(attrs={'placeholder':'Enter password'}),
            'birth_date':forms.DateInput(attrs={'type':'date'}),
            'appoiment_time':forms.TimeInput(attrs={'type':'time'}),
            'about_me':forms.Textarea(attrs={'placeholder':'tell us about yourself'}),
            'gender':forms.RadioSelect,
            'interests':forms.CheckboxSelectMultiple,
            'agree_terms':forms.CheckboxInput,
            'profile_picture':forms.FileInput(),
            'secret_code':forms.HiddenInput(attrs={'value':'ABC123'}),
        }
    gender = forms.ChoiceField(choices=UserProfile.gender_choices,widget=forms.RadioSelect)
    interests = forms.MultipleChoiceField(choices=UserProfile.interests_choices,widget=forms.CheckboxSelectMultiple)

# todo create view
from .forms import UserRegistrationForm
from .models import UserProfile
from django.contrib.auth.hashers import make_password

def user_registration_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            hased_password = make_password(form.cleaned_data['password'])
            UserProfile.objects.create(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                 password = hased_password,
                birth_date=form.cleaned_data['birth_date'],
                appoiment_time=form.cleaned_data['appoiment_time'],
                about_me=form.cleaned_data['about_me'],
                gender=form.cleaned_data['gender'],
                interests=','.join(form.cleaned_data['interests']),
                agree_terms=form.cleaned_data['agree_terms'],
                profile_picture=request.FILES.get('profile_picture'),
                secret_code=form.cleaned_data['secreet_code'],
            )
            return redirect('success')
    else:
        form=UserRegistrationForm()
    
    return render(request,'user_registration.html',{'form':form})
    
# todo create url
path('register/',views.user_registration_view,name='user_registration'),

# todo create 'user_registration.html' templates
<html>
<head>
    <title>User Registration Form</title>
   
</head>
<body>
    <h1>User Registation</h1>
    <form method='post' enctype="multipart/form-data">
        {% csrf_token %}
        {{form.as_p}}
        <input type="submit" value="Register">
    </form>
</body>
</html>

# ///////////////////////////////////////
# 129 - different form fields
# //////////////////////////////////////

# todo create model
class XUserProfile(models.Model):
    GENDER_CHOISE = [
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1,choices=GENDER_CHOISE,default='M')
    has_mca_degree = models.BooleanField('MCA',default=False)
    has_mba_degree = models.BooleanField('MBA',default=False)
    has_mcm_degree = models.BooleanField('MCM',default=False)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField()
    birth_date = models.DateField()

# todo create forms.py
from django import forms
from .models import XUserProfile

class XUserProfileForm(forms.ModelForm):
    class Meta:
        model = XUserProfile
        fields = ['first_name','last_name','gender','has_mca_degree','has_mba_degree','has_mcm_degree','username','password','country','description','birth_date']

        widgets = {
            'password':forms.PasswordInput(),
            'gender':forms.RadioSelect(),
            'birth_date':forms.DateInput(attrs={'type':'date'}),
        }

# todo create view
from django.shortcuts import render
from .forms import XUserProfileForm

def profile_form_view(request):
    if request.method == 'POST':
        form = XUserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    
    else:
        form = XUserProfileForm()

    return render(request,'profile_form.html',{'form':form})

# todo add url
path('profile/',views.profile_form_view,name='profile_form'),

# todo create profile_form.html
<html>
<head>
    <title>User Profile Form</title>
   
</head>
<body>
    <h1>User Profile</h1>
    <form method='post' enctype="multipart/form-data">
        {% csrf_token %}
        {{form.as_p}}
       <button type="submit">Submit</button>
    </form>
</body>
</html>

# ////////////////////////////////
# 130 - form fields - booleanfield,charfield
# ///////////////////////////////////////
# todo create model
class ExampleModel(models.Model):
    boolean_field = models.BooleanField(default=False)
    char_field = models.CharField(max_length=100)
    choise_field = models.CharField(max_length=10,choices=[('01','option 1'),('02','option 2'),('03','option 3')])
    typed_choice_field = models.CharField(max_length=10,choices=[('t1','type 1'),('t2','type 2'),('t3','type 3')])

# todo create form
from django import forms
from .models import ExampleModel

class ExampleForm(forms.ModelForm):
    class Meta:
        model = ExampleModel
        fields = ['boolean_field','char_field','typed_choice_field']

# todo create view
from .forms import ExampleForm

def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ExampleForm()
    
    return render(request,'example_form.html',{'form':form})

# todo Add url
path('example/',views.example_form_view,name='example_form')

# todo create example_form.html
<html>
<head>
    <title>Example Form</title>
   
</head>
<body>
    <h1>Example Form</h1>
    <form method='post' >
        {% csrf_token %}
        {{form.as_p}}
       <button type="submit">Submit</button>
    </form>
</body>
</html>


# //////////////////////////////////////////
# 131 - Form Fields - DateField, DateTimeField
# /////////////////////////////////////////

# todo create model
class Event(models.Model):
    name = models.CharField(max_length=100)
    event_date = models.DateField()
    event_datetime = models.DateTimeField()

# todo migrations
# ! pythomn manage.py makemigrations front
# ! python manage.py migrate front 

# todo create form
from .models import Event

class EventForm(forms.ModelsForm):
    class Meta:
        model = Event
        fields = ['name','event_date','event_datetime']

    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)

        self.fields['event_date'].widget = forms.DateInput(attrs={'type':'date'})
        self.fields['event_datetime'].widget = forms.DateInput(attrs={'type':'datetime-local'})

# todo create view
from .forms import EventForm

def event_form_view(request):
    if request_form_view(request):
        if request.method =='POST':
            form = EventForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('success')
        else:
            form = EventForm()

        return render(request,'event_form.html',{'form':form})
    
# todo Add urls
path('event/',views.event_form_view,name='event_form')

# todo create event_form.html
<html>
<head>
    <title>Event Form</title>
   
</head>
<body>
    <h1>Event Form</h1>
    <form method='post' >
        {% csrf_token %}
        {{form.as_p}}
       <button type="submit">Submit</button>
    </form>
</body>
</html>

# ///////////////////////////////////////
# 132 - Form Fields:DecimalFields,DurationField,EmailField
# ////////////////////////////////////////////
# todo create model
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    delivery_time = models.DurationField()
    email = models.EmailField()

# todo migrate
# ! python manage.py makemifrations front
# ! python manage.py migrate front

# todo create form
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','delivery_time','email']

        widgets = {
            'price' :forms.NumberInput(attrs={'step':'1.0'}),
            'delivery_time':forms.TextInput(attrs={'placeholder':'HH:MM:SS'}),
        }

# todo create view
from .forms import ProductForm

def product_form_view(request):
   
    if request.method =='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ProductForm()

    return render(request,'product_form.html',{'form':form})
    
# todo add urls
path('product/',views.product_form_view,name='product_form'),

# todo create product_form.html
<html>
<head>
    <title>Product Form</title>
   
</head>
<body>
    <h1>ProductForm</h1>
    <form method='post' >
        {% csrf_token %}
        {{form.as_p}}
       <button type="submit">Submit</button>
    </form>
</body>
</html>

# ////////////////////////////////////
# 133 - Form Field:FileField
# /////////////////////////////////
# todo create model
class Document(models.Model):
    title = models.CharField(max_length=100)
    file_upload = models.FileField(upload_to='documents/')

# todo migtions
# ! python manage.py makemigrations front
# ! python manage.py migrate.py front

# todo create form
from .models import Document
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title','file_upload']

# todo create view
from .forms import DocumentForm

def upload_document(request):
   
    if request.method =='POST':
        form = DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = DocumentForm()

    return render(request,'upload_document.html',{'form':form})

# todo add urls
path('document/',views.upload_document,name='upload_document'),

# todo create upload_document.html
<html>
<head>
    <title>Upload Document</title>
   
</head>
<body>
    <h1>Upload Document</h1>
    <form method='post' enctype="multipart/form-data">
        {% csrf_token %}
        {{form.as_p}}
       <button type="submit">Submit</button>
    </form>
</body>
</html>

# todo add project setting
MEDIA_ROOT = os.path.join(BASE_DIR,'data/')
MEDIA_URL = '/media/'

# //////////////////////////////////
# 134 - Form Fields - FilePathField
# /////////////////////////////////

# todo ceate model
# ? umlike filefield,filepathfield does not upload or save any files to the server file system
# ?it only store the chosen file path as a string in the database
# ? "recursive" attribute can be set to set to true to serch for files in subdirectories as well

class Song(models.Model):
    title = models.CharField(max_length=100)
    audio_file = models.FilePathField(path='data/audio/',recursive=True)

# ! python manage.py makemigrations front
# ! python manage.py migrate front

# todo create form
from .models import Song
class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title','audio_file']

# todo views

from .forms import SongForm

def upload_song(request):
   
    if request.method =='POST':
        form = SongForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = SongForm()

    return render(request,'upload_song.html',{'form':form})

# todo add url
path('song/',views.upload_song,name='upload_song'),

# todo create upload_song.html
<html>
<head>
    <title>Upload Song</title>
   
</head>
<body>
    <h1>Upload Song</h1>
    <form method='post' enctype="multipart/form-data">
        {% csrf_token %}
        {{form.as_p}}
       <button type="submit">Upload</button>
    </form>
</body>
</html>


# /////////////////////////////
# 135 - Form Filds -FloatFilds,IntegerFilds,ImageFilds
# //////////////////////////////////
# todo create model
class xProduct(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quentity = models.IntegerField()
    image = models.ImageField(upload_to='product_images/',blank=True,null=True)

# todo migrtaion
# ! python manage.py makemigrations front
# ! python manage.py migrate front

# todo create form
from .models import xProduct

class xProductForm(forms.ModelForm):
    class Meta:
        model = xProduct
        fields = ['name','price','quentity','image']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise forms.ValidationError("price  must be a positive value")
        return price
    
    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity is not None and quantity < 0:
            raise forms.ValidationError("Quantity can not be negative")
        return quantity
    
# todo create view
from .forms import xProductForm

def add_product(request):
   
    if request.method =='POST':
        form = xProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = xProductForm()

    return render(request,'xproduct_form.html',{'form':form})

# todo add urls
path('xproduct/',views.add_product,name='add_product'),

# todo create xproduct_form.html
<html>
<head>
    <title>Add Product</title>
   
</head>
<body>
    <h1>Add Product</h1>
    <form method='post' enctype="multipart/form-data">
        {% csrf_token %}
        {{form.as_p}}
       <button type="submit">Add Product</button>
    </form>
</body>
</html>

# //////////////////////////////////
# 136 - Form Fields - GenericIPAddressFields
# /////////////////////////////////////////
# todo create model
class Device(models.Model):
    DEVICE_TYPES = [
        ('Router','Router'),
        ('Switch','Switch'),
        ('Firewall','Firewall'),
        ('Server','Server'),
        ('Other','Other'),
    ]

    DEVICE_VENDORS = [
        ('Cisco','Cisco'),
        ('Juniper','Juniper'),
        ('HP','HP'),
        ('Dell','Dell'),
        ('Other','Other'),
    ]

    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField(protocol='IPv4',null=True,blank=True)
    mac_address = models.CharField(max_length=17,null=True,blank=True)
    device_type = models.CharField(max_length=20,choices=DEVICE_TYPES,default='Other')
    vendor = models.CharField(max_length=20,choices=DEVICE_VENDORS,default='Other')

    def __str__(self):
        return self.name
    
# todo create form
from .models import Device
class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name','ip_address','mac_address','device_type','vendor']

    ip_address = forms.GenericIPAddressField(protocol='IPv4',required=False)

# todo create views
from .forms import DeviceForm

def create_device(request):
   
    if request.method =='POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = DeviceForm()

    return render(request,'device_form.html',{'form':form})

# todo add urls
path('device/',views.create_device,name='create_device'),

# todo create device_form.html
<html>
<head>
    <title>Create Device</title>
   
</head>
<body>
    <h1>Create Device</h1>
    <form method='post' >
        {% csrf_token %}
        {{form.as_p}}
       <button type="submit">Create</button>
    </form>
</body>
</html>

# //////////////////////////////
# 137 - Form Fields: MultipleChoiceField
# ///////////////////////////////////
# todo create model
class Survey(models.Model):
    GENDER_CHOICES = [
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    questions = models.ManyToManyField('Question',blank=True)

    def __str__(self):
        return self.name
    
class Question(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text 
    
# todo add some records
from front.models import Question

Question.objects.create(text='what is the capital of France?')
Question.objects.create(text='which planet is closest to the sun?')
Question.objects.create(text='who painted theMona Lisa?')
Question.objects.create(text='what is the tallest mountain in the world?')

# todo create form
from .models import Survey,Question
class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['name','age','gender','questions']

    age = forms.IntegerField(min_value=1)
    gender = forms.ChoiceField(choices=Survey.GENDER_CHOICES,widget=forms.RadioSelect())
    questions = forms.ModelMultipleChoiceField(queryset=Question.objects.all(), widget=forms.CheckboxSelectMultiple())

# todo create view
from .forms import SurveyForm

def create_survey(request):
   
    if request.method =='POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = SurveyForm()

    return render(request,'survey_form.html',{'form':form})

# todo add urls
path('survey/',views.create_survey,name='create_survey'),

# todo survey_form.html
<html>
<head>
    <title>Survey Form</title>
   
</head>
<body>
    <h1>Survey Form</h1>
    <form method='post' >
        {% csrf_token %}
        {{form.as_p}}
       <button type="submit">Submit</button>
    </form>
</body>
</html>

# ////////////////////////////////
# 138 - Form Fields - BooleanField,RegexField,SlugField
# ///////////////////////////////////////
# todo create model
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_published = models.BooleanField(default=None)
    slug = models.SlugField(max_length=100,unique=True)
    category = models.CharField(max_length=50,blank=True)
    tags = models.CharField(max_length=200,blank=True,null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# todo migration
# ! python manage.py makemigrations front
# ! python manage.py migrate front

# todo create form
from django.core.validators import RegexValidator
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','content','is_published','slug','category','tags']

    tags = forms.RegexField(
        label = 'Tags',
        regex=r'^[a-zA-Z, ]+$',
        help_text = 'Comma-Separated tags (letters only)',
        required = False,
        error_messages ={
            'invalid':'please enter valid tags (letters only).'
        }
    )

# todo create view
from .forms import BlogPostForm

def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = BlogPostForm()

    return render(request,'post_create.html',{'form':form})

# todo Add urls
path('blog/',views.create_blog_post,name='blog_form'),

# todo create post_create.html
<html>
<head>
    <title>Create Blog post</title>
   
</head>
<body>
    <h1>Create Blog Post</h1>
    <form method='post' >
        {% csrf_token %}
        {{form.as_p}}
       <button type="submit">Submit</button>
    </form>
</body>
</html>

# ////////////////////////////////
# 139 - Form Fields - TimeField,URLField,UUIDField
# /////////////////////////////////////////
import uuid

class xExampleModel(models.Model):
    time_field = models.TimeField(verbose_name="Custom Time Field",auto_now_add=True)
    url_field = models.URLField(verbose_name="Custom URL Field",max_length=200,blank=True,null=True)
    uuid_field = models.UUIDField(verbose_name="Custom UUID Field",default=uuid.uuid4,editable=False)

# todo migration
# ! python manage.py makemigrations front
# ! python manage.py migrate front

# todo create form
from .models import xExampleModel

class xExampleModelForm(forms.ModelForm):
    class Meta:
        model = xExampleModel

        exclude = ['time_field','uuid_field']
        labels = {
            'url_field':'Custom URL Label',
        }
        help_texts = {
            'url_field':'Enter a valid URL',
        }
        widgets = {
            'time_field':forms.TimeInput(format='%H:%M:%S'),
        }

# todo create view
from .forms import xExampleModelForm
from django.utils import timezone

def xexample_view(request):
    if request.method == 'POST':
        form = xExampleModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.time_field = timezone.now().strftime('%H:%M:%S')
            instance.save()
            return redirect('success')
    else:
        form = xExampleModelForm()

    return render(request,'xtemplate.html',{'form':form})

# todo add urls
path('xexample/',views.xexample_view,name='example')

# todo create xtemplate.html
<html>
<head>
    <title>Example Form</title>
   
</head>
<body>
    <h1>Example Form</h1>
    <form method='post' >
        {% csrf_token %}
        {{form.as_p}}
       <button type="submit">Submit</button>
    </form>
</body>
</html>

# ///////////////////////////////
# 140 - SplitDateTimeField
# ////////////////////////////////
# todo create model
class xEvent(models.Model):
    name = models.CharField(max_length=100)
    start_date_time = models.DateTimeField()

# todo migration
# ! python manage.py makemigrations front
# ! python manage.py migrate front

# todo create form
from .models import xEvent
import datetime

class xEventForm(forms.ModelForm):
    class Meta:
        model = xEvent
        fields = ['name','start_date_time']
        widgets = {
            'start_date_time':forms.DateTimeInput(attrs={'type':'datetime-local'}),
        }

# or
class xEventForm(forms.ModelForm):
    start_date_time = forms.SplitDateTimeField(
        input_date_formats=['%Y-%m-%d'],
        input_time_formats=['%H:%M','%I:%M %p'],
    )
    class Meta:
        model = xEvent
        fields = ['name','start_date_time']
        widgets = {
            'start_date_time':forms.SplitDateTimeWidget(),
        }

# or
class xEventForm(forms.ModelForm):
    start_date_time = forms.SplitDateTimeField(
        widget=forms.SplitDateTimeWidget(
        date_attrs={'placeholder':'YYYY-MM-DD'},
        time_attrs={'placeholder':'HH:MM'},
        ),
    )

    class Meta:
        model=xEvent
        fields = ['name','start_date_time']
        labels = {
            'name':'Event Name',
        }
        help_texts = {
            'start_date_time':'Enter the date and time of the event',
        }

    # to_python makes sure that the data entered belongs to the correct datatype and raises a validation error otherwise
    def to_python(self,value):
        if not value:
            return None
        date_str,time_str = value
        if date_str and time_str:
            return datetime.datetime.combine(date_str,time_str)
        return None

# todo create view
from .forms import xEventForm

def xcreate_event(request):
    if request.method == 'POST':
        form = xEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = xEventForm()

    return render(request,'create_event.html',{'form':form})

# todo add url
path('xevent/',views.xcreate_event,name='student_profile_form'),

# todo create template create_event.html
<html>
<head>
    <title>Create Event</title>
   
</head>
<body>
    <h1>Create Event</h1>
    <form method='post' >
        {% csrf_token %}
        {{form.as_p}}
       <input type="submit" value="Save">
    </form>
</body>
</html>

# ///////////////////////////
# 141 -  Form Fields - ModelMultipleChoiseFields
# ///////////////////////////
class Worker(models.Model):
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Training(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    workers = models.ManyToManyField(Worker,related_name='trainings',blank=True)

    def __str__(Self):
        return self.title 
    
# todo migrations
# ! python manage.py makemigrations front
# ! python manage.py migrate front

# Todo add data
# ! python manage.py shell
from front.models import Worker,Training

Worker(name='John Doe',job_title='Software Engineer').save()
Worker(name='jane Smith',job_title='Data Scientist').save()
Worker(name='Michael johnson',job_title='Project manager').save()

Training(title='Python Programming',description='Learn Python basic and advanced concepts.').save()
Training(title='Data Analysis',description='Master data analysis techniques with python.').save()
Training(title='Project Management',description='Learn project management methodologies').save()

# todo create form
from .models import Worker,Training

class TrainingForm(forms.Form):
    worker = forms.ModelChoiceField(
        queryset=Worker.objects.all(),
        widget =forms.Select,
        required = True,
        help_text ="Select a worker"
    )
    trainings = forms.ModelMultipleChoiceField(
        queryset=Training.objects.all(),
        widget =forms.CheckboxSelectMultiple,
        required = True,
        help_text ="Select one or more trainings"

    )

# todo create view
from .forms import TrainingForm
from .models import Worker

def training_selection_view(request):
    if request.method == 'POST':
        form = TrainingForm(request.POST)
        if form.is_valid():
            selected_trainings = form.cleaned_data['trainings']
            selected_worker = form.cleaned_data['worker']
            selected_worker.trainings.set(selected_trainings)
            return redirect('success')
        
    else:
        form =  TrainingForm()

    return render(request,'training_selection.html',{'form':form})

# todo add url
path('training/',views.training_selection_view,name='training_selection'),

# todo create training_selection.html
<html>
<head>
    <title>Training Selection</title>
   
</head>
<body>
    <h1>Choise Your Trainings</h1>
    <form method='post' >
        {% csrf_token %}
        {{form.as_p}}
       <input type="submit" value="Save">
    </form>
</body>
</html>

# ///////////////////////////
# 142 - Form Fields - ModelChoiceFields
# ///////////////////////////
# todo create Model
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
# todo migrations
# ! python manage.py makemigrations front
# ! python manage.py migrate front

# todo add data
# ! python manage.py shell
from  front.models import Author

Author.objects.create(name='J.K.Rowling')
Author.objects.create(name='George R.R Martiin')
Author.objects.create(name='Stephen King ')


# todo create form
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author']
        widgets = {
            'author':forms.Select(attrs={'class':'custom-select'})
        }

# todo create view
from .forms import BookForm

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    
    else:
        form=BookForm()

    return render(request,'add_book.html',{'form':form})

# todo add urls
path('book/',views.add_book,name='add_book'),

# todo create add_book.html
<html>
<head>
    <title>Add Book</title>
   
</head>
<body>
    <h1>Add Book</h1>
    <form method='post' >
        {% csrf_token %}
        {{form.as_p}}
       <button type="submit">Save</button> 
    </form>
</body>
</html>

# ============================
# 143 - Form Validation
# ===========================

# todo create Model
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    feedback_message = models.TextField()

    def __str__(self):
        return self.name
    
# todo create form
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name','feedback_message']

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name.strip())<3:
            raise forms.ValidationError("Name must be at lest 3 cherecter long ")
        return name
    
    def clean_feedback_message(self):
        feedback_message = self.cleaned_data['feedback_message']
        if len(feedback_message.strip())<10:
            raise forms.ValidationError('Feedback messege must be 10 cherecter long ')
        return feedback_message
    
# create view
from .forms import FeedbackForm

def feedback_form_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    
    else:
        form=FeedbackForm()

    return render(request,'feedback_form.html',{'form':form})

# todo add urls
path('feedback/',views.feedback_form_view, name='feedback'),

# todo create feedback_form.html
<html>
<head>
    <title>Feedback Form</title>
   
</head>
<body>
    <h1>Feedback Form</h1>
    <form method='post' >
        {% csrf_token %}
        {{form.as_p}}
       <button type="submit">Save</button> 
        {% if form.errors %}
            <p style="color:red">{{form.errors}}</p>
        {% endif %}
    </form>
</body>
</html>

# or
<html>
<head>
    <title>Feedback Form</title>
   
</head>
<body>
    <h1>Feedback Form</h1>
    <form method='post' >
        {% csrf_token %}
        <div>
            {{form.name.label_tag}}: {{form.name}}
            {% if form.name.errors %}
                <div style="color:red;">{{form.name.errors}}</div>
            {% endif %}
        </div>
        <div>
            {{form.feedback_message.label_tag}} : {{form.feedback_message}}
            {% if form.feedback_message.errors %}
                <div style="color:red;">{{form.feedback_message.errors}}</div>
            {% endif %}
        </div>
        <button type="submit">Submit</button>
    </form>
</body>
</html>

# //////////////////////////////
# 144 - Working with Formets
# ///////////////////////////
# todo create Model
class Magazine(models.Model):
    title = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    publication_year  = models.IntegerField()

    def __str__(self):
        return self.title
    
# Todo migrations
# ! python manage.py makemigrations front
# ! python manage.py migrate front

# todo create form
class MagazineForm(forms.ModelForm):
    class Meta:
        model = Magazine 
        fields = ['title','publisher','publication_year']

MagazineFormSet = forms.formset_factory(MagazineForm,extra=1,can_delete=True)

# todo create view
from .forms import MagazineForm,MagazineFormSet
from django.forms import formset_factory

def magazine_list(request):
    MagazineFormSet = formset_factory(MagazineForm,extra=3,can_delete=True)

    if request.method == 'POST':
        formset = MagazineFormSet(request.POST,prefix='magazines')

        if formset.is_valid():
            for form in formset:
                form.save()
            return redirect('success')
        
    else:
        formset = MagazineFormSet(prefix='magazines')

    return render(request,'magazine_list.html',{'formset':formset})

# todo add urls
path('magazines/',views.magazine_list, name='magazine_list') 

# todo create magazine_list.html
<html>
<head>
    <title>Magazine List</title>
   
</head>
<body>
    <h1>Magazine List</h1>
    <form method='post' >
        {% csrf_token %}
        {{ formset.management_form}}
        <table>
        {% for form in formsaet %}
            {{ from.as_div}}
            <hr>
        {% endfor %}
        </table>

       
       <button type="submit">Save</button> 
    </form>
</body>
</html>

# ///////////////////////////
# 145 - Formsets with Dropdown
# ///////////////////////////

# todo create model
class Area(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Property(models.Model):
    area = models.ForeignKey(Area,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
# todo migrations
# ! python manage.py makemigrations front
# ! python manage.py migrate front

# todo Add Records
# ! python manage.py shell
from front.models import Area

Area(name='City Center').save()
Area(name='Suburbia').save()
Area(name='Riverside').save()

# todo create form
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['area','name','description']
        widgets = {
            'area':forms.Select(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
        }

# todo create view
from .forms import PropertyForm
from django.forms import modelformset_factory
from .models import Property

def property_formset_view(request):
    PropertyFormSet = modelformset_factory(Property,form=PropertyForm,extra=3)

    if request.method == 'POST':
        # queryset=Property.objects.none() create creates an empty queryset of the Property model
        # means when formset is initialized,it won't contain any pre-existing instance of the property model
        formset = PropertyFormSet(request.POST,queryset=Property.objects.none())
        if formset.is_valid():
            formset.save()
            return redirect('success')
        
    else:
        formset = PropertyFormSet(queryset=Property.objects.none())

    return render(request,'property_formset.html',{'formset':formset})

# todo add urls
path('properties/',views.property_formset_view,name='property_formset'),

# todo create property_formset.html
<html>
<head>
    <title>Property Formset</title>
</head>
<body>
    <h1>Property Formset</h1>
    <form method='post' >
        {% csrf_token %}
        {{ formset.management_form}}
        
        {% for form in formset %}
            <h2>Property {{ forloop.counter }}</h2>
            <div>
                {{form.area.label_tag }} {{ form.area }}
            </div>
            <div>
                {{form.name.label_tag }} {{ form.name }}
            </div>
            <div>
                {{form.description.label_tag }} {{ form.description }}
            </div>
            <hr>
        {% endfor %}
       <button type="submit">Save</button> 
    </form>
</body>
</html>

# ///////////////////////////
# 146 -Add Formsets Dynamically
# ///////////////////////////
# todo create model
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# ! python manage.py makemigrations front
# ! python manage.py migrate front

# tode create form
from .models import Department

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']

# todo create view
from .forms import DepartmentForm
from django.forms import formset_factory

def manage_departments(request):
    DepartmentFormSet = formset_factory(DepartmentForm,extra=1)

    if request.method == 'POST':
        formset = DepartmentFormSet(request.POST,prefix='departments')

        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    form.save()
            return redirect('success')
    else:
        formset = DepartmentFormSet(prefix='departments')
    
    return render(request,'manage_departments.html',{'formset':formset})

# todo add url
path('departments/',views.manage_departments,name='manage_departments'),

# todo add manage_departments.html
<html>
<head>
    <title>Manage Department</title>
   
</head>
<body>
    <h1>Manage Department</h1>
    <form method='post' >
        {% csrf_token %}
        {{ formset.management_form }}
        <table>
            {%  for form in formset %}
                {{ form.non_field_errors }}
                {% for field in form.visible_fields %}
                    <tr>
                        <th>{{ field.label_tag }}</th>
                        <td>{{field}}</td>
                    </tr>
                {% endfor %}
            {% endfor %}
        </table>
        <button type="submit">Save</button>
       
    </form>
    <button id="add-form">Add Department</button>

    <script>
        document.getElementById('add-form').addEventListener('click', function () {
            // "id_departments-TOTAL_FORMS" Retrieves the current number of form instances 
            var formIdx = parseInt(document.getElementById('id_departments-TOTAL_FORMS').value);
            var template = document.querySelector('#empty-form').innerHTML.replace(/__prefix__/g, formIdx);
            
            // Inserts the modified template content at the end of the <table> element, menas adding a new row.
            document.querySelector('table').insertAdjacentHTML('beforeend', template);

            // Updates the value of the hidden input field id_departments-TOTAL_FORMS 
            // ensuring that Django is aware of the new total number of forms
            document.getElementById('id_departments-TOTAL_FORMS').value = formIdx + 1;
        });
    </script>

    <script type="empty/form-template" id="empty-form">
        <tr>
            <th><label for="id_departments-__prefix__-name">Name:</label></th>
            <td><input type="text" name="departments-__prefix__-name" id="id_departments-__prefix__-name"></td>
        </tr>        
    </script> 
</body>
</html>


# ===============================
# ==============================
# ==========================
# Without Model
# ==========================

# TODO Setting required

INSTALLED_APPS = [
    ...
    'django.contrib.sessions',
    ...
]

MIDDLEWARE = [
    ...
    'django.contrib.sessions.middleware.SessionMiddleware',
    ...
]

SESSION_ENGINE = 'django.contrib.sessions.backends.db'


# TODO Run migrations to create the necessary database tables:
python manage.py makemigrations 
python manage.py migrate 

# TODO Create View

from django.shortcuts import render, redirect

def input_form(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        birthdate = request.POST.get('birthdate')

        # Store data in session
        request.session['first_name'] = first_name
        request.session['last_name'] = last_name
        request.session['age'] = age
        request.session['birthdate'] = birthdate
        
        return redirect('display_data')
    return render(request, 'input_form.html')

def display_data(request):
    first_name = request.session.get('first_name')
    last_name = request.session.get('last_name')
    age = request.session.get('age')
    birthdate = request.session.get('birthdate')

    context = {
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'birthdate': birthdate
    }
    return render(request, 'display_data.html', context)


# TODO Create template "input_form.html"
<!DOCTYPE html>
<html>
<head>
    <title>Input Form</title>
</head>
<body>

<h2>Enter Your Details</h2>

<form method="post">
    {% csrf_token %}
    <label>First Name:</label>
    <input type="text" name="first_name"><br>
    
    <label>Last Name:</label>
    <input type="text" name="last_name"><br>
    
    <label>Age:</label>
    <input type="number" name="age"><br>
    
    <label>Birthdate:</label>
    <input type="date" name="birthdate"><br>

    <input type="submit" value="Store in Session">
</form>

</body>
</html>


# TODO Create template "display_data.html"

<!DOCTYPE html>
<html>
<head>
    <title>Display Data</title>
</head>
<body>

<h2>Your Details:</h2>
<p>First Name: {{ first_name }}</p>
<p>Last Name: {{ last_name }}</p>
<p>Age: {{ age }}</p>
<p>Birthdate: {{ birthdate }}</p>

</body>
</html>


# TODO App's URL setting
path('input/', views.input_form, name='input_form'),
path('display/', views.display_data, name='display_data'),

# Run server
python manage.py runserver

# ///////////////////////////////
# models.py

from django.db import models

class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_date = models.DateField()
    photo = models.ImageField(upload_to='employees/')
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField()
    zipcode = models.CharField(max_length=10)
    date_of_joining = models.DateField()
    description = models.TextField()


# forms.py

from django import forms
from .models import Employee

class EmployeeForm1(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'gender', 'birth_date']

class EmployeeForm2(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['photo', 'country', 'state', 'city']

class EmployeeForm3(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['address', 'zipcode', 'date_of_joining', 'description']


# views.py

from django.shortcuts import render, redirect
from formtools.wizard.views import SessionWizardView
from .forms import EmployeeForm1, EmployeeForm2, EmployeeForm3

class EmployeeWizard(SessionWizardView):
    template_name = "employee_registration.html"
    form_list = [EmployeeForm1, EmployeeForm2, EmployeeForm3]

    def done(self, form_list, **kwargs):
        employee = Employee()
        for form in form_list:
            for field, value in form.cleaned_data.items():
                setattr(employee, field, value)
        employee.save()
        return redirect('some_success_url')


# employee_registration.html

<!DOCTYPE html>
<html>
<head>
    <title>Display Data</title>
</head>
<body>

    <form method="post">
        {% csrf_token %}
        <table>
        {{ wizard.management_form }}
        {% if wizard.form.forms %}
            {{ wizard.form.management_form }}
            {% for form in wizard.form.forms %}
                {{ form.as_table}}
            {% endfor %}
        {% else %}
            {{ wizard.form }}
        {% endif %}
        </table>
        <input type="submit" value="Next" />
    </form>

</body>
</html>


# URL

path('employee/register/', EmployeeWizard.as_view(), name='employee_registration'),


# //////////////////////////////
# API Project
# /////////////////////////////

# TODO Create Project for API

python -m venv myenv
myenv\Scripts\activate
pip install django   
python -m pip install --upgrade pip
django-admin startproject ECommerce .
python manage.py startapp books
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
admin
admin@gmail.com
password
password
y
pip install djangorestframework
python manage.py runserver


# TODO Install Apps in setting.py

'rest_framework',
'books',

# TODO Create Model

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.title
    
# TODO Create serializers.py in apps directory

from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

# TODO Create view

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

@api_view(['GET', 'POST'])
def BookListCreateView(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# TODO add urls into app's urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListCreateView, name='book-list-create'),
]

# TODO add urls into project's urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),  # Add this line
]

# TODO Test api in command mode

curl -X GET http://127.0.0.1:8000/api/books/

curl -X POST -d "title=Great india&author=Sardar patel&published_date=2023-01-01" http://127.0.0.1:8000/api/books/


# TODO Test api in postman

# To GET a list of books
set the method to GET the URL to http://127.0.0.1:8000/api/books/ 
press "Send".


# To POST (create) a new book, 
set the method to POST, the URL to http://127.0.0.1:8000/api/books/, 
go to the "Body" tab, choose "x-www-form-urlencoded", and 
add the keys title, author, and published_date.


# ////////////////////////////
# Client Project
# ///////////////////////////

python -m venv myenv
myenv\Scripts\activate
pip install django   
python -m pip install --upgrade pip
django-admin startproject ECommerce .
python manage.py startapp books
pip install requests  
python manage.py runserver

# TODO Install Apps in setting.py

'books',

# TODO Carete services.py in apps' directory

import requests

BASE_URL = 'http://127.0.0.1:8000/api/'

def get_all_books():
    response = requests.get(f"{BASE_URL}books/")
    if response.status_code == 200:
        return response.json()
    else:
        return []

def create_book(data):
    response = requests.post(f"{BASE_URL}books/", data=data)
    if response.status_code == 201:
        return response.json()
    else:
        return None


# TODO Create views

from django.shortcuts import render, redirect
from .services import get_all_books, create_book

def book_list(request):
    books = get_all_books()
    return render(request, 'book_list.html', {'books': books})

def add_book(request):
    if request.method == "POST":
        data = {
            'title': request.POST['title'],
            'author': request.POST['author'],
            'published_date': request.POST['published_date']
        }
        response = create_book(data)
        if response:
            return redirect('book_list')
    return render(request, 'add_book.html')


# TODO app's urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('add/', views.add_book, name='add_book'),
]


# TODO project's urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
]


# TODO create book_list.html in app's templates

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book List</title>
</head>
<body>
    <h1>Book List</h1>

    <a href="{% url 'add_book' %}">Add New Book</a>
    
    <table border="1">
        <thead>
            <tr>
                <th>Title</th>
                <th>Author</th>
                <th>Published Date</th>
            </tr>
        </thead>
        <tbody>
            {% for book in books %}
            <tr>
                <td>{{ book.title }}</td>
                <td>{{ book.author }}</td>
                <td>{{ book.published_date }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>


# TODO create add_book.html in app's templates

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Book</title>
</head>
<body>
    <h1>Add Book</h1>

    <form action="{% url 'add_book' %}" method="post">
        {% csrf_token %}
        <div>
            <label for="title">Title:</label>
            <input type="text" name="title" required>
        </div>
        <div>
            <label for="author">Author:</label>
            <input type="text" name="author" required>
        </div>
        <div>
            <label for="published_date">Published Date:</label>
            <input type="date" name="published_date" required>
        </div>
        <div>
            <input type="submit" value="Add Book">
        </div>
    </form>

    <a href="{% url 'book_list' %}">Back to Book List</a>
</body>
</html>


# TODO Run Server
# ? With different port to avoid conflict between api server and client server
python manage.py runserver 9000

# ========================
# webapi
# =======================

# TODO Define a model for Students in models.py:

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    grade = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

# TODO Run migrations:
python manage.py makemigrations
python manage.py migrate

# TODO Create serializers for the model in serializers.py:
# ? This will allow for easy conversion between Django models and JSON data.

from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


# ================================================
# TODO Define the API views in views.py:

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ViewSet):

    def list(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        try:
            student = Student.objects.get(pk=pk)
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete_all(self, request):
        count = Student.objects.all().delete()[0]
        return Response({'message': f'{count} students were deleted.'}, status=status.HTTP_200_OK)

# TODO Define URLs in app/urls.py:

from django.urls import path
from .views import StudentViewSet

urlpatterns = [
    path('student/getall', StudentViewSet.as_view({'get': 'list'}), name='get_all_students'),
    path('student/get/<int:pk>/', StudentViewSet.as_view({'get': 'retrieve'}), name='get_student_by_id'),
    path('student/add', StudentViewSet.as_view({'post': 'create'}), name='add_student'),
    path('student/update/<int:pk>/', StudentViewSet.as_view({'put': 'update'}), name='update_student_by_id'),
    path('student/deleteall', StudentViewSet.as_view({'delete': 'delete_all'}), name='delete_all_students'),
    path('student/delete/<int:pk>/', StudentViewSet.as_view({'delete': 'destroy'}), name='delete_student_by_id'),
]
# ================================================

# OR  Function based view and URL setting

# ================================================
# TODO Define the API views in views.py:

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

@api_view(['GET'])
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def student_create(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def student_update(request, pk):
    try:
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def student_delete(request, pk):
    try:
        student = Student.objects.get(pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def student_delete_all(request):
    count = Student.objects.all().delete()[0]
    return Response({'message': f'{count} students were deleted.'}, status=status.HTTP_200_OK)


# TODO Define URLs in app/urls.py:

from django.urls import path
from .views import student_list, student_detail, student_create, student_update, student_delete, student_delete_all

urlpatterns = [
    path('student/getall/', student_list, name='student-list'),
    path('student/get/<int:pk>/', student_detail, name='student-detail'),
    path('student/add/', student_create, name='student-create'),
    path('student/update/<int:pk>/', student_update, name='student-update'),
    path('student/delete/<int:pk>/', student_delete, name='student-delete'),
    path('student/deleteall/', student_delete_all, name='student-delete-all'),
]

# ================================================



# TODO Define URLs in project/urls.py:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('your_app.urls')),  
]

# TODO Testing with CMD (using curl):

# a. Get all students:
curl -X GET http://127.0.0.1:8000/api/student/getall

# Get student by ID (let's assume ID is 1 for this example):
curl -X GET http://127.0.0.1:8000/api/student/get/1/

# c. Add a student:
curl -X POST http://127.0.0.1:8000/api/student/add -H "Content-Type: application/json" -d '{"name": "John", "age": 18, "grade": "A"}'

# d. Update student by ID (let's assume ID is 1):
curl -X PUT http://127.0.0.1:8000/api/student/update/1/ -H "Content-Type: application/json" -d '{"name": "Jane", "age": 19, "grade": "11th"}'

# e. Delete all students:
curl -X DELETE http://127.0.0.1:8000/api/student/deleteall

# f. Delete student by ID (let's assume ID is 1):
curl -X DELETE http://127.0.0.1:8000/api/student/delete/1/


# TODO Testing with Postman:

# a. Get all students:
Set request type to GET.
Enter URL: http://127.0.0.1:8000/api/student/getall
Click Send.

# b. Get student by ID:
Set request type to GET.
Enter URL: http://127.0.0.1:8000/api/student/get/1/ (assuming ID is 1)
Click Send.

# c. Add a student:
Set request type to POST.
Enter URL: http://127.0.0.1:8000/api/student/add
Go to Body, select raw and choose JSON format.

Enter the student data:
{
  "name": "John",
  "age": 18,
  "grade": "10th"
}
Click Send.

# d. Update student by ID:
Set request type to PUT.
Enter URL: http://127.0.0.1:8000/api/student/update/1/ 
Go to Body, select raw and choose JSON format.

Update the student data:
{
  "name": "Jane",
  "age": 19,
  "grade": "11th"
}
Click Send.

# e. Delete all students:
Set request type to DELETE.
Enter URL: http://127.0.0.1:8000/api/student/deleteall
Click Send.

# f. Delete student by ID:
Set request type to DELETE.
Enter URL: http://127.0.0.1:8000/api/student/delete/1/ 
Click Send.

# ==========================
# Class base view
# =======================
# 1. models.py

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

# 2. forms.py

from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']

# 3. views.py

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Product
from .forms import ProductForm

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')

# 4. urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('create/', views.ProductCreateView.as_view(), name='product_create'),
]

# 5. product_list.html (for listing all products)

<!DOCTYPE html>
<html>
<head>
    <title>Products</title>
</head>
<body>
    <h1>Product List</h1>
    <ul>
    {% for product in products %}
        <li><a href="{% url 'product_detail' product.pk %}">{{ product.name }}</a> - ${{ product.price }}</li>
    {% endfor %}
    </ul>
    <a href="{% url 'product_create' %}">Add Product</a>
</body>
</html>

# 6. product_detail.html (for showing product details)

<!DOCTYPE html>
<html>
<head>
    <title>{{ object.name }}</title>
</head>
<body>
    <h1>{{ object.name }}</h1>
    <p>Price: ${{ object.price }}</p>
    <p>Description: {{ object.description }}</p>
    <a href="{% url 'product_list' %}">Back to list</a>
</body>
</html>

# 7. product_form.html (for creating a product)

<!DOCTYPE html>
<html>
<head>
    <title>Create Product</title>
</head>
<body>
    <h1>Create Product</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Save">
    </form>
    <a href="{% url 'product_list' %}">Cancel</a>
</body>
</html>


#====================================
# Class based view with Image
#====================================

# TODO necessary setting

# 1. Install Necessary Packages:

pip install Pillow

# 2. Add django.contrib.staticfiles:

INSTALLED_APPS = [
    ...
    'django.contrib.staticfiles',
    ...
]

# 3. Configure Media Settings: settings.py

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# 4. Configure URLs for Serving Media Files into app's urls.py:

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ---------------------------------

# TODO Start Project
# 1. Model: models.py

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
    
# 2. ModelForm: forms.py

from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image']

# 3. Class Based Views: views.py

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from .forms import ProductForm

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('product_list')


# 4. URL Patterns: urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('create/', views.ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product_edit'),
    path('<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
]

# 5. Templates
# a) For listing all products: product_list.html

<!DOCTYPE html>
<html>
<head>
    <title>Products</title>
</head>
<body>
    <h1>All Products</h1>
    <ul>
        {% for product in products %}
            <a href="{% url 'product_detail' product.pk %}">{{ product.name }}</a><br>
        {% endfor %}
    </ul>
    <a href="{% url 'product_create' %}">Add New Product</a>
</body>
</html>

# b) For product details: product_detail.html

<!DOCTYPE html>
<html>
<head>
    <title>{{ object.name }}</title>
</head>
<body>
    <h1>{{ object.name }}</h1>
    <img src="{{ object.image.url }}" alt="{{ object.name }}">
    <p>Price: {{ object.price }}</p>
    <p>{{ object.description }}</p>
    <a href="{% url 'product_edit' object.pk %}">Edit</a>
    <a href="{% url 'product_delete' object.pk %}">Delete</a>
</body>
</html>

# c) For adding a product: product_form.html

<!DOCTYPE html>
<html>
<head>
    <title>Create Product</title>
</head>
<body>
    <h1>Create Product</h1>
    <form method="post" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>
    <a href="{% url 'product_list' %}">Cancel</a>
</body>
</html>

# d)  product_confirm_delete.html

<!DOCTYPE html>
<html>
<head>
    <title>Delete Product</title>
</head>
<body>    
    <p>Are you sure you want to delete {{ object.name }}?</p>
    <form method="post">
        {% csrf_token %}
        <button type="submit">Confirm Delete</button>
    </form>
    <a href="{% url 'product_list' %}">Cancel</a>
</body>
</html>


# ==============================

# TODO Necessary setting for images
# 1. Install Necessary Packages:

pip install Pillow

# 2. Add django.contrib.staticfiles:

INSTALLED_APPS = [
    ...
    'django.contrib.staticfiles',
    ...
]

# 3. Configure Media Settings: settings.py

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# 4. Configure URLs for Serving Media Files into app's urls.py:

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# ===============================================================
# Create Operation
# ===============================================================


# TODO Create Model

from django.db import models

class Person(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='persons_photos/')


# TODO Migrations

python manage.py makemigrations <appname>
python manage.py migrate <appname>


# TODO Create serializers.py:

from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


# TODO Create Views

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer

class PersonCreateAPI(APIView):

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# TODO URL Configuration:

from django.urls import path
from .views import PersonCreateAPI

urlpatterns = [
    path('person/add/', PersonCreateAPI.as_view(), name='add_person'),
]

# TODO Testing:

# using http
# You can use the httpie tool (pip install httpie). 

http -f POST http://localhost:8000/person/add/ name='John Doe' date_of_birth='1990-01-01' gender='M' age=33 salary=1000.00 photo@C:/images/jhon.png


# using curl

curl -X POST -F "name=John Doe" -F "date_of_birth=1990-01-01" -F "gender=M" -F "age=33" -F "salary=1000.00" -F "photo=@C:/images/jhon.png" http://localhost:8000/person/add/


# Postman:

1. Start Postman.
2. Select the "POST" method and enter http://localhost:8000/person/add/.
3. Under the "Body" tab, select "form-data".
4. Add keys (name, date_of_birth, gender, age, salary, and photo) with their corresponding values. For the photo, select "File" from the dropdown to upload an image.
5. Click "Send" to send the request.


# ===============================================================
# Select Operation
# ===============================================================

# TODO Update Views

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer

class PersonDetailAPI(APIView):

    def get(self, request, pk):
        try:
            person = Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PersonSerializer(person)
        return Response(serializer.data)


# TODO Update URL Configuration:

from django.urls import path
from .views import PersonDetailAPI

urlpatterns = [
    # ... other URL patterns
    path('person/detail/<int:pk>/', PersonDetailAPI.as_view(), name='person_detail'),
]


# TODO Testing:

# using http
# You can use the httpie tool (pip install httpie). 

http GET http://localhost:8000/person/detail/1/

# using curl

curl -X GET http://localhost:8000/person/detail/1/


# Postman:

1. Start Postman.
2. Select the "GET" method and enter http://localhost:8000/person/detail/1/ (assuming you want to get the details of the record with ID 1).
3. Click "Send" to send the request.


# ===============================================================
# Select All Operation
# ===============================================================

# TODO Update Views

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer

class PersonListAPI(APIView):

    def get(self, request):
        try:
            persons = Person.objects.all()
            if not persons:
                return Response({"error": "No persons found"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = PersonSerializer(persons, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# TODO Update URL Configuration:

from django.urls import path
from .views import PersonListAPI

urlpatterns = [
    # ... other URL patterns
    path('persons/', PersonListAPI.as_view(), name='persons_list'),
]


# TODO Testing:

# using http
# You can use the httpie tool (pip install httpie). 

http GET http://localhost:8000/persons/


# using curl

curl http://localhost:8000/persons/


# Postman:

1. Start Postman.
2. Select the "GET" method.
3. Enter the URL http://localhost:8000/persons/.
4. Click "Send".


# ===============================================================
# Update Operation
# ===============================================================

# TODO Update Views

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer

class PersonUpdateAPI(APIView):

    def put(self, request, pk):
        try:
            person = Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# TODO Update URL Configuration:

from django.urls import path
from .views import PersonUpdateAPI

urlpatterns = [
    # ... other URL patterns
    path('person/update/<int:pk>/', PersonUpdateAPI.as_view(), name='update_person'),
]


# TODO Testing:

# using http
# You can use the httpie tool (pip install httpie). 

http PUT http://localhost:8000/person/update/1/ name='Jane Doe' date_of_birth='1991-02-01' gender='F' age=32 salary=1100.00 photo@C:/images/new.png

# using curl

curl -X PUT http://localhost:8000/person/update/1/ \
     -H "Content-Type: multipart/form-data" \
     -F "name=Jane Doe" \
     -F "date_of_birth=1991-02-01" \
     -F "gender=F" \
     -F "age=32" \
     -F "salary=1100.00" \
     -F "photo=@C:/images/new.png"


# Postman:

1. Start Postman.
2. Select the "PUT" method and enter http://localhost:8000/person/update/1/ (assuming you want to update the record with ID 1).
3. Under the "Body" tab, select "form-data".
4. Add keys (name, date_of_birth, gender, age, salary, and photo) with their new values. For the photo, select "File" from the dropdown to upload a new image.
5. Click "Send" to send the request.


# ===============================================================
# Delete Operation
# ===============================================================

# TODO Update Views

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Person

class PersonDeleteAPI(APIView):

    def delete(self, request, pk):
        try:
            person = Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# TODO Update URL Configuration:

from django.urls import path
from .views import PersonDeleteAPI

urlpatterns = [
    # ... other URL patterns
    path('person/delete/<int:pk>/', PersonDeleteAPI.as_view(), name='delete_person'),
]


# TODO Testing:

# using http
# You can use the httpie tool (pip install httpie). 

http DELETE http://localhost:8000/person/delete/1/

# using curl

curl -X DELETE http://localhost:8000/person/delete/1/


# Postman:

1. Start Postman.
2. Select the "DELETE" method and enter http://localhost:8000/person/delete/1/ (assuming you want to delete the record with ID 1).
3. Click "Send" to send the request.


# ===============================================================
# Delete All Operation
# ===============================================================

# TODO Update Views

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Person

class PersonDeleteAllAPI(APIView):

    def delete(self, request):
        Person.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# TODO Update URL Configuration:

from django.urls import path
from .views import PersonDeleteAllAPI

urlpatterns = [
    # ... other URL patterns
    path('person/delete_all/', PersonDeleteAllAPI.as_view(), name='delete_all_persons'),
]


# TODO Testing:

# using http
# You can use the httpie tool (pip install httpie). 

http DELETE http://localhost:8000/person/delete_all/

# using curl

curl -X DELETE http://localhost:8000/person/delete_all/


# Postman:

1. Start Postman.
2. Select the "DELETE" method and enter http://localhost:8000/person/delete_all/.
3. Click "Send" to send the request.


# ===============================================================
# Filter Operation
# ===============================================================

# TODO Update Views

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer

class PersonFilterAPI(APIView):

    def get(self, request):
        persons = Person.objects.all()

        # Name filters
        name_start = request.query_params.get('name_start', None)
        if name_start:
            persons = persons.filter(name__istartswith=name_start)
        
        name_end = request.query_params.get('name_end', None)
        if name_end:
            persons = persons.filter(name__iendswith=name_end)

        # Salary filters
        salary_gt = request.query_params.get('salary_gt', None)
        if salary_gt:
            persons = persons.filter(salary__gt=salary_gt)

        salary_lt = request.query_params.get('salary_lt', None)
        if salary_lt:
            persons = persons.filter(salary__lt=salary_lt)

        salary_range = request.query_params.getlist('salary_range', None)
        if salary_range and len(salary_range) == 2:
            persons = persons.filter(salary__range=(salary_range[0], salary_range[1]))

        # Birthdate filters
        birthdate_gt = request.query_params.get('birthdate_gt', None)
        if birthdate_gt:
            persons = persons.filter(date_of_birth__gt=birthdate_gt)

        birthdate_lt = request.query_params.get('birthdate_lt', None)
        if birthdate_lt:
            persons = persons.filter(date_of_birth__lt=birthdate_lt)

        birthdate_range = request.query_params.getlist('birthdate_range', None)
        if birthdate_range and len(birthdate_range) == 2:
            persons = persons.filter(date_of_birth__range=(birthdate_range[0], birthdate_range[1]))

        # Gender filter
        gender = request.query_params.get('gender', None)
        if gender:
            persons = persons.filter(gender=gender.upper())

        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)
    

# TODO Update URL Configuration:

from django.urls import path
from .views import PersonFilterAPI

urlpatterns = [
    # ... other URL patterns
    path('person/filter/', PersonFilterAPI.as_view(), name='person_filter'),
]


# TODO Testing:

# using http
# You can use the httpie tool (pip install httpie). 

http GET "http://localhost:8000/person/filter/?name_start=Jo&salary_gt=5000&gender=M"


# using curl

curl "http://localhost:8000/person/filter/?name_start=Jo&salary_gt=5000&gender=M"


# Postman:

1. Start Postman.
2. Select the "GET" method.
3. Enter the URL http://localhost:8000/person/filter/ followed by query parameters for filtering. For example: http://localhost:8000/person/filter/?name_start=Jo&salary_gt=5000&gender=M
4. Click "Send".


#====================================
# Passing Object to HTML Page
#====================================

# 1. models.py

from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=40)
    birthdate = models.DateField()
    email = models.CharField(max_length=60)
    phone = models.IntegerField()    
    hiredate = models.DateTimeField()
    salary = models.FloatField()

class EmployeeDetails(models.Model):
    empid = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)     # Default one-one relationship
    passport = models.CharField(max_length=10)

class EmployeeQualification(models.Model):
    empid = models.ForeignKey(Employee, on_delete=models.CASCADE)      # Default one-many relationship
    qualification = models.CharField(max_length=10)


# 2. forms.py

from django import forms
from .models import Employee, EmployeeDetails, EmployeeQualification

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeDetailsForm(forms.ModelForm):
    class Meta:
        model = EmployeeDetails
        fields = '__all__'

class EmployeeQualificationForm(forms.ModelForm):
    class Meta:
        model = EmployeeQualification
        fields = '__all__'


# 3. views.py

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Employee, EmployeeDetails, EmployeeQualification
from .forms import EmployeeForm, EmployeeDetailsForm, EmployeeQualificationForm

# Employee views
class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'

class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list')

# EmployeeDetails views
class EmployeeDetailsListView(ListView):
    model = EmployeeDetails
    template_name = 'employeedetails_list.html'

class EmployeeDetailsCreateView(CreateView):
    model = EmployeeDetails
    form_class = EmployeeDetailsForm
    template_name = 'employeedetails_form.html'
    success_url = reverse_lazy('employeedetails_list')

class EmployeeDetailsUpdateView(UpdateView):
    model = EmployeeDetails
    form_class = EmployeeDetailsForm
    template_name = 'employeedetails_form.html'
    success_url = reverse_lazy('employeedetails_list')

class EmployeeDetailsDeleteView(DeleteView):
    model = EmployeeDetails
    template_name = 'employeedetails_confirm_delete.html'
    success_url = reverse_lazy('employeedetails_list')


# EmployeeQualification views
class EmployeeQualificationListView(ListView):
    model = EmployeeQualification
    template_name = 'employeequalification_list.html'

class EmployeeQualificationCreateView(CreateView):
    model = EmployeeQualification
    form_class = EmployeeQualificationForm
    template_name = 'employeequalification_form.html'
    success_url = reverse_lazy('employeequalification_list')

class EmployeeQualificationUpdateView(UpdateView):
    model = EmployeeQualification
    form_class = EmployeeQualificationForm
    template_name = 'employeequalification_form.html'
    success_url = reverse_lazy('employeequalification_list')

class EmployeeQualificationDeleteView(DeleteView):
    model = EmployeeQualification
    template_name = 'employeequalification_confirm_delete.html'
    success_url = reverse_lazy('employeequalification_list')


# 4. urls.py

from django.urls import path
from .views import (
    EmployeeListView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView,
    EmployeeDetailsListView, EmployeeDetailsCreateView, EmployeeDetailsUpdateView, EmployeeDetailsDeleteView,
    EmployeeQualificationListView, EmployeeQualificationCreateView, EmployeeQualificationUpdateView, EmployeeQualificationDeleteView
)

urlpatterns = [
    path('employees/', EmployeeListView.as_view(), name='employee_list'),
    path('employee/add/', EmployeeCreateView.as_view(), name='employee_add'),
    path('employee/edit/<int:pk>/', EmployeeUpdateView.as_view(), name='employee_edit'),
    path('employee/delete/<int:pk>/', EmployeeDeleteView.as_view(), name='employee_delete'),
    
    path('employeedetails/', EmployeeDetailsListView.as_view(), name='employeedetails_list'),
    path('employeedetails/add/', EmployeeDetailsCreateView.as_view(), name='employeedetails_add'),
    path('employeedetails/edit/<int:pk>/', EmployeeDetailsUpdateView.as_view(), name='employeedetails_edit'),
    path('employeedetails/delete/<int:pk>/', EmployeeDetailsDeleteView.as_view(), name='employeedetails_delete'),

    path('employeequalification/', EmployeeQualificationListView.as_view(), name='employeequalification_list'),
    path('employeequalification/add/', EmployeeQualificationCreateView.as_view(), name='employeequalification_add'),
    path('employeequalification/edit/<int:pk>/', EmployeeQualificationUpdateView.as_view(), name='employeequalification_edit'),
    path('employeequalification/delete/<int:pk>/', EmployeeQualificationDeleteView.as_view(), name='employeequalification_delete'),
]
# 5. employee_list.html:

{% for employee in object_list %}
    {{ employee.name }} - {{ employee.email }}
    <a href="{% url 'employee_edit' employee.pk %}">Edit</a>
    <a href="{% url 'employee_delete' employee.pk %}">Delete</a>
    <br>
{% endfor %}

# 6. employee_form.html:

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save</button>
</form>

# 7. employee_confirm_delete.html:

<p>Are you sure you want to delete {{ object.name }}?</p>
<form method="post">
    {% csrf_token %}
    <button type="submit">Yes, Delete</button>
</form>

# 8. employeedetails_list.html:

{% extends 'base.html' %}

{% block content %}
<h2>Employee Details List</h2>
<table class="table">
    <thead>
        <tr>
            <th>ID</th>
            <th>Passport</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        {% for detail in object_list %}
        <tr>
            <td>{{ detail.empid.id }}</td>
            <td>{{ detail.passport }}</td>
            <td>
                <a href="{% url 'employeedetails_edit' detail.pk %}" class="btn btn-primary">Edit</a>
                <a href="{% url 'employeedetails_delete' detail.pk %}" class="btn btn-danger">Delete</a>
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
<a href="{% url 'employeedetails_add' %}" class="btn btn-success">Add New</a>
{% endblock %}

# 9. employeedetails_form.html:

{% extends 'base.html' %}

{% block content %}
<h2>Add/Edit Employee Details</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-primary">Submit</button>
</form>
{% endblock %}

# 10. employeedetails_confirm_delete.html:

{% extends 'base.html' %}

{% block content %}
<h2>Are you sure you want to delete this record?</h2>
<form method="post">
    {% csrf_token %}
    <button type="submit" class="btn btn-danger">Yes, Delete</button>
    <a href="{% url 'employeedetails_list' %}" class="btn btn-secondary">Cancel</a>
</form>
{% endblock %}

# 11. employeequalification_list.html:

{% extends 'base.html' %}

{% block content %}
<h2>Employee Qualifications List</h2>
<table class="table">
    <thead>
        <tr>
            <th>ID</th>
            <th>Qualification</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        {% for qualification in object_list %}
        <tr>
            <td>{{ qualification.empid.id }}</td>
            <td>{{ qualification.qualification }}</td>
            <td>
                <a href="{% url 'employeequalification_edit' qualification.pk %}" class="btn btn-primary">Edit</a>
                <a href="{% url 'employeequalification_delete' qualification.pk %}" class="btn btn-danger">Delete</a>
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
<a href="{% url 'employeequalification_add' %}" class="btn btn-success">Add New</a>
{% endblock %}

# 12. employeequalification_form.html:

{% extends 'base.html' %}

{% block content %}
<h2>Add/Edit Employee Qualification</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-primary">Submit</button>
</form>
{% endblock %}

# 13. employeequalification_confirm_delete.html:

{% extends 'base.html' %}

{% block content %}
<h2>Are you sure you want to delete this qualification?</h2>
<form method="post">
    {% csrf_token %}
    <button type="submit" class="btn btn-danger">Yes, Delete</button>
    <a href="{% url 'employeequalification_list' %}" class="btn btn-secondary">Cancel</a>
</form>
{% endblock %}

# ================================

#====================================
# Many to Many Relationship
#====================================

# 1. models.py

from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=200)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name



# 2. forms.py

from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'



# 3. views.py

from django.shortcuts import render, redirect
from .models import Student, StudentForm

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = '/success/'

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'


# 4. urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.StudentCreateView.as_view(), name='student-create'),
    path('list/', views.StudentListView.as_view(), name='student-list'),
]

# 5. base.html:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django M2M</title>
</head>
<body>
    {% block content %}
    {% endblock %}
</body>
</html>


# 6. student_form.html:

{% extends 'base.html' %}

{% block content %}
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
  </form>
{% endblock %}


# 7. student_list.html:

{% extends 'base.html' %}

{% block content %}
  <h2>Students</h2>
  <ul>
    {% for student in students %}
      <li>{{ student.name }} - Enrolled in: 
        {% for course in student.courses.all %}
          {{ course.name }}{% if not forloop.last %}, {% endif %}
        {% endfor %}
      </li>
    {% endfor %}
  </ul>
{% endblock %}


# =================================
# Implement Validation
# =================================

# 1. Models

from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=200)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

# 2. Form

from django import forms

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def clean_salary(self):
        salary = self.cleaned_data.get('salary')
        if salary < 0:
            raise forms.ValidationError('Salary cannot be less than zero.')
        return salary
    
# 3. Views

from django.shortcuts import render, redirect
from .models import Person, PersonForm
from django.views.generic import CreateView, ListView

class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'person_form.html'
    success_url = '/persons/'

class PersonListView(ListView):
    model = Person
    template_name = 'person_list.html'
    context_object_name = 'persons'

# 4. URLs

from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.PersonCreateView.as_view(), name='person-create'),
    path('persons/', views.PersonListView.as_view(), name='person-list'),
]

# 5. Templates - person2_form.html:

{% extends 'base.html' %}

{% block content %}
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
  </form>
{% endblock %}

# person_list.html:

{% extends 'base.html' %}

{% block content %}
  <h2>Persons</h2>
  <ul>
    {% for person in persons %}
      <li>{{ person.name }} - {{ person.email }}</li>
    {% endfor %}
  </ul>
{% endblock %}

# 6. base.html:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django Person App</title>
</head>
<body>
    {% block content %}
    {% endblock %}
</body>
</html>

# ================================
# User Authentication
# ==============================

# ? Creating an entire authentication system with Django involves quite a bit of code. 
# ? I'll provide you with a step-by-step guide on how to set it up:

# TODO models.py:
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
      (1, 'customer'),
      (2, 'seller'),
    )
    
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)



# (in project's settings)

AUTH_USER_MODEL = 'appname.modelname'

# Comment this app from project's setting's installed app 
'django.contrib.admin'

# Comment admin's path fron project's url
    # path('admin/', admin.site.urls)
    

# TODO Do Migration
python manage.py makemigrations <app name>
python manage.py migrate <app name>


# TODO forms.py:
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'user_type')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'user_type')


# TODO views.py:
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views import View
from .forms import CustomUserCreationForm, CustomUserChangeForm, PasswordChangeForm
from .models import CustomUser

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html', {'form': CustomUserCreationForm()})
    
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.user_type == 1: # customer
                return redirect('customer_dashboard')
            else: # seller
                return redirect('seller_dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('login')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

@login_required
def customer_dashboard(request):
    if request.user.user_type != 1:
        return redirect('login')
    return render(request, 'customer_dashboard.html')

@login_required
def seller_dashboard(request):
    if request.user.user_type != 2:
        return redirect('login')
    return render(request, 'seller_dashboard.html')


# TODO urls.py:
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('change-password/', views.change_password, name='change_password'),
    path('dashboard/customer/', views.customer_dashboard, name='customer_dashboard'),
    path('dashboard/seller/', views.seller_dashboard, name='seller_dashboard'),
]


# TODO base.html - A basic structure that other templates extend from:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Dashboard System</title>
</head>
<body>
    <header>
        <nav>
            <!-- You can add a navbar here -->
            <a href="{% url 'login' %}">Login</a>
            <a href="{% url 'register' %}">Register</a>
        </nav>
    </header>
    <main>
        {% block content %}
        {% endblock %}
    </main>
</body>
</html>


# TODO register.html:
{% extends "base.html" %}

{% block content %}
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Register</button>
</form>
{% endblock %}



# TODO login.html - A basic login page:
{% extends "base.html" %}

{% block content %}
<h2>Login</h2>
<form method="post">
    {% csrf_token %}
    <div>
        <label for="id_username">Username:</label>
        <input type="text" name="username" required>
    </div>
    <div>
        <label for="id_password">Password:</label>
        <input type="password" name="password" required>
    </div>
    <button type="submit">Login</button>
</form>
{% if error %}
    <p style="color: red;">{{ error }}</p>
{% endif %}
{% endblock %}


# TODO change_password.html - For changing the password:
{% extends "base.html" %}

{% block content %}
<h2>Change Password</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Change Password</button>
</form>
{% endblock %}


# TODO customer_dashboard.html - A dashboard for customers:
{% extends "base.html" %}

{% block content %}
<h2>Customer Dashboard</h2>
<p>Welcome, {{ request.user.username }}!</p>
<p>This is your customer dashboard. Explore our features!</p>
{% endblock %}


# TODO seller_dashboard.html - A dashboard for sellers:
{% extends "base.html" %}

{% block content %}
<h2>Seller Dashboard</h2>
<p>Welcome, {{ request.user.username }}!</p>
<p>This is your seller dashboard. Manage your products and track sales here!</p>
{% endblock %}


