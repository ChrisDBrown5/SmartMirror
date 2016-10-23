#Author: Christopher Brown
#Date Started: 10/15/2016
#Uses: Python 2.7, graphics (by Zelle), pyowm (weather), datetime (guess), and time (for delays) and more to come.
#Project Description: 	This is going to be the main file for the magic mirror I am building
#			and I will probably be using this file for all updates and future
#			creation involving the magic mirror (will become known as photon mirror)

#Update 10/23/16: Looking to use a different GUI, starting work with Tkinter to see if it's a viable module.
#                  Also added a few pictures for weather information, but these are likely to change, so I will not upload them, 
#                  nor include the code needed to use them, at this time.


#So far, I've gotten temperature, date, time, and weather to work and appear on a black screen with white characters, left aligned.

from datetime import datetime
from datetime import date
import pyowm
import time
from graphics import *

#Opening the graphics window
win = GraphWin("", 1440, 900)

def main():
    #initializations, cause it doesn't work all the time without them.
    Sun = ""
    Temper = ""
    t = ""
    d = ""
    
    if owm.is_API_online()==True:
        forecast = owm.daily_forecast("Gainesville,US")
        #tomorrow = pyowm.timeutils.tomorrow()
        if forecast.will_have_rain()==False:
                rain = 'No rain today!'
                if forcast.will_have_sun() ==False:
                        Sun = 'But it wont be sunny.'
                else:
                        Sun = 'AND it is going to be sunny!'
        else:
                rain = "Bring an umbrella today,\nthere is a chance of rain"

        observation = owm.weather_at_place('Gainesville,US')
        w = observation.get_weather()
        #this creates a dictionary of max, min, kf?, and average temp
        temp = w.get_temperature('fahrenheit') 
        #temp['temp'] calls the dictionary of average temp
        tempe = str(temp['temp'])
        Temper = tempe + " Degrees Fahrenheit"
        
    else:
        #Signals that the program is offline/not connected to Weather API
        win.setBackground('blue')
        time.sleep(5)
    today = date.today()
    #ex. "Monday, March 5, 2016"
    d = today.strftime("%A, %B %d, %Y")
    #ex. "05:26PM"
    t = datetime.now().strftime("%I:%M%p")
    win.setBackground('black')
    #set text in respective places
    mTime = Text(Point(100,100), t)
    mDate = Text(Point(213,50), d)
    mTemper = Text(Point(203,150), Temper)
    mSun = Text(Point(150,200), Sun)
    mRain = Text(Point(195,250), rain)
    #Change text color to white and increase size
    mTime.setFill('white')
    mDate.setFill('white')
    mTemper.setFill('white')
    mSun.setFill('white')
    mRain.setFill('white')
    mTime.setSize(20)
    mDate.setSize(20)
    mTemper.setSize(20)
    mSun.setSize(20)
    mRain.setSize(20)
    #print text on window
    mTime.draw(win)
    mDate.draw(win)
    mTemper.draw(win)
    mSun.draw(win)
    mRain.draw(win)
    #This waits for a mouseclick, then closes
    #win.mouseget()
    # I changed it..^
    time.sleep(5)
    #updates every 5 seconds, that way it doesn't ping the weather API too often
    #pinging too often results in them possibly shutting it off for my API Key
    main()
    

    
    
#API KEY         vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
owm = pyowm.OWM('72c92dce615514f154477952ce9af6d8')
#Start the actual program.
main()

