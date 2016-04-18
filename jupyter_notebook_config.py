# Set options for certfile, ip, password, and toggle off browser auto-opening
c.NotebookApp.certfile = u'/home/jupyteruser/.ssh/notebook.pem'
c.NotebookApp.keyfile = u'/home/jupyteruser/.ssh/notebook.key'
# Set ip to '*' to bind on all interfaces (ips) for the public server
c.NotebookApp.ip = '*'
c.NotebookApp.password = u'sha512:cbc8fdab837:4473787eeda1f82c7aecb8a40180fb31c6261e4d6cb60958b49c93bb454073c8851afe2edbc5668988a4373958f5b8a5d724f6288594eb4998d6ee6791ca7770'
c.NotebookApp.open_browser = False

# It is a good idea to set a known, fixed port for server access
c.NotebookApp.port = 9999
