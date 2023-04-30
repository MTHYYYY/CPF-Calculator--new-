'''
Write a program to calculate the CPF contribution for an employee based on their monthly salary and age.
The program is to display the employee’s, employer’s and total CPF contribution.
The program will only terminate if the letter q (lowercase) is entered in the prompt for monthly salary.
'''
while True:
    monthly_salary = input("What is your monthly salary (Enter q to quit): ")
    if monthly_salary == 'q':
        break

    try:
        monthly_salary = float(monthly_salary)
        age = int(input("What is your age:"))
    except:
        print("You have entered a wrong input, Please Try again")
        continue

    if age <= 55:
        employee_rate = monthly_salary * 0.2
        employer_rate = monthly_salary * 0.17
    elif age <= 60:
        employee_rate = monthly_salary * 0.13
        employer_rate = monthly_salary * 0.13
    elif age <= 65:
        employee_rate = monthly_salary * 0.075
        employer_rate = monthly_salary * 9
    elif age > 65:
        employee_rate = monthly_salary * 0.005
        employer_rate = monthly_salary * 7.5

    print("The employee's contribution is: ", employee_rate)
    print("The employer's contribution is: ", employer_rate)
    print("Total contribution is: ", employee_rate + employer_rate)
