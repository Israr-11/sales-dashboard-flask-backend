import requests

def getCoordinates(customerCity, customerCountry):
    cityUrl = f"https://nominatim.openstreetmap.org/search?q={customerCity},{customerCountry}&format=json"
    countryUrl = f"https://nominatim.openstreetmap.org/search?q={customerCountry}&format=json"

    # Fetch coordinates for the city
    cityResponse = requests.get(cityUrl)
    if cityResponse.status_code == 200:
        cityData = cityResponse.json()
        if cityData:
            cityLatitude = cityData[0]['lat']
            cityLongitude = cityData[0]['lon']
        else:
            cityLatitude = None
            cityLongitude = None
    else:
        cityLatitude = None
        cityLongitude = None

    # Fetch coordinates for the country
    countryResponse = requests.get(countryUrl)
    if countryResponse.status_code == 200:
        countryData = countryResponse.json()
        if countryData:
            countryLatitude = countryData[0]['lat']
            countryLongitude = countryData[0]['lon']
        else:
            countryLatitude = None
            countryLongitude = None
    else:
        countryLatitude = None
        countryLongitude = None

    return cityLatitude, cityLongitude, countryLatitude, countryLongitude
