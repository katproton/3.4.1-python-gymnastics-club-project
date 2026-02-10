# import re
# from datetime import datetime 
from validations import (
    valid_age, valid_name, valid_gender, valid_membership, 
    valid_date, valid_fee, valid_skill_level, 
    valid_sessions, generate_id, input_required, prompt_validated)


# Adds a new member
def add_new_member(members):
    name = input_required("Name: ", valid_name)
    age = input_required("Age: ", valid_age)
    gender = input_required("Gender: ", valid_gender)
    membership = input_required("Membership Type: ", valid_membership)
    date = input_required("Join Date: ", valid_date)
    fee = input_required("Monthly Fee (£ pm): ", valid_fee)
    level = input_required("Skill Level: ", valid_skill_level)
    sessions = input_required("Sessions Per Week: ", valid_sessions)
   
    new_member = {
        "ID": generate_id(members), # automatically generates next id in order
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Membership Type": membership,
        "Join Date": date,
        "Monthly Fee (£ pm)": fee,
        "Skill Level": level,
        "Sessions Per Week": sessions
    }
    members.append(new_member)
    print("\n---New member added successfully---\n")
