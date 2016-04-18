# Set options for certfile, ip, password, and toggle off browser auto-opening
c.NotebookApp.certfile = u'/.ssh/notebook.pem'
c.NotebookApp.keyfile = u'/.ssh/notebook.key'
# Set ip to '*' to bind on all interfaces (ips) for the public server
c.NotebookApp.ip = '*'
c.NotebookApp.password = u'sha512:2a5f9f98a787:b98a1b5e46f73847df668a074632a633799d7aaa8769c66d45b1afc2b09a4649624c281509c8e7679af342caa1b10d79bcc12d350eb3b2c806e0bd9827b2d77b'
c.NotebookApp.open_browser = False

# It is a good idea to set a known, fixed port for server access
c.NotebookApp.port = 9999
