# Ask the user for their name and remove whitespace and capitalize str in one step
name = input ("What's your first and last name? ").strip().title()

'''
#Remove the whitespace from the user imput (str)
name = name.strip()
#Capitalize str
name = name.title()
'''

#Sprit the user's name into first and last names
First, Last = name.split(" ")

# Say hello to the user
print("Hello, ",name,"!",sep="")
#Sep is the seperation between parameters.
#The built in Python seperation is a space but this code overrides that to not have a space before the !

'''
#Print only the first name
print ("Hello, ", First, "!", sep="")
'''