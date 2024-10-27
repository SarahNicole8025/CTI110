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
    print("As you and your friends stand beforw the imposing gates of Blackwood Asylum. the air")
    print("is thick with anticipation and an unsetting chill. You can't shake teh feeling something is")
    print("waitig. As your friends buzz with exitemen, urging you to be the brave one, you feel a mixture")
    print("of anixety and thri;;. You glance back at them,their faes a mix of aniticipation and concern")
    print("Are you willing to venture into the asylum alone, relying on your instincts, or would you prefer")
    print("to explore it with a group")
    print("[Alone]or[Group]")
    choice = input()
    if choice == "group":
        go_group
    elif choice == "alone":
        go_alone
def go_group():
    print("One of your other friends steps forward, concern etched on their face.'No way! we can't send you")
    print("in alone. What id somethinf happens to you?'The atmosphere thickens with tension. you take a deep breath,")
    print("feeling the weight o thier expectations and fears. Finally, you nod in agreement.Thank god someone said")
    print("so i didn't have to and sound like a coward you think to yourself. As you and your friends step into the")
    print("dark asylum,the heavy door creaks shut behind you, echoing through the dimly lit foyer. Dust particales")
    print("dance in the beams of your flashlights, casting eerie shadows n the peeling walls. The air is thick")
    print("with the scent o mildew and decay. After a moment of uneasy silence, you turn to yur friends and suggest")
    print("your next move. Do you want to split into pairs and explore diferent areas or stick together and head")
    print("to the administrations office?")
    print("[Pairs]or[Together]")
    choice = input()
    if choice == "pairs":
        go_pairs
    elif choice == "together":
        go_together
def go_together():
    print("You and yur friends agree that it's best to sta togethe. th group moves cautiously toward the admins office,")
    print("each step echoing int he eerie silence. The door creaks open, revealing a room shrouded in darkness and dust")
    print("Do you continue into the Admins office or go back home?")
    choice = input()
    if choice =="admins office":
        go_admin
    elif choice == "back":
        go_back
def go_admin():
    print("The office is cluttered with old files, overturned furniture, and a thick layer of dust covering")
    print("everything. As you shine your flashlights around, can't shake the feeling that you're being watched.")
    print("An old wooden desk stands in the corner, covered in dust. There might be something interesting hidden inside")
    print("Your friends are torn between checking the desk or going to another room it comes down to your vote. Do you ")
    print("vote to stay and check the desk or Explore the Main Hall")
    print("[Desk]or[Main Hall]")
    choice = input()
    if choice == "desk":
        explore_desk
    elif choice == "main hall":
        explore_main_hall
def explore_desk():
    print("Suddenly,A loud bang rverberated fro the hallway outside, makin everyone jump. You exchange nervous")
    print("glances as the noise grows louder, echoing through the halls.")
    print("Do you walk toward the noise or run back to the front door")
    print("[Noise]or[back]")
    choice = input()
    if choice == "noise":
        examine_noise
    elif choice =="back":
        go_back
        def examine_noise():
            print("You exchange worried glances with your friends, and adrenaline surges through you.")
            print("'We should check that out,' you suggest, and everyone nods in agreement")
            print("Cautiously, you make your way toward the door, your hearts pounding in unison.")
            print("[The Noise]")
            choice = input()
            if choice == "noise":
             go_to_noise
def go_to_noise():
    print("As you step into the dimly lit hallway, the air feels charged with anticipation. The sound echoes again—this time, a series of heavy thuds,") 
    print("as if something is being dragged across the floor.You decide to follow the sound, moving deeper into the asylum. The thuds seem to lead you toward a")
    print("darkened corridor at the end of the hall.As you approach, the noise grows louder, and your pulse quickens.With each step, the atmosphere becomes more")
    print("oppressive.The shadows stretch ominously,and the flickering light from your flashlight barely cuts through the darkness. Suddenly, the thuds stop.You")
    print("turn a corner and find yourself in a large,dimly lit room filled with old medical equipment.The air is thick with dust, and the silence is deafening.In") 
    print("the corner, something shifts, and you catch a glimpse of a shadow darting away.'Did you see that?' Marina whispers, her voice trembling. Just thena chilling")
    print("breeze sweeps through the room, extinguishing your flashlight for a moment.When the light flickers back on, you see it—a ghostly figure standing at the far end ")
    print("of the room, its eyes locked onto yours.The atmosphere is charged with tension and fear.What happens next unfolds in slow motion. A chilling wail pierces the") 
    print("silence, echoing from the depths of the asylum—a sound that could only belong to the tormented souls trapped within its grasp. You feel a cold sweat trickle ") 
    print("ldown your spine as the shadows stretch and twist, revealing grotesque figures in the gloom.Suddenly, a door slams shut somewhere behind you, the sound reverberating ") 
    print("like a gunshot. The walls seem to pulse, as if alive, and your heart races with a mix of fear and adrenaline. You turn to Royce, only to find him staring, horror-stricken,") 
    print("at something behind you.Before you can react, a pair of skeletal hands burst through the wall, dragging Marina back into the darkness. Blood splatters across her face,")
    print(" warm and sticky, as Royce reaches for her. “No!” he screams, but it’s too late. The asylum devours her scream, leavinonly silence, the echoes of their terror swallowed by the")
    print(" very walls that had witnessed so much suffering.Asher’s flashlight flickers, illuminating nothing but shadows, and he stumbles backward, nearly tripping over the debris. 'We ") 
    print("have to go!'he shouts, but the despair in his voice is lost amidst the creeping dread.In that moment, the asylum claims another soul, its hunger insatiable. The last thing you see ") 
    print("is Royce’s desperate face fading into the shadows, forever haunted by the horrors you uncovered. Asher’s cries echo in your mind, a chilling reminder of the price of curiosity, as ")
    print("the darkness closes in around you all.")
    print("You have reached the end of the line,Go back to find the eay out.")






#Start Program
main()