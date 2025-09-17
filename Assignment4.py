import json
import ssl
from urllib.request import urlopen

def main():
    #points for munice
    url = "https://api.weather.gov/points/40.1934,-85.3864"
    #ignores verification
    context = ssl._create_unverified_context()
    #first url
    response = urlopen(url, context=context)
    points = json.loads(response.read())
    #get url
    forecast_url = points["properties"]["forecast"]
    print("Forecast URL: ",forecast_url, "\n")
    #fetch the data
    response = urlopen(forecast_url,context=context)
    forecast = json.loads(response.read())

    #get the list of periods
    periods = forecast["properties"]["periods"]
    print(f"Total forecast periods: {len(periods)}\n")

    for period in periods:
        print(f"{period['name']}: {period['temperature']}{period['temperatureUnit']},{period['shortForecast']}") 
        print(f"Details: {period['detailedForecast']}\n")   
    
main()