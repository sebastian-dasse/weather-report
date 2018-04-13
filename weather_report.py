#!/usr/bin/env python

"""
TODO: comment
"""

import urllib
import requests


base_url     = "https://query.yahooapis.com/v1/public/yql?"
img_base_url = "http://l.yimg.com/a/i/us/we/52/"

data_format = "&format=json"
img_format = ".gif"

temp_unit  = "C"
speed_unit = "km/h"

yql_query = (
  'select item.condition, wind from weather.forecast '
   'where woeid in (select woeid from geo.places(1) where text="berlin, de") '
     'and u = "c"' # metric scale
)


def query_weather_data_as_json():
  yql_url = base_url + urllib.urlencode({"q": yql_query}) + data_format
  return requests.get(yql_url).json()


def query_weather_data():
  data = query_weather_data_as_json()
  results = data["query"]["results"]["channel"]
  condition, wind = results["item"]["condition"], results["wind"]
  return [condition[k] for k in ["code", "temp", "text"]] + [wind["speed"]]


def weather_icon(code):
  return img_base_url + code + img_format


def print_today_s_weather_report():
  code, temp, text, wind_speed = query_weather_data()

  print "'{}', '{} {}', '{} {}', '{}'".format(
    text,
    temp, temp_unit,
    wind_speed, speed_unit,
    weather_icon(code)
  )



def main():
  print_today_s_weather_report()


if __name__ == '__main__':
  main()
