from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    status = db.Column(db.String(20), nullable=False, default="pending")
    due_date = db.Column(db.String(10), nullable=True)

# Create Task - POST /tasks
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if 'title' not in data or 'status' not in data:
        abort(400, description="Missing required fields")
    new_task = Task(
        title=data['title'],
        description=data.get('description'),
        status=data['status'],
        due_date=data.get('due_date')
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.id), 201

# Retrieve All Tasks - GET /tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

# Retrieve Single Task - GET /tasks/<id>
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.query.get_or_404(id)
    return jsonify(task.to_dict())

# Update Task - PUT /tasks/<id>
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get_or_404(id)
    data = request.get_json()
    for key in ('title', 'description', 'status', 'due_date'):
        if key in data:
            setattr(task, key, data[key])
    db.session.commit()
    return jsonify(task.to_dict())

# Delete Task - DELETE /tasks/<id>
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return '', 204

# Utility function to convert task objects to dictionary
def to_dict(self):
    return {
        'id': self.id,
        'title': self.title,
        'description': self.description,
        'status': self.status,
        'due_date': self.due_date
    }

Task.to_dict = to_dict

if __name__ == '__main__':
    app.run(debug=True)
