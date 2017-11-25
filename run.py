#!flask/bin/python
from app import app
HOST='192.168.0.25'
 
# Starting on my server, your ip address may be different.
app.run(host=HOST, debug=True)
