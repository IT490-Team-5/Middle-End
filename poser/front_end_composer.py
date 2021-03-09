import subprocess
from subprocess import Popen, PIPE
import paramiko

def middle_end_composer():
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect("25.121.196.54", username="teo", password="123")
	
	channel = ssh.get_transport().open_session()
	ssh.exec_command("python3 ~/scripts/proj/poser/receive.py > /dev/null 2>&1 &")


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

def front_end_composer():
	p = Popen('lsof -Pi :5000 -sTCP:LISTEN -t >/dev/null', shell=True, stdout=PIPE)
	o = p.communicate()[0].strip().decode()
	print(o)
	if not o:
		print("Flask server was off. Turning on..")
		subprocess.run(["python3", "app.py"])
	else:
		print("Front end services already on.")



middle_end_composer()
back_end_composer()
database_composer()

front_end_composer()


