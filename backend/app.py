import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from emotion_detection import detect_emotion  # Your emotion detection model function
from spotipy_handler import get_songs_by_mood
from pymongo import MongoClient

MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')

client = MongoClient(MONGO_URI)
db = client['M4']  
signup_collection = db['signup']
contact_collection = db['contactus']

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.json
    email = data.get('email')
    
    if not email:
        return jsonify({'error': 'Email is required'}), 400
    
    signup_collection.insert_one({'email': email})
    
    return jsonify({'message': 'Signup successful'}), 200

@app.route('/api/contactus', methods=['POST'])
def contactus():
    data = request.json
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')
    phone_number = data.get('phone')
    message = data.get('message')

    if not email or not message:
        return jsonify({'error': 'Email and message are required'}), 400

    contact_collection.insert_one({'first_name': first_name, 'last_name': last_name, 'email': email, 'phone': phone_number, 'message': message})

    return jsonify({'message': 'Contact form submitted successfully'}), 200
    
    

@app.route('/api/detect-emotion', methods=['POST'])
def detect_emotion_route():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']
    try:
        emotion = detect_emotion(image_file)
        return jsonify({'emotion': emotion})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/recommend-songs', methods=['POST'])
def recommend_songs_route():
    data = request.json
    mood = data['mood']
    songs = get_songs_by_mood(mood)  # Call your Spotify handler function
    return jsonify({'songs': songs})

if __name__ == '__main__':
    app.run(debug=True)
