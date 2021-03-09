from subprocess import Popen, PIPE
import os

def middle_end_composer():
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect("25.121.196.54", username="teo", password="123")
	
	channel = ssh.get_transport().open_session()
	ssh.exec_command("python3 ~/scripts/proj/poser/receive.py > /dev/null 2>&1 &")


def back_end_composer():
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect("25.3.6.226", username="eg237", password="Platano01!")

	channel = ssh.get_transport().open_session()
	channel.exec_command('python3 ~/my_flask_app/IT490/Backend/receive.py > /dev/null 2>&1 &')

	
def front_end_composer():  # jnb27@ubuntu
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect("25.121.163.217", username="jnb27", password="IT490@FE")

	channel = ssh.get_transport().open_session()
	channel.exec_command('python3 ~/IT490/front-end/app.py > /dev/null 2>&1 &')


def database_composer():
	p = Popen('systemctl status mysql | grep "inactive"', shell=True, stdout=PIPE)
	o = p.communicate()[0].strip().decode()
	print(o)
	if not o:
		print("DB was off. Turning on..")
		sp = Popen(["bash", "dbstart.sh"])
	else:
		print("DB already on.")


middle_end_composer()
front_end_composer()
back_end_composer()

database_composer()




