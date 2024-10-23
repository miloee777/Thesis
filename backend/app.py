from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
import base64

app = Flask(__name__)
CORS(app)  


ROBOFLOW_API_KEY = 'kBv3Mms6A8C2LF8V5gsX'
ROBOFLOW_MODEL_ID = 'weeddetection-abvxw'
ROBOFLOW_VERSION = '13'  
ROBOFLOW_MODEL_URL = 'https://detect.roboflow.com/weeddetection-abvxw/13?api_key=kBv3Mms6A8C2LF8V5gsX'

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

    
    print(f"Image width: {result['image']['width']}")
    print(f"Image height: {result['image']['height']}")

    predictions = result.get('predictions', [])
    for prediction in predictions:
        class_name = prediction.get('class')
        confidence = prediction.get('confidence')
        x = prediction.get('x')
        y = prediction.get('y')
        width = prediction.get('width')
        height = prediction.get('height')

        # Print all the details
        print(f"Detected {class_name} with confidence {confidence:.2%}")
        print(f"Position: (X: {x}, Y: {y}), Bounding Box: (Width: {width}, Height: {height})")

    # ส่งข้อมูล predictions และขนาดของภาพกลับไปยัง frontend
    return jsonify({
        'predictions': result.get('predictions', []),
        'image_width': result['image']['width'],
        'image_height': result['image']['height']
    })

if __name__ == '__main__':
    app.run(debug=True)

    #update