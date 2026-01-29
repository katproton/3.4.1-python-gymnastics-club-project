import re
import unittest
from home_page import generate_id

# def contains_special_character(s):
#     # Define a regex pattern for special characters
#     pattern = re.compile('[^a-zA-Z0-9]')
#     # Search for the pattern in the string
#     return bool(pattern.search(s))

# # Test the function
# test_string = "Hello@&*World!"
# print(contains_special_character(test_string))  

def validate_name(text):
    if re.search(r'[^a-zA-Z\s]', text):
        raise ValueError("Name cannot contain numbers or special characters")
    
    cleaned = " ".join


    while True:
        pattern = r'[^a-zA-Z]'
        full_name = input("Enter full name: ").strip()
        if validate_name(text):
            return "Name cannot contain numbers or special characters. Please try again."
        else:
            continue