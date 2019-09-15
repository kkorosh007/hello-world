#!/usr/bin/env python2
from SimpleHTTPServer import SimpleHTTPRequestHandler
import BaseHTTPServer

class CORSRequestHandler (SimpleHTTPRequestHandler):
	#def end_headers (self):
	#	self.send_header('Access-Control-Allow-Origin', '*')
	#	SimpleHTTPRequestHandler.end_headers(self)
	def do_GET(self):
		print("HERE MAN")
		self.send_response(200)
		self.send_header('Access-Control-Allow-Origin', '*')
		self.send_header('Access-Control-Allow-Headers', '*')
		self.end_headers()
		self.wfile.write("HELLO THERE") #bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))
	def do_POST(self):
		print("HERE MANIIIIIIIII")
		self.send_response(200)
		self.send_header('Access-Control-Allow-Origin', '*')
		self.end_headers()
		self.wfile.write("HELLO FROM The Stealth Server")

if __name__ == '__main__':
    BaseHTTPServer.test(CORSRequestHandler, BaseHTTPServer.HTTPServer)