#CTI-110
#Ayress
#11-14-24
'''
print("test program")
count = 1
while count <= 5:
    print("count is", count)
    #count = count + 1
    count += 1
print("Done")

for number in range(1,6):
    print(number)
print("done")
#Input validation
num = int(input("Type a number from 1 to 5"))
while num < 1 or num >3:
    print("Please try again")
    num = int(input("Type a number from 1 to 5:"))
print(" You Entered:",num)
'''
#P4LAB2 - Times Table
#Ask for a number that is 0 or higher
#dislay the times table for that number
#from times 1 to 12
# Finally repeat if they want

def times_table():
    num = int(input("Enter an Number:"))
    while (num < 0):
        print("No neggative numbers please.")
        num = int(input("Enter an Number:"))
    print("You Entered",num)
    #finally, do the ties table
    for num2 in range(1,13):
        answer = num * num2
        print(num,"*",num2,"=", answer)

def main():
    times_table()
    again = input ("Do you want to run again?")
    while (again == "yes"):
        times_table()
        again = input ("Do you want to run again?")
    print("BYE BYE!!")
        

#Start program
main()
