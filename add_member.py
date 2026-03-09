from validations import (
    valid_age, valid_name, valid_gender, valid_membership, 
    valid_date, valid_fee, valid_skill_level, 
    valid_sessions, generate_id, input_required, prompt_validated)


# Adds a new member
def add_new_member(members):
    # calls imported function from validations to ensure all fields are filled in 
    # calls field validating function for corresponding fields to ensure valid data is added 
    name = input_required("Name: ", valid_name)
    age = input_required("Age (3-17): ", valid_age)
    gender = input_required("Gender (f/m): ", valid_gender)
    membership = input_required("Membership Type. Enter r/d/c (Recreational/Development/Competitive): ", valid_membership)
    date = input_required("Join Date (YYYY-MM-DD): ", valid_date)
    fee = input_required("Monthly Fee (£25-£80 pm): ", valid_fee)
    level = input_required("Skill Level. Enter b/i/a (Beginner/Intermediate/Advanced): ", valid_skill_level)
    sessions = input_required("Sessions Per Week (1-7): ", valid_sessions)
   
    # assigns above data to new member dict
    new_member = {
        "ID": generate_id(members), # automatically generates next id in order
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Membership Type": membership,
        "Join Date": date,
        "Fee": fee,
        "Skill Level": level,
        "Sessions Per Week": sessions
    }
    members.append(new_member)
    print("\n---New member added successfully---\n")
