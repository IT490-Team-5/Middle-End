
from subprocess import Popen, PIPE

#p = subprocess.Popen("ls ..", shell=True)


#grep_cond = subprocess.Popen(('ps aux | grep python3 receive.py | grep -v grep'), shell=True, stdout=subprocess.PIPE)



#p1 = Popen(["ps", "aux"], stdout=PIPE)
#p2 = Popen(["grep", 'python3', "receive.py"], stdin=p1.stdout, stdout=PIPE, stderr=PIPE)



# =========================================
# Name: front_end_composer
# Returns: None
# Description:
# This part of the code uses ssh and starts the front end composer script, if it is not already on.
# =========================================

def front_end_composer():
	pass
def database_composer():
	pass
def back_end_composer():
	pass




# =========================================
# Name: middle_end_composer
# Returns: None
# Description:
# This part of the code checks if receive.py is running, for middle end.
# =========================================

def middle_end_composer():	
	p = Popen('ps aux | grep "python3 receive.py" | grep -v "grep"', shell=True, stdout=PIPE)
	o = p.communicate()[0].strip().decode()
	print(o)
	if not o:
		print("Middle end server was off. Turning on..")
		sp = Popen(["python3", "receive.py"])
	else:
		print("Middle end services already on.")


middle_end_composer()
if __name__ == "__main__":
	front_end_composer()
	back_end_composer()
	database_composer()













#p1.stdout.close()
#p2.wait()
#p1.wait()

#p3 = Popen(["grep", "-v", "grep"], stdin=PIPE)
#p2.stdout.close()

#output = p3.communicate()[0]
#print(output)
