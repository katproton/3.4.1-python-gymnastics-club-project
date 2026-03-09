# from datetime import datetime 
# import re
from validations import valid_age, valid_name, valid_gender, valid_membership, valid_date, valid_fee, valid_skill_level, valid_sessions, prompt_validated
# from display_all import view_all_members

# maps each member data field to its corresponding validation function 
field_validators = {
    "Name": valid_name,
    "Age": valid_age,
    "Gender": valid_gender,
    "Membership Type": valid_membership,
    "Join Date": valid_date,
    "Fee": valid_fee,
    "Skill Level": valid_skill_level,
    "Sessions Per Week": valid_sessions
}

# maps internal data field names to user-friendly prompt labels 
field_labels = {
    "Name": "Name",
    "Age": "Age (3-17)",
    "Gender": "Gender (f/m)",
    "Membership Type": "Membership Type. Enter r/d/c (Recreational/Development/Competitive)",
    "Join Date": "Join Date (YYYY-MM-DD)",
    "Fee": "Monthly Fee (£25-£80 pm)",
    "Skill Level": "Skill Level. Enter b/i/a (Beginner/Intermediate/Advanced)",
    "Sessions Per Week": "Sessions Per Week (1-7)"
}

# amend member
def amend_member(members):

    select_id = int(input("Enter the member ID to amend: "))

    # iterates through each member to find matching id
    for member in members:
        if member["ID"] == select_id:
            print("\nEditing member (press Enter to skip)")

            for key, value in member.items():
                if key == "ID":
                    continue
                
                # gets the keys from the field validators and assigns to 'validator'
                validator = field_validators.get(key)

                # instructing to find a key name from 'field labels' 
                # if it exists, otherwise use default key 
                label = field_labels.get(key, key)

                # if user skips, blank is allowed and returns None
                new_value = prompt_validated(f"{label}, [{value}]: ", validator=validator, allow_blank=True)

                # if new value entered, assign new value
                # otherwise None is allowed and keep original value
                if new_value is not None:
                    member[key] = new_value

            print("\n---Member updated successfully---\n")
            return

    print("\n---Member not found---\n")