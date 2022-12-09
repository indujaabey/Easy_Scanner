import requests

def http_login(target_ip, target_port, target_dir, username, password):

	target_url = f'http://{target_ip}:{target_port}{target_dir}'

	auth_request = requests.get(target_url, auth=(username, password))

	if auth_request.status_code == 200:

		return True 
		
	else:

		return False