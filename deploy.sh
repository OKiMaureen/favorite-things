#!/bin/bash

sudo apt-get update && sudo apt-get upgrade -y

echo "Python installation started...."
{
  export LC_ALL=C
  sudo apt-get install python-pip -y
  sudo add-apt-repository ppa:deadsnakes/ppa
  sudo apt-get update
  sudo apt-get install python3.7 -y
  sudo apt-get install libpq-dev
  sudo apt-get install python3.7-dev
	echo "Python Installed"
} || {
	echo "Python installation failed"
}

echo "Pipenv installation started..."
{ 
	pip install pipenv
	echo "Pipenv installed"
} || {
	echo "Pipenv installation failed"
}

echo "Server dependencies installation started..."
  pipenv run pipenv install -r  requirements.txt
  cd favourite_things_api && pipenv run python manage.py migrate && pipenv run python manage.py loaddata category_fixtures.json
echo "Server dependencies installed"

echo "Gunicorn starting"
{  
  gunicorn --bind 0.0.0.0:8000 favourite_things_api.wsgi:application --daemon && cd -
  echo "Gunicorn started...."
} || {
  echo "Gunicorn not started"
}


echo "Nodejs installation started...."
{   
    sudo apt-get install curl
	curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
    sudo apt-get install nodejs
	echo "Node installed"
} || {
	echo "Nodejs installation failed"
}

echo "Client dependencies installation started..."
{
cd favourite-things-client && npm install && cd -
echo "Client dependencies installed"
} || {
    echo "Client dependencies installation failed"
}

echo "Client build started...."
{
cd favourite-things-client && npm run build && cd -
echo "Client built"
} || {
    echo "Client build failed"
}


echo "Nginx installation started...."
sudo apt-get install nginx -y
sudo touch /etc/nginx/sites-available/django.conf
sudo cp django.conf /etc/nginx/sites-available/django.conf
sudo ln -s /etc/nginx/sites-available/django.conf /etc/nginx/sites-enabled/django.conf
sudo nginx -t
sudo service nginx restart
echo "Nginx started and Deployment Successful"
} || {
    echo "Deployment failed"
}

