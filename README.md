# RESOURCE TRACKING FOR COMPUTER CLUSTERS
This project is created to serve users of computer clusters where ssh-ing to a compute node is not allowed. The tools in this repository will allow users to track resources in compute nodes without using ssh.

Currently, supported resources are:
 - CPU usage (through Linux' `ps` command)
 - Memory usage (through Linux' `ps` command)
 - GPU usage (through `nvidia-smi` command)

## HOW TO INSTALL AND SETUP
### On Compute Node
Requirements: `python` and `pip`, assuming `systemd` is being used.
```
git clone https://github.com/minhhpham/Cluster-Resource-Tracker
cd Cluster-Resource-Tracker
pip install -r requirements.txt
python configure.py
chmod +x install-server.sh
sudo ./install-server.sh
```
### On Control Node/Head Node
```
git clone https://github.com/minhhpham/Cluster-Resource-Tracker
cd Cluster-Resource-Tracker
chmod +x isntall-client.sh
sudo ./install-client.sh
```