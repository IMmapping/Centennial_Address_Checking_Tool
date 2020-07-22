"""
This handy little script will start up a web server in your local environment which
is great for testing. By default it will serve out whatever files are in the directory
it is pu in e.g. if it is in C:\Website and inside that folder there are files it will host them
on port 8000. So if you were to go to http://localhost:8000/ in a web browser, it would display!

I have included an os.chdir command so you can store this python file in a different location should you wish.
it is currently commented out
"""
import os
#This command will allow you to change the script to first move to the website folder, then start the server up
os.chdir(r'X:\GIS\Ian\Definitely\address_adding_app')
import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print(("serving at port", PORT))
httpd.serve_forever()