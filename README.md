# jattul
Just Another Time Tracking Utility


The server supports CRUD operations for various resources (roles, users, tasks, projects, trackings)
through RESTful APIs like the following:

HTTP Method |	URI                                               | Action
----------- | ------------------------------------------------- | -----------------------
GET         |	http://[hostname]/jattul/api/v1.0/users           | Retrieve list of users
GET	        | http://[hostname]/jattul/api/v1.0/users/[task_id]	| Retrieve a user
POST        | http://[hostname]/jattul/api/v1.0/users           | Create a new user
PUT         | http://[hostname]/jattul/api/v1.0/users/[task_id] | Update an existing user
DELETE      | http://[hostname]/jattul/api/v1.0/users/[task_id] | Delete a user

Also, login (username, password) and logout operations are supported

To install the server, clone the repository and install the dependencies through `pip install -r requirements.txt`
It is advisable, to use [virtual-env](https://virtualenv.pypa.io) before setting up the environment

To run the server, activate the environment (if virtual-env is used) and issue the command `python app.py`.
This will run the server at localhost:5000
