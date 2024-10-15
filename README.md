# Flask Task Manager

## Description
Flask Task Manager is a RESTful API for managing tasks. It supports Create, Read, Update, and Delete (CRUD) operations with a simple interface. The app uses SQLAlchemy for ORM, is containerized using Docker, and can be deployed on Kubernetes.

## Features
- CRUD operations for tasks
- Simple and lightweight Flask application
- SQLite database support (easily switchable to other databases)
- Docker and Kubernetes deployment-ready

## Prerequisites
- Python 3.8+
- Docker
- Kubernetes (Minikube or other Kubernetes cluster)
- Docker Hub account (optional)


## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your_username/flask-task-manager.git
cd flask-task-manager
```

##  Test the API Endpoints

###  1. flask-task-manager:
Use an API client like Postman, or curl from the terminal, to interact with the endpoints.
Add a New Task:
```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"title": "Finish project", "description": "Complete the API project", "status": "pending", "due_date": "2024-12-01"}' \
http://127.0.0.1:5000/tasks
```
Get All Tasks:
```bash
curl http://127.0.0.1:5000/tasks
```
Get a Task by ID:
```bash
curl http://127.0.0.1:5000/tasks/1
```
Update a Task by ID:
```bash
curl -X PUT -H "Content-Type: application/json" \
-d '{"status": "completed"}' \
http://127.0.0.1:5000/tasks/1
```
Delete a Task by ID:
```bash
curl -X DELETE http://127.0.0.1:5000/tasks/1
```

###  2. flask-bookshelf-api:
Create a Book:
```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"title": "Kubernetes in Action", "author": " Marko Lukša", "genre": "Science and technology", "publication_year": 2017}' \
http://127.0.0.1:5000/books
```
Retrieve All Books:
```bash
curl http://127.0.0.1:5000/books
```
Retrieve a Single Book (replace 1 with the book ID):
```bash
curl http://127.0.0.1:5000/books/1
```





# flask-api-examples
