#Create a list of cities in Washington
cities = ["Seattle", "Olympia", "Tum Water", "Yakima"]

#Print each city one line at a time
'''
#This example lets Python read into the data list
for C in cities:
    print(C)
'''
    
#This method dictates specifically how Python should read the data list
for i in range(len(cities)):
    print (i + 1, cities[i])