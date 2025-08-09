import os
import io
import numpy as np
from flask import Flask, render_template, request, jsonify
from PIL import Image
import tensorflow as tf

app = Flask(__name__)

# --- We must load the model at the module level so Gunicorn can find it ---
model = None

def load_model():
    """Loads the pre-trained model from the file system."""
    global model
    # Get the directory of the current script (main.py)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(script_dir, 'saved_models', 'final_model_for_deployment.keras')
    model = tf.keras.models.load_model(model_path)
    print("Model loaded successfully!")

# Call the function here, outside of any conditional blocks
load_model()

# A quick utility function for preprocessing
def preprocess_image(image_bytes):
    """Preprocesses an uploaded image to match the model's input size and format."""
    image = Image.open(io.BytesIO(image_bytes))
    image = image.resize((224, 224))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        image_bytes = file.read()
        if model:
            processed_image = preprocess_image(image_bytes)
            # Make a prediction with the model 

            prediction = model.predict(processed_image)
            predicted_class = np.argmax(prediction)
            return jsonify({'diagnosis': int(predicted_class)})
        else:
            return jsonify({'error': 'Model not loaded'}), 500

if __name__ == '__main__':
    pass