# Django To Do

* sudo pip3 install django==1.11

* django-admin startproject django_todo . 

* python3 manage.py runserver $IP:$C9_PORT

> Error:
You may need to add 'django-todo-coffeeipsum.c9users.io' to ALLOWED_HOSTS

Go to settings.py and add the ULR to ALLOWED_HOSTS[ ]
Then:
* django-admin startapp todo

# SQLite3
bash $:
sqlite3 db.sqlite3


# Django Super User
bash $:
python3 manage.py createsuperuser

# Nice Trick:
To avoid typing the commands `.headers` on and `.mode column` we can create a
new file called `.sqliterc` under FAVORITES > workspace

