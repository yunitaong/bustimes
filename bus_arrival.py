import requests
from datetime import datetime, timezone
import time
from IPython.display import clear_output

# Define your ACCOUNT_KEY
ACCOUNT_KEY = "INSERTHERE"

def get_bus_arrival(bus_stop_code):
    url = f'http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode={bus_stop_code}'
    headers = {'AccountKey': ACCOUNT_KEY}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving bus arrival information: {e}")
        return None

def display_bus_arrival_info(bus_stop_code, service_nos):
    bus_arrival_data = get_bus_arrival(bus_stop_code)

    if bus_arrival_data:
        for bus in bus_arrival_data.get('Services', []):
            if bus['ServiceNo'] in service_nos:
                print(f"Bus {bus['ServiceNo']}: ", end="")
                next_buses = [bus['NextBus'], bus['NextBus2'], bus['NextBus3']]
                next_buses = [b for b in next_buses if b]
                if next_buses:
                    for next_bus in next_buses:
                        if 'EstimatedArrival' in next_bus:
                            arrival_time = next_bus['EstimatedArrival']
                            if arrival_time:
                                current_time = datetime.now(timezone.utc)
                                arrival_time = datetime.strptime(arrival_time, "%Y-%m-%dT%H:%M:%S%z")
                                time_difference = arrival_time - current_time
                                minutes_remaining = int(time_difference.total_seconds() / 60)
                                print(f"{minutes_remaining} min", end="")
                                if next_bus != next_buses[-1]:
                                    print(", ", end="")
                            else:
                                print("NA", end="")
                                if next_bus != next_buses[-1]:
                                    print(", ", end="")
                        else:
                            print("NA", end="")
                            if next_bus != next_buses[-1]:
                                print(", ", end="")
                else:
                    print("NA", end="")
                print()
    else:
        print(f"No bus arrival information available for Bus Stop {bus_stop_code}")
                      
                      # Function to update and display bus arrival information
def update_bus_arrival_info():
    clear_output(wait=True)
    display_bus_arrival_info('52569', ['230'])
    display_bus_arrival_info('52081', ['142', '506'])

# Run the scheduled tasks
while True:
    try:
        update_bus_arrival_info()
        # Wait for 1 minute
        time.sleep(60)
    except Exception as e:
        print(f"An error occurred: {e}")
