import os, sys

# generate service file
try:
	os.remove('./resource-tracking.service')
except OSError:
	pass

with open('./resource-tracking.service', 'w') as file:
	file.write("[Unit]\n")
	file.write("Description=Tracker for resource on compute node\n\n")
	file.write("[Service]\n")
	file.write("ExecStart="+sys.executable+" "+str(os.getcwd())+"/tracker.py\n")
	file.write("Restart=always\n\n")
	file.write("[Install]\n")
	file.write("WantedBy=default.target\n")
