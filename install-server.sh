#!/bin/bash
# copy service file to /etc
cp ./resource-tracking.service /etc/systemd/system/

# start service
systemctl daemon-reload
systemctl enable resource-tracking.service
systemctl start resource-tracking.service
