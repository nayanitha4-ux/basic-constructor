
# 1. Employee Details
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.name)
        print("Salary:", self.salary)

e = Employee(101, "Ramesh", 30000)
e.display()


# 2. Mobile Details
class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)

m1 = Mobile("Samsung", "S24", 70000)
m2 = Mobile("Apple", "iPhone 15", 65000)

print("\nMobile 1:")
m1.display()

print("\nMobile 2:")
m2.display()


# 3. Bank Account
class BankAccount:
    def __init__(self, acc_no, holder, balance):
        self.acc_no = acc_no
        self.holder = holder
        self.balance = balance

    def display(self):
        print("Account Number:", self.acc_no)
        print("Account Holder:", self.holder)
        print("Balance:", self.balance)

b = BankAccount(12345, "Rahul", 50000)
b.display()
