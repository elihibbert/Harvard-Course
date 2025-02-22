#A code to check the file type and print the corresponding web browser media type.
def main():
    #Ask user for name of the file
    file = str(input("What is the name of your file? ")).lower().strip()
    finder(file)




def finder(file):

    #If statement to find out which file type it is and print the media type.
    if file.endswith(".gif"):
        print("This file has a MIME type of:\n image/gif")
    elif file.endswith(".jpg") or file.endswith(".jpeg"):
        print("This file has a MIME type of:\n image/jpeg")
    elif file.endswith(".png"):
        print("This file has a MIME type of:\n image/png")
    elif file.endswith(".pdf"):
        print("This file has a MIME type of:\n application/pdf")
    elif file.endswith(".txt"):
        print("This file has a MIME type of:\n text/plain")
    elif file.endswith(".zip"):
        print("This file has a MIME type of:\n application/zip")
    else:
        print("application/octet-stream")
    
    
    
    
main()