import re

""" A program to check the validity of a post code against UK postcode patterns. 
    Regular expressions (regex) used here are formulated according to the postcode patterns here:
    https://ideal-postcodes.co.uk/guides/uk-postcode-format 
"""

def get_input():
    """ Prompts for user input """
    code = input("Enter a post code: ")

    checker.check_code(code)


class PostcodeChecker:

    def check_code(self, pcode):
        """ Checks the input against UK postcode formats"""

        # First, check the length:
        length = len(pcode)

        if length == 8:
            check = bool(re.search(r'[A-Z][A-Z]\d([A-Z]|\d)\s\d[A-Z][A-Z]', pcode))
            if check:
                print("This is a valid UK postcode!")
                return check
            else:
                print("This is not a valid UK postcode!")
                return check
        elif length == 7:
            check = bool(re.search(r'[A-Z]\d[A-Z]\s\d[A-Z][A-Z]', pcode))
            if check:
                print("This is a valid UK postcode!")

            else:
                check = bool(re.search(r'[A-Z]\d\d\s\d[A-Z][A-Z]', pcode))
                if check:
                    print("This is a valid UK postcode!")
                    return check
                else:
                    check = bool(re.search(r'[A-Z][A-Z]\d\s\d[A-Z][A-Z]', pcode))
                    if check:
                        print("This is a valid UK postcode!")
                        return check
                    else:
                        print("This is not a valid UK postcode!")
                        return check
        elif length == 6:
            check = bool(re.search(r'[A-Z]\d\s\d[A-Z][A-Z]', pcode))
            if check:
                print("This is a valid UK postcode!")
                return check
            else:
                print("This is not a valid UK postcode!")
                return check
        else:
            print("Invalid input!")
            return 

checker = PostcodeChecker()
