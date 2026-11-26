
from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Memuat model Decision Tree
model = joblib.load("model_kelulusan.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None

    if request.method == "POST":
        g1 = int(request.form["g1"])
        g2 = int(request.form["g2"])
        studytime = int(request.form["studytime"])
        failures = int(request.form["failures"])
        absences = int(request.form["absences"])

        data = pd.DataFrame([{
            "G1": g1,
            "G2": g2,
            "studytime": studytime,
            "failures": failures,
            "absences": absences
        }])

        hasil = model.predict(data)[0]

    return render_template("index.html", hasil=hasil)

if __name__ == "__main__":
    app.run(debug=True)
