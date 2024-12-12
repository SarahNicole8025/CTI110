# 11-2-24
# P3HW1
# Sarah Ayres
# This program takes a number grade , determines average and displays letter
# grade for average.

# Enter grades for six modules

mod_1 = input('Enter grade for Module 1: ')
mod_2 = input('Enter grade for Module 2: ')
mod_3 = input('Enter grade for Module 3: ')
mod_4 = input('Enter grade for Module 4: ')
mod_5 = input('Enter grade for Module 5: ')
mod_6 = input('Enter grade for Module 6: ')

# add grades entered to a list

grades = [float(mod_1),float(mod_2),float(mod_3),float(mod_4),float(mod_5),float(mod_6)] 
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
total = sum(grades)  
avg = total / len(grades)

print(f'Module 1 Grade: {mod_1}')
print(f'Module 2 Grade: {mod_2}')
print(f'Module 3 Grade: {mod_3}')
print(f'Module 4 Grade: {mod_4}')
print(f'Module 5 Grade: {mod_5}')
print(f'Module 6 Grade: {mod_6}')
print('--------------Results--------------')
print(f'Lowest grade: {low:.2f}')
print(f'Highest grade: {high:.2f}')
print(f'Sum of Grades: {total:.2f}')
print(f'Average: {avg:.2f}')

print('-----------------------------------')
# determine letter grade for average
if avg >= 90:
    print('Your grade is: A')
    
elif avg > 80:
 print('Your grade is: B')

elif avg > 70:
    print('Your grade is: C')

elif avg > 60:
    print('Your grade is: D')
    
else:
    print('Your grade is: F') # TO DO: finish this



