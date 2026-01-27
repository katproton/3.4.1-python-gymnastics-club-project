import csv
import re
from datetime import datetime 


# Creating initial dict of 10 records of members
members = [{"ID": 1, "Name": "Emma Johnson", "Age": 12, "Gender": "F", "Membership Type": "Recreational",
          "Join Date": "2023-1-15", "Monthly Fee (£ pm)": 25, "Skill Level": "Beginner", "Sessions Per Week": 1},
{"ID": 2, "Name": "Jack Smith", "Age": 15, "Gender": "M", "Membership Type": "Development",
          "Join Date": "2022-3-20", "Monthly Fee (£ pm)": 35, "Skill Level": "Intermediate", "Sessions Per Week": 2},
{"ID": 3, "Name": "Olivia Brown", "Age": 10, "Gender": "F", "Membership Type": "Recreational",
          "Join Date": "2023-5-25", "Monthly Fee (£ pm)": 25, "Skill Level": "Beginner", "Sessions Per Week": 1},
{"ID": 4, "Name": "Ethan Davis", "Age": 17, "Gender": "M", "Membership Type": "Competitive",
          "Join Date": "2021-2-3", "Monthly Fee (£ pm)": 65, "Skill Level": "Advanced", "Sessions Per Week": 4},
{"ID": 5, "Name": "Ava Wilson", "Age": 13, "Gender": "F", "Membership Type": "Development",
          "Join Date": "2022-9-9", "Monthly Fee (£ pm)": 35, "Skill Level": "Intermediate", "Sessions Per Week": 2},
{"ID": 6, "Name": "Noah Taylor", "Age": 14, "Gender": "M", "Membership Type": "Development",
          "Join Date": "2023-6-14", "Monthly Fee (£ pm)": 35, "Skill Level": "Intermediate", "Sessions Per Week": 2},
{"ID": 7, "Name": "Mia Anderson", "Age": 9, "Gender": "F", "Membership Type": "Recreational",
          "Join Date": "2022-4-29", "Monthly Fee (£ pm)": 25, "Skill Level": "Beginner", "Sessions Per Week": 1},
{"ID": 8, "Name": "Lucas Thomas", "Age": 16, "Gender": "M", "Membership Type": "Competitive",
          "Join Date": "2023-4-3", "Monthly Fee (£ pm)": 65, "Skill Level": "Advanced", "Sessions Per Week": 4},
{"ID": 9, "Name": "Lily Moore", "Age": 11, "Gender": "F", "Membership Type": "Recreational",
          "Join Date": "2023-9-16", "Monthly Fee (£ pm)": 25, "Skill Level": "Beginner", "Sessions Per Week": 1},
{"ID": 10, "Name": "Hattie Jackson", "Age": 18, "Gender": "F", "Membership Type": "Competitive",
          "Join Date": "2023-1-7", "Monthly Fee (£ pm)": 65, "Skill Level": "Advanced", "Sessions Per Week": 4}]


# Function to initially write the dict to a csv file. Only needed once
def save_members_to_csv(members):
    with open("members.csv", mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["ID", "Name", "Age", "Gender", "Membership Type", "Join Date", 
                    "Monthly Fee (£ pm)", "Skill Level", "Sessions Per Week"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(members)
# save_members_to_csv(members)


# Function to load data from csv
def load_members(members):
    members = []
    with open("members.csv", mode="r", encoding="utf-8")as file:
        reader = csv.DictReader(file)
        members = list(reader)
    return members

load_members(members)



# Views all members
def view_all_members(members):
    print("List of all members:\n")
    for member in members:
        print(f"ID: {member["ID"]} | Name: {member["Name"]} | Age: {member["Age"]} | Gender: {member["Gender"]} | "
              f"Membership Type: {member["Membership Type"]} | Join Date: {member["Join Date"]} |\n Monthly Fee (£ pm): {member["Monthly Fee (£ pm)"]} | "
              f"Skill Level: {member["Skill Level"]} | Sessions Per Week: {member["Sessions Per Week"]}\n")


# Views a single member
def single_member(members):
    name = input("Enter full name: ").strip()
    for member in members:
        # converting names to lowercase to see if it exists
        if member["Name"].lower() == name.lower():
            print("\n---Member Found---\n")
            print(member)
            break
    # once converted to lowercase, if there's no match that member doesn't exist    
    if member["Name"].lower() != name.lower():
        print("\n---Member Not Found---\n")


# boolean to check if contains numbers or special chars
def contains_numbers_or_specials(text):
       return bool(re.search(r'[^a-zA-Z\s]', text))

# validates name entry 
def enter_name():
    while True:
        full_name = input("Enter full name: ").strip().title()
        if contains_numbers_or_specials(full_name):
            print("Name cannot contain numbers or special characters. Please try again.")
        return full_name 

# validating age
def valid_age():
    while True:
        member_age = int(input("Enter age: "))
        if 3 <= member_age <= 17:
            return member_age
        else:
            print("Invalid entry. Members must be 3-17 years old. Try again")


# checks date is correct format
def valid_date():
    while True:
        user_date = input("Enter join date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(user_date, "%Y-%m-%d")
            return user_date
        except ValueError:
            print("Invalid date format. Please try again using YYYY-MM-DD")

# validating membership type
def valid_membership(): 
    valid = ["Recreational", "Development", "Competitive"]
    while True:
        user_membership = input("Enter membership type (Recreational/Development/Competitive): ").title().strip() 
        if user_membership in valid:
            return user_membership
        else:
            print("Invalid membership. Please try again using Recreational/Development/Competitive")

# validating skill level
def valid_skill_level():
    valid = ["Beginner", "Intermediate", "Advanced"]
    while True:
        member_level = input("Enter skill level (Beginner/Intermediate/Advanced): ").strip().title()
        if member_level in valid:
            return member_level
        else:
            print("Invalid skill level. Please try again using Beginner/Intermediate/Advanced")

# validating number of sessions per week
def valid_sessions():
    while True:
        member_sessions = int(input("Enter number of sessions per week: ")) 
        if 1 <= member_sessions <= 7:
            return member_sessions
        else:
            print("Invalid entry. Member can only attend 1-7 sessions per week")

# Adds a new member
def add_new_member(members):
    member_id = input ("Enter ID: ")
    name = enter_name()
    age = valid_age()
    gender = input("Enter gender: ")
    membership = valid_membership()
    date = valid_date() 
    fee = input("Enter monthly fee (£ pm): ")
    level = valid_skill_level()
    sessions = valid_sessions()
    new_member = {
        "ID": member_id,
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
    print("New member added successfully")


# Deletes a member
def delete_member(members):
    view_all_members(members)
    name = input("Enter full name of the member you want to delete: ")
    for member in members:
        if member["Name"] == name:
            members.remove(member)
            print(f"{member["Name"]} successfully deleted")


def main_menu(members):
    while True:
        print("---Welcome to Silver Springs Gymnastics Club Home Page---\n")
        print(""" 
            ---Menu Options--- 

            1. View all members 
            2. View a single member
            3. Add a new member
            4. Amend a member
            5. Delete a member
            6. Exit

            """)

        # Allows user to input choice form main menu
        choice = input("Select menu selection: ")

        if choice == "1":
            view_all_members(members)
        elif choice == "2":
            single_member(members)
        elif choice == "3":
            add_new_member(members)
        elif choice == "5":
            delete_member(members)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

main_menu(members)