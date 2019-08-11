from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.stationdata import build_station_list
import matplotlib.pyplot as plt
import matplotlib
from floodsystem.analysis import polyfit



def plot_water_levels(station, dates, levels):

    #function that plots the water levels for the given station over that last x amount of days where x is the parameter dates,
    #and plots the given levels, levels, as lines on the graph for comparison
    stations = build_station_list()

    #find the station to be ploted 
    station_to_plot = None
    for x in stations:
        if x.name == station.name:   #finds the station to be plotted in the list of station objects
            station_to_plot = x 
            break
        else:
            print(station , 'could not be found in the data')
    
    dt = dates
    #creates list of dates and the water levels at the station on those dates
    dates1, levels1 = fetch_measure_levels(station_to_plot.measure_id, dt=datetime.timedelta(days=dt)) 

    #tests
    assert levels[0] < levels[1]

    # Plot
    plt.plot(dates1, levels1, 'b-', label ='plot')
    plt.axhline(y=levels[0], label = "min typical level", color = 'g')   #plots the minimum typical level as line on graph
    plt.axhline(y=levels[1], label = "max typical level", color = 'r')   #plots the maximum typical level as line on graph

        # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('relative water level (m)')
    plt.xticks(rotation=45);
    plt.title(station_to_plot.name)
    plt.legend(loc='upper left')
        # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
    # #find the dates to be assesed 
    # current_date = dt.date.today()
    # start_date = dt.date(dates)      #******dates needs to be imputed in datetime form******
    # dates_for_graph = []
    # time = current_date - start_date #output in the form: 00:00:00, 1 day
    # no_days = int(time.days)         #output in the form: 1
    
    # for i in range(no_days):
    #     dates_for_graph[i] = start_date + dt.timedelta(days=i) #creates list of graph of dates from start date to end date
    # t = dates_for_graph #now ready for plotting


    # #find the water level at these dates
    # fetch


    # # plot
    # plt.plot(t, level)

    # # Add axis labels, rotate date labels and add plot title
    # plt.xlabel('date')
    # plt.ylabel('water level (m)')
    # plt.xticks(rotation=45)
    # plt.title("Station A")

    # # Display plot
    # plt.tight_layout()  # This makes sure plot does not cut off date labels

    # plt.show()


def new_plot(station, net_days, levels):
    plt.plot(net_days, levels, label = "Height from data")#plot height
    plt.show
    







def plot_water_level_with_fit(station,dates, levels, p):
    function, offset = polyfit(dates,levels,p) #Find the expression and offset for the funciton of best fit
    days = matplotlib.dates.date2num(dates)#Change dates to list of days
    net_days =(offset-days)#start counted from day one
    plt.plot(net_days, function(net_days), label="Height from best fit")#Plot the graph
    new_plot(station,net_days,levels) #plot the height coming from data
    typical = station.typical_range
    plt.axhline(y=typical[0], label = "min typical level", color = 'g')   #plots the minimum typical level as line on graph
    plt.axhline(y=typical[-1], label = "max typical level", color = 'r')   #plots the maximum typical level as line on graph
    plt.xlabel('$days$')
    plt.ylabel('$heights$')
    plt.legend()

    plt.show()
