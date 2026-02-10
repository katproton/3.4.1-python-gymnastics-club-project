SILVER SPRINGS GYMNASTICS CLUB APPLICATION

Overview

I have created a command line menu application for a Gymnastics Club that allows users to navigate through a menu to perform various tasks to help in the running of the business. Such as viewing current member data, searching a specific member for information, adding new joiners, amending current member data, and deleting members from the system. By creating this app, it allows the gymnastics club to transition from paper based to digital record keeping, reducing the likelihood of human-errors and increasing efficiency and business. 

Requirements

- At least 10 records with a minimum of 8 fields
- The data can be hard-coded or sourced externally from .CSV or .TXT files
- I chose to hard-code the data and write it to a CSV file, and any changes made to the data can be saved to the CSV upon exiting the application
- When the application launches, the user is presented with a home page showing a menu of options, including viewing all data records as required
- The menu shows all of the required options:
    - View all members
    - View a single member
    - Add a member
    - Amend a member
    - Delete a member
    - Exit
- Validation checks and error handling to guide users effectively using prompts
- Structure the application by dividing its functionality into appropriate, manageable modules or components
- Follow best programming practices

UML DIAGRAMS HERE

Data Dictionary

Below I have put together a data dictionary to document all the data used in the system along with their associated validation rules that have
been applied on user input. All data items below have been stripped of extra white spaces upon user input for validation checks. 

Data Item: ID
Description: Unique identifier for each member
Data type: Integer
Validation Rules: Must be numeric and unique. Automatically assigns next integer when adding a new member and doesn't allow you to amend.

Data Item: Name
Description: Full name of the member
Data Type: String 
Validation Rules: Must not be empty and must contain alphabetical characters only

Data Item: Age
Description: Member's age
Data Type: Integer
Validation Rules: Must be a number and between 3 - 17 inclusive.

Data Item: Gender
Description: Member's gender
Data Type: String
Validation Rules: Only 2 valid options given: F/M, any other input is invalid. Capitalises the input to validate.

Data Item: Membership Type
Description: The level of membership the member holds
Data Type: String
Validation Rules: Only the valid options given are accepted. Formats valid inputs to 'title' for validation.

Data Item: Join Date
Description: Date the member joined
Data Type: String (YYYY-MM-DD)
Validation Rules: Takes the user's input and checks it against the valid date format. 

Data Item: Monthly Fee (£ pm)
Description: Member's monthly membership fee
Data Type: Integer
Validation Rules: Checks if the input is a number and between 25 - 80 inclusive.

