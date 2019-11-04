class Worker:

    def lists_work(self, name, surname, position, income=None):
        self.name = name
        self.surname = surname
        self.position = position


    def salary(self, profit, bonus):
        self.profit = profit
        self.bonus = bonus

    def list_salary(self):
        return (self.profit, self.bonus)

    def statement(self):
        return {"profit": self.profit, "bonus": self.bonus}


class Position(Worker):

    def get_full_name(self):
        print(self.name + ' ' + self.surname)

    def get_full_profit(self):
        print(self.profit + self.bonus)

numer_Position = Position()
numer_Position.lists_work('Ivan', 'Simonov', 'manager')
numer_Position.salary(2000, 5000)

print(numer_Position.statement())
numer_Position.get_full_name()
numer_Position.get_full_profit()