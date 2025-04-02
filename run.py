from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import cv2

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///parking.db'
db = SQLAlchemy(app)

# Database model for parking slots
class ParkingSlot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_occupied = db.Column(db.Boolean, default=False)

@app.route('/')
def home():
    return render_template('dashboard.html')  # Ensure the template name matches the new file

@app.route('/detect', methods=['POST'])
def detect_vehicle():
    # Simulate vehicle detection using OpenCV
    # ...existing code for image processing...
    image = request.files['image']
    # Process the image using OpenCV
    # ...existing code...
    return jsonify({"message": "Vehicle detected", "status": "success"})

@app.route('/slots', methods=['GET', 'POST'])
def manage_slots():
    if request.method == 'GET':
        slots = ParkingSlot.query.all()
        return jsonify([{"id": slot.id, "is_occupied": slot.is_occupied} for slot in slots])
    elif request.method == 'POST':
        # Add a new parking slot
        new_slot = ParkingSlot()
        db.session.add(new_slot)
        db.session.commit()
        return jsonify({"message": "New slot added", "id": new_slot.id})

@app.route('/slots-ui', methods=['GET'])
def slots_ui():
    slots = ParkingSlot.query.all()
    return render_template('slots.html', slots=slots)  # Ensure the template name matches the new file

@app.route('/basement')
def basement():
    return render_template('basement.html')  # Ensure the template name matches the new file

@app.route('/first-floor')
def first_floor():
    return render_template('first_floor.html')  # Ensure the template name matches the new file

if __name__ == '__main__':
    with app.app_context():  # Ensure the application context is active
        db.create_all()  # Initialize the database
    app.run(debug=True)
