import paramiko
import socket

def ssh_login(ip_addr, port, username, password):

	# Build client and set policy

	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	# Actual login code

	try:

		auth = client.connect(ip_addr, port, username=f'{username}', password=f'{password}', timeout=5)

	# If the authentication fails

	except paramiko.AuthenticationException:

		return False

	# If the server times out

	except socket.error:

		print("\nCould not connect to SSH server!\n")
		exit()

	# If there is some other random error

	except Exception as e:

		print("Unknown error occured with the SSH server!\n")
		exit()

	# If the authentication is successful

	else:
			
		return True