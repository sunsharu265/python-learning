class Employee:
    def __init__(self, name, age, monthly_salary):
        self.name = name
        self.age = age
        self.monthly_salary = monthly_salary

    def calculate_sum(self):
        return self.monthly_salary * 12

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Monthly salary:", self.monthly_salary)
        print("Yearly salary:", self.calculate_sum())

def main():
    employee = Employee("kishore", 30, 25000)
    employee.show_details()
    return employee


if __name__ == "__main__":
    main()



   