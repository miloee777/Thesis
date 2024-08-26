from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
import base64

app = Flask(__name__)
CORS(app)  # Allow requests from your Vue.js frontend


ROBOFLOW_API_KEY = 'UhmFJgFYw4Cvq3ZkaFej'
ROBOFLOW_MODEL_ID = 'weeddetecttion'
ROBOFLOW_VERSION = '2'  # หรือเวอร์ชันที่คุณใช้งานอยู่
ROBOFLOW_MODEL_URL = 'https://detect.roboflow.com/weeddetecttion/1?api_key=UhmFJgFYw4Cvq3ZkaFej'

@app.route('/detect', methods=['POST'])
def detect():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    # Send the file to Roboflow
    response = requests.post(
        ROBOFLOW_MODEL_URL,
        files={'file': file.read()}
    )
    
    if response.status_code != 200:
        return jsonify({'error': 'Detection failed'}), response.status_code
    
    result = response.json()

    # ส่งข้อมูล predictions และขนาดของภาพกลับไปยัง frontend
    return jsonify({
        'predictions': result.get('predictions', []),
        'image_width': result['image']['width'],
        'image_height': result['image']['height']
    })

if __name__ == '__main__':
    app.run(debug=True)