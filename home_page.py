import csv
import re
from datetime import datetime 
from tabulate import tabulate


# ***DATA & STORAGE***

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


# Saves changes to csv file 
def save_members_to_csv(members):
    with open("members.csv", mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["ID", "Name", "Age", "Gender", "Membership Type", "Join Date", 
                    "Monthly Fee (£ pm)", "Skill Level", "Sessions Per Week"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(members)


# Function to load data from csv
def load_members():
    with open("members.csv", mode="r", encoding="utf-8")as file:
        reader = csv.DictReader(file)
        return list(reader)


# validating new ID, automatically assigns next id in order
def generate_id(members):
    if not members:
        return "1"
    max_id = max(int(member["ID"]) for member in members)
    return str(max_id + 1)


# ***VALIDATIONS***

# boolean to check if contains numbers or special chars
def contains_numbers_or_specials(text):
       return bool(re.search(r'[^a-zA-Z\s]', text))

# validates NAME entry 
def enter_name():
    while True:
        full_name = input("Enter full name: ").strip().title() 

        if not full_name:
            print("Name is required")
            continue

        if contains_numbers_or_specials(full_name):
            print("Name cannot contain numbers or special characters. Please try again.")
            continue

        return full_name   
             
# validating AGE
def valid_age():
    while True:
        member_age = input("Enter age: ").strip()
        if member_age.isdigit():
            age = int(member_age)
            if 3 <= int(age) <= 17:
                return age
        print("Invalid entry. Members must be 3-17 years old. Try again")

# validating GENDER
def valid_gender():
    valid = ["F", "M"]
    while True:
        input_gender = input("Enter member gender (F/M): ").capitalize().strip()
        if input_gender in valid:
            return input_gender
        else:
            print("Invalid entry. Please try again (F/M)")

# validating DATE format
def valid_date():
    while True:
        user_date = input("Enter join date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(user_date, "%Y-%m-%d")
            return user_date
        except ValueError:
            print("Invalid date format. Please try again using YYYY-MM-DD")

# validating monthly FEE
def valid_fee():
    while True:
        input_fee = input("Enter monthly fee (£ pm): ")
        if input_fee.isdigit() and 25 <= int(input_fee) <= 80:
            return input_fee
        else:
            print("Invalid fee. Please try again (£25-£80)")

# validating MEMBERSHIP type
def valid_membership(): 
    valid = ["Recreational", "Development", "Competitive"]
    while True:
        user_membership = input("Enter membership type (Recreational/Development/Competitive): ").title().strip() 
        if user_membership in valid:
            return user_membership
        else:
            print("Invalid membership. Please try again using Recreational/Development/Competitive")

# validating SKILL level
def valid_skill_level():
    valid = ["Beginner", "Intermediate", "Advanced"]
    while True:
        member_level = input("Enter skill level (Beginner/Intermediate/Advanced): ").strip().title()
        if member_level in valid:
            return member_level
        else:
            print("Invalid skill level. Please try again using Beginner/Intermediate/Advanced")

# validating number of SESSIONS per week
def valid_sessions():
    while True:
        member_sessions = input("Enter number of sessions per week: ") 
        if member_sessions.isdigit() and 1 <= int(member_sessions) <= 7:
            return member_sessions
        else:
            print("Invalid entry. Members can attend 1-7 sessions per week")


# ***CRUD OPERATIONS***

# Views all members
def view_all_members(members):
    print(tabulate(members, headers="keys", tablefmt="fancy_grid"))
    # print("List of all members:\n")
    # for member in members:
    #     print(f"ID: {member["ID"]} | Name: {member["Name"]} | Age: {member["Age"]} | Gender: {member["Gender"]} | "
    #           f"Membership Type: {member["Membership Type"]} | Join Date: {member["Join Date"]} |\n Monthly Fee (£ pm): {member["Monthly Fee (£ pm)"]} | "
    #           f"Skill Level: {member["Skill Level"]} | Sessions Per Week: {member["Sessions Per Week"]}\n")


# Views a single member
def single_member(members):
    name = input("Enter full name: ").strip()

    for member in members:
        #converting names to lowercase to see if it exists
        if member["Name"].lower() == name.lower():
            print("\n---Member Found---\n")
            rows = [(k, v) for k, v in member.items()]
            print(tabulate(rows, headers=["Information", "Member Info"], tablefmt="fancy_grid"))
            break

    # once converted to lowercase, if there's no match that member doesn't exist    
    if member["Name"].lower() != name.lower():
        print("\n---Member Not Found---\n")


# Adds a new member
def add_new_member(members):
    name = enter_name()
    age = valid_age()
    gender = valid_gender()
    membership = valid_membership()
    date = valid_date() 
    fee = valid_fee()
    level = valid_skill_level()
    sessions = valid_sessions()
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


# Amend a member 
def amend_member(members):
    select_id = input("Enter the member ID to amend: ").strip()

    for member in members:
        if str(member.get("ID", "")).strip() == select_id:
            print("\nEditing member (press Enter to skip)")

            for key, value in member.items():
                if key == "ID":
                    continue

                new_value = input(f"{key}, [{value}]: ").strip()

                if not new_value:
                    continue

                elif key == "Name":
                    while True: 
                        new_name = new_value.title()

                        if contains_numbers_or_specials(new_name):
                            print("Invalid entry. Enter full name")
                            new_value = input(f"{key}, [{value}]: ").strip()
                            if not new_value:
                                break
                            continue
                        member[key] = new_name 
                        break                      
                            
                elif key == "Age":
                   while True:
                       new_age = new_value.strip()

                       if new_age.isdigit() and 3 <= int(new_age) <= 17:
                           member[key] = new_age
                           break

                       print("Please try again. Enter a valid age")   
                       new_value = input(f"{key}, [{value}]: ").strip()        
                       if not new_value:
                           break
                       
                elif key == "Gender":
                    valid = ["F", "M"]
                    while True:
                        new_gender = new_value.strip()

                        if new_gender in valid:
                            member[key] = new_gender
                            break
                        print("Invalid entry. Please try again (F/M)")
                        new_value = input(f"{key}, [{value}]: ").strip().capitalize()
                        if not new_value:
                            break


                elif key == "Membership Type":
                    valid = ["Recreational", "Development", "Competitive"]
                    while True:
                        new_membership = new_value.title() 

                        if new_membership in valid:
                            member[key] = new_membership
                            break
                        
                        print("Invalid membership. Please try again using Recreational/Development/Competitive")   
                        new_value = input(f"{key}, [{value}]: ").strip()  
                        if not new_value:
                            break 


                elif key == "Join Date":
                    while True: 
                        try:
                            datetime.strptime(new_value, "%Y-%m-%d")
                            member[key] = new_value
                            break
                        except ValueError:
                            print("Invalid date format. Please try again using YYYY-MM-DD")
                            new_value = input(f"{key}, [{value}]: ").strip()
                            if not new_value:
                                break


                elif key == "Monthly Fee (£ pm)":
                    while True:
                        new_fee = new_value.strip()

                        if new_fee.isdigit() and 25 <= int(new_fee) <= 80:
                            member[key] = new_fee
                            break
                        print("Invalid fee. Please try again (£25-£80)")
                        new_value = input(f"{key}, [{value}]: ").strip()
                        if not new_value:
                            break
              

                elif key == "Skill Level":
                    valid = ["Beginner", "Intermediate", "Advanced"]
                    while True:
                        new_level = new_value.title()

                        if new_level in valid:
                            member[key] = new_level
                            break

                        print("Invalid skill level. Please try again using Beginner/Intermediate/Advanced")
                        new_value = input(f"{key}, [{value}]: ").strip()
                        if not new_value:
                            break


                elif key == "Sessions Per Week":
                    while True:
                        new_sessions = new_value.strip()

                        if new_sessions.isdigit() and 1 <= int(new_sessions) <= 7:
                            member[key] = new_sessions
                            break
                        print("Invalid entry. Members can attend 1-7 sessions per week")
                        new_value = input(f"{key}, [{value}]: ").strip()
                        if not new_value:
                            break                

                else:
                    member[key] = new_value

            print("\n---Member updated successfully---\n")
            return

    print("\n---Member not found---\n")


# Deletes a member
def delete_member(members):
    view_all_members(members)
    id = input("Enter ID to delete member: ").strip()

    for member in members:
        if str(member.get("ID", "")).strip() == id:
            members.remove(member)
            print(f"\nMember ID: {member['ID']}, {member['Name']} successfully deleted\n")
            return
        
    print("\nMember not found\n")


# ***MAIN MENU OPERATIONS*** 

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
        elif choice == "4":
            amend_member(members)
        elif choice == "5":
            delete_member(members)
        elif choice == "6":
            print("Goodbye!")
            save_members_to_csv(members)
            break
        else:
            print("Invalid choice")


members = load_members() # assign load function to members  
main_menu(members) # so on running main menu 'members' is reading from csv to get up-to-date records