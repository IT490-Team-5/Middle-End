#!/bin/bash

if ps aux | grep "python3 receive.py" | grep -v "grep"; then
	echo server already on!!!!!!!!!
else
	python3 receive.py
fi
