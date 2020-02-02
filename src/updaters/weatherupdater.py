import os
import time
import threading

import requests

from src.updaters.updater import Updater


class WeatherUpdater(Updater):
    def __init__(self, return_type):
        # Every hour
        super().__init__(3600)

        allowed_types = [
            'summary',
            'icon',
            'temperature',
            'humidity'
        ]

        if return_type not in allowed_types:
            raise TypeError("Type must be one of " + ", ".join('"{0}"'.format(at) for at in allowed_types))

        self.content = 0
        self.complete = True
        self.return_type = return_type

    def update(self):
        # Only run if there isn't another ajax call already waiting
        if self.complete:
            self.complete = False
            # Todo: Move configs
            r = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" +
                             os.getenv("OPEN_WEATHER_MAP_CITY") +
                             "&appid=" + os.getenv("OPEN_WEATHER_MAP_KEY") +
                             "&units=" + os.getenv("OPEN_WEATHER_MAP_UNITS"))
            data = r.json()

            if data['cod'] != 200:
                self.logger.exception('Weather API failed to return a valid response. ')
                self.logger.exception('API Message: ' + data['message'])
                self.custom_interval = int(os.getenv("OPEN_WEATHER_MAP_RETRY_TIME"))
            else:
                self.content = self.get_return_content(data)

            self.complete = True
            super().update()

    @staticmethod
    def get_weather_summary(json):
        return json["weather"][0]["description"]

    @staticmethod
    def get_weather_temperature(json):
        return json["main"]["temp"]

    @staticmethod
    def get_weather_humidity(json):
        return json["main"]["humidity"]

    @staticmethod
    def get_weather_icon(json):
        return json["weather"][0]["icon"]

    def get_return_content(self, json):
        method_name = 'get_weather_' + self.return_type
        method = getattr(self, method_name, lambda: "No function for return type")
        return method(json)


    def get_content(self):
        if self.check_updater():
            t1 = threading.Thread(target=self.update)
            t1.start()

        return str(self.content)
