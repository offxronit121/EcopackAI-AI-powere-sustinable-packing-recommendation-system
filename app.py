from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

cost_model = joblib.load("D:\EcoPack AI\models\cost_model.pkl")
co2_model = joblib.load("D:\EcoPack AI\models\co2_model.pkl")

def strength_to_encoded(mpa):
    if mpa < 20:
        return 0
    elif mpa < 50:
        return 1
    else:
        return 2

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    df = pd.DataFrame([data])

    if "strength_mpa" in df.columns and "cost_inr_per_kg" in df.columns:
        df["cost_efficiency_index"] = df["strength_mpa"] / df["cost_inr_per_kg"]
        df["strength_encoded"] = df["strength_mpa"].apply(strength_to_encoded)

    required_cols = list(cost_model.feature_names_in_)
    X = df.reindex(columns=required_cols, fill_value=0)

    X = X.replace([np.inf, -np.inf], 0)

    predicted_cost = cost_model.predict(X)[0]
    predicted_co2 = co2_model.predict(X)[0]

    return jsonify({
        "predicted_cost": float(predicted_cost),
        "predicted_co2": float(predicted_co2)
    })

if __name__ == "__main__":
    app.run(debug=True)
