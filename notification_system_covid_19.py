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
  
  data = covidData.json()["Success"]
  
  while True:
    
    notification.notify(
    
    title = "COVID-19 Statistics for {}".format(datetime.date.today())
    
    message = "Total Cases: {totalcases}\nNew Cases Today: {todaycases}\nTotal Deaths: {totaldeaths}\nNew Deaths Today: {todaydeaths}\nTotal Active: {active}\nTotal Critical: {critical}".format(
                        totalcases = data['cases'],
                        todaycases = data['todayCases'],
                        todaydeaths = data['todayDeaths'],
                        active = data["active"],
                        critical = data["critical"]),
      
                        # icon for notification
      
                        app_icon = "299096_calendar_clock_icon.ico"
                        
                        # how long notification is on the screen
                        
                        timeout = 60
    )

# repeats after every 5 hours

time.sleep(60*60*5)
    
