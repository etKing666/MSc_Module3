import re

""" A program to check the validity of a post code against UK postcode patterns. 
    Regular expressions (regex) used here are formulated according to the postcode patterns here:
    https://ideal-postcodes.co.uk/guides/uk-postcode-format 
"""

# Get the user input
pcode = input("Enter a post code: ")

# First, check the length:
length = len(pcode)

if length == 8:
    check = bool(re.search(r'[A-Z][A-Z]\d[A-Z]\s\d[A-Z][A-Z]', pcode))
    if check:
        print("This is a valid UK postcode!")
    else: # Did not use here (and below) elif because there is no proper bool statement to go with it
        check = bool(re.search(r'[A-Z][A-Z]\d\d\s\d[A-Z][A-Z]', pcode))
        if check:
            print("This is a valid UK postcode!")
        else:
            print("This is not a valid UK postcode!")

elif length == 7:
    check = bool(re.search(r'[A-Z]\d[A-Z]\s\d[A-Z][A-Z]', pcode))
    if check:
        print("This is a valid UK postcode!")
    else:
        check = bool(re.search(r'[A-Z]\d\d\s\d[A-Z][A-Z]', pcode))
        if check:
            print("This is a valid UK postcode!")
        else:
            check = bool(re.search(r'[A-Z][A-Z]\d\s\d[A-Z][A-Z]', pcode))
            if check:
                print("This is a valid UK postcode!")
            else:
                print("This is not a valid UK postcode!")

elif length == 6:
    check = bool(re.search(r'[A-Z]\d\s\d[A-Z][A-Z]', pcode))
    if check:
        print("This is a valid UK postcode!")
    else:
        print("This is not a valid UK postcode!")

else:
    print("Invalid input!")
