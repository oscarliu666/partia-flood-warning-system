import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import datetime

def polyfit(dates, levels, p):
    days = matplotlib.dates.date2num(dates)#Change list of dates to number of days 
    
    shift =days[0]#find the largest day in the list
    net_days = (shift-days)#Giving a list of days from 0
    y = levels#List of levels for each day
    p_coeff = np.polyfit(net_days, y, p ) #Find coefficient of polynomial of best fit
    poly = np.poly1d(p_coeff)# Convert coefficient into a polynomial that can be evaluated,
    return poly,shift
