#A code that takes an input and outputs the same prompt without vowels

#Ask for user input
prompt = str(input("What would you like to say? ")).lower()

#Loop to remove vowels from the prompt
#Iterate over each letter in the prompt
for letter in prompt:
    #If the letter is a vowel, remove.
    if letter == "a":
        print("", end="")
    elif letter == "e":
        print("", end="")
    elif letter == "i":
        print("", end="")
    elif letter == "o":
        print("", end="")
    elif letter == "u":
        print("", end="")
    #If the letter is not a vowel, print as is.
    else:
        print(letter, end="")
        
