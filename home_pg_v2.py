import csv
from datetime import datetime 
import amend_member
import add_member
from tabulate import tabulate

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
    with open("members.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(members)


# Function to load data from csv
def load_members():
    try:
        with open("members.csv", mode="r", encoding="utf-8")as file:
            reader = csv.DictReader(file)
            members = list(reader)
        
        for m in members: # converts numbers to ints for compatibility 
            m["ID"] = int(m["ID"])
            m["Age"] = int(m["Age"])
            m["Fee"] = int(m["Fee"])
            m["Sessions Per Week"] = int(m["Sessions Per Week"])

        return members 
    except FileNotFoundError:
        return [] # if the file isn't found, start with an empty list


# ***CRUD OPERATIONS***

# Views all members
def view_all_members(members):
    print(tabulate(members, headers="keys", tablefmt="fancy_grid"))
    # print("List of all members:\n")
    # for member in members:
    #     print(f"ID: {member["ID"]} | Name: {member["Name"]} | Age: {member["Age"]} | Gender: {member["Gender"]} | "
    #           f"Membership Type: {member["Membership Type"]} | Join Date: {member["Join Date"]} |\n Fee: {member["Fee"]} | "
    #           f"Skill Level: {member["Skill Level"]} | Sessions Per Week: {member["Sessions Per Week"]}\n")


# Views a single member
def single_member(members):
    id = int(input("Enter member ID: "))

    for member in members:
        if member["ID"] == id:
            print("\n---Member Found---\n")
            rows = [(k, v) for k, v in member.items()]
            print(tabulate(rows, headers=["Information", "Member Info"], tablefmt="fancy_grid"))
            return
    
    print("\n---Member Not Found---\n")


# Deletes a member
# ADD IN ARE YOU SURE YOU WANT TO DELETE ETC...
def delete_member(members):
    view_all_members(members)
    id = int(input("Enter ID to delete member: "))

    for member in members:
        if member["ID"] == id:
            members.remove(member)
            save_members_to_csv(members)
            print(f"\nMember ID: {member['ID']}, {member['Name']} successfully deleted and saved\n")
            return
        
    print("\nMember not found\n")

# summary of data
def summary(members):
    rows = [
        {"ID": m["ID"], "Name": m["Name"]}
        for m in members
    ]
    print(tabulate(rows, headers="keys", tablefmt="fancy_grid"))
    
# ***MAIN MENU OPERATIONS*** 

def main_menu(members):
    loaded = load_members()
    if not loaded:
        save_members_to_csv(members)
    else:
        members = loaded
    
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
            break
        else:
            print("Invalid choice")


main_menu(members)