# Author: Steven Wang    Date:20160704
# python 3.5.2
from threading import Thread
import time

def timer(name, delay, repeat):
	print('Timer: ' + name + 'Started')
	while repeat > 0:
		time.sleep(delay)
		print(name + ': ' + str(time.ctime(time.time())))
		repeat -= 1
	print('Timer: ' + name + ' Completed')

def main():
	t1 = Thread(target=timer, args=("Timer1", 1, 5))
	#target function name
	#arguments for the target function is ()
	t2 = Thread(target=timer, args=("Timer2", 2, 5))
	t1.start()
	#tell thread t1 to start
	t2.start()
	print('main function complete')

if __name__ == '__main__':
	main()
