from flask import Flask, render_template, request
import pandas as pd
import joblib
import model

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index', methods=['POST'])
def predict_role():
    # Retrieve form data
    name = request.form.get('name', '').strip()
    runs = request.form.get('runs', None)
    batting_avg = request.form.get('batting_avg', None)
    wickets = request.form.get('wickets', None)
    bowling_avg = request.form.get('bowling_avg', None)
    economy_rate = request.form.get('economy_rate', None)
    
    predicted_role = None

    try:
        runs = int(runs)
        batting_avg = float(batting_avg)
        wickets = int(wickets)
        bowling_avg = float(bowling_avg)
        economy_rate = float(economy_rate)

        predicted_role = model.predict(runs,batting_avg,bowling_avg,economy_rate,wickets)

    except ValueError:
        predicted_role = "Invalid input. Please provide numerical values where required."

    # Render the result back to the page
    return render_template(
        'index.html', 
        name=name or "Player", 
        predicted_role=predicted_role or "No role predicted"
    )

if __name__ == '__main__':
    app.run(debug=True)
