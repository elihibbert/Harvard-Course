#Create 2 functions that take user input of time and output if it is time for a meal
#if the input time does not fall into mealtime, do not output anything.

#Use the main function to get a user input
def main():
    time = str(input("What time is it? "))
    convert(time)
    
    
#Use the convert function to see if input time falls under mealtime
def convert(time):
    
    #Convert the time into a float
    #Split the hours and minutes
    hours, minutes = time.split(":")
    #Change from strings to floats
    minutes = float(minutes)
    hours = float(hours)
    #change minutes to a decimal
    minutes = minutes / 60
    #join time back together
    time_dec = hours + minutes
    
    
    #Match the time to see if it falls into meal times
    #Breakfast
    if 7 <= time_dec <= 8:
        print("It's Breakfast Time!")
    #Lunch
    elif 12 <= time_dec <= 13:
        print("It's Lunch Time!")
    #Dinner
    elif 18 <= time_dec <= 19:
        print("It's Dinner Time!")
        
    
        
      
#Using the if name=main loop will run main if the program is run on this file
#With this syntax, we we run the file, __name__ is automatically set to __main__
#If this function is pulled in through a library on a different file, __name__ will no longer equal __main__
if __name__ == "__main__":
    main()