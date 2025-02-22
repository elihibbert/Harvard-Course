#Write a code that takes camel case font (likeThisFont) and changes it to snake case font (like_this_font)

#Ask for user input in camel case (rememberToUseCamelCase)
prompt = str(input("whatWouldYouLikeToSayInCamelCase?\n"))

#Iterate through each letter in the input.
for letter in prompt:
    #If the letter is a capital, add a space before. Also make it lower case.
    if letter.istitle():
        print(f"_{letter.lower()}", end="")
    #If the letter is lowercase, do not change.
    else:
        print(letter, end="")

