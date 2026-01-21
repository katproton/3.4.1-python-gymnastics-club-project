import csv


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
    name = input("Enter full name: ")
    for member in members:
        if member["Name"].lower() == name.lower():
            print("\n---Member Found---\n")
            print(member)
            break
    if member["Name"].lower() != name.lower():
        print("\n---Member Not Found---\n")


# Adds a new member
def add_new_member(members):
    new_member = {
        "ID": input("Enter ID: "),
        "Name": input("Enter full name: "),
        "Age": input("Enter age: "),
        "Gender": input("Enter gender: "),
        "Membership Type": input("Enter membership type (Recreational/Development/Competitive): "),
        "Join Date": input("Enter join date (YYY-MM-DD): "),
        "Monthly Fee (£ pm)": input("Enter monthly fee (£ pm): "),
        "Skill Level": input("Enter skill level (Beginner/Intermediate/Advanced): "),
        "Sessions Per Week": input("Enter number of sessions per week: ")
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