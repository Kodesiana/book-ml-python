import os
import requests
import tempfile
import base64

from flask import Flask
from flask import request
from flask import render_template

# --- Objects
app = Flask(__name__)

# --- API routes
@app.route("/predict-house", methods=["POST"])
def predict_house():
    body = { 'rm': request.form["ruangan"] }
    result = requests.post("http://localhost:3001/predict", data=body)

    response = result.json()
    return render_template('hasil.html', hasil=response["predicted"])
    

@app.route("/predict-animals", methods=["POST"])
def predict_animals():
    file = request.files["file"]
    save_path = os.path.join(tempfile.gettempdir(), file.filename)
    file.save(save_path)

    body = { 'file': ('image.jpg', open(save_path, 'rb')) }
    result = requests.post("http://localhost:3002/predict", files=body)

    with open(save_path, "rb") as img_file:
        image_data = "data:image/jpg;base64," + base64.b64encode(img_file.read()).decode('utf-8')

    response = result.json()
    return render_template('hasil.html', hasil=response["predicted"], img=image_data)

@app.route("/")
def index():
    return render_template('home.html')


# --- App entry point
if __name__ == "__main__":
    app.run(debug=True, port=5000)