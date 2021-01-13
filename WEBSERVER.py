import sys
import time
import os
import http.server
import subprocess
from threading import Thread
from time import strftime

ip = input('IP: ')
udp = input('UDP: ')

httpd=None
try:
	if sys.version_info[0] is 3:
		class ServerHandler(http.server.BaseHTTPRequestHandler):
			def do_POST(self):
				self.send_response(200)
				self.end_headers()
				self.wfile.write(str.encode("server|%s\nport|%s\ntype|1\n#maint|Mainetrance message (Not used for now) -- Pyhton WebServer Made By DisMiss\n\nbeta_server|%s\nbeta_port|%s\n\nbeta_type|1\nmeta|thisislife\nRTENDMARKERBS1001" % (ip, udp)))
		server_address = ('', 80)
		httpd = http.server.HTTPServer(server_address, ServerHandler)
		print("HTTP server is running!")
		httpd.serve_forever()
	else:
		import SimpleHTTPServer
		import SocketServer
		print("Launching HTTP server! (Python 2.x)")
		class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
			def do_POST(self):
				self.send_response(200)
				self.end_headers()
				self.wfile.write(str.encode("server|%s\nport|%s\ntype|1\n#maint|Mainetrance message (Not used for now) -- Pyhton WebServer Made By DisMiss\n\nbeta_server|%s\nbeta_port|%s\n\nbeta_type|1\nmeta|thisislife\nRTENDMARKERBS1001" % (ip, udp)))
		Handler = ServerHandler
		httpd = SocketServer.TCPServer(("", 80), Handler)
		print("HTTP server is running! Don't close this or GT will be unable to connect!")
		httpd.serve_forever()
except:
	print("[EROR] 80 Port Using By Another Program Run As This File Adminstrator")