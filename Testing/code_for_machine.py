import paramiko
import time

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect('ev3dev', username='robot', password='maker')
print("Connected!")

time.sleep(1)
client.exec_command("w")  # this returns a log history
time.sleep(3)  # making sure that the command is send
client.close()
