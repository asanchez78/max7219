#!/usr/bin/python3

import urllib.request as urllib2
import simplejson as json
import max7219.led as led
import time
from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT

device = led.matrix(cascaded = 3)

device.orientation(90)


forecastioApikey = "52edcc0d3cd9c59a8b67e3d5cd7888ec"
latlong = "30.315995, -97.867995"

def getWeather(t):
  try:
    decoded = json.load(urllib2.urlopen("https://api.forecast.io/forecast/" + forecastioApikey + "/" + latlong))
 
    # For debugging, show json-formatted string
    #print json.dumps(decoded, sort_keys=True, indent=4)
 
    if(t == 1):
      summary = decoded['minutely']['summary']
      summary = "The short-term forecast is: " + summary
    if(t == 2):
      summary = decoded['hourly']['summary']
      summary = "The longer-term forecast is: " + summary
    if(t == 3):
      temperature = int(decoded['currently']['temperature'])
      temperature = temperature // 1
      condition = decoded['currently']['summary']
      summary = str(temperature)
      #print(summary) 
      return(summary)
  except (ValueError, KeyError, TypeError):
    print ("Error: Problem parsing the weather feed.")

temperature = getWeather(3)
timesLooped = 0

device.show_message("    " + temperature,font=proportional(TINY_FONT))

while True:
    if timesLooped > 600:
        temperature = getWeather(3)
        timesLooped = 0
        device.show_message("    " + temperature,font=proportional(TINY_FONT))
    else:
        #device.show_message("    " + temperature,font=proportional(TINY_FONT))
        timesLooped += 1
        time.sleep(1)
