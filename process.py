from flask import Flask, request, jsonify, send_from_directory
from PIL import Image
import os, random, datetime

app = Flask(__name__)
UPLOAD_FOLDER = 'assets'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/process', methods=['POST'])
def process_image():
    image = request.files['image']
    filename = image.filename
    path = os.path.join(UPLOAD_FOLDER, filename)
    image.save(path)

    # Convert to grayscale as a dummy processing
    img = Image.open(path).convert('L')
    processed_filename = 'processed_' + filename
    processed_path = os.path.join(UPLOAD_FOLDER, processed_filename)
    img.save(processed_path)

    # Generate random analysis data to simulate real output
    urban_area = round(random.uniform(200, 500), 2)
    green_loss = round(random.uniform(5, 30), 2)
    growth_rate = round(random.uniform(3, 12), 2)
    zones = random.sample(
        ['Central Zone', 'East Expansion', 'North Suburb', 'Tech Corridor', 'Industrial Belt', 'Green Ring'],
        k=3
    )

    # Current date and time for timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    analysis = {
        'image_url': f'/assets/{processed_filename}',
        'urban_area': urban_area,
        'green_loss': green_loss,
        'growth_rate': growth_rate,
        'zones': zones,
        'timestamp': timestamp
    }

    return jsonify(analysis)

@app.route('/assets/<filename>')
def serve_image(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
