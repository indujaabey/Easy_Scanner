#!/usr/bin/python
import requests
from time import sleep
import os.path

URL = input('URL?\n')
w_path = input('Wordlist path?\n')

def start():
	print("Starting Attack On : " + URL)
	sleep(2)
	print("Loading Wordlist...")
	if os.path.isfile(str(w_path)) == True: 
		print("Wordlist Loaded Succesfully")
		sleep(2)
		with open(str(w_path)) as wordlist:
			read_line = wordlist.readlines()
		for read_each_line in read_line:
			path_of_url = URL + "/" + read_each_line
			get_url = requests.get(path_of_url).status_code
			if get_url == 200:
				print( path_of_url + " => " + "Found!" + "\n")
			elif get_url == 404:
				print(path_of_url + " => " + "Not Found!" + "\n")
			else:
				print(path_of_url + " => " + get_url + "\n")
	else:
		print("Error In Loading Wordlist,Check Permissions Or Path Of Your File")
start()
