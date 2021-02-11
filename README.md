# price-history-django
Price History Project Tokopedia Scrapper using Django

## Installation 
If you wish to run your own build, you two options
 1. Use Docker compose.
    
    `$ git clone https://github.com/wikankun/price-history-django.git`
    
    `$ cd price-history-django`
    `$ docker-compose up`
 
 2. Without docker
 
First ensure you have python globally installed in your computer. If not, you can get python [here](python.org).

After doing this, confirm that you have installed virtualenv globally as well. If not, run this:

    $ pip install virtualenv
Then, Git clone this repo to your PC

    $ git clone https://github.com/wikankun/price-history-django.git
    $ cd price-history-django
Create a virtual environment

    $ virtualenv .venv && source .venv/bin/activate
Install dependancies

    $ pip install -r requirements.txt
Make migrations & migrate

    $ python manage.py makemigrations && python manage.py migrate
Create Super user
    
    $ python manage.py createsuperuser

## Launching the app
    $ python manage.py runserver
