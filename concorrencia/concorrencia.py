import _thread
import time

num_thread = 1
thread_started = False

def task(task_name, delay):
	global num_thread, thread_started
	thread_started = True
	num_thread += 1
	cont = 0
	for cont in range(5):
		time.sleep(delay)
		print("Thread : %s" % (task_name))
		cont += 1
	num_thread -= 1

_thread.start_new_thread(task, ("Tarefa 1", 2))
_thread.start_new_thread(task, ("Tarefa 2", 4))

while not thread_started:
	pass
while num_thread > 0:
	pass