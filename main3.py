import os
import requests 

from http.server import HTTPServer, CGIHTTPRequestHandler
# Make sure the server is created at current directory
os.chdir('.')

# Create server object listening the port 80
server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=CGIHTTPRequestHandler)
# Start the web server
print("rrrrrrrrrrrr")
server_object.serve_forever()
#La direccion del server es      localhost

r = requests.post('localhost / post', data ={'post':120})

print(r)
  
print(r.json())