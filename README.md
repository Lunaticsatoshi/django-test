<p align="center">
  <h2 align="center">Django Pricing API</h2>

  <p align="center">
    A base template for a simple Django based backend API
  </p>  
</p>

## Features

* [x] Get Pricing
* [x] Create Pricing config

### 🏗️ Built With

<div>

[<img src="https://img.shields.io/badge/-Python-306998?style=for-the-badge&labelColor=black&logo=python&logoColor=4b8bbe" >](https://www.python.org/)

[<img src="https://img.shields.io/badge/-Django-092e20?style=for-the-badge&labelColor=black&logo=Django&logoColor=092e20" >](https://www.djangoproject.com/)

</div>

## 🧩 Getting Started

To get a local copy up and running follow these simple steps.

### Clone the repo
1. Clone the repository using the following command

```bash
git clone https://github.com/Lunaticsatoshi/django-test.git
# After cloning, move into the directory having the project files using the change directory command
cd django-test
```

### Starting the development server with docker 🐳 (Recommended)

#### Prerequisites

Make sure you have Docker and docker-compose installed on your machine.

#### Steps to start the server

Adding Docker support soon

<!-- 1. Add environment file .env in server directory with the variables fiven in the .env.example file.
2. Run the following command to build the docker containers in the project directory itself.

      ```sh
      docker-compose -f docker/docker-compose.debug.yml build
      ```
2. Run the following command to run the docker containers in the project directory itself.

      ```sh
      docker-compose -f docker/docker-compose.debug.yml up
      ```

3. Open <http://localhost:8000> to view it in the browser. -->

### Starting the development server without docker 📡

#### Prerequisites

Make sure you have Python installed on your machine.

> **_NOTE:_**
>
>_The project was made with python version 3.10._

1. Create a virtual environment using pipenv where all the required python packages will be installed

```bash
# Use this on Windows
py -m venv env
# Use this on Linux and Mac
python3 -m venv env
```
2. Active venv

```bash
# Windows
env/bin/activate
# Linux and Mac
source ./env/bin/activate
```

3. Install all the project Requirements
```bash
pip install -r requirements.txt
```
-Apply migrations and create your superuser (follow the prompts)

```bash
# create migrations
python manage.py makemigrations

# apply migrations and create your database
python manage.py migrate

# Create a user with manage.py
python manage.py createsuperuser
```


4. Run the development server

```bash
# run django development server
python manage.py runserver
```

## 🔐 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Suggestions and Bug Reports
Since this is an open source project all suggestions, requests and bug reports are always welcomed. If you have any don't forget to leave them in the issues section. But we recommend creating an issue or replying in a comment to let us know what you are working on first that way we don't overwrite each other.