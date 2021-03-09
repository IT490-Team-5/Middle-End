#!/bin/bash

if ps aux | grep "receive.py" | grep -v "grep"; then
	pkill -f receive.py
	echo it\s gone!!!
else
	echo server is already off!!!!!!!!	
fi
