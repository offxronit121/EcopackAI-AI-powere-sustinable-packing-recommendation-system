from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)

#  Model paths 
COST_MODEL_PATH = os.path.join("models", "cost_model.pkl")
CO2_MODEL_PATH = os.path.join("models", "co2_model.pkl")

# Load models
cost_model = joblib.load(COST_MODEL_PATH)
co2_model = joblib.load(CO2_MODEL_PATH)

@app.route("/")
def home():
    return " EcoPackAI Backend Running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    input_df = pd.DataFrame([data])

    predicted_cost = cost_model.predict(input_df)[0]
    predicted_co2 = co2_model.predict(input_df)[0]

    return jsonify({
        "predicted_cost": float(predicted_cost),
        "predicted_co2": float(predicted_co2)
    })

if __name__ == "__main__":
    app.run(debug=True)
