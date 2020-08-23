import joblib

from sklearn.linear_model import LinearRegression

from flask import Flask
from flask import request
from flask import jsonify

# --- Objects
app = Flask(__name__)
regressor: LinearRegression = joblib.load("model/housing.joblib")

# --- API routes
@app.route("/predict", methods=["POST"])
def api_predict():
    if "rm" not in request.form:
        return jsonify({"message": "Field `rm` harus ada."})

    rm = float(request.form["rm"])

    result = regressor.predict([[rm]])
    result = result[0]

    return jsonify({
            "rm": rm,
            "predicted": result
        })

@app.route("/")
def index():
    return "Hello!"

# --- App entry point
if __name__ == "__main__":
    app.run(debug=True, port=3001)
