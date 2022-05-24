from concurrent.futures import ThreadPoolExecutor
import time
import threading    

class ContaBancaria:
    def __init__(self, slt):
        self.saldo = slt
        self.lock = threading.Lock()
        
    def transacao(self, nome, valor):
        with self.lock:
            saldo_conta = self.saldo
            print(f'{nome} o saldo é {saldo_conta}')
            time.sleep(1)
            self.saldo = saldo_conta + valor
            print(f'{nome} atualizou o saldo para:{self.saldo}')
            



if __name__ == '__main__':
    ac = ContaBancaria(50)
    print(f'Saldo inicial {ac.saldo}')
    transactions= [["A", "B"], [100, 50]]
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(ac.transacao, *transactions)
    print(f'Saldo final depois da transação {ac.saldo}')
    