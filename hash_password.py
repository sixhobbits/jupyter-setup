import codecs
import os

from hashlib import sha512

import config

# Generate random bytes for the salt
thebytes = os.urandom(100)
hexstr = str(codecs.encode(thebytes, 'hex'))
salt = hexstr[3:14]

# Hash the password with the salt
tohash = config.password + salt
tohash = tohash.encode("utf8")
hashed = sha512(tohash).hexdigest()

# Remove the config.py file which contains  the plaintext password
for fn in ("config.py", "config.pyc"):
    try:
        os.remove(fn)
    except OSError as e:
        print e

# Output in correct format
print("sha512:{}:{}".format(salt, hashed))
