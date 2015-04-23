Gender = str(input("Enter the gender of an employee (M or F)."))
c_salary = int(input("Enter the Current Salary of an employee."))

if(c_salary < 1000 and Gender == 'M'):
    Bonus = (c_salary * 5) / 100
    print("Bonus =", Bonus)

elif(c_salary < 1000 and Gender == 'F'):
    Bonus = (c_salary * 5.5) / 100
    print("Bonus =", Bonus)

elif(c_salary > 1000):
    Bonus = (c_salary * 5) / 100
    print("Bonus =", Bonus)
