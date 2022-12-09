import ipaddress
import sys
import os

# Argument validation

def validate_args(execution_mode, target_ip, target_port, target_dir, user_list, pass_list):

	# Check to see if any arg is left empty

	if execution_mode is None:

		print("\n[-] You must enter an execution mode! Brutus supports the following modes: [ftp | basic | ssh]")
		exit()

	if target_ip is None:
		
		print("\n[-] You must enter a valid IP address!")
		exit()
	
	if target_port is None:

		print("\n[-] You must enter a valid service port!")
		exit()

	if execution_mode == 'basic' and target_dir is None:

		print("\n[-] HTTP BASIC attacks require a valid sub-directory! (i.e. /manager/html)")
		exit()

	if user_list is None:

		print("\n[-] You must enter a valid path to a username list!")
		exit()

	if pass_list is None:

		print("\n[-] You must enter a valid path to a password list!")
		exit()

	# Check to see if the IP address is valid

	try:

		ip = ipaddress.ip_address(target_ip)

		pass

	except ValueError:

		print("\n[-] Your IP address in invalid!")
		exit()

	# Check to make sure that the port # is valid

	if (int(target_port) == 0 or int(target_port) > 65535):

		print("\n[-] The port number must be between 1 and 65535!")
		exit()

	# Check to make sure python can access the username and password lists

	if os.path.exists(user_list) and os.path.exists(pass_list):

		u = open(user_list, "r")
		p = open(pass_list, "r", encoding = "ISO-8859-1")

		usernames_imported = len(u.readlines())
		passwords_imported = len(p.readlines())

		print("\n[!] {} usernames and {} passwords have been imported!".format(usernames_imported, passwords_imported))

	else:

		print("\n[-] Error! Please ensure that the paths provided for the username and password lists are correct.")
		exit()
