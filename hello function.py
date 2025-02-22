#Creates the new function "Hello"
def hello(to="World"):
    print("Hello,", to)
    
hello()    
name = input("What is your name? ").title()
hello(name)