#This code will ask the user which fruit they are going to consume then outputs the calories in the fruit

#User input asking for which fruit
fruit = str(input("What type of fruit are you selecting? ")).lower()

#Save FDA fruit data as a dict
FDA_data = {
    "apple" : 130, "avocado" : 50, "banana" : 110,
    "cantaloupe" : 50, "grapefruit" : 60, "grapes" : 90,
    "honeydew melon" : 50, "kiwifruit" : 90, "lemon" : 15,
    "lime" : 20, "nectarine" : 60, "orange" : 80,
    "peach" : 60, "pear" : 100, "pineapple" : 50,
    "plums" : 70, "strawberries" : 50, "sweet cherries" : 100,
    "tangerine" : 50, "watermelon" : 80
    }


#Find fruit and print Calories. Send message if not in database
#Use an if statement to find key in dictionary
if fruit in FDA_data:
    print(f"The calories in a {fruit} are: ", FDA_data[fruit])
else:
    print("Not in FDA database for fruit")
