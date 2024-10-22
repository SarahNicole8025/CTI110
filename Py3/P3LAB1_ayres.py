# CTI 110
# P3LAB1 - Choose your own Adventure
# Ayress
# 10-22-24

def main():
    print("Choose you own Adventure")
    print("Your friends have invited you to explore an abbandden Insane Asythem")
    go_Asythem()
    go_home()

def go_Asythem():
    print("You are dared to go in alone")
    print("You go in as groups of two")
    choice = input()
    if choice == alone:
        go_alone
    elif choice == group:
        go_in_group

def go_alone():
    pass

def go_in_group():
    pass


def go_home():
    print("You decide to go Home.")
    print("But should you order some takeout?")
    print("chinese")
    print("thai")
    choice = input()
    if choice == chinese:
        get_chinese()
    elif choice == thai:
        get_thai()

def  get_chinese():
    print("You go looking for your chinese takeout booklet")
    print("You find 3 places that has what you want.")
    print("1.Dragon Tails")
    print("2.Luckys")
    print("3.Zou's Place")
    choice = int(input())
    if choice == 1:
        get_Dragon_()
    elif choice == 2:
        get_luckys()
    elif choice == 3:
        get_zou_place()

     # replace

def get_thai():
    print("You look up tai places near you")
    print("There are only 2 places n your town.")
    print("1.Delivers but is two stars.")
    print("2.Is only carryout but is 5 stars.")
    choice = int(input())
    if choice == 1:
        get_delivery()
    elif choice == 2:
        get_carryout()

#Start Program
main()