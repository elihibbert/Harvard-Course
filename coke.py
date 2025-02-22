#Set amount due equal to $0.50 (the cost of the coke)
amount_due = 50

#Tell the user the rules
print("Welcome to the vending machine, a coke costs 50 cents")
print("The following coins are accepted:")
print("5 cents, 10 cents, 25 cents")
print("Please input cent amounts as integers")
      

#Loop to have user insert coin and inform of the amount remaining until balance is met.
while amount_due > 0:
    #Print amount due
    print(f"Amount due: {amount_due} Cents")
    #Ask for coin
    coin = int(input("Insert Coin: "))
    #Adjust amount due using loop to make sure only correct coins are inserted
    if coin == 25:
        amount_due = amount_due - coin
    elif coin == 10:
        amount_due = amount_due - coin
    elif coin == 5:
        amount_due = amount_due - coin

    
    
#Display any change due
print(f"Change Owed: {amount_due*-1} Cents")
print("Thank you for purchasing a Coke! Enjoy!")




