#!/bin/bash

if ps aux | grep "python3 receive.py" | grep -v "grep"; then
	pkill -f receive.py
else
	echo server is already off!!!!!!!!	
fi
