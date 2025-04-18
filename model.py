from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Load model
        with open('model.pkl', 'rb') as file:
            model = pickle.load(file)

        # Get form data
        passenger_id = float(request.form['Passenger_ID'])
        name = float(request.form['Name'])
        age = float(request.form['Age'])
        gender = float(request.form["Gender"])
        passenger_class = float(request.form["Class"])  # Renamed from 'Class'
        seat = float(request.form['Seat_Type'])
        fare = float(request.form["Fare_Paid"])

        # Prepare data for prediction
        data = np.array([[passenger_id, age, gender, passenger_class, fare, name, seat]])

        # Make prediction
        prediction = model.predict(data)

        # Format prediction output
        prediction_text = f"Survival Prediction: {'Survived' if prediction[0] == 1 else 'Did Not Survive'}"

        return render_template('index.html', prediction_text=prediction_text)

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
