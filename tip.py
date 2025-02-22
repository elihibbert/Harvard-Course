#Create a few functions that take the meal amount and percentage of tip desired then gives the amount.
def main():
    #Ask for cost of meal
    dollars = dollars_to_float(input("How much was the meal? "))  
    percent = percent_to_float(input("What percentage would you like to tip? "))    
    
    #Calculate tip amount
    tip = dollars * percent
    
    #Print tip amount
    print(f"Leave ${tip:.2f}")



#Additional function that converts cost of the meal into a float. $5.22 --> 5.22
def dollars_to_float(money):
    #Strip $ sign
    money = float(money.lstrip("$"))
    #Return value
    return money


#Additional function that converts a typed percentage into a float 20.1% --> 0.201
def percent_to_float(per):
    #Remove percentage sign
    per = per.removesuffix("%")
    #Divide by 100 to get decimal
    per = float(per) / 100
    #Return value
    return per




#Perform main function
main()
