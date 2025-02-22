#Ask for the family member's name
name = input("Which family member are you searching for? ")

#Use the match loop to search for keywords
match name:
    case "Liam":
        print("Lives in New York")
    case "Heika" | "Jeff":
        print("Lives in Seattle")
    case "Grandpa Wharton" | "Grandma Wharton":
        print("Lives in Illinois")
    case _:
        print("Who?")
        
