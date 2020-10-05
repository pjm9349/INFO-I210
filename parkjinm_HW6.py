# Justin Park
# INFO - I210

                                                # Homework 6 #

# 8.20
class BankAccount(object):

# Creating amount with the given balance

    def __init__(self, amount):
        self.amount = float(amount)

    def withdraw(self, amount):
        self.amount -= float(amount)

# Creating deposits the amount
    def deposit(self, amount):
        self.amount += float(amount)

    def balance(self):
        val = round(self.amount, 2)
        return val

x = BankAccount(700)
print(x.balance())
x.withdraw(70)
print(x.balance())
x.deposit(7)
print(x.balance())

# 8.22
class Worker(object):
    def __init__(self, name="Unknown", rate=0):
        # takes name and the time-based compensation rate of laborer
        self.name = name
        self.rate = rate

    def changeRate(self, new_rate):
        # takes the new pay rate as info and changes the compensation rate to the new_rate
        self.rate = new_rate

    def pay(self, hours):
        # takes the quantity of hours functioned as info and prints "Not Implemented"
        return "Not Implemented"

class HourlyWorker(Worker):
    def pay(self, hours):
        # takes number of hours worked as input and returns the wage
        # if worked more than 40 hours; then those of who are paid double
        if hours > 40:
            return 40 * self.rate + (hours - 40) * self.rate * 2
        return self.rate * hours

class SalariedWorker(Worker):
    def pay(self, hours = 40):
        return self.rate * 40

w1 = Worker("Joe", 15)
print(w1.pay(35))

w2 = SalariedWorker("Sue", 14.50)
print(w2.pay())
print(w2.pay(60))

w3 = HourlyWorker("Dana", 20)
print(w3.pay(25))
w3.changeRate(35)
print(w3.pay(25))

# 8.35
class Stack(object):

    def __init__(self): #making a lst for stack
        self.stack = []

    def push(self, push): #appending the input to the stack
        self.stack.append(push)
    def pop(self): #popping the last card added to that stack by using index -1
        return_Pop = self.stack[len(self.stack)-1]
        del self.stack[len(self.stack)-1]
        return return_Pop

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)

    def isEmpty(self): #returning True if the stack is empty
        if len(self.stack) == 0:
            return True
        return False

s = Stack()
s.push("plate 1")
s.push("plate 2")
s.push("plate 3")
print(s)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.isEmpty())

# 8.40
class BankAccount(object):
    def __init__(self, balance):
        if(balance >= 0):
            self.balance = balance
            self.account = balance
        else:
            raise ValueError("Illegal Balance")

    def deposit(self, amount):
        if(amount >= 0):
            self.account += amount
        else:
            raise ValueError("Negative Deposit")

    def withdraw(self, amount):
        if(amount >= self.account):
            self.account -= amount
        else:
            raise ValueError("Overdraft")

# main
x = BankAccount(-700)
x.balance()
x.withdraw(70)
x.balance()
x.deposit(-7)
x.balance()
x = BankAccount2(-700)
