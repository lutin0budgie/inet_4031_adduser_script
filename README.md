#inet_4031_adduser_scripts

This repository contains Python scripts that automate Linux account creation.

##Files
create-users.py
Original script that reads input stdin and creates users using Linux adduser commands.

create-users2.py
Modified version of the script that includes a dry-run feature.

create-users.input
Input file containing user account info in this format:
username:password:last:first:groups

##Dry Run Logic
When running create-users2.py, the script asks:

Dry run? (Y/N)

If Y is entered:
the commands are printed but NOT executed.

If N is entered:
the commands run and users are created.

This allows testing the script safely before making system changes.

##Author

Disha Ghosh
INET 4031
Spring 2026
