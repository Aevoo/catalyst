"""
Collection of utility functions for catalyst
"""

import sys, traceback, os

def capture_traceback():
	etype, value, tb = sys.exc_info()
	s = [x.strip() for x in traceback.format_exception(etype, value, tb)]
	return s

def print_traceback():
	for x in capture_traceback():
		print x

def load_module(name):
	try:
		# I'm not sure if it's better to use imp.load_module() for this, but
		# it seems to work just fine this way, and it's easier.
		exec("import " + name)
		return sys.modules[name]
	except Exception:
		return None

def find_binary(myc):
	"""look through the environmental path for an executable file named whatever myc is"""
	# this sucks. badly.
	p=os.getenv("PATH")
	if p == None:
		return None
	for x in p.split(":"):
		#if it exists, and is executable
		if os.path.exists("%s/%s" % (x,myc)) and os.stat("%s/%s" % (x,myc))[0] & 0x0248:
			return "%s/%s" % (x,myc)
	return None

def readfile(file):
	file_contents = ""
	try:
		myf = open(file, "r")
		file_contents = "".join(myf.readlines())
		myf.close()
		return file_contents
	except:
		return None
		#raise CatalystError, "Could not read file " + file

def list_bashify(mylist):
	if isinstance(mylist, str):
		mypack = [mylist]
	else:
		mypack = mylist[:]
	for x in range(0,len(mypack)):
		# surround args with quotes for passing to bash,
		# allows things like "<" to remain intact
		mypack[x] = "'" + mypack[x] + "'"
	mypack = "".join(mypack)
	return mypack

def list_to_string(mylist):
	if isinstance(mylist, str):
		mypack=[mylist]
	else:
		mypack=mylist[:]
	mypack = " ".join(mypack)
	return mypack

