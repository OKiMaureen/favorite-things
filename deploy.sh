#!/bin/bash

sudo apt-get update && sudo apt-get upgrade -y

echo "Starting python installation...."
{
  export LC_ALL=C
  sudo apt-get install python-pip -y
  sudo add-apt-repository ppa:deadsnakes/ppa
  sudo apt-get update
  sudo apt-get install python3.7 -y
  sudo apt-get install libpq-dev
  sudo apt-get install python3.7-dev
	echo "Python Installed :)"
} || {
	echo "Python installation failed"
}

echo "Installing pipenv..."
{ 
	pip install pipenv
	echo "Pipenv installed :)"
} || {
	echo "Pipenv installation failed"
}

echo "Installing server dependencies"
  cd favorite-things &&  pipenv run pipenv install -r  requirements.txt
  cd favourite_things_api && pipenv run python manage.py migrate && pipenv run python manage.py loaddata category_fixtures.json cd -
echo "Dependencies installed and defaults added"

echo "Starting gunicorn"
{  
  cd favourite_things_api && pipenv run pipenv install gunicorn  && sudo apt install gunicorn
  gunicorn --bind 0.0.0.0:8000 favourite_things_api.wsgi:application --daemon cd -
  echo "gunicorn running"
} || {
  echo "gunicorn not running"
}


echo "Installing nodejs"
{   
    sudo apt-get install curl
	curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
    sudo apt-get install nodejs
	echo "Node installed :)"
} || {
	echo "Nodejs installation failed"
}

echo "Installing client dependencies"
cd favourite-things-client && npm install && cd -
echo "Dependencies installed :)"

echo "building client"
cd favourite-things-client && npm run build && cd -
echo "client built :)"


echo "Installing Nginx"
sudo apt-get install nginx -y
sudo touch /etc/nginx/sites-available/django.conf
sudo cp django.conf /etc/nginx/sites-available/django.conf
sudo ln -S /etc/nginx/sites-available/django.conf /etc/nginx/sites-enabled/django.conf

sudo nginx -t
sudo service nginx restart

