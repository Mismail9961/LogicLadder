1. os module
Used to interact with the operating system.

Common Functions:

os.listdir(path) – list files/folders in a directory

os.rename(old_name, new_name) – rename a file/folder

os.remove(file) – delete a file

os.path.exists(path) – check if a path exists

2. shutil module
Used for high-level file operations.

Common Functions:

shutil.copy(src, dst) – copy a file

shutil.move(src, dst) – move a file

shutil.rmtree(path) – delete a directory recursively

3. time module
Used to handle time-based functions.

Common Functions:

time.sleep(seconds) – pause execution

time.strftime("%Y-%m-%d %H:%M:%S") – format time

time.localtime() – get current local time

4. smtplib module
Used to send emails through SMTP.

Steps to Send Email:

Login to SMTP server

Compose email (with email.message)

Send using smtplib.SMTP_SSL or SMTP