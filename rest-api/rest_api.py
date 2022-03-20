import os
import tempfile

import joblib
import numpy as np
import tensorflow as tf

from flask import Flask
from flask import request
from flask import jsonify

# --- Create flask app
app = Flask(__name__)

# --- Load model
regressor = joblib.load("model/housing.joblib")
class_dict = joblib.load("model/cifar10_dict.joblib")
classifier = tf.keras.models.load_model("model/cifar10_classify")

# --- API routes
@app.route("/")
def index():
    return "Hello!"

@app.route("/predict_reg", methods=["POST"])
def api_predict_reg():
    if "rm" not in request.form:
        return jsonify({"message": "Field `rm` harus ada."})
    if "lstat" not in request.form:
        return jsonify({"message": "Field `lstat` harus ada."})

    rm = float(request.form["rm"])
    lstat = float(request.form["lstat"])

    result = regressor.predict([[rm, lstat]])

    return jsonify({
            "rm": rm,
            "lstat": lstat,
            "predicted": result[0]
        })

@app.route("/predict_classify", methods=["POST"])
def api_predict_classify():
    if "file" not in request.files:
        return jsonify({"message": "Field `file` harus ada."})

    save_path = os.path.join(tempfile.gettempdir(), "upload.jpg")
    file = request.files["file"]
    file.save(save_path)

    img = tf.keras.preprocessing.image.load_img(save_path, target_size=(32, 32))
    img = tf.keras.preprocessing.image.img_to_array(img)
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    pred = classifier.predict(img)
    pred = np.argmax(pred, axis=1)[0]

    os.remove(save_path)

    return jsonify({"predicted": class_dict[pred]})

# --- App entry point
if __name__ == "__main__":
    app.run(debug=True, port=5000)
