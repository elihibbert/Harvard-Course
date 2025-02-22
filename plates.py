#This is code that will take a user input for a new custom license plate number.
#If the license plate number meets the Massachusetts requirements, "Valid" will be output.

#Define main function to take plate number and output valid or invalid.
def main():
    plate = str(input("Plate Desired: "))
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")





#Function to check if plate number is valid. If valid, return True
def is_valid(s):

    #Outer while loop needed to make sure everycase is true
    while True: 
    
        #Check for periods, spaces, and punctuation marks (not allowed)
        for i in s:
            if i.isalnum() == False:
                return False
            
        #Check that plate has maximum 6 characters, minimum 2
        if len(s) < 2:
            return False
        elif len(s) > 6:
            return False
        
        #Check that plate starts with 2 letters. Isalpha gives true if character is alphabetic.
        if s[0].isalpha() == False:
            return False
        if s[1].isalpha() == False:
            return False
    
        #Check for numbers in the middle (Not allowed if the plate ends with a letter)
        if s[-1].isalpha() == True:                
            for i in s[0:-1]:
                if i.isalpha() == False:
                    return False        
    
        #Check if the first number is a 0
        for i in s[0:-1]:
            if i.isalpha() == False:
                if i == "0":
                    return False
                    
        #If none of the checks returned false, now I return true...
        return True
    
        
        
        


#Loop to run this function if this file is activated.
if __name__ == "__main__":
    main()



