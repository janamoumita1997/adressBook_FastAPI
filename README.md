# Adress_Book_FastAPI

This repository contains Create-Read-Update-Delete(CRUD) operation using FastAPI for an dummy adress book.

# Swagger UI

Fast API provides an interactive API that’s brought to us by swagger UI.
To see it in action, add `/docs#` to the end of the URL we set for our first route.

![image](https://user-images.githubusercontent.com/81233305/173826805-40903ca3-f121-4a7e-9df3-6146c33bdc86.png)


# Recap:
````
1. POST:Adding data
2. PUT:Updating Data
3. Delete: Deleting data(as name suggest ,ha  !)
````


# Requirements:
````
1. Python>=3.6
2. pydantic
3. Fastapi
4. sqlalchemy
5. sqlite
6. uvicorn 
````

# Quick Guide:
To run this repo:

````
$uvicorn main:app --reload
````

# In-Depth Description
The folder structure is as follows:
````
CRUD
|---database.py
|---main.py
|---models.py
|---schemas.py
|---todo.db
````

1. database.py: creates database engine and to establish a connection.

2. models.py: Once the database connectuon is configured, a database ````models```` has to be created to represent our db tables

3. schemas.py: nothing but contains only the type of each attribute/column whichever specified in models.py.

4. main.py: main file to run create-read-update-delete operations.

