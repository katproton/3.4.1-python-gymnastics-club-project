import csv
from datetime import datetime 
import amend_member
import add_member
from tabulate import tabulate
import sys

# ***DATA & STORAGE***

# Creating initial dict of 10 records of members
members = [{"ID": 1, "Name": "Emma Johnson", "Age": 12, "Gender": "F", "Membership Type": "Recreational",
          "Join Date": "2023-1-15", "Fee": 25, "Skill Level": "Beginner", "Sessions Per Week": 1},
{"ID": 2, "Name": "Jack Smith", "Age": 15, "Gender": "M", "Membership Type": "Development",
          "Join Date": "2022-3-20", "Fee": 35, "Skill Level": "Intermediate", "Sessions Per Week": 2},
{"ID": 3, "Name": "Olivia Brown", "Age": 10, "Gender": "F", "Membership Type": "Recreational",
          "Join Date": "2023-5-25", "Fee": 25, "Skill Level": "Beginner", "Sessions Per Week": 1},
{"ID": 4, "Name": "Ethan Davis", "Age": 17, "Gender": "M", "Membership Type": "Competitive",
          "Join Date": "2021-2-3", "Fee": 65, "Skill Level": "Advanced", "Sessions Per Week": 4},
{"ID": 5, "Name": "Ava Wilson", "Age": 13, "Gender": "F", "Membership Type": "Development",
          "Join Date": "2022-9-9", "Fee": 35, "Skill Level": "Intermediate", "Sessions Per Week": 2},
{"ID": 6, "Name": "Noah Taylor", "Age": 14, "Gender": "M", "Membership Type": "Development",
          "Join Date": "2023-6-14", "Fee": 35, "Skill Level": "Intermediate", "Sessions Per Week": 2},
{"ID": 7, "Name": "Mia Anderson", "Age": 9, "Gender": "F", "Membership Type": "Recreational",
          "Join Date": "2022-4-29", "Fee": 25, "Skill Level": "Beginner", "Sessions Per Week": 1},
{"ID": 8, "Name": "Lucas Thomas", "Age": 16, "Gender": "M", "Membership Type": "Competitive",
          "Join Date": "2023-4-3", "Fee": 65, "Skill Level": "Advanced", "Sessions Per Week": 4},
{"ID": 9, "Name": "Lily Moore", "Age": 11, "Gender": "F", "Membership Type": "Recreational",
          "Join Date": "2023-9-16", "Fee": 25, "Skill Level": "Beginner", "Sessions Per Week": 1},
{"ID": 10, "Name": "Hattie Jackson", "Age": 18, "Gender": "F", "Membership Type": "Competitive",
          "Join Date": "2023-1-7", "Fee": 65, "Skill Level": "Advanced", "Sessions Per Week": 4}]

fieldnames = ["ID", "Name", "Age", "Gender", "Membership Type", 
              "Join Date", "Fee", "Skill Level", 
              "Sessions Per Week"]


# Saves changes to csv file 
def save_members_to_csv(members):
    # opens members.csv and writes new data to file 
    with open("members.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(members)


# Function to load data from csv
def load_members():
    try: # try to find members.csv file to read and assign to members 
        with open("members.csv", mode="r", encoding="utf-8")as file:
            reader = csv.DictReader(file)
            members = list(reader)
        
        for m in members: # converts numbers to ints for compatibility for each member record
            m["ID"] = int(m["ID"])
            m["Age"] = int(m["Age"])
            m["Fee"] = int(m["Fee"])
            m["Sessions Per Week"] = int(m["Sessions Per Week"])

        return members 
    
    except FileNotFoundError:
        return [] # if the file isn't found, start with an empty list


# ***CRUD OPERATIONS***

# Views all members into a visual table 
def view_all_members(members):
    print(tabulate(members, headers="keys", tablefmt="fancy_grid"))

# Views a single member
def single_member(members):
    id = int(input("Enter member ID: "))
    # iterates to find matching id for user input
    for member in members:
        if member["ID"] == id:
            print("\n---Member Found---\n")
            rows = [(k, v) for k, v in member.items()] # finds all key, value pairs for member if id found and presents in visual table 
            print(tabulate(rows, headers=["Information", "Member Info"], tablefmt="fancy_grid"))
            return
    
    print("\n---Member Not Found---\n")


# Deletes a member
def delete_member(members):
    view_all_members(members)
    id = int(input("Enter ID to delete member: "))

    for member in members:
        if member["ID"] == id: # if finds a match between member id and user input
            while True:
                # checks deletion confirmation of correct member before deleting
                delete_confirmation = input(f"Are you sure you want to delete member: {member['ID']} {member['Name']}?\nY/N: ").upper().strip()
                # if user confirms deletion, remove member record and save changes, shows confirmation message
                if delete_confirmation == 'Y': 
                    members.remove(member)
                    save_members_to_csv(members)
                    print(f"\nMember ID: {member['ID']}, {member['Name']} successfully deleted and saved\n")
                    return
                # if user selects NO, displays message and cancels operation returning user to main menu 
                elif delete_confirmation == 'N':
                    print("Deletion cancelled")
                    return
                # if user enters anything other than valid option, will ask user again for valid input
                else:
                    print("Please enter Y or N")
    # displays message if user input id does not match any member id in records                    
    print("\nMember not found\n")

# summary of data
def summary(members):
    rows = [
        {"ID": m["ID"], "Name": m["Name"]} # only displays member's id and name for data summary
        for m in members
    ]
    # formats into visual table   
    print(tabulate(rows, headers="keys", tablefmt="fancy_grid"))
    
# ***MAIN MENU OPERATIONS*** 

def main_menu(members):
    loaded = load_members() # calls load function to load member data 
    if not loaded:
        save_members_to_csv(members) # if unsuccessful load calls save function 
    else:
        members = loaded # if successful load, assigns load to members
    # home page display format and on a loop to always allow user interaction
    while True:
        print("\n---Welcome to Silver Springs Gymnastics Club Home Page---\n")
        summary(members)
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
        choice = input("Select menu selection: ").strip()

        # calls appropriate function according to user selection followed by save function
        if choice == "1":
            view_all_members(members)
        elif choice == "2":
            single_member(members)
        elif choice == "3":
            add_member.add_new_member(members)
            save_members_to_csv(members)
            print("Any changes saved successfully")
        elif choice == "4":
            amend_member.amend_member(members)
            save_members_to_csv(members)
            print("Any changes saved successfully")
        elif choice == "5":
            delete_member(members)
        elif choice == "6":
            print("Saved. Goodbye!")
            save_members_to_csv(members)
            sys.exit()
        else:
            print("Invalid choice") # error message if user input is invalid 

# calls main menu function to start up programme 
main_menu(members)