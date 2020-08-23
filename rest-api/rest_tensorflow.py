import os
import tempfile

import joblib
import numpy as np
import tensorflow as tf

from flask import Flask
from flask import request
from flask import jsonify

# -- Activate GPU memory growth
gpu_devices = tf.config.experimental.list_physical_devices('GPU')
for device in gpu_devices:
    tf.config.experimental.set_memory_growth(device, True)

# --- Objects
app = Flask(__name__)
classifier: tf.keras.models.Model = tf.keras.models.load_model("model/animals")
class_dict = joblib.load("model/animals_dict.joblib")

# --- API routes
@app.route("/predict", methods=["POST"])
def api_predict():
    if "file" not in request.files:
        return jsonify({"message": "Field `file` harus ada."})

    file = request.files["file"]
    save_path = os.path.join(tempfile.gettempdir(), next(tempfile._get_candidate_names()) + ".jpg")
    file.save(save_path)

    img = tf.keras.preprocessing.image.load_img(save_path, target_size=(150, 150))
    img = tf.keras.preprocessing.image.img_to_array(img)
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    pred = classifier.predict(img)
    pred = np.argmax(pred, axis=1)[0]

    return jsonify({"predicted": class_dict[pred]})

@app.route("/")
def index():
    return "Hello!"

# --- App entry point
if __name__ == "__main__":
    app.run(debug=True, port=3002)
