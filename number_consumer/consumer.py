import time
import requests
import datetime
import os

# os.mkdir("/data_from_number_consumer")
def save_file():
    # api-endpoint
    URL = "http://myfirst_docker_app_random_generator_1:80/random_number"

    # sending get request and saving the response as response object
    r = requests.get(url=URL)

    # extracting data in json format
    data = r.json()

    # using now() to get current time
    current_time = str(datetime.datetime.now())

    path_to_file = "/data_from_number_consumer/saved_data"
    data_to_save = f"{current_time}    {data}\n"
    with open(path_to_file, 'a') as saved_info:
        saved_info.write(str(data_to_save))
    # extracting latitude, longitude and formatted address how to access one container from another
    # of the first matching location
    # printing the output
    return data


time.sleep(20)
print("Hello Docker")
while True:
    print('aaa')
    to_sleap = save_file()
    print(to_sleap)
    time.sleep(int(to_sleap))
    print('sssss')
