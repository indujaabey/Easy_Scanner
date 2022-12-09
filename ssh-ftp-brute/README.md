
# brutus

###  Authentication Bruteforcing Tool for Network Services 

Welcome to the brutus project repo! Brutus is a fast and simple way to bruteforce authentication on network services such as SSH, FTP, IMAP, and more.

If you have any suggestions, feedback, issues, etc... feel free to reach out or create an issue or pull request. 

____

### Contents

- [Features](#features)
- [Pre-Requisites](#pre-requisites)
- [Usage](#usage)
- [Demo](#demo)
- [Troubleshooting](#troubleshooting)
- [How to protect yourself?](#how-to-protect-yourself)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)
- [Acknowledgement](#acknowledgement)
- [Contact](#contact)

____

### Features

The tool currently supports the following services:

- [x] HTTP BASIC
- [x] SSH
- [x] FTP
- [x] IMAP
- [ ] SMTP
- [ ] MySQL

____

### Pre-Requisites

Clone the repository to your machine:

```git clone https://github.com/shehzade/brutus.git```

Install dependencies:

```pip3 install -r requirements.txt```

____

### Usage

```
python3 brutus.py [-m _EXECUTION_MODE] [-t _TARGET_IP] [-p _TARGET_PORT] [-d _TARGET_DIR] [-U _USER_LIST] [-P _PASS_LIST]

options:

  -h, --help          show this help message and exit
  -m _EXECUTION_MODE  Execution Mode [ftp | basic | ssh | imap]
  -t _TARGET_IP       IP address of the target (i.e. 192.168.22.100)
  -p _TARGET_PORT     Port of the network service (i.e. 22)
  -d _TARGET_DIR      Sub-directory path requiring BASIC authentication (i.e. /manager/html)
  -U _USER_LIST       Path to username list (i.e. /root/users.txt)
  -P _PASS_LIST       Path to password list (i.e. /
```

Tomcat Example: ```python3 brutus.py -m basic -t 192.168.100.200 -p 8080 -d /manager/html -U usernames.txt -P passwords.txt```

SSH Server Example: ```python3 brutus.py -m ssh -t 192.168.200.100 -p 2222 -U usernames.txt -P passwords.txt```

____

### Demo

Coming soon!

____

### Troubleshooting

If you encounter any issues, please raise them here in this repository.

____

### How to protect yourself?

1.  Implement account lockouts
2.  Blacklist malicious IP addresses
3.  Have a strong password policy

____

### Contributing

When contributing to this repository, please discuss the changes you wish to make via issue, [email](mailto:abdullahansari1618@outlook.com), or [LinkedIn](https://www.linkedin.com/in/abdullahansari0/).

____

### Disclaimer

 This project is only for educational purposes. Any kind of bad behavior conducted with this project is the user's own responsibility. I hereby forfeit responsiblity for any illegal actions.
 
____

### Acknowledgement 

 This project was born from a capstone excercise in TCM's [Python 101 course](https://academy.tcm-sec.com/p/python-101-for-hackers) but was overhauled to incorporate some new ideas I had and new skills I had learned.

____

### Contact
Author - Abdullah Ansari ©

Contact Info - [Email](mailto:abdullahansari1618@outlook.com)

____