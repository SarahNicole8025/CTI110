# CTI 110
# P3LAB1 - Choose your own Adventure
# Ayress
# 10-22-24

def main():
    print("Choose you own Adventure")
    print("Your friends have invited you to explore an abandoned Insane Asylum")
    print("[asylum] or [home]")
    choice = input()
    if choice == "asylum":
        go_asylum()
    elif choice == "home":
        go_home()

def go_asylum():
    print("1.You are dared to go in alone")
    print("2.You go in as groups of two")
    choice = input()
    if choice == "alone":
        go_alone()
    elif choice == "group":
        go_in_group()

def go_alone():
    print("You walk down a dark hallway with a flashlight")
    print("You hit a juntion with three other hallways")
    print("1.Left")
    print("2.Right")
    print("3.Forward")
    print("4.Back the way you came")
    choice = input()
    if choice == "left":
        go_left
    elif choice == "right":
        go_right
    elif choice == "forwar":
        go_forward
    elif choice == "back":
        go_back

def go_left():
    pass

def go_right():
    pass

def go_forward():
    pass

def go_back():
    print("You make it back to your friends. They call you a whimp and make fun of you.")

def go_in_group():
    pass


def go_home():
    print("Your a WHIMP!!!!!!")

#Start Program
main()