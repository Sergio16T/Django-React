## PyCharm Setup
**Select Python Interpretor:**  PyCharm > preferences > Project:Django-React > Python Interpretor

#### Enable Django Support 
1) PyCharm > preferences > Languages & Frameworks > Django
2) Select Enable Django Support 
3) Fill out project root, settings and manage script.

## Model Migrations - SQL
By running makemigrations, you’re telling Django that you’ve made some changes to your models
and that you’d like the changes to be stored as a migration:
```shell
python manage.py makemigrations polls
```

 
The sqlmigrate command takes migration names and returns their SQL:
```shell
python manage.py sqlmigrate polls 0001
```

to create those model tables in your database:
```shell
python manage.py migrate
```

## Apps in Project 
- polls: inital intro to Django. Some sample code to connect with a DB.
- todolist: Simple REST API






