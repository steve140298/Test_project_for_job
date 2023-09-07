import requests


# Function parsing station temperature
def station_temperature():
    stations_id = ['S50', 'S107', 'S60']
    response = requests.get("https://api.data.gov.sg/v1/environment/air-temperature").json()['items'][0]['readings']
    temperature = list()
    for res in response:
        if res['station_id'] in stations_id:
            print(f"Для станции {res['station_id']} температура воздуха равняется {res['value']}")
            temperature.append({res['station_id']: res['value']})
    return temperature


# Function parsing status API
def status_api():
    status = requests.get("https://api.data.gov.sg/v1/environment/air-temperature").json()['api_info']['status']
    print(f'status_api = {status}')
    return status
