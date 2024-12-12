#P3HW2
#11-2-24
#program to calculate an employees regulate pay, overtime pay, and their gross pay

'''
Pseudocode for Salary Calculation Program

FUNCTION calculate_overtime_and_regular_pay(hours_worked, pay_rate)
    SET overtime_hours = MAX(0, hours_worked - 40)
    SET regular_hours = MIN(40, hours_worked)
    SET overtime_pay = overtime_hours * pay_rate * 1.5
    SET reg_hour_pay = regular_hours * pay_rate
    SET gross_pay = reg_hour_pay + overtime_pay
    RETURN overtime_hours, overtime_pay, reg_hour_pay, gross_pay

FUNCTION print_employee_pay_summary(employee_name, hours_worked, pay_rate, overtime_hours, overtime_pay, reg_hour_pay, gross_pay)
    PRINT "--------------------------------"
    PRINT "Employee Name: employee_name"
    PRINT ""
    PRINT "Hours Worked     Pay Rate       OverTime       OverTime Pay    RegHour Pay      Gross Pay"
    PRINT "-----------------------------------------------------------------------------------------"
    PRINT formatted values of hours_worked, pay_rate, overtime_hours, overtime_pay, reg_hour_pay, gross_pay

 FUNCTION calculate_pay()
     PROMPT user for "Enter Employee's Name"
     READ employee_name
     PROMPT user for "Enter Number of Hours Worked"
     READ hours_worked
     PROMPT user for "Enter Employee's Pay Rate"
     READ pay_rate

     CALL calculate_overtime_and_regular_pay(hours_worked, pay_rate) 
          AND STORE returned values in overtime_hours, overtime_pay, reg_hour_pay, gross_pay

     CALL print_employee_pay_summary(employee_name, hours_worked, pay_rate, 
                                         overtime_hours, overtime_pay, reg_hour_pay, gross_pay)

CALL calculate_pay()
'''
def calculate_overtime_and_regular_pay(hours_worked, pay_rate):
    overtime_hours = max(0, hours_worked - 40)
    regular_hours = min(40, hours_worked)
    overtime_pay = overtime_hours * pay_rate * 1.5
    reg_hour_pay = regular_hours * pay_rate
    gross_pay = reg_hour_pay + overtime_pay
    return overtime_hours, overtime_pay, reg_hour_pay, gross_pay

def print_employee_pay_summary(employee_name, hours_worked, pay_rate, overtime_hours, overtime_pay, reg_hour_pay, gross_pay):
    print("-" * 40)
    print(f"Employee Name: {employee_name}")
    print()
    print(f"{'Hours Worked':15} {'Pay Rate':15} {'OverTime':15} {'OverTime Pay':15} {'RegHour Pay':15} {'Gross Pay':15}")
    print("-" * 90)
    print(f"{hours_worked:<15.2f} {pay_rate:<15.2f} {overtime_hours:<15.2f} {overtime_pay:<15.2f} ${reg_hour_pay:<15.2f} ${gross_pay:<15.2f}")

def calculate_pay():
    employee_name = input("Enter Employee's Name: ")
    hours_worked = float(input("Enter Number of Hours Worked: "))
    pay_rate = float(input("Enter Employee's Pay Rate: "))

    overtime_hours, overtime_pay, reg_hour_pay, gross_pay = calculate_overtime_and_regular_pay(hours_worked, pay_rate)

    
    print_employee_pay_summary(employee_name, hours_worked, pay_rate, overtime_hours, overtime_pay, reg_hour_pay, gross_pay)


calculate_pay()
