#A code to replace the spaces in speach with ...
#Prompt the user for an input. Seperate words by the spaces
response = input("What would you like to say? ").split(sep=" ")


#Recreate the sentance with ... instead of spaces
response = "...".join(response)


#Print the users input after editting
print(response)