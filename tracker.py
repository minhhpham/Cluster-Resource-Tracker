import subprocess
import os
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/cpu')
def cpu_query():
	UID = request.args.get('UID')
	if UID is None:
		return b""
	
	out = subprocess.Popen(['ps',  'u', '-u', str(UID)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	stdout, stderr = out.communicate()
	return stdout

@app.route('/gpu')
def gpu_query():
	out = subprocess.Popen(['nvidia-smi'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	stdout, stderr = out.communicate()
	return stdout

@app.route('/')
def all_query():
	cpu_data = cpu_query()
	gpu_data = gpu_query()
	output = b'======== CPU AND MEMORY USAGE ============\n'
	output = output + cpu_data
	output = output + b'\n' + b'======== GPU USAGE ============\n'
	output = output + gpu_data
	return output

if __name__=="__main__":
	app.run(host = "0.0.0.0", port=2108, threaded=True)
