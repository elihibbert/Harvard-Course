
#ask for user input and convert it to an integer
x = float(input("What is X? "))
y = float(input("What is Y? "))

#This will round the sum to 1 decimal
z = round(x + y, 1)

#This will print the Z variable with commas for 1000's
print(f"{z:,}")