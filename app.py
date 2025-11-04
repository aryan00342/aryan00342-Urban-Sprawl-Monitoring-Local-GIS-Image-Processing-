from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
import random

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Return success response
    return jsonify({'message': 'Image uploaded successfully!', 'path': filepath})

@app.route('/process', methods=['POST'])
def process():
    try:
        # Dummy analysis data
        analysis = {
            'urban_area': round(random.uniform(35, 60), 2),
            'vegetation_area': round(random.uniform(20, 40), 2),
            'water_area': round(random.uniform(5, 15), 2)
        }
        return jsonify(analysis)
    except Exception as e:
        return jsonify({'error': f'Error processing image: {str(e)}'}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
