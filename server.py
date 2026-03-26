import os
import io
import numpy as np
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import tensorflow as tf
from PIL import Image

# --- KERAS PATCH (FIX FOR BATCH_SHAPE ERROR) ---
# This block intercepts the InputLayer configuration and renames 'batch_shape' to 'batch_input_shape'
# which is compatible with newer Keras engines. 
from tensorflow.keras.layers import InputLayer
original_from_config = InputLayer.from_config

@classmethod
def patched_from_config(cls, config):
    if 'batch_shape' in config:
        config['batch_input_shape'] = config.pop('batch_shape')
    return original_from_config(config)

InputLayer.from_config = patched_from_config
# --- END OF PATCH ---

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

model = None

# --- 1. MODEL LOADING ---
print("⏳ Initializing AI model loading with Legacy Patch...")
try:
    # We use compile=False to avoid loading training configurations that cause conflicts
    model = tf.keras.models.load_model('inti_check_v5_pro.h5', compile=False)
    print("✅ SUCCESS: Model loaded and patched successfully!")
except Exception as e:
    print(f"🚨 CRITICAL ERROR: Could not load model even with patch. {e}")

# --- 2. KNOWLEDGE BASE ---
KNOWLEDGE_BASE = {
    0: {
        "category": "Fungal Skin Infection / Candidiasis",
        "description": "Analysis suggests a fungal infection (itchy, red, or scaly patches).",
        "first_aid": "Keep the area dry. Use separate towels. Avoid steroids.",
        "specialist": "👨‍⚕️ Dermatologist"
    },
    1: {
        "category": "Nail Pathology",
        "description": "Indicates potential fungus, onycholysis, or nail damage.",
        "first_aid": "Avoid nail polish. Disinfect footwear. Dry feet thoroughly.",
        "specialist": "👨‍⚕️ Podiatrist or Dermatologist"
    },
    2: {
        "category": "Pigmented Lesion (Mole / Suspicious)",
        "description": "Classified as a pigmented lesion. Requires clinical monitoring.",
        "first_aid": "Do not scratch. Protect from UV. Document changes.",
        "specialist": "🚨 Urgent: Dermatologist / Oncologist"
    },
    3: {
        "category": "Suspected Viral Infection (e.g., Herpes, HPV)",
        "description": "Resembles viral blisters or warts; may be contagious.",
        "first_aid": "Do not pop blisters. Wash hands. Wear loose cotton.",
        "specialist": "👨‍⚕️ Venereologist or Gynecologist"
    },
    4: {
        "category": "Ectoparasites (Scabies / Bites)",
        "description": "Suggests insect bites or a potential scabies infestation.",
        "first_aid": "Avoid scratching. Wash bedding at 60°C.",
        "specialist": "👨‍⚕️ GP or Dermatologist"
    },
    5: {
        "category": "Acne / Inflammatory Lesions",
        "description": "Classified as acne or hair follicle inflammation.",
        "first_aid": "Do not squeeze; use gentle, non-comedogenic cleansers.",
        "specialist": "👨‍⚕️ Dermatologist"
    }
}

# --- 3. API ROUTES ---
@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    global model
    if model is None:
        return jsonify({"error": "Model not initialized"}), 500

    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400
    
    file = request.files['image']
    try:
        img_raw = Image.open(io.BytesIO(file.read()))
        img = img_raw.convert('RGB').resize((224, 224))
        
        img_array = np.array(img).astype('float32') / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        
        prediction = model.predict(img_array)
        top_class_index = int(np.argmax(prediction))
        confidence = float(np.max(prediction)) * 100
        
        result = KNOWLEDGE_BASE[top_class_index].copy()
        result['confidence'] = round(confidence, 1)
        
        return jsonify(result)
    except Exception as e:
        print(f"Prediction Error: {e}")
        return jsonify({"error": "Processing error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)