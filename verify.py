# symmetrical_meme, a resource management system
# Copyright (C) 2023 Allied Islands Software
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import hashlib
import getpass
import json
import uuid
import warnings

ESC = chr(27)

def generate_hash(password, verify=False, salt=None):

    """Generates a salted hash from the given password."""

    if salt == None:
        salt = uuid.uuid4().hex

    hash = hashlib.pbkdf2_hmac('sha256',
                               password.encode('utf-8'),
                               salt.encode('utf-8'),
                               100000).hex()
    if verify == False:
        return json.dumps({'hash': hash, 'salt': salt})
    else:
        return hash

def verify_password(input_password, correct_hash, salt):

    """Verifies a salted and hashed password."""

    if generate_hash(input_password, verify=True, salt=salt) == correct_hash:
        return True
    else:
        return False

def login():

    """Logs in a user."""

    warnings.filterwarnings("error")

    print("Allied Islands Resource Management System")
    print("Version 0.0a0")
    print("Welcome. Please log in to continue.")
    print()

    username = input("Username: ")
    try:
        password = getpass.getpass(prompt="Password: ")
    except getpass.GetPassWarning:
        print(f"{ESC}[37,41m[L1] Password entry is not secure. The program cannot continue.")
        input(f"Press Enter to quit{ESC}[0m")
        quit()

    # Load hash and salt here from file

    correct_hash = "c8c091427b033146202fec00a39cdd72b1c836fe8e3a19dfb44ac2c06fb4c988"
    salt = "568083a12c40495db6a6355ea6e3ed71"

    if verify_password(password, correct_hash, salt):
        print()
        print(f"Welcome, {username}")
    else:
        print()

login()
