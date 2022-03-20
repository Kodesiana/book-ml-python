import joblib

from flask import Flask
from flask import request
from flask import jsonify

# --- Create flask app
app = Flask(__name__)

# --- Load model
regressor = joblib.load("model/housing.joblib")

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

# --- App entry point
if __name__ == "__main__":
    app.run(debug=True, port=3001)
