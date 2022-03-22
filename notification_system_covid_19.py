import datetime

import requests

from plyer import notification

covidData = None

try:
  
  covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/uk/")
  
except:
  
  # if user lacks internet connection
  
  print("Error processing data! Please check your internet/data connection!")

if covidData != None:
  
  data = CovidData.json()["Success!"]
  
  while True:
    
    notification.notify()
