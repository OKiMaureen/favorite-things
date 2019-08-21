#!/bin/bash

sudo apt-get update && sudo apt-get upgrade -y

echo "Starting python installation...."
{
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
	pip3 install pipenv
	echo "Pipenv installed :)"
} || {
	echo "Pipenv installation failed"
}

echo "Installing server dependencies"
  pipenv run pipenv install
  pipenv run python manage.py migrate
  pipenv run python manage.py loaddata category_fixtures.json
echo "Dependencies installed and defaults added"

echo "Starting gunicorn"
{
  sudo apt-get install -y supervisor
  sudo touch /etc/supervisor/conf.d/gunicorn.conf
  sudo cp gunicorn.conf /etc/supervisor/conf.d/gunicorn.conf
  sudo mkdir /var/log/gunicorn
  sudo supervisorctl reread 
  sudo supervisorctl update
  echo "gunicorn running"
} || {
  echo "gunicorn not running"
}


echo "Installing nodejs"
{   sudo apt-get install curl
	curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
    sudo apt-get install nodejs
	echo "Node installed :)"
} || {
	echo "Nodejs installation failed"
}

echo "Installing client dependencies"
cd favourite_things_client && npm install && cd -
echo "Dependencies installed :)"

echo "building client"
cd favourite_things_client && npm run build && cd -
echo "client built :)"


echo "Installing Nginx"
cd /etc/nginx/sites-available
sudo cp django.conf /etc/nginx/sites-available/django.conf
sudo nginx -t
sudo service nginx restart

