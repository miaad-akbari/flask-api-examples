### 1. Clone the Repository
```bash
git clone https://github.com/your_username/flask-task-manager.git
cd flask-task-manager
```


###  2. Set Up Python Environment

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

###  3. Install dependencies:
```bash
pip install -r requirements.txt
```

###  4. Run Locally

Initialize and migrate the database:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

###  5. Start the server:
```bash
flask run 
```
###  6. Docker Deployment
Build and Run Docker Image

Build the image:
```bash
docker build -t your_dockerhub_username/flask-task-manager:latest .
```
Run the container:
```bash
docker run  -d -p 5000:5000 your_dockerhub_username/flask-task-manager:latest
```
Push Image to Docker Hub

Tag and push the image:
```bash
docker tag your_dockerhub_username/flask-task-manager:latest
docker push your_dockerhub_username/flask-task-manager:latest
```

###  7. Kubernetes Deployment
Apply Kubernetes Configuration
```bash
kubectl apply -f deployment.yaml
```
Access the Application

Use port-forwarding to access the app:
```bash
kubectl port-forward pod/<pod_name> 5000:5000
```
Verify Deployment
```bash 
kubectl get pods
kubectl get svc
```