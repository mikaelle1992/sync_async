from concurrent.futures import ThreadPoolExecutor
import threading
import time


class Projector:
    def __init__(self):
        self.lock = threading.Lock()
        
    def acquire(self, name):
        print(f'{name} está adquirindo o  projetor')
        self.lock.acquire()
        print(f'O projetor é concedido a {name}')
    
    
    def release(self, name):
        self.lock.release()
        print(f'{name} solte o projetor')
 
        
class Computer:
    def __init__(self):
        self.lock = threading.Lock()
        
    def acquire(self, name):
        print(f'{name} está adquirindo o computador')
        self.lock.acquire()
        print(f'O Computador é concedido a {name}')
    
    
    def release(self, name):
        self.lock.release()
        print(f'{name} solte o  Computador')
        
def present(name, resurce1, resurce2):
    resurce1.acquire(name)
    time.sleep(2)
    resurce2.acquire(name)
    time.sleep(2)
    print("Apresentação concluida")
    resurce1.release(name)
    resurce2.release(name)
    
if __name__ == '__main__':
    projector = Projector()
    computer = Computer()
    transactions= [["A", "B"], [projector, computer], [computer, projector]]
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(present, *transactions)
