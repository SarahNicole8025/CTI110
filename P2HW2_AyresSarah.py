# Sarah Ayres
#10-25-2024
#P2HW2
# This program will store and show the grades for each model as well
# as showing you the lowest grade, the highest, the sum of the grades, and
# the grades' average

print("Student Grades")
print("-----------------------------------")
grades_list=[]

grade1 = float(input("Enter grade for Module 1: "))
grades_list.append(grade1)
grade2 = float(input("Enter grade for Module 2: "))
grades_list.append(grade2)
grade3 = float(input("Enter grade for Module 3: "))
grades_list.append(grade3)
grade4 = float(input("Enter grade for Module 4: "))
grades_list.append(grade4)
grade5 = float(input("Enter grade for Module 5: "))
grades_list.append(grade5)
grade6 = float(input("Enter grade for Module 6: "))
grades_list.append(grade6)
grade7 = float(input("Enter grade for Module 7: "))
grades_list.append(grade7)

#caluclations
lowest_grade = min(grades_list)
highest_grade = max(grades_list)
sum_of_grades = sum(grades_list)
average_grade = sum_of_grades/ len(grades_list)

#What is Displayed
print("Results")
print("--------------Results--------------")
print(f"Lowest Grade: {lowest_grade:.2f}")
print(f"Highest Grade: {highest_grade:.2f}")
print(f"Sum of Grades: {sum_of_grades: .2f}")
print(f"Average Grade: {average_grade:.2f}")
