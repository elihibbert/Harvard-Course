'''
#How to accomplish this with a while loop
#Programming standard is to count up for loops
i = 0

#Loop through printing meows
while i < 3:
    print("Meow")
    #This is python shorthand to increase i
    i += 1
'''

#How to accomplish this with a for loop
#Ask the user how many Meow's they want. Use a loop to make sure they give a positive number
while True:
    n = int(input("How many Meow's does the cat make? "))
    if n > 0:
        break

#Use python's function "range"
for _ in range(n):
    print("Meow")

'''
#The print function also can be used as a loop
print("Meow \n" * 3, end="")
'''