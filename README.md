# Keylogger

This is a simple keylogging program developed in Python for educational purposes only. This project was created to understand how malicious software operates and to improve security awareness. **It is not intended for any unethical or illegal use.**

## Features
- Logs keystrokes and saves them to a `keylog.txt` file.
- Special keys (Ctrl, Shift, etc.) are ignored.
- After 180 keystrokes, the log file is sent via email using SMTP (port 465).
- The log file is overwritten after each email is sent to maintain minimal storage usage.

## Setup and Configuration

In order to setup and configure the program, users must follow the following steps:

1. Clone or download the repository.
2. Change the SMTP_SERVER to the server that you are going to be using
3. Edit the script to include your sender and recipient email addresses.
4. **Set up an App Password** for the sender email to allow Python to send emails securely. This is required since many email providers block direct password authentication. Refer to your email provider's documentation on how to generate an app password.
5. It is suggested that users set the App Password as an environmental variable for increased security.
6. Run the script:
```sh
python keylogger.py
```
5. In order to end the script, the user can press the "Esc" key.

## Disclaimer
This software is for educational and research purposes only. Unauthorized use of keyloggers may violate privacy laws and terms of service.

