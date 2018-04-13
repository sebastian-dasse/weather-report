#!/usr/bin/env python

"""
TODO: comment
"""

import urllib
import requests


base_url = "https://query.yahooapis.com/v1/public/yql?"
yql_query = (
  'select item.condition, wind from weather.forecast '
   'where woeid in (select woeid from geo.places(1) where text="berlin, de") '
     'and u = "c"' # metric scale
)
data_format = "&format=json"
img_base_url = "http://l.yimg.com/a/i/us/we/52/"
img_format = ".gif"
temp_unit = " C"
speed_unit = " km/h"


def print_today_s_weather_report():
  yql_url = base_url + urllib.urlencode({"q": yql_query}) + data_format
  data = requests.get(yql_url).json()

  results = data["query"]["results"]["channel"]
  condition, wind = results["item"]["condition"], results["wind"]
  
  code, temp, text = [condition[k] for k in ["code", "temp", "text"]]
  wind_speed = wind["speed"]
  img_url = img_base_url + code + img_format

  print "'{}', '{} {}', '{} {}', '{}'".format(
    text,
    temp, temp_unit,
    wind_speed, speed_unit,
    img_url
  )



def main():
  print_today_s_weather_report()


if __name__ == '__main__':
  main()
