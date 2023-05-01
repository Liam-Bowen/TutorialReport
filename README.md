# TutorialReport
First you will need to make sure you have python3, pip, virtualenv, and MongoDB installed through your terminal. 

Then you will need to create a virtualenv for your project by calling the command 'virtualenv -p python3 env', and then activate the env by writing 'env/bin/activate'.

In your env, you need to install flask, pymongo, and passlib in order to run your code.

You will need to then create files in your project called templates, static, and user. The templates file will hold your html files that you create. Static will have two files in it called css and js which hold your css code and js code respectively. The user folder will hold more .py files including __init__.py, routes.py, and models.py.

The html files are the templates for each of your pages, and the css and js files are used to style and script the pages. 

In your main branch, you will need to import Flask, render_template, session, and redirect from flask, wraps from functools, pymongo, and routes from user in order to run your code.

In routes.py you need to import Flask from flask, User from user.models where User is the user session you create, and app from main where app is what you initialize as your Flask app in main.

In models.py you will need to import Flask, jsonify, request, session, and redirect from flask, db from main where db is a variable you initialized for your database, uuid to help create unique ids for users, and pbkdf2_sha256 from passlib.hash to encrypt the password of users.

In order to run a flask session of your code, enter the following into your terminal: FLASK_APP=main.py FLASK_ENV=development flask run
This will create a session and generate a link. The link will take you to your session and you will be able to see your progress and test your code.
