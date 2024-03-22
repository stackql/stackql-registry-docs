#!/bin/bash

# Search for the process running stackql
PID=$(sudo ps -ef | grep './stackql ' | grep -v 'grep' | awk '{print $2}')

# Check if the process exists
if [ -z "$PID" ]; then
  echo "No stackql process found."
else
  # Kill the process
  echo "Killing stackql process with PID: $PID"
  sudo kill -9 $PID
fi
