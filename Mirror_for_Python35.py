# -*- coding: utf-8 -*-
#^^^^ This is for the degre symbol for temperature
import tkinter as Tk
#GUI package^
from datetime import datetime
from datetime import date
import pyowm
import time
import requests
from yahoo_finance import Share


#API KEY         vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
owm = pyowm.OWM('72c92dce615514f154477952ce9af6d8')

###########################################################################################
def getTime():
    timeNow = datetime.now().strftime("%I:%M:%S %p")
    return timeNow

def getDate():
    today = date.today()
    dateNow = today.strftime("%A, %B %d, %Y")
    return dateNow

def getWeather():
    forecast = owm.weather_at_place('Gainesville,US').get_weather()
    Sun = "Today's Forcast: "
    Sun = Sun + forecast.get_status()
    
    return Sun

def getWeather2():
    forecast = owm.weather_at_place('Gainesville,US').get_weather()
    if forecast.get_status()=="Clear":
        level = 1
    else:
        level = 3
    return level

def getTemp():
    w = owm.weather_at_place('Gainesville,US').get_weather()
    #this creates a dictionary of max, min, kf?, and average temp
    temp = w.get_temperature('fahrenheit') 
    #temp['temp'] calls the dictionary of average temp
    tempe = str(temp['temp'])
    Temper = tempe +  "°F"
    #pinging too often results in them possibly shutting it off for my API Key
    return Temper

def td():
    global time1
    # get the current local time from the PC
    time2 = getTime()
    date = getDate()
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        ti.config(text=time2)
    if date != getDate():
        da.config(text=date)
    # updates time every 200 milliseconds.
    top.after(200, td)

def te():
    temp.config(text = getTemp())
    top.after(60000, te)
    
def w():
    sun.config(text = getWeather())
    top.after(60100, w)

def i():
    global level1
    level2 = getWeather2()
    if level1 != level2:
        if getWeather2() == 1:
            im = Tkinter.PhotoImage(file = "sun-128.gif")
        elif getWeather2() == 2:
            im = Tkinter.PhotoImage(file = "clouds-128.gif")
        else:
            im = Tkinter.PhotoImage(file = "rain-128.gif")
        icon.config(image = im)
    top.after(60150,i)

def getDist():
	if datetime.now().strftime("%p") == "PM":
		if int(datetime.now().strftime("%I")) >= int(5):
			b = "Bus isn't running at this time."
			return b
	else:
	    # These code snippets use an open-source library. http://unirest.io/python --PSYCH Switched to "Requests" because unirest isnt supported on 3.4/3.5
	    response = requests.get("https://transloc-api-1-2.p.mashape.com/arrival-estimates.json?agencies=116&callback=call&routes=4001178&stops=4091950%2C1408",
	                          headers={"X-Mashape-Key": "WMF100LDSSmsh0jWk7IQ8V3Bt5Pip1PSC8Cjsnwip0newzTPkO","Accept": "application/json"})
	    x = str(response.body['data'])
	    time2 = x[119:124]
	    b = "122 arrives at " + time2 
	    return b
	

		


def bu():
    bus.config(text = getDist())
    top.after(5030, bu)

def getStock(ticker):
    stock = Share(ticker)
    #name = stock.get_name()
    po = str(stock.get_open())
    pn =  str(stock.get_price())
    pcl =  str(stock.get_prev_close())
    pc = str(stock.get_percent_change())
    low = str(stock.get_days_low())
    high = str(stock.get_days_high())
    h = datetime.now().strftime("%I")
    p = datetime.now().strftime("%p")
    x = ticker.upper() + "\nCurrent: " + pn +"\nClose: " + pcl + "\nChange: "+ pc + "\nLow: " + low + "\nHigh: " + high
    y = ticker.upper() + "\nCurrent: " + pn + "\nOpen: " + po + "\nChange: " + pc + "\nLow: " + low + "\nHigh: " + high
    
    if h <= "4" and p == "PM":
        return x
    elif h >= "4" and p == "PM":
        return y
    elif h <= "8" and p == "AM":
        return y
    else:
        return x


    
def sto1():
    stock1.config(text = getStock('ugaz'))
    #stock2.config(text = getStock('xgti'))
    #add more stocks as necessary
    top.after(3000, sto1)

def sto2():
    #stock1.config(text = getStock('UGAZ'))
    stock2.config(text = getStock('xgti'))
    #add more stocks as necessary
    top.after(8000, sto2)

level1 = getWeather2()
time1 = getTime()
top = Tk.Tk()
top.title("Chris' Magic Mirror")
top.geometry("1440x900")
top.wm_iconbitmap("favicon.ico")
top.configure(bg = 'black')
temp = Tk.Label(top, bg = 'black', fg = 'white', font=('times', 20, 'bold'))
sun = Tk.Label(top, bg = 'black', fg = 'white', font=('times', 20, 'bold'))
ti = Tk.Label(top, bg = 'black', fg = 'white', font=('times', 40, 'bold'))
da = Tk.Label(top, bg = 'black', fg = 'white', font=('times', 20, 'bold'))
icon = Tk.Label(top, bg = 'black')
bus = Tk.Label(top, bg = 'black', fg = 'white', font=('times', 20, 'bold'))
#add more buses as necessary
stock1 = Tk.Label(top, bg = 'black', fg = 'white', font=('times', 12, 'bold'))
stock2 = Tk.Label(top, bg = 'black', fg = 'white', font=('times', 12, 'bold'))
#add more stocks as necessary

ti.config(text = getTime())
da.config(text = getDate())
temp.config(text = getTemp())
sun.config(text = getWeather())
bus.config(text = getDist())
stock1.config(text = getStock('UGAZ'))
stock2.config(text = getStock('xgti'))
if getWeather2() == 1:
    im = Tk.PhotoImage(file = "sun-128.gif")
elif getWeather2() == 3:
    im = Tk.PhotoImage(file = "rain-128.gif")
else:
    im = Tk.PhotoImage(file = "clouds-128.gif")
icon.config(image = im)

ti.pack()
ti.place(bordermode = 'outside', x = 30, y = 30)
da.pack()
da.place(bordermode = 'outside', x = 30, y = 90)
temp.pack()
temp.place(bordermode= 'outside', x = 1215, y = 30)
icon.pack()
icon.place(bordermode = 'outside', x = 1190, y = 70)
sun.pack()
sun.place(bordermode = 'outside', x = 1100, y = 200)
bus.pack()
bus.place(bordermode = 'outside', x = 1085, y = 820)
stock1.pack()
stock1.place(bordermode = 'outside', x = 30, y = 590)
stock2.pack()
stock2.place(bordermode = 'outside', x = 30, y = 730)
top.after(100, td)
top.after(3000, sto1)
top.after(8000, sto2)
top.after(5030, bu)
top.after(150000, te)
top.after(300000, w)
top.after(300150, i)
top.mainloop()
#use place functions to change the positions



