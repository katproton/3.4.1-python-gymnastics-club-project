import re
from datetime import datetime

# ***VALIDATIONS***

# input required for add member 
def input_required(prompt, validator):
    while True:
        value = prompt_validated(prompt, validator=validator, allow_blank=False)

        if value is None:
            print("Field is required")
            continue
        return value

# prompt validator
def prompt_validated(prompt:str, validator=None, allow_blank=True):
    while True:
        raw = input(prompt).strip()

        if raw == "" and allow_blank:
            return None 
        
        if validator is None:
            return raw

        try:
            return validator(raw)
        except ValueError as e:
            print(f"Invalid entry {e}")

# validating new ID, automatically assigns next id in order
def generate_id(members)->int:
    if not members:
        return 1
    max_id = max(int(member["ID"]) for member in members)
    return max_id + 1

# validates NAME entry 
def valid_name(value):
    value = value.strip().title()

    if re.search(r'[^a-zA-Z\s]', value):
        raise ValueError("Name must only contain alphabetic characters")
    return value  
             
# validating AGE
def valid_age(value:str)->int:
    value = value.strip()
    if not value.isdigit():
        raise ValueError("Age must be a number")
    age = int(value)
    if not (3 <= age <= 17):
        raise ValueError("Member must be 3-17 years old")
    return age
    
# validating GENDER
def valid_gender(value):
    value = value.strip().upper()

    if value not in ["F", "M"]:
        raise ValueError("Must be F or M")
    
    return value

# validating DATE format
def valid_date(value:str)->datetime:
    try:
        return datetime.strptime(value.strip(), "%Y-%m-%d").date()
    except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD")

# validating monthly FEE
def valid_fee(value:str)->int:
    value = value.strip()

    if not value.isdigit():
        raise ValueError("Fee must be a number")
    
    fee = int(value)
    if not (25 <= fee <= 80):
        raise ValueError("Membership fee must be £25-£80")
    
    return fee 

# validating MEMBERSHIP type
def valid_membership(value): 
    value = value.strip().title()

    if value not in ["Recreational", "Development", "Competitive"]:
        raise ValueError("Memberships must be Recreational/Development/Competitive")
    
    return value
    
# validating SKILL level
def valid_skill_level(value):
    value = value.strip().title()

    if value not in ["Beginner", "Intermediate", "Advanced"]:
        raise ValueError("Member must be Beginner/Intermediate/Advance")
    return value
      
# validating number of SESSIONS per week
def valid_sessions(value:str)->int:
    value = value.strip()

    if not value.isdigit():
        raise ValueError("Sessions must be a number")
    
    sessions = int(value)
    if not (1 <= sessions <= 7):
        raise ValueError("Sessions must be 1-7")
    
    return sessions 