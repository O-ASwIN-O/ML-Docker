from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the model
model = joblib.load("model.pkl")

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ML Iris Predictor</title>
        <style>
            body { background-color: #121212; color: #ffffff; font-family: Arial, sans-serif; margin: 0; padding: 20px; }
            .container { max-width: 600px; margin: 0 auto; }
            h1 { text-align: center; color: #bb86fc; }
            form { background-color: #1e1e1e; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.5); }
            label { display: block; margin-bottom: 8px; }
            input { width: 100%; padding: 10px; margin-bottom: 15px; border: 1px solid #333; border-radius: 4px; background-color: #2c2c2c; color: #ffffff; }
            button { background-color: #bb86fc; color: #000; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; width: 100%; }
            button:hover { background-color: #9c4dcc; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Iris Flower Predictor</h1>
            <form action="/predict" method="post">
                <label for="sepal_length">Sepal Length (cm):</label>
                <input type="number" step="0.1" id="sepal_length" name="sepal_length" required>
                <label for="sepal_width">Sepal Width (cm):</label>
                <input type="number" step="0.1" id="sepal_width" name="sepal_width" required>
                <label for="petal_length">Petal Length (cm):</label>
                <input type="number" step="0.1" id="petal_length" name="petal_length" required>
                <label for="petal_width">Petal Width (cm):</label>
                <input type="number" step="0.1" id="petal_width" name="petal_width" required>
                <button type="submit">Predict</button>
            </form>
        </div>
    </body>
    </html>
    """

@app.route('/predict', methods=['POST'])
def predict():
    if request.is_json:
        data = request.get_json()
        features = np.array(data['features']).reshape(1, -1)
    else:
        # Form data
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])
        features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    
    prediction = model.predict(features)
    class_names = ['Setosa', 'Versicolor', 'Virginica']
    result = class_names[int(prediction[0])]
    
    if request.is_json:
        return jsonify({'prediction': int(prediction[0]), 'class': result})
    else:
        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Prediction Result</title>
            <style>
                body {{ background-color: #121212; color: #ffffff; font-family: Arial, sans-serif; margin: 0; padding: 20px; text-align: center; }}
                .container {{ max-width: 600px; margin: 0 auto; }}
                h1 {{ color: #bb86fc; }}
                .result {{ background-color: #2e7d32; padding: 20px; border-radius: 8px; margin-top: 20px; }}
                a {{ color: #bb86fc; text-decoration: none; }}
                a:hover {{ text-decoration: underline; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Prediction Result</h1>
                <div class="result">
                    <h2>Predicted Class: {result}</h2>
                    <p>Class ID: {int(prediction[0])}</p>
                </div>
                <p><a href="/">Predict Another</a></p>
            </div>
        </body>
        </html>
        """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)