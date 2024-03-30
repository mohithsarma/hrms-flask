HRMS application in Flask 
use .env.example as .env in the folder. 
install pipenv from pip

run pipenv shell to be in the custom env 

run 
```bash
$ flask db init
```
```bash
$ flask db migrate
``` 
```bash
$ flask db upgrade
``` 
now the database is setup to run the app

run
```bash 
$ flask run 
```
the link will be in the terminal which is 
hardcoded to http://127.0.0.1:5000 in settings.py

Thank you for taking the time to view my project. 
Feedback is always welcome.

- klkmohith00@gmail.com 