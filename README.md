# Django Verkkokauppa
Verkkokauppasovellus toteutettu Django-frameworkilla

- Python 3.9.3
- Django 4.0.5

## How to run this app

|Run these commands in terminal in the app directory|Command|
|-|-|
Create virual env: | `python3 -m venv venv`
Activate virtual env: | `.venv\Scripts\Activate.ps1` windows `.venv/bin/activate` linux
Install dependencies: | `pip install -r .\requirements.txt`
Make migrations: | `python3 verkkokauppa\manage.py makemigrations`
Run migrations: | `python3 verkkokauppa\manage.py migrate`
Launch the app: | `python3 verkkokauppa\manage.py runserver`

The app will run on localhost http://127.0.0.1:8000

## Ominaisuudet
* Login/logout
* Shopping cart
* Add and remove from cart
* Profile page
* Feedback form
* Updating profile

### Base
Sivut:
* Home
* Store
* About
* Products

### Cart
* Shopping cart
* Checkout
* Payment processed

### Users
* Contact
* Login
* Logout
* Profile
* Register
* Update
