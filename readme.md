![Alt Python Django](/screenshots/database_illustration.gif "Python Django")

## How to connect Python **Django REST framework** with **MongoDB** database for a **REST API** project?
Make sure you have python 3 installed on your machine. This tutorial will be covered based on Ubuntu 20 Operating System. <br>

![Alt Django REST framework](/screenshots/logo.png "Django REST framework")

[Visit this link if you didn't install Python yet!](https://www.python.org/downloads/) 

* Check your Python installed successfully or not <br>

```python 
  python3 --version
```
* Update the packages <br>

```python 
  sudo apt update
```

* Install **pip** and **Python Virtual Environment**  <br>

```python 
  sudo apt install python3-pip python3-venv
```

* Create a new directory in  your machine and allow **Read Write** permission to it  <br>

```python 
  sudo mkdir test
  cd test
  sudo chmod -R 777 ./ #You can edit permission later
```


* Create your **Python Virtual Environment**, here I named it **my_env**  <br>

```python 
  python3 -m venv my_env
```

* Enable your virtual environment  <br>

```python 
  source my_env/bin/activate
```

* Install **Django**  <br>

```python 
  pip install django
```

* Check Django installed successfully or not  <br>

```python 
  django-admin --version
```

* Create a new project with Django   <br>

```python 
  
  django-admin startproject my_project .


  ls # You will see a file named manage.py
  
```

* Now, **Start the server!** <br>

```python 
  python3 manage.py runserver
```

A server will run on your machine on 8000 port. <br>
Now open your browser and copy and paste the link **http://127.0.0.1:8000/** or **http://localhost:8000** or **localhost:8000**

### If you see something like the screenshot below then **Congratulation!** You successfully installed **Python Django** on your machine. <br><br>

![Alt text](/screenshots/_django_installation.JPG "Python Django")

## Now, we have to install **Django Rest Framework** 
#### Django REST framework is a powerful and flexible toolkit for building Web APIs.

[Django REST framework](https://www.django-rest-framework.org/) 

* Create an app <br>

```python 
  django-admin startapp my_rest_api_app
```


* Install the main framework <br>

```python 
  pip install djangorestframework
```



* Add **'rest_framework'** to your **INSTALLED_APPS** setting. <br>

```python 
  INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

![Alt djangorestframework](/screenshots/s1.png "djangorestframework")

### And thats all! You successfully installed **Django REST Framework**.

## Install MongoDB database (Install MongoDB Community Edition)
[How to install MongoDB on Ubuntu](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/)

* Import the public key used by the package management system. <br>

```python 
  wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
```
> *The operation should respond with an **OK*** 
* However, if you receive an error indicating that gnupg is not installed, you can:

1. Install gnupg and its required libraries using the following command:

```python 
  sudo apt-get install gnupg
```

2. Once installed, retry importing the key:

```python 
  wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
```

* Create a list file for MongoDB
> Create the list file /etc/apt/sources.list.d/mongodb-org-5.0.list for your version of Ubuntu. If you are unsure of what Ubuntu version the host is running, open a terminal or shell on the host and execute **lsb_release -dc**

1.  Ubuntu 20.04 (Focal)

```python 
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
```

2.  Ubuntu 18.04 (Bionic)

```python 
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
```

3.  Ubuntu 16.04 (Xenial)

```python 
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
```

* Reload local package database

```
sudo apt update
```

* Install the MongoDB packages

```
sudo apt-get install -y mongodb-org
```
> To install a specific release, you must specify each component package individually along with the version number, as in the following example:
```
sudo apt-get install -y mongodb-org=5.0.7 mongodb-org-database=5.0.7 mongodb-org-server=5.0.7 mongodb-org-shell=5.0.7 mongodb-org-mongos=5.0.7 mongodb-org-tools=5.0.7
```

* Start MongoDB
```
sudo systemctl start mongod
#or 
sudo service mongod start
```

* Verify that MongoDB has started successfully
```
sudo systemctl status mongod
#or 
sudo service mongod status
```

> You can optionally ensure that MongoDB will start following a system reboot by issuing the following command:

```
sudo systemctl enable mongod
```

* Stop MongoDB
```
sudo service mongod stop
```

* Restart MongoDB
```
sudo service mongod restart
```
* Begin using MongoDB
```
mongosh
#or
mongo
```
* To exit from MongoDB command shell
```
exit
#or
bye
```

## Connecting **MongoDB** database with **Django Rest Framework**

* First add your app in installed app list

![add app](/screenshots/add_app.JPG)

* Install **djongo** plugin or library
```
pip install djongo
```

* Configuring MongoDB
> Navigate to the **settings.py** file and change the DATABASES setting as follows:
```
DATABASES = {
   'default' : {
      'ENGINE' : 'djongo',
      'NAME' : 'my_custom_db' #database name
   }
}
```

## Building the **User Info Database** app via API
* Let’s define a model for the notes in the **models.py** file of the **my_rest_api_app** app that we have created

```
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.TextField(max_length=200)
    def __str__(self):
        return self.name
```

* Let’s migrate the model into the database
```
python3 manage.py makemigrations

python3 manage.py migrate
```

> If you face any problem during **makemigrations** command then may be your **pymongo version** not comptible with **djongo version**

```
pip install pymongo==3.12.3
```

* If you see something like this then database migration completed succesfully 

![Python Database Migration](/screenshots/database_migration.JPG)

* Next, let’s create a **serializer** class. When users make requests to the API, the serializers format the corresponding responses. Create a new **serializers.py** file in the **my_rest_api_app** app folder. Make the necessary imports as demonstrated below and create the **UserSerializer** class.

```
from rest_framework import serializers
from .models import User
class UserSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = User
        fields = ( 'name', 'email', 'address')
```

* Next, let’s create the views that will handle the request and response actions of our API. Create the **UserList** view in the **views.py** file of the **my_rest_api_app** app.

```
from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

* Create a new **urls.py** file inside the **my_rest_api_app** app directory. 
> Create the **urlpatterns** as follows inside:

```
from django.urls import path
from my_rest_api_app import views

urlpatterns = [
    path('', views.UserList.as_view()),
]
```

* Next, set up the **urls.py** file of the **my_project** to point to the app level urlpatterns. Then, include a path to the **urls.py** file of the **my_rest_api_app** app.
```
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('my_rest_api_app.urls')),  # add this line
]
```

> The endpoint receives the actions ‘LIST’ and ‘CREATE’ actions of the **UserList** view.

## Testing with browsable API
### Django REST framework comes shipped with the browsable API. You can test your API endpoints with the browsable API.

* Activate the test server:
```
python3 manage.py runserver
```

* Then navigate to 127.0.0.1:8000/api/ on your browser to create users.

![User List](/screenshots/c1.JPG)

* Create an user

![User List](/screenshots/c2.JPG)

* After creating an user successfully, previous users data will show in a list.

![User List](/screenshots/c3.JPG)

* Direct data view from database

![Direct data view](/screenshots/c4.JPG)

## By this tutorial we successfully:
1. Created a Python Django REST API project
2. Connected our project with MongoDB
3. Created sample REST API for testing purpose



## Now, go ahead and create something awesome on you own! Keep Coding!!! 😄 😄 😄