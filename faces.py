#This code will have a main function to take user input and print the same text with smiley faces converted.
#A second function named convert will change any :) or :( to the equivalent emoji's

#Main function defined
def main():
    #Input text with a :) or :(
    prompt = str(input("Are you happy or sad?\n"))
    #Use the convert function to change the prompt to include emoji's
    prompt = convert(prompt)
    #Print out the new prompt
    print(prompt)
    
#Define convert function to change to emoji's
def convert(emoji):
    #Replace happy face emoji's
    emoji = emoji.replace(":)", "🙂")
    emoji = emoji.replace("(:", "🙂")
    #Replace sad face emoji's
    emoji = emoji.replace(":(", "🙁")
    emoji = emoji.replace("):", "🙁")
    return emoji

#Run main function
main()
