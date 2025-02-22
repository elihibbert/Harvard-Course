#Ask user for x and y integer values
x = int(input("What's x? "))
y = int(input("What's y? "))

#See where x lands in respect to y
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else x == y:
    print ("x is equal to y")
 
'''    
#Shortened to just ask if x is equal or not to y
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")
'''    