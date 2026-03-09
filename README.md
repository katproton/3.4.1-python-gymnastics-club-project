**SILVER SPRINGS GYMNASTICS CLUB Member Management Application**

**Description**

This is a console-based Python application that allows staff at Silver Springs Gymnastics Club to manage member records.
The system allows users to view, add, amend, and delete member records which are stored in a csv file.
By creating this app, it allows the gymnastics club to transition from paper based to digital record keeping, reducing the likelihood of human-errors and increasing efficiency and business. 

**Requirements**

Python 3.14.0
tabulate
pytest 

**Installing dependencies**

pip install tabulate pytest

**Running the application**

Open a terminal in the project folder and run:

python home_pg_v2.py

**Running automated tests**

To run the automated unit tests:

python -m pytest

**Project structure**

home_pg_v2.py      - Main menu and program control
add_member.py      - Add new members
amend_member.py    - Update existing members
validations.py     - Input validation functions
members.csv        - Member data storage
tests/             - Automated pytest tests
test_generate_id.py
test_inpupt_required.py
test_validate_name.py