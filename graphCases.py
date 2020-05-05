import csv
from matplotlib import pyplot as plt

with open('time_series_covid19_confirmed_global.csv') as file: 
    reader = csv.reader(file)
    #countries list will be used for graph legend
    countries =[]

    #function takes String as argument. String should be country name in the list
    #currently no error handling in code so name must be accurate
    #function will plot specified country data based on csv file
    def graph_country(countryName):

    def graph_country(countryName):
        for row in reader:
            if(row[1] == countryName):
                countryList = row[4:]
        countArray = list(range(len(countryList)))
        file.seek(0)
        countryList = list(map(int, countryList))
        plt.plot(countArray, countryList)
        countries.append(countryName)

    #function calls  
    graph_country('US')
    graph_country('Japan')
    graph_country('Italy')
    graph_country('Korea, South')
    graph_country('Germany')

    #UK must be added manually because there are multiple UK entries in CSV
    #uses data from row[2] to determine which UK entry to gather data from
    for row in reader:
        if(row[1] == "United Kingdom" and row[2] == '55.3781'):
            ukList = row[4:]
    countArray4 = list(range(len(ukList)))
    ukList= list(map(int, ukList))
    plt.plot(countArray4, ukList)
    countries.append('UK')

    #labels
    plt.xlabel('Days Since 1/22/2020')
    plt.ylabel('Number of Confirmed Cases(in millions)')
    plt.title('Corona Virus Confirmed Cases')

    #use contries list to populate graph legend
    plt.legend(countries)
    
    plt.show()

