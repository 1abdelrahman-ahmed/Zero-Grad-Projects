# ☀️ Weather App

A Python application that fetches and displays current weather data for any city using the OpenWeatherMap API.

---

## 📋 Project Description

### 🔹 First: User Input

- The user enters a city name
- The app validates the city name exists

### 🔹 Second: API Request

- Makes a request to OpenWeatherMap API
- Handles API responses (success/error cases)
- Processes JSON weather data

### 🔹 Finally: Display Results

- Shows cleanly formatted weather data including:
  - Temperature 🌡️
  - Humidity 💧
  - Pressure 🏗️
  - And other metrics

---

## ▶️ How to Run

1. First install dependencies:
```bash
pip install requests
```

2. Then run the app:
```bash
python weather_app.py
```

---

## 🧪 Example Output

```
=========================
    ## Weather App ##
=========================

Enter a city name: Cairo

#########################
## Weather in Cairo ##
#########################

Temp           : 28.5
Feels Like     : 29.1
Temp Min       : 26.8
Temp Max       : 30.2
Pressure       : 1012
Humidity       : 65

=========================
```

---

## 🛠️ Built With

- Python 3
- Requests library
- OpenWeatherMap API

---

## ⚠️ Important Notes

1. You need to:
   - Get your own API key from [OpenWeatherMap](https://openweathermap.org/)
   - Replace the `my_key` value in the code

2. The free API tier has limits:
   - 60 calls per minute
   - 1,000,000 calls per month

---

## 📄 License

This project is open-source and free to use.
