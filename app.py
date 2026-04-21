from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load model & preprocessor
with open("artifacts/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("artifacts/preprocessor.pkl", "rb") as f:
    preprocessor = pickle.load(f)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    # Get form data
    data = {
        "gender": request.form["gender"],
        "race/ethnicity": request.form["race"],
        "parental level of education": request.form["education"],
        "lunch": request.form["lunch"],
        "test preparation course": request.form["prep"]
    }

    # Convert to DataFrame
    sample = pd.DataFrame([data])

    # Preprocess
    processed = preprocessor.transform(sample)
    processed = processed.toarray() if hasattr(processed, "toarray") else processed

    # Predict
    prediction = model.predict(processed)[0]

    return render_template("index.html", prediction=round(prediction, 2))


if __name__ == "__main__":
    app.run(debug=True)