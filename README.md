# PhoneBook

This is a simple website to create and store Contact of companies. This website using Django Framework.

## Getting Started
First clone the repository

```console
$ git clone https://github.com/justA-Noobdev/PhoneBook.git
$ cd Phonebook

# Sometimes virtualenv doesn't work properly so you can install it as superuser to avoid that issue
$ sudo pip install virtualenv

# Create a virtual enviroment and activate it
$ virtualenv venv
$ source venv/bin/activate

# Install Django and run the server
$ pip install django
$ python manage.py runserver
```
You can go to [127.0.0.1:8000](https://127.0.0.1:8000) to view the website.

## Feature of website
* You can add and delete contacts.
* You can add user with or without superuser access.
* Only superusers/admins can add, edit or delete contacts and users.
* You can we the companies by the type of contract you have with them.
