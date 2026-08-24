import httpx


class City_COORDS:
    BASE_URL = "https://geocoding-api.open-meteo.com/v1/search"

    def __init__(self):
        pass

    def get_city_coords(self, city):
        params = {"name": city, "count": 1}
        response = httpx.get(self.BASE_URL, params=params)
        response.raise_for_status()

        geo_data = response.json()
        location = geo_data["results"][0]

        lat = location["latitude"]
        longt = location["longitude"]

        return {"lat": lat, "longt": longt}
