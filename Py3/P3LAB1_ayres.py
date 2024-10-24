# CTI 110
# P3LAB1 - Choose your own Adventure
# Ayress
# 10-22-24

def main():
    print("CHOOSE YOUR OWN ADVENTURE")
    print("It was a chilly evening when your friends burst into your room, excitement written all over their faces.")
    print("Come on! We're going to the old ayslum! You must come. It'll be an adventure!")
    print("You glance outside at the darkening clouded sky and feel curiosity as well as apprehension")
    print("What will you do?")
    print("[home] or [asylum]")
    choice = input()
    if choice == "home":
        stay_home()
    elif choice == "asylum":
        go_asylum()
def stay_home():
    print("You glance at the flickering TV and the takeout menu spread out on the coffee table.")
    print("The thought of exploring a creepy, abandoned asylum sends chills down your spine.")
    print("You can alreay inamgine the shadows lurking in every corner, Your friends can tell from")
    print("your face what your answer is. So, they groan but ultimately head out without you. You")
    print("pullout your phone, order a pizza, and settle back into the comfort of your blankey,")
    print("relieved to be in your safe space.")
    print("Yay! Your Safe, but you find out in the morning on the news that they were all killed by a ")
    print("axe whilding Masked figure that has been terrizing the town as of late.")

#Start Program
main()