import threading
from threading import Thread, Lock


class BankAccount(Thread):

    def __init__(self):
        super().__init__()
        self.balance = 1000
        self.lock = Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f'Внесено {amount}, новый баланс{self.balance}')

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f'Снято {amount}, новый баланс{self.balance}')
            else:
                print(f'Недостаточно денег на счету, баланс {self.balance}')


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)


account = BankAccount()

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()










