import os
from city_coords import City_COORDS


import httpx
from dotenv import load_dotenv

load_dotenv()

class Weather_Tool:
    # BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    BASE_URL = "https://api.weatherapi.com/v1/current.json"
    METEO_BASE_URL = "https://api.open-meteo.com/v1/forecast?latitude=17.433037&longitude=78.325457&current=temperature_2m"

    def __init__(self):
        self.city_coords = City_COORDS()

    @property
    def name(self):
        return "weather"
    @property
    def description(self):
        return "Returns current weather for a given city."
    
    @property
    def parameters(self):
        return {
            "city": {
                "type": "string",
                "description": "City name"
            }
        }
    
    def execute(self,city):
        coords = self.city_coords.get_city_coords(city)
        temp_data = self.get_weather_by_coords(coords)
        return temp_data

    def get_weather_by_coords(self,coords):
        params = {
            "latitude":coords['lat'],
            "longitude":coords['longt'],
            "current":"temperature_2m"
            
        }

        response = httpx.get(self.METEO_BASE_URL,params=params)
        response.raise_for_status()

        return response.json()
