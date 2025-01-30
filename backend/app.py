from flask import Flask, jsonify
from db import db
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)

# Route to test MongoDB connection
@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/connect', methods=['GET'])
def connect_db():
    try:
        # Check if MongoDB is connected
        db_status = db.is_connected()
        if db_status:
            return jsonify({"message": "MongoDB connected successfully!"}), 200
        else:
            return jsonify({"message": "Failed to connect to MongoDB"}), 500
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
