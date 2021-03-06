from model import sunriseReport
# from geopy.geocoders import Nominatim
from datetime import datetime
import requests, os, json


class Controller:

    def getSunriseReport(self, date, latitude, longitude):
        #date = datetime.strptime('%Y-%m-%d')
        latitude = str(latitude)
        longitude = str(longitude)
        sunriseSunset = []
        response = requests.get("https://api.sunrise-sunset.org/json?lat="+latitude+"&lng="+longitude+"&date="+date)
        jsonResponse = response.json()
        sunrise = jsonResponse['results']['sunrise']
        sunset = jsonResponse['results']['sunset']
        report = sunriseReport(date, sunrise, sunset)
        sunriseSunset.append(report)
        jsonReport = json.dumps(report.__dict__)
        return jsonReport
