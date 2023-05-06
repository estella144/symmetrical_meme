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
import json
import uuid

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
