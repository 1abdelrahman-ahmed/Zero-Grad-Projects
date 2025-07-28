import requests

def display_weather(data_dic):
    print("\n" + "=" * 25)
    for key, value in data_dic.items():
        print(f"{key.title():<15}: {value}")
    print("=" * 25 + "\n")

def get_weather_data(city):
    my_key = '2e5256639905e8614ccd1c761d197435'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={my_key}'
    response = requests.get(url)
    data = response.json()
    if data['cod'] != 200:
        print("\n" + "!" * 25)
        print(f"Error: City '{city}' not found!")
        print("!" * 25 + "\n")
        return None
    else:
        print("\n" + "#" * 25)
        print(f"## Weather in {data['name']} ##")
        print("#" * 25)
        display_weather(data['main'])
        return data['main']

def main():
    print("\n" + "=" * 25)
    print(" " * 4 + "## Weather App ##")
    print("=" * 25)
    city = input("\nEnter a city name: ")
    get_weather_data(city)

if __name__ == "__main__":
    main()