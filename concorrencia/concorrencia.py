import _thread
import time

finalizar_tarefa = 0
tarefa_iniciada = False

def task(nome_tarefa, atraso):
	global finalizar_tarefa, tarefa_iniciada
	tarefa_iniciada = True
	finalizar_tarefa += 1
	cont = 0
	for cont in range(5):
		time.sleep(atraso)
		print("Thread : %s" % (nome_tarefa))
		cont += 1
	finalizar_tarefa -= 1

_thread.start_new_thread(task, ("Tarefa 1", 2))
_thread.start_new_thread(task, ("Tarefa 2", 4))

while not tarefa_iniciada:
	pass
while finalizar_tarefa > 0:
	pass