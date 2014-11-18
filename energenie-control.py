from energenie import switch_on, switch_off
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from urllib.parse import urlparse

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		o = urlparse.urlparse(self.path)
		s = urlparse.parse_qs(o.query)
		# Send the html message
		self.wfile.write(s)
		return
	def do_POST(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		content_len = int(self.headers.getheader('content-length', 0))
		post_body = self.rfile.read(content_len)
		self.wfile.write(post_body)

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
