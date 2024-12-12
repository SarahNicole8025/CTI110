#CTI 110
#P1HW2
#S Ayres
#10/8/2024
'''
3. Ask user to enter their budget

4. Ask user to enter travel destination

5.  Ask user for amount they will spend on gas

6. Ask user for amount they will spend on accommodation

7. Ask user for amount they will spend on food

8. Add expenses

9. Subtract expenses from budget

10. Display results
'''

print("-----Trip Calculator-----")
#Ask user to enter their budget
budget = float(input("What is your travel budget?:$ "))
#Ask user to enter travel destination
destination = input("Where are you going?: ")
# Ask user for amount they will spend on gas
gas = float(input("How amount for gas?:$ "))
#Ask user for amount they will spend on accommodation
hotel = float(input("Lodging budget?:$ "))
#Ask user for amount they will spend on food
food = float (input("Food Budget:$ "))
#Add expenses
extras = float(input("How much to alot for extras?:$ "))
#Subtract expenses from budget
used = gas + hotel + food + extras
remaining = budget - used
'''
print("-----Results-----")
print("Destination: ",destination)
#print("Amount Used: ",format(used,".2f"))
#print(f"Amount Used: ${used:.2f}")
print(f"Amount Used: ${used:.2f}")
#print("Remaining Budget: ",format(remaining, ".2f"))
print(f"Budget Left: ${remaining:.2f}")
'''
print("\n------------Travel Expenses-------------")
print(f"Destination:       {destination}")
print(f"Budget:            ${budget:.2f}")
print(f"Gas Amount:        ${gas:.2f}")
print(f"Lodging Amount:    ${hotel:.2f}")
print(f"Food Budget:       ${food:.2f}")
print(f"Extra:             ${extras:.2f}")
print("----------------------------------------")
print(f"Remaining Balance: ${remaining:.2f}")


