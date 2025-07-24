🔹 1. Importing Modules
Use built-in modules with import, e.g., import math, import random.

You can import:

Entire module: import datetime

Specific functions: from math import sqrt

With alias: import os as operating

🔹 2. pip – Python Package Installer
Install packages: pip install requests

View installed packages: pip list

Uninstall: pip uninstall package-name

🔹 3. Virtual Environments (venv)
Create: python -m venv env

Activate:

Windows: env\Scripts\activate

macOS/Linux: source env/bin/activate

Deactivate: deactivate

Keeps project dependencies isolated.

🔹 4. Standard Library Modules
Module	Common Uses
math	Math functions like sqrt(), ceil()
random	Generate random numbers and choices
datetime	Work with current date/time
os	File system: os.mkdir(), os.getcwd()

🎯 Project: Dice Roller Game
Rolls two dice using random.

Adds up and tracks score.

Stores roll history with datetime.

Loop until user quits with 'q'.

