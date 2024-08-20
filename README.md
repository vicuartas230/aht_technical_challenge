# AHT Technical Test

## 1. Project Description

    The **AHT Technical Test** is a web application used to demostrate the skills as a backend developer utilizing Pyhton, FLask and SQLAlchemy in order to build an application capable of perform CRUD (Create, Read, Update, Delete) operations on a MySQL database.

## 2. Installation Instructions

    - Clone the repository in your local machine.
        ``` bash
        git clone https://github.com/vicuartas230/aht_technical_test.git
    - Enter to the project folder.
        ``` bash
        cd aht_technical_test/
    - Create a file .env to add the database password as a enviroment variable DB_PASSWORD=password
        ``` bash
        DB_PASSWORD=<password> > .env
    - Ensure docker compose is installed
    - Run the command to build the image and exec the container
        ``` bash
        docker compose build
    - Browse the application on a browser with the url http://127.0.0.1:5000

## 3. Technologies

    Flask and Python were used in the project's construction. The MySQL database and the backend were connected via SQLAlchemy. HTML, CSS, JavaScript, and Bootstrap with Jinja2 and JQuery were used to construct some front end features.
