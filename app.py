from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

bundle = pickle.load(open("crop_model.pkl", "rb"))
model = bundle["model"]
num_to_crop = bundle["num_to_crop"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    N = float(request.form["N"])
    P = float(request.form["P"])
    K = float(request.form["K"])
    temp = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    ph = float(request.form["ph"])
    rainfall = float(request.form["rainfall"])

    features = np.array([[N, P, K, temp, humidity, ph, rainfall]])

    pred_num = model.predict(features)[0]
    crop_name = num_to_crop[pred_num]

    return render_template("index.html", result=f"Recommended Crop: {crop_name}")

if __name__ == "__main__":
    app.run(debug=True)
