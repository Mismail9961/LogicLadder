File Handling & Exception Handling :

📄 1. File Handling in Python
Python provides built-in functions to handle files, such as:

open(filename, mode): Opens a file.

Modes:

'r' – Read (default)

'w' – Write (overwrites file)

'a' – Append

'x' – Create file (error if exists)

'b' – Binary mode

't' – Text mode (default)

read(), readline(), readlines(): Reading files

write(), writelines(): Writing to files

close(): Always close files after use


⚠️ 2. Exception Handling
Exceptions are errors that occur during execution. Python lets you handle them gracefully using:

try:
    # code that might raise an error
except SomeError:
    # handling code
else:
    # if no error occurs
finally:
    # always executes


🔍 Common Exception Types :

FileNotFoundError

ZeroDivisionError

TypeError

ValueError

IOError