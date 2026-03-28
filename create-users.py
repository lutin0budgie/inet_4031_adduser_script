#!/usr/bin/python3

#INET4031
#Disha Ghosh
#3/28/26

#Importing modules:
# os -> used to run system (Linux) commands
# re -> used for pattern matching (regular expressions)
# sys -> used to read input from stdin (the input file)
import os
import re
import sys

def main():
	#loop through each line from the input file (via stdin)
	for line in sys.stdin:
		#check if the line starts with '#' (used for comments/skip lines in input file)
		match = re.match("^#", line)
		#split the line into fields using ':' as delimiter
		fields = line.strip().split(':')
		#skip lines that are comments OR do not have exactly 5 fields (invalud input)
		if match or len(fields) != 5:
			continue


		#extract user data from fields (maps to entries in /etc/passwd)
		username = fields[0]
		password = fields[1]
		gecos = "%s %s,,," % (fields[3], fields[2])  #first + last name format

		#split group list (comma separated) into individual groups
		groups = fields[4].split(',')

		#print status msg for user creation
		print("==> Creating account for %s..." % (username))
		cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

		print(cmd)
		#os.system(cmd)

		#build command to set user password using echo + passwd
		print("==> Setting the password for %s..." % (username))
		cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

		#for dry run: print command instead of executing
		print(cmd)
		#os.system(cmd)

		#loop thru each group and assign user
		for group in groups:
			#if group is not '-' (which means no group), add user to group
			if group != '-' :
				print("==> Assigning %s to the %s group..." % (username,group))
				cmd = "/usr/sbin/adduser %s %s %" (username, group)
				print(cmd)
				#os.system(cmd)

#run main function
if __name__ == '__main__':
	main()
