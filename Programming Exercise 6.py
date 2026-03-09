import re

#function for validating phone
def validate_phone(phone):
    #our format we use for validation
    pattern = r"^\d{3}-\d{3}-\d{4}$"
    #our return value to receive true/false boolean values
    return re.fullmatch(pattern, phone) is not None

#function for validating social security
def validate_ssn(ssn):
    # our format we use for validation
    pattern = r"^\d{3}-\d{2}-\d{4}$"
    # our return value to receive true/false boolean values
    return re.fullmatch(pattern, ssn) is not None

#function for validating zip code
def validate_zip(zip_code):
    # our format we use for validation
    pattern = r"^\d{5}$"
    # our return value to receive true/false boolean values
    return re.fullmatch(pattern, zip_code) is not None

#Main function to interact with user
def main():

    #ask user series of prompts for validation
    phone = input("Enter telephone number(xxx-xxx-xxxx): ")
    ssn = input("Enter social security number(xxx-xx-xxxx): ")
    zip_code = input("Enter zip code(xxxxx): ")

    #if statements to take our boolean values and use them to get valid/invalid results
    if validate_phone(phone):
        print("Phone number is valid")
    else:
        print("Phone number is invalid")

    if validate_ssn(ssn):
        print("Social security number is valid")
    else:
        print("Social security number is invalid")

    if validate_zip(zip_code):
        print("Zip code is valid")
    else:
        print("Zip code is invalid")

main()