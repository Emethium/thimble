import sys
import time
import platform
import telepot
import subprocess
import psutil

def handle(msg):
	chatId = msg['chat']['id']
	command = msg['text']
	prefix = command.split(" ")[0]

	print 'Got command: %s' % command

	if command == '/who':
		bot.sendMessage(chatId, 'I am your RaspberryPi! You hear the noise coming from the living room? No? Thats because my fan died on me :(). ')
	elif command == '/time':
		bot.sendMessage(chatId, time.strftime("%A, %d %B of %Y, exact time of %H:%M:%S"))
	elif command == '/system':
		bot.sendMessage(chatId, "Architecture: " + platform.machine() + '\n' + "Platform: " + platform.platform() + '\n' + "System: " +
			platform.system() + '\n' + "Name: " + platform.node() + '\n')
	elif command == '/satan':
		bot.sendPhoto(chatId, open("satan.png"))
	elif prefix == '/checkProcess':
		sufix = command.split(" ")[1]
		pid = getPid(sufix)
		if pid != 0:
			bot.sendMessage(chatId, "The process is runnig with PID " + str(pid))
		else:
			bot.sendMessage(chatId, "No process with the name " + sufix + " is running!")



def getPid(name):
	print 'Checking if process %s is running..' % name
	pid = 0
	for proc in psutil.process_iter():
		 if proc.name() == name:
			 pid = proc.pid
	print 'Found PID of %s' % pid
	return pid


bot = telepot.Bot('242541288:AAEiiRLOUpulOkw10NmGZnJh5Z8kthQDQoo')
bot.message_loop(handle)
print 'On standby'

while 1:
	time.sleep(10)
