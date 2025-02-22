#Ask the user for a greeting and respond by paying $0 if it is hello, $20 if it starts with h, and $100 for something else
#Ask for greeting
greeting = str(input("What is your greeting? ")).lower()
               
#If statement to address cases
#If statement starts with hello
if greeting.startswith("hello"):
    print("Here is $0")
    
#elif statement starts with h
elif greeting.startswith("h"):
    print("Here is $20")

#Else print $100
else:
    print("Here is $100")