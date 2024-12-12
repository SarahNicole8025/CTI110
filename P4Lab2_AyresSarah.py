#P4LAB2_AyresSarah
#11-10-24
#program that uses a for loop to display the multiplcation table
# of that digit and a while loop to either run program again or not
def display_multiplication_table(num):
    print(f"Multiplication table for {num}:")
    for i in range(1, 13):
        print(f"{num} x {i} = {num * i}")

def main():
    while True:
        try:
            user_input = int(input("Enter an integer: "))
            if user_input < 0:
                print("Cannot accept negative values. Please enter a zero or higher integer.")
            else:
                display_multiplication_table(user_input)

            again = input("Do you wish to run it again? (yes/no): ").strip().lower()
            if again != 'yes':
                print("Thank you for using the program!")
                break
                
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()