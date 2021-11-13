# Login-Using-Flask
This project allows the user to login or register using flask, and allocate random courses.

### Description
This project allows the user to login and register into the server and allocates 2-4 random courses to the user.
The passwords are protected using sha1 encryption.
The website provides useful error messages and redirects, making a smooth experience for the user.

### Tech Stacks
1. HTML5 - To build the structure for webpages
2. CSS - To beautify the webpages
3. Javascript - To validate forms
4. Python 3.8 - Scripting Language for Backend
5. Flask - Micro Framework for Backend
6. SQLAlchemy - To connect Backend with a Database
7. MySQL - To store user information
8. Bootstrap-5 - CSS Framework to make responsive webpages

### How to Reproduce
1. Install all the files in a folder.
2. Install pipenv if not installed in the terminal.
3. Install MySQL if not installed.
4. MySQL should have a mydb database, without having any tables named "courses" or "student".
5. Change Line 10 of app.py and write your respective password after root.
6. In the terminal, in the folder having the respective files, write 
   --> pipenv install
   --> pipenv shell
   --> flask run

