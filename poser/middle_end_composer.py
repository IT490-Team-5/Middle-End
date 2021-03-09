from subprocess import Popen, PIPE
import paramiko
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

def front_end_composer():  # jnb27@ubuntu
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect("25.121.163.217", username="jnb27", password="IT490@FE")

	channel = ssh.get_transport().open_session()
	channel.exec_command('python3 ~/IT490/front-end/app.py > /dev/null 2>&1 &')
	
	#ssh.close()
	#p = Popen(["sshpass", "-p", "IT490@FE", "ssh", "jnb27@25.121.163.217"], shell=True, stdout=PIPE)
	#p.stdin.write("bash ~/IT490/front-end/flaskstart.sh")
	#print(channel.read().strip().decode())

def database_composer():
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect("25.3.178.5", username="duttp1998", password="ubuntu")
	
	channel = ssh.get_transport().open_session()
	channel.exec_command('bash ~/../Desktop/dbstart.sh > /dev/null 2>&1 &')

def back_end_composer():
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect("25.3.6.226", username="eg237", password="Platano01!")

	channel = ssh.get_transport().open_session()
	channel.exec_command('python3 ~/my_flask_app/IT490/Backend/receive.py > /dev/null 2>&1 &')




# =========================================
# Name: middle_end_composer
# Returns: None
# Description:
# This part of the ccodeode checks if receive.py is running, for middle end.
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


#p = Popen("whoami", shell=True, stdout=PIPE)
#whom = p.communicate()[0].read().decode()
#if p == "teo":
#	front_end_composer()
#	back_end_composer()
#	database_composer()

front_end_composer()
database_composer()
backend_composer()

middle_end_composer()











#p1.stdout.close()
#p2.wait()
#p1.wait()

#p3 = Popen(["grep", "-v", "grep"], stdin=PIPE)
#p2.stdout.close()

#output = p3.communicate()[0]
#print(output)
