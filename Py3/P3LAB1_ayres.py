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
def go_asylum():
    print("As you and your friends stand before the imposing gates of Blackwood Asylum, the air")
    print("is thick with anticipation and an unsettling chill. You can't shake the feeling something is")
    print("waiting. As your friends buzz with excitement, urging you to be the brave one, you feel a mixture")
    print("of anxiety and thrill. You glance back at them, their faces a mix of anticipation and concern.")
    print("Are you willing to venture into the asylum alone, relying on your instincts, or would you prefer")
    print("to explore it together?")
    print("[Alone] or [Together]")
    choice = input()
    if choice == "together":
        go_group()  
    elif choice == "alone":
        go_alone()  
def go_group():
    print("One of your friends steps forward, concern etched on their face. 'No way! We can't send you")
    print("in alone. What if something happens to you?' The atmosphere thickens with tension. You take a deep breath,")
    print("feeling the weight of their expectations and fears. Finally, you nod in agreement. Thank god someone said")
    print("so I didn't have to and sound like a coward, you think to yourself. As you and your friends step into the")
    print("dark asylum, the heavy door creaks shut behind you, echoing through the dimly lit foyer. Dust particles")
    print("dance in the beams of your flashlights, casting eerie shadows on the peeling walls. The air is thick")
    print("with the scent of mildew and decay. After a moment of uneasy silence, you turn to your friends and suggest")
    print("your next move. Do you want to split into pairs and explore different areas or stick together and head")
    print("to the administration office?")
    print("[Pairs] or [ Stay together]")
    choice = input()
    if choice == "pairs":
        go_pairs()  # Call go_pairs function
    elif choice == "stay together":
        go_together()  # Call go_together function
def go_together():
    print("You and yur friends agree that it's best to sta togethe. th group moves cautiously toward the admins office,")
    print("each step echoing int he eerie silence. The door creaks open, revealing a room shrouded in darkness and dust")
    print("Do you continue into the Admins office or go back home?")
    choice = input()
    if choice =="admins office":
        go_admin
    elif choice == "back":
        go_back





#Start Program
main()