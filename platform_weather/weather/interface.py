import requests


class Weather(object):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    API_KEY = "9442a271d49d2a40722421b563bed571"

    def lookup_by_location(self, location, period):
        _data = {}
        _url = self.BASE_URL + "q=" + location + "&appid=" + self.API_KEY
        if period:
            _url = f"{_url}&cnt={period}"
        response = requests.get(_url)
        if response.status_code == 200:
           # getting data in the json format
           data = response.json()
           print(data)
           main = data['main']
           temperature = main['temp']
           humidity = main['humidity']
           pressure = main['pressure']
           report = data['weather']
        else:
           data['error'] = "Error in the HTTP request"

        return data

