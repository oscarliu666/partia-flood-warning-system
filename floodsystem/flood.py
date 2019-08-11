from floodsystem.station import MonitoringStation
# take second element for sort
def takeSecond(elem):
    return elem[1] #function to assist in sorting by second element of tuple


def stations_level_over_threshold(stations, tol):
    #function that returns a list of tuples holding the station object, and the relative water level

    
    stations_tuple_with_relative = [] #empty list for the tuples

    for i in stations:
        if i.typical_range_consistent() == True: #ensures that the typical ranges of the object are conistent
            i.relative_water_level() 
            # print (i, i.typical_range_consistent(), i.relative_level)
            if i.relative_level is not None: #checks that there is a value for the relative water level
                # print(i, i.relative_level)
                if i.relative_level > tol:
                    stations_tuple_with_relative.append((i.name, i.relative_level))  #creates the unsorted list
        
    sortedList = sorted(stations_tuple_with_relative , key=takeSecond, reverse = True) #sorts by relative value in
    
    #tests
    for i in sortedList:
        assert i[1] > 0.0
    
    for n in range(0, len(sortedList)-1):
        assert sortedList[n][1] > sortedList[n+1][1]
    
    
    
    return(sortedList)



def stations_highest_rel_level(stations, N):
    stations_tuple_with_relative = []
    for i in stations:
        if i.typical_range_consistent() == True:
            i.relative_water_level() 
            if i.relative_level == None:
                continue
            else:
                stations_tuple_with_relative.append((i.name, i.relative_level))
        
    full_List = sorted(stations_tuple_with_relative , key = lambda x:x[1], reverse = True) 
    result = full_List[0:N]
    return(result)