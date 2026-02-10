# from datetime import datetime 
# import re
from validations import valid_age, valid_name, valid_gender, valid_membership, valid_date, valid_fee, valid_skill_level, valid_sessions, prompt_validated
from display_all import view_all_members

# assigning fields to validators
field_validators = {
    "Name": valid_name,
    "Age": valid_age,
    "Gender": valid_gender,
    "Membership Type": valid_membership,
    "Join Date": valid_date,
    "Monthly Fee (£ pm)": valid_fee,
    "Skill Level": valid_skill_level,
    "Sessions Per Week": valid_sessions
}


# amend member
def amend_member(members):
    view_all_members(members)

    select_id = int(input("Enter the member ID to amend: "))

    for member in members:
        if member["ID"] == select_id:
            print("\nEditing member (press Enter to skip)")

            for key, value in member.items():
                if key == "ID":
                    continue

                validator = field_validators.get(key)

                new_value = prompt_validated(f"{key}, [{value}]: ", validator=validator, allow_blank=True)

                if new_value is None:
                    continue
                member[key] = new_value

            print("\n---Member updated successfully---\n")
            return

    print("\n---Member not found---\n")