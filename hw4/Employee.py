#create class
class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def increase_salary(self):
        return print(self.name, "salary:", self.salary, "updated salary:", self.salary * 1.1)

#create object and call function
john = Employee("John", 5000)
john.increase_salary()
    


