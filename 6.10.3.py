class Client:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def account(self):
        return f'Клиент «{self.name}». Баланс: {self.balance} руб.'