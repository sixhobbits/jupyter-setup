"""This will generate a config file for your Jupyter notebook.
  
  Certificate 
  -----------
  The accompanying setup.sh script will use openssl to generate a certificate and key file. These will be placed in i
  your ~/.ssh directory. This script assumes that the setup.sh script is unmodified and configures the Jupyter 
  settings accordingly.

  Password 
  --------
  The password you use to access your notebook server should be stored in a file named config.py which should be in 
  the same directory as this script. In config.py you should have a variable called password. e.g.
  password = "mypassword"
  
  This script will automatically delete the config.py file after use.

  Note that password generation method using notebook.auth.passwd recommended by the Jupyter docs uses sha1. Due to
  recent security concerns with the sha1 hashing protocol, we use sha512 instead, saving the password with a random 
  salt in the same format required by Jupyter.
 
  This script requires Python 3.4+ and has only been tested on Ubuntu 14.04
"""
 
import codecs
import os
from hashlib import sha512

import config

CONFIG_TEMPLATE = """# Basic configuration for a public Jupyter server
c.NotebookApp.certfile = u'{}/.ssh/notebook.pem'
c.NotebookApp.keyfile = u'{}/.ssh/notebook.key'

# Allow traffic from all IPs
c.NotebookApp.ip = '*'
c.NotebookApp.password = u'{}'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8888
"""


def create_hashed_password(password):
    """IN: plaintext password
       OUT: sha512 of salted password + salt in the format 'sha512:salt:hashed'
       we use hash(password + salt) as expected by Jupyter config
    """

    # Generate some random bytes for the salt
    thebytes = os.urandom(100)
    hexstr = str(codecs.encode(thebytes, 'hex')) # Rquires Python 3.4+
    salt = hexstr[3:14]  # 11 character hex salt without prefix 
   
    # Salt and hash the password
    tohash = password + salt
    tohash = tohash.encode("utf8")
    hashed = sha512(tohash).hexdigest()

    # Delete the config.py and config.pyc files
    for fn in ("config.py", "config.pyc"):
       try:
           os.remove(fn)
       except OSError as e:
            print(e)

    rs = "sha512:{}:{}".format(salt, hashed)
    return rs


def get_populated_config(config_template):
    """IN: config_template - the config with placeholders for the user directory and password
       OUT: the config template populated with user directory and password
    """
    hashedpw = create_hashed_password(config.password)
    userdir = os.getenv("HOME")
    return CONFIG_TEMPLATE.format(userdir, userdir, hashedpw)

def main():
    cfg = get_populated_config(CONFIG_TEMPLATE)
    with open("notebook_config.py", "w") as f:
        f.write(cfg)

if __name__ == "__main__":
    main()










