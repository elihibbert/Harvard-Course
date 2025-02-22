#Ask the great question of life looking for the answer 42

#ask the user for input to the great question
response = str(input("What is the answer to the Great Question of Life, the Universe and Everything? ")).lower().strip()

if response == "42":
    print("Yes")
elif response == "fourty-two":
    print("Yes")
elif response == "fourty two":
    print("Yes")
else:
    print("No")
    
    