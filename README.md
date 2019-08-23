[![CircleCI](https://circleci.com/gh/OKiMaureen/favorite-things.svg?style=svg)](https://circleci.com/gh/OKiMaureen/favorite-things)

# About Favourite Things
This application is to enable users create favourite things of their choice under different categories. Favourite things created can be updated or deleted. Favourite things created also have logs which keep track of changes made on them. A user can also create a category aprt from the default categories.

## API Endpoints

<table>
<tr><th>HTTP VERB</th><th>ENDPOINT</th><th>FUNCTIONALITY</th></tr>

<tr><td>POST</td> <td>/api/v1/category</td>  <td>Creates  a new category</td></tr>

<tr><td>GET</td> <td>/api/v1/category</td>  <td>Gets all categories created</td></tr>

<tr><td>GET</td> <td>/api/v1/category/:categoryId</td>  <td>Gets a single category and it's favourite things</td></tr>

<tr><td>POST</td> <td>/api/v1/favourite</td>  <td>Creates a favourite thing</td></tr>

<tr><td>GET</td> <td>/api/v1/favourite</td> <td> Gets all favourite things created</td></tr>

<tr><td>PUT</td> <td>/api/v1/favourite/:favouriteId</td> <td>Modify a favourite thing</td></tr>

<tr><td>DELETE</td> <td>/api/v1/favourite</td> <td>Delete a favourite thing</td></tr>

<tr><td>GET</td> <td>/api/v1/favourite/:favouriteId/logs</td> <td>Gets the audit logs of a favourite thing</td></tr>

</table>

## Frontend Coding Style
* Airbnb style guide. 

## Features
 * Users can create a category
 * Users can view all favourite things
 * Users can create a favourite thing
 * Users can update a favourite thing
 * Users can delete a favourite thing
 * Users can view all favourite things created
 * Users can rank favourites things created under a category
 * Users can view all favourite things under a category
 * Users can view the logs of a favourite thing
 * Users can view the details of a favourite thing

# Project Setup
##  Installation
Install the following:
- [Python 3.7](https://www.python.org/downloads/release/python-374/)
- [Pipenv](https://pypi.org/project/pipenv/)
- [Postgres](https://www.postgresql.org/download/)
- [Node](https://nodejs.org/en/)


* **Clone repository:** 
```
git clone https://github.com/OKiMaureen/favorite-things.git
```

Follow the following steps to set up the API  locally
* install the dependences using the command below
```
pipenv install
```
* Create env.sh file, copy sample database url in env.sample and replace with your variables in curly brackets with your credentials.

* Run the migrations using the command below
```
python manage.py migrate
```
* Load default categories using the command below
```
python manage.py loaddata category_fixture.json
```
* Start the API application using the command below
```
python manage.py runserver
```
* Run tests using the command below
```
python manage.py test
```

## Frontend Application
Follow the following steps to set up the Frontend locally

* Navigate to the favourite-things-client directory
* install the dependences using the command below
```
npm install
```

* Start vue application using the command below
```
npm run serve
```

## Automated AWS Deployment
- Create or log into an aws account
- Set up and launch instance using UBUNTU Server 16.04 LTS
- Navigate to directory where instance key-pair is located
- SSH to “PUBLIC_DNS” obtained from created instance using the command below
```
ssh -i {key-pair file name}ubuntu@PUBLIC_DNS
```
- Update the rules in the security group of your EC2 instance

Inbound rules section
- Type: HTTP, Port Range: 80
- Type: Custom TCP Rule, Port Range: 8000
- On your created ubuntu instance type the following commands
```
sudo apt-get update && apt-get upgrade -y
```
- Install the PostgreSQL using the following command
  
```
sudo apt-get install postgresql postgresql-contrib
```
- Clone the repository as given above
- Create a database user and database
   NB: make the user created a super user in other to access hstore.
- Create a env.sh file in the favourite_things_api folder in the root directory.
- Populate the created env.sh file with your DATABASE_URL credentials using the sample provided in 'env.sample' file in the root folder
- Source the env.sh file using the command below
```
source env.sh
```
- Navigate to django.conf file in the root folder and open the file using the command below
```
sudo nano django.conf
```
- Replace the {{Public DNS}} with the public dns of your instance and close file

-  On the root folder, Set file permission using the command below
```
sudo chmod +x {key-pair file name}
```

Run the deployment script using the command below
```
./deploy.sh
```
- Accept all prompts in the process of deployment script running.

- When prompted with 'Deployment Succesful', Your EC2 instance is ready and you can visit the deployed app using your address.

## Application Hosted on
- AWS

## Author
- Maureen Okafor

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

