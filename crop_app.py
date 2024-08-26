import joblib
import requests
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


model = joblib.load('crop_app')  


def get_weather_data(city):
    api_key = '1bffeac4e19307fa76afbe3e1af64e11'  
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(api_url)
        data = response.json()
        
        
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        rainfall = data.get('rain', {}).get('1h', 0)  
        
        return temperature, humidity, rainfall
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None, None, None

@app.route('/')
def home():
    return render_template('Home_1.html')

@app.route('/Predict')
def prediction():
    return render_template('Index.html')

@app.route('/form', methods=["POST"])
def brain():
    Nitrogen = float(request.form['Nitrogen'])
    Phosphorus = float(request.form['Phosphorus'])
    Potassium = float(request.form['Potassium'])
    Ph = float(request.form['ph'])

    
    city = request.form.get('city', 'London')  

    
    Temperature, Humidity, Rainfall = get_weather_data(city)

    if Temperature is None or Humidity is None:
        return "Error fetching weather data. Please try again."

    values = [Nitrogen, Phosphorus, Potassium, Temperature, Humidity, Ph, Rainfall]
    
    if 0 < Ph <= 14 and Temperature < 100 and Humidity > 0:
        arr = [values]
        acc = model.predict(arr)
        return render_template('prediction.html', prediction=str(acc))
    else:
        return "Sorry... Error in entered values in the form. Please check the values and fill it again."

if __name__ == '__main__':
    app.run(debug=True)
