import requests

def get_data(make):
    req = requests.get(
        url='https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/' + make + '?format=json')
    cars = req.json()
    return cars["Results"]
