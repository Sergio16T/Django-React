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