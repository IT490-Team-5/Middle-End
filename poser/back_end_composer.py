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
	
def front_end_composer():  # jnb27@ubuntu
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect("25.121.163.217", username="jnb27", password="IT490@FE")

	channel = ssh.get_transport().open_session()
	channel.exec_command('python3 ~/IT490/front-end/app.py > /dev/null 2>&1 &')


def back_end_composer():	
	p = Popen('ps aux | grep "python3 receive.py" | grep -v "grep"', shell=True, stdout=PIPE)
	o = p.communicate()[0].strip().decode()
	print(o)
	if not o:
		print("Backend server was off. Turning on..")
		sp = Popen(["python3", "receive.py"])
	else:
		print("Backend services already on.")


middle_end_composer()
front_end_composer()
back_end_composer()

database_composer()




