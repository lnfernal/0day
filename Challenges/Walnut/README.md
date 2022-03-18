# Using Flask

In order to run flask:
```bash
export FLASK_APP=hello.py
flask run
```

We will use pipenv to setup the virtual environment
```bash
pipenv --three
pipenv install flask
```
This creates the virtual environment, where all our dependencies will be installed, and the third command will add Flask as our first dependency. If we check our project's directory,
we will see that two files are created after executing these commands.<br><br>
this creates two files after executing the command:
1. Pipfile, a file that contains details about our project, like the Python version that we are using and the packages that our project needs.
2. Pipenv.lock, a file that contains exactly what version of each package our project depends on, and its transitive dependencies

In order to create a Python application, we just need to create a folder and add an empty file called __init__.py to it.<br>
In the root directory, create bootstrap.sh. This file will facilitate the start up of our application.
```bash
#!/bin/sh

export FLASK_APP=./cashman/index.py
source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0
```

After building our endpoints (refer to cashman/index.php) with the '/incomes' endpoint which shows our current incomes and the '/incomes' POST request endpoint which allows us to add new incomes. We can query the endpoint using curl
```bash
curl 'http://127.0.0.1:5000/incomes'
[{"amount":5000,"description":"salary"}]
```
And POST request
```bash
curl -X POST -H "Content-Type: application/json" -d '{"description":"lottery","amount":1000}' 'http://127.0.0.1:5000/incomes'
[{"amount":5000,"description":"salary"},{"amount":1000,"description":"lottery"}]
```

## Mapping Models with Python Classes
Most of the times, dictionaries are enough. However, for more complex applications that deal with entities and have multiple businesses rules and validation, we might need to encapsulate our data into Python classes.<br>
The first thing we will do is create a submodule to hold all our entities. Create a directory called model inside cashman module and add an empty filew called __init__.py.
```bash
# create model directory inside teh cashman module
mkdir -p cashman/model

# initialize it as a module
touch cashman/model/__init__.py

```

### Mapping a Python Superclass
We will create three classes: Transactions, Income, Expense. The first class will be the base for the two others, and we will call it Transactions. This python script is located in cashman/model/transactions.py<br>
TransactionSchema is used to deserialize and serialize instances of Transaciton from and to JSON objects. This class inherits from another superclass called Schema that is defined on a package yet to be installed.
```bash
# installing marchmallow as project dependency
pipenv install marshmallow
```
marshmallow is a popular Python package for converting complex datatypes, such as objects, to and from native Python datatypes. We can use this package to fvalidate, serialize, and deserialize data.<br>

## Dockerizing Flask Applications
If we are to deploy our API into the cloud, we are going to need to create a Dockerfile to describe what is needed to run the application on a Docker container. This is, in the future, we will also install Docker and run our program on environments like production and staging.<br>
Create the Dockerfile in the root directory of our project. This is located in Dockerfile.<br>
To create and run a Docker container based on the Dockerfile that we created, we can execute the following commands:
```bash
# build the image
docker built -t cashman .

# run a new docker container named cashman
docker run --name cashman -d -p 5000:5000 cashman

# fetch incomes from the dockerized instance
curl http://localhost:5000/incomes/
```
