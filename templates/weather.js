async function fetchWeatherData() {
    const city = document.getElementById('city').value;
    const apiKey = '1bffeac4e19307fa76afbe3e1af64e11';  
    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

    try {
        const response = await fetch(apiUrl);
        const data = await response.json();

        if (response.ok && data.main) {
            document.getElementById('Temperature').value = data.main.temp + ' °C';
            document.getElementById('Humidity').value = data.main.humidity + ' %';
            document.getElementById('Rainfall').value = (data.rain && data.rain['1h']) ? data.rain['1h'] + ' mm' : '0 mm';

            
            document.getElementById('submit').disabled = false;
        } else {
            displayError('Failed to fetch weather data. Please check the city name.');
        }
    } catch (error) {
        console.error('Error fetching weather data:', error);
        displayError('An error occurred while fetching weather data.');
    }
}

function displayError(message) {
    const errorDiv = document.getElementById('error-message');
    if (errorDiv) {
        errorDiv.textContent = message;
    } else {
        const newErrorDiv = document.createElement('div');
        newErrorDiv.id = 'error-message';
        newErrorDiv.style.color = 'red';
        newErrorDiv.textContent = message;
        document.body.appendChild(newErrorDiv);
    }
}

document.querySelector('form').addEventListener('submit', function(event) {
    
});

document.getElementById('city').addEventListener('change', fetchWeatherData);


document.getElementById('submit').disabled = true;
