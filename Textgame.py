import sys
import time


def one_character_at_time(a):
    for x in a:
        print(x, end="", flush=True)
        time.sleep(0.008)


# all the text is here
a = """'You are a reporter due to your succesful sting operations the department has asked you to cover one such case which includes some sort of cult involved as the passersby have reported some supernatural phenomenons like sudden weather change, weird bright flashes and some otherworldy screams.All of these sightings were reported in the region of Massive Quagmire Forest near the town of Qwerbert."""

b = """You go over there by a car, on the side of the highway you slow your car down as you see some orange glow from the middle of the forest you decide that you will go and have a look. You go inside the forest and ..
..You stumble upon a crypt more like a home of cult followers 
the cult has its symbol on the door
the door is slightly open and you can see warm yellow flickering light coming through like a fire is burning in the fireplace."""

f = """You saw a strange gate with a weird symbol on it, intuitively you thought that it must be leading to the root of all of this You tried asking some of the cult members about how to enter the main grounds. No one answered your question but some of them said you need to provide the gates some of your blood, so that you can enter the main area"""

h = """You started looking for a sharp thing so that you can cut yourself in order to open the gates,at first you thought that maybe you should find your chance to run away, but soon you looked around and realised that you cannot escape this place anymore"""

n = """You secretively snuck into the suspiciously lit cave it turned out to be a establishment of a tribe and you saw various arts and writings. The writings were smudged and in an ancient tounge so you couldnt make much of it.\n The art depicted that there is supposed to be a magical dagger in here somewhere and you need to somehow manage to either make someone bleed this someone could be yourself,and let the spirit of the gurdian diety take you."""

n1 = """Is what was written on the wall but you couldnt understand the writing but by looking at the art all you guessed was that there is a special dagger in this cave you went on to find it."""

q = """You have acqquired the special dagger, you felt a tingle in your spine as soon as you picked the dagger."""

r = """You were secretively trying to rach back the main area but to your notice some of the cultists know what has happend and they came to capture you."""

r1 = """You had no choice but to kill them one by one, suddenly you notice that the look of the dagger has changed, you rushed towards the outside in order to flee from this place as the entire place was in utter chaos"""

s = """You tripped on a stone and fell, the dagger slipped out of your hand, before you could grasp the daggger, you felt something was off, the next moment your wrist was cutted clean off by the dagger.THE DAGGER HAD ITS OWN WILL"""

t = """The ritual was complete and now the being came into existence, it took your body, your soul was nothing compared to his, you perished instantly and then the being confronted all three of the higher members of the cult and finished them off one by one."""

u = """Sister Marisol was decapitated in an instant by the being, blood spilled on the ground, Brother Diego was chopped into pieces, and Brother Javier begged for his life to be spared but the being did not spare anyone and mutilated every cultist present in the area \n"""

v = """The screams were slowly absorbed by the dense forest, Your body wasnt found, no bodies were found and your investigation file was closed.\n"""

w = """The company you worked for told your colleague that you left the company and moved to a different town.\n"""

x = """Sadly, no was there to check whether it was truth or a lie.\n"""


def start_game():
    time.sleep(2)
    print(
        r"""
 ___ _,_ __,    _,  _, _, _  _, ___ _,_  _, __, , _   ___ __, _  _, _,   _,
  |  |_| |_    (_  /_\ |\ | / `  |  | | /_\ |_) \ |    |  |_) | /_\ |   (_ 
  |  | | |     , ) | | | \| \ ,  |  | | | | | \  \|    |  | \ | | | | , , )
  ~  ~ ~ ~~~    ~  ~ ~ ~  ~  ~   ~  `~' ~ ~ ~ ~   )    ~  ~ ~ ~ ~ ~ ~~~  ~ 
                                                 ~'"""
    )
    time.sleep(7)
    one_character_at_time(a)
    time.sleep(3)
    print("\n")
    print(
        "Your job is to investigate the location and report back with whatever evidence you can get."
    )
    time.sleep(2)
    animation_chars = ["|", "/", "-", "\\"]
    for _ in range(10):  # Adjust the number of iterations as needed
        for char in animation_chars:
            sys.stdout.write("\rStarting the investigation " + char)
            sys.stdout.flush()
            time.sleep(0.05)  # Adjust the delay as needed
    print("\n")
    one_character_at_time(b)
    time.sleep(2)
    investigate_glow()


def investigate_glow():
    time.sleep(1)
    print("\n")
    print("1. Open the door and enter.")
    print("2. Leave this case and go back")

    choice = input("Enter your choice: ")
    time.sleep(3)

    if choice == "1":
        enter_cult_home()
    elif choice == "2":
        print("Congratulations! You returned back safely.\n")
        print(
            r"""
__   __            _     _             _____       _____              ___              _   _                ______            _ _ _ 
\ \ / /           | |   (_)           |_   _|     /  ___|            / _ \            | | | |               |  _  \          | | | |
 \ V /___  _   _  | |    ___   _____    | | ___   \ `--.  ___  ___  / /_\ \_ __   ___ | |_| |__   ___ _ __  | | | |__ _ _   _| | | |
  \ // _ \| | | | | |   | \ \ / / _ \   | |/ _ \   `--. \/ _ \/ _ \ |  _  | '_ \ / _ \| __| '_ \ / _ | '__| | | | / _` | | | | | | |
  | | (_) | |_| | | |___| |\ V |  __/   | | (_) | /\__/ |  __|  __/ | | | | | | | (_) | |_| | | |  __| |    | |/ | (_| | |_| |_|_|_|
  \_/\___/ \__,_| \_____|_| \_/ \___|   \_/\___/  \____/ \___|\___| \_| |_|_| |_|\___/ \__|_| |_|\___|_|    |___/ \__,_|\__, (_(_(_)
                                                                                                                         __/ |      
                                                                                                                        |___/
                                                                                                                        
                                                                                                                        
                                                                                                                        """
        )
        input("Press any key to exit")
        exit()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        investigate_glow()


def enter_cult_home():
    print(
        "\nYou chose to open the door, you enter the house and see its a cozy place at first nothing seems wrong but suddenly you felt that someone was watching you through the windows and you hear rustling of bushes and leaves. You felt that your cabin is surrounded by the cult members."
    )
    time.sleep(1)
    print("1. Try to run.")
    print("2. Stay calm and see through it.")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print(
            "\nYou tried to run but unfortunately you got meleed by a cult member yet you ran in a random direction, you had a blurry vision and you were running blindly you tripped and hit your head on a rock, the rock was sharp enough to crack your skull open, you died."
        )
        time.sleep(2)
        print(
            r"""    
           ______
        .-"      "-.
       /            \ 
      |              |
      |,  .-.  .-.  ,|
      | )(__/  \__)( |
      |/     /\     \|
      (_     ^^     _)
       \__|IIIIII|__/
        | \IIIIII/ |
        \          /
         `--------`
         
         _______            ______ ________________ ______  
|\     /(  ___  |\     /|  (  __  \\__   __(  ____ (  __  \ 
( \   / | (   ) | )   ( |  | (  \  )  ) (  | (    \| (  \  )
 \ (_) /| |   | | |   | |  | |   ) |  | |  | (__   | |   ) |
  \   / | |   | | |   | |  | |   | |  | |  |  __)  | |   | |
   ) (  | |   | | |   | |  | |   ) |  | |  | (     | |   ) |
   | |  | (___) | (___) |  | (__/  ___) (__| (____/| (__/  )
   \_/  (_______(_______)  (______/\_______(_______(______/ """
        )
        input("Press any key to exit: ")
        exit()
    elif choice == "2":
        print(
            "\nYou tried to keep yourself as calm as possible even though it didn't feel like it helped but, one of the cult members safely escorted you out of the house without harming you and you found that all the cult members were escorting you to an area which looked like the main grounds of the cult"
        )
        time.sleep(0.5)
        print("\n")
        one_character_at_time(f)
        time.sleep(2)
        sacrifice_choice()


def sacrifice_choice():
    time.sleep(3)
    print(
        r"""

         A                                                                                            A
        / \                                                                                          / \ 
       _\_/_                                         /\  /\                                         _\_/_
      / _ __\                                 /\     \/  \/     /\                                 / _ __\ 
      \_____/                                 \/    <``><''>    \/                                 \_____/
       |___|                           /\    <``>    TT  TT    <''>    /\                           |___|
      /     \                          \/     TT     ||  ||     TT     \/                          /     \ 
     /       \                  /\    <``>    ||     ||  ||     ||    <''>    /\                  /       \ 
  __/____ ____\__               \/     TT    <||>._.<||  ||>._.<||>    TT     \/               __/____ ____\__
 /_______________\       /\    <``>    ||>.=""||,.-. ||  || .-.,||""=.<||    <''>    /\       /_______________\ 
 )_______________(       \/     TT    <||,.-.<||"   "||  ||"   "||>.-.,||>    TT     \/       )_______________(
  |_|___|___|___|       <``>    ||>.=""||"   "||     ||  ||     ||"   "||""=.<||    <''>       |_|___|___|___|
  |___|___|___|_| /\     TT    <||,.-.<||     ||"-_-"||  ||"-_-"||     ||>.-.,||>    TT     /\ |___|___|___|_|
  |_|___|___|___| \/     ||>.=""||"   "||"-_-"||> .=<||  ||>=. <||"-_-"||"   "||""=.<||     \/ |_|___|___|___|
  |___|___|___|_|<``>    ||,.-.<||     ||> .=<||>"   ||__||   "<||>=. <||     ||>.-.,||    <''>|___|___|___|_|
  |_|___|___|___| TT    <||"   "||"-_-"||."   ||     ||/\||     ||   ".||"-_-"||"   "||>    TT |_|___|___|___|
  |___|___|___|_| ||  ,* ||     ||> .=<||>    ||     ||()||     ||    <||>=. <||     || *,  || |___|___|___|_|
  |_|___|___|___|_||>*  ,||"-_-"||."   ||     ||     ||\/||     ||     ||   ".||"-_-"||,  *<||_|_|___|___|___|
  |___|___|___|_|__|,.-.<||> .=<||>    ||     ||     ||__||     ||     ||    <||>=. <||>.-.,|__|___|___|___|_|
  |_|___|___|___| ||`   "||."   ||     ||     ||   ,<||  ||>,   ||     ||     ||   ".||"   '|| |_|___|___|___|
  |___|___|___|_| ||"    ||>    ||     ||     ||>,","||  ||",",<||     ||     ||    <||    "|| |___|___|___|_|
  |_|___|___|___| ||"-_-"||     ||     ||   ,<|| .-. ||  || .-. ||>,   ||     ||     ||"-_-"|| |_|___|___|___|
  |___|___|___|_| ||> .=<||     ||     ||>," "||"   "||  ||"   "||" ",<||     ||     ||>=. <|| |___|___|___|_|
  |_|___|___|___|_||>"   ||     ||>,_,<|| .-.<||     ||  ||     ||>.-. ||>,_,<||     ||   "<||_|_|___|___|___|
  |___|___|___|_|__|     ||>,_,<|| .-. ||"   "||"-_-"||  ||"-_-"||"   "|| .-. ||>,_,<||     |__|___|___|___|_|
  |_|___|___|___| ||>,_,<|| .-. ||"   "||     ||  .=<||  ||>=.  ||     ||"   "|| .-. ||>,_,<|| |_|___|___|___|
  |___|___|___|_| || .-. ||"   "||     ||"-_-"||>"   ||  ||   "<||"-_-"||     ||"   "|| .-. || |___|___|___|_|
  |_|___|___|___| ||"   "||     ||"-_-"||  .=<||     ||  ||     ||>=.  ||"-_-"||     ||"   "|| |_|___|___|___|
  |___|___|___|_| ||     ||"-_-"||  .=<||>"   ||     ||  ||     ||   "<||>=.  ||"-_-"||     || |___|___|___|_|
  |_|___|___|___|_||"-_-"||  .=<||>"   ||     ||     ||  ||     ||     ||   "<||>=.  ||"-_-"||_|_|___|___|___|
  |___|___|___|_|__|  .=<||>"   ||     ||     ||     ||  ||     ||     ||     ||   "<||>=.  |__|___|___|___|_|
  |_|___|___|___| ||>"   ||     ||     ||     ||     ||  ||     ||     ||     ||     ||   "<|| |_|___|___|___|
  |___|___|___|_| ||     ||     ||     ||     ||     ||  ||     ||     ||     ||     ||     || |___|___|___|_|
  |_|___|___|___| ||>___<||>___<||>___<||>___<||>___<||  ||>___<||>___<||>___<||>___<||>___<|| |_|___|___|___|
  |___|___|___|_| "-----------------------------------"  "-----------------------------------" |___|___|_____|"""
    )
    time.sleep(4)
    one_character_at_time(h)
    print("\n")
    animation_chars = ["|", "/", "-", "\\"]
    for _ in range(10):  # Adjust the number of iterations as needed
        for char in animation_chars:
            sys.stdout.write("\rSearching " + char)
            sys.stdout.flush()
            time.sleep(0.05)  # Adjust the delay as needed
    print("\n You found a shard of the glass lying around")
    print("\nYou have to sacrifice something of yours to proceed.")
    print("1. Cut off two fingers from your left hand.")
    sacrifice = input("Enter your choice (1): ")
    print("You cutted your pinky and ring finger from your left hand")
    print(
        "Your hand was bleeding heavily but one of the cult members dressed your hand."
    )

    if sacrifice == "1":
        print(
            "\n'You noticed that the gates were open now and 3 figures were waiting for you\n'"
        )
        time.sleep(4)
        print(
            r"""
         A                                                                                            A
        / \                                                                                          / \ 
       _\_/_                                                                                        _\_/_
      / _ __\                                 /\                /\                                 / _ __\ 
      \_____/                                 \/                \/                                 \_____/
       |___|                           /\    <``>              <''>    /\                           |___|
      /     \                          \/     TT                TT     \/                          /     \ 
     /       \                  /\    <``>    ||                ||    <''>    /\                  /       \ 
  __/____ ____\__               \/     TT    <||>              <||>    TT     \/               __/____ ____\__
 /_______________\       /\    <``>    ||>.=""||                ||""=.<||    <''>    /\       /_______________\ 
 )_______________(       \/     TT    <||,.-.<||                ||>.-.,||>    TT     \/       )_______________(
  |_|___|___|___|       <``>    ||>.=""||"   "||                ||"   "||""=.<||    <''>       |_|___|___|___|
  |___|___|___|_| /\     TT    <||,.-.<||     ||                ||     ||>.-.,||>    TT     /\ |___|___|___|_|
  |_|___|___|___| \/     ||>.=""||"   "||"-_-"||                ||"-_-"||"   "||""=.<||     \/ |_|___|___|___|
  |___|___|___|_|<``>    ||,.-.<||     ||> .=<||                ||>=. <||     ||>.-.,||    <''>|___|___|___|_|
  |_|___|___|___| TT    <||"   "||"-_-"||."   ||                ||   ".||"-_-"||"   "||>    TT |_|___|___|___|
  |___|___|___|_| ||  ,* ||     ||> .=<||>    ||                ||    <||>=. <||     || *,  || |___|___|___|_|
  |_|___|___|___|_||>*  ,||"-_-"||."   ||     ||                ||     ||   ".||"-_-"||,  *<||_|_|___|___|___|
  |___|___|___|_|__|,.-.<||> .=<||>    ||     ||                ||     ||    <||>=. <||>.-.,|__|___|___|___|_|
  |_|___|___|___| ||`   "||."   ||     ||     ||                ||     ||     ||   ".||"   '|| |_|___|___|___|
  |___|___|___|_| ||"    ||>    ||     ||     ||                ||     ||     ||    <||    "|| |___|___|___|_|
  |_|___|___|___| ||"-_-"||     ||     ||   ,<||                ||>,   ||     ||     ||"-_-"|| |_|___|___|___|
  |___|___|___|_| ||> .=<||     ||     ||>," "||                ||" ",<||     ||     ||>=. <|| |___|___|___|_|
  |_|___|___|___|_||>"   ||     ||>,_,<|| .-.<||                ||>.-. ||>,_,<||     ||   "<||_|_|___|___|___|
  |___|___|___|_|__|     ||>,_,<|| .-. ||"   "||                ||"   "|| .-. ||>,_,<||     |__|___|___|___|_|
  |_|___|___|___| ||>,_,<|| .-. ||"   "||     ||                ||     ||"   "|| .-. ||>,_,<|| |_|___|___|___|
  |___|___|___|_| || .-. ||"   "||     ||"-_-"||                ||"-_-"||     ||"   "|| .-. || |___|___|___|_|
  |_|___|___|___| ||"   "||     ||"-_-"||  .=<||                ||>=.  ||"-_-"||     ||"   "|| |_|___|___|___|
  |___|___|___|_| ||     ||"-_-"||  .=<||>"   ||                ||   "<||>=.  ||"-_-"||     || |___|___|___|_|
  |_|___|___|___|_||"-_-"||  .=<||>"   ||     ||                ||     ||   "<||>=.  ||"-_-"||_|_|___|___|___|
  |___|___|___|_|__|  .=<||>"   ||     ||     ||                ||     ||     ||   "<||>=.  |__|___|___|___|_|
  |_|___|___|___| ||>"   ||     ||     ||     ||                ||     ||     ||     ||   "<|| |_|___|___|___|
  |___|___|___|_| ||     ||     ||     ||     ||                ||     ||     ||     ||     || |___|___|___|_|
  |_|___|___|___| ||>___<||>___<||>___<||>___<||                ||>___<||>___<||>___<||>___<|| |_|___|___|___|
  |___|___|___|_| "----------------------------                 -----------------------------" |___|___|_____|

"""
        )
        time.sleep(3)

        print(
            "\nYou approached the figures they introduced themselves as Brother Diego Sister Marisol and Brother Javier, by the looks of it all 3 of them appeared that they must be in their mid-40's\n"
        )
        time.sleep(2)

        print(
            "\nThey gave you information about how this cult came to existence and what does this cult do what is their idealogy, at first you thought that they are not that harmful but suddenly they mentioned that there is a power hidden in these grounds which is far beyond our understandings\n"
        )
        time.sleep(1)
        one_character_at_time(n)
        one_character_at_time(n1)
        explore_dungeons()
    else:
        print("Invalid choice. Please enter 1.")
        sacrifice_choice()


def explore_dungeons():
    print(
        "\nWhile exploring the cave you stumbled on a crossroads but since there were no roads they were crossways(bad pun) choose which way you want to go\n"
    )
    time.sleep(1)
    print("1. Left?")
    print("2. Right?")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print(
            "\nYou chose to go on left side and as you were going through the cave you stepped on something and the floor plate felt like it sunk in and a soft rumbling sound is what you heard you started walking in the direction of the sound but unfortunately it was the pressure plate which activated the defense system of the entire cave and you fell for one such trap you fell in a hole full of spikes.\n"
        )
        time.sleep(2)
        print(
            r"""
 __      __   ______   __    __        _______   ______  ________  _______  
|  \    /  \ /      \ |  \  |  \      |       \ |      \|        \|       \ 
 \$$\  /  $$|  $$$$$$\| $$  | $$      | $$$$$$$\ \$$$$$$| $$$$$$$$| $$$$$$$\ 
  \$$\/  $$ | $$  | $$| $$  | $$      | $$  | $$  | $$  | $$__    | $$  | $$
   \$$  $$  | $$  | $$| $$  | $$      | $$  | $$  | $$  | $$  \   | $$  | $$
    \$$$$   | $$  | $$| $$  | $$      | $$  | $$  | $$  | $$$$$   | $$  | $$
    | $$    | $$__/ $$| $$__/ $$      | $$__/ $$ _| $$_ | $$_____ | $$__/ $$
    | $$     \$$    $$ \$$    $$      | $$    $$|   $$ \| $$     \| $$    $$
    \$$      \$$$$$$   \$$$$$$        \$$$$$$$  \$$$$$$ \$$$$$$$$ \$$$$$$$ """
        )
        input("Press any key to exit:")
        exit()
    elif choice == "2":
        print(
            "\nYou chose to go on the right path and you found a corpse.Search the corpse?"
        )
        animation_chars = ["|", "/", "-", "\\"]
        for _ in range(20):  # Adjust the number of iterations as needed
            for char in animation_chars:
                sys.stdout.write("\rSearching " + char)
                sys.stdout.flush()
                time.sleep(0.05)

        print(
            "\nYou found a lighter luckilly enough it has some juice left in it. \nYou chose to move straight up ahead after exploring through the caves for some hours you managed to find a chest with a weird symbol on its front."
        )
        time.sleep(2)
        print(
            r'''
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \  
             \____\ /_________\####/_________\ /____/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |===| |====    .'.'^'.'.   ====| |===|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""` '''
        )
        print(
            "\nBy the looks of the chest you guessed that the chest wont open easily you used a nearby rock to smash it open."
        )
        time.sleep(2)
        print(
            r''' 
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************'''
        )
        time.sleep(3)
        print(
            r"""


         ____
        (____)
        /____\
        |___.-~-.-~-.
        |__(  __|__  )_
        |/ \/\_/^\._)/ \
        (  (__{(@)}\_)  )
        |\_/ (/(_)\_))_/
  ______|_(  (__)_)_/ )
 /_________\_/  |  \_/
|/   /' |\  /'-~'~-'\|
    |  (| \/ |
    |   `\   |
     `\  `\  |    ___
       `\  `\|  /' ..'>
      ___`\  `\: ,' /'
    /' _ /''`\  '__'
   < .'./'   |  |
    `~' |    |  |
        |    |/'
        |    |
        |    |
        |    |
         \  /
          \/
"""
        )
        time.sleep(2)
        print(
            """

┓┏      ┓                       ┓              •       ┓            •   ┓   ┓          ╻
┗┫┏┓┓┏  ┣┓┏┓┓┏┏┓  ┏┳┓┏┓┏┓┏┓┏┓┏┓┏┫  ╋┏┓  ┏┓┏┏┓┓┏┓┏┓┏┓  ╋┣┓┏┓  ┏┳┓┏┓┏┓┓┏┏┓┃  ┏┫┏┓┏┓┏┓┏┓┏┓┃
┗┛┗┛┗┻  ┛┗┗┻┗┛┗   ┛┗┗┗┻┛┗┗┻┗┫┗ ┗┻  ┗┗┛  ┗┻┗┗┫┗┻┗┛ ┗   ┗┛┗┗   ┛┗┗┗┻┗┫┗┗┗┻┗  ┗┻┗┻┗┫┗┫┗ ┛ •
                            ┛               ┗                      ┛            ┛ ┛     

"""
        )
        time.sleep(2)
        one_character_at_time(q)
        time.sleep(2)
        one_character_at_time(r)
        time.sleep(2)
        one_character_at_time(r1)
        time.sleep(2)
        one_character_at_time(s)
        time.sleep(2)
        print(
            r"""

                                                      )         
                                                        (            
                                                      '    }      
                                                    (    '      
                                                   '      (   
                                                    )  |    ) 
                                                  '   /|\    `
                                                 )   / | \  ` )   
                                                {    | | |  {   
                                               }     | | |  .
                                                '    | | |    )
                                               (    /| | |\    .
                                                .  / | | | \  (
                                              }    \ \ | / /  .        
                                               (    \ `-' /    }
                                               '    / ,-. \    ' 
                                                }  / / | \ \  }
                                               '   \ | | | /   } 
                                                (   \| | |/  (
                                                  )  | | |  )
                                                  .  | | |  '
                                                     J | L
                                               /|    J_|_L    |\ 
                                               \ \___/ o \___/ /
                                                \_____ _ _____/
                                                      |-|
                                                      |-|
                                                      |-|
                                                     ,'-'.
                                                     '---' """
        )
        one_character_at_time(t)
        time.sleep(2)
        one_character_at_time(u)
        time.sleep(2)
        one_character_at_time(v)
        time.sleep(2)
        one_character_at_time(w)
        time.sleep(2)
        one_character_at_time(x)
        time.sleep(2)
        print(
            r"""\n
 ,__ __                    _                           _     _                      _                            _         _                           
 /|  |  |                  | |                         | |   | |o            |      | |                          | |       | |                          
  |  |  |  __,          _|_| |             ,  __       | |   | |    _  _   __|  __|_| |         _  _  __,  __  _ | |       | |    ,_   _   _  __  ,  _  
  |  |  | /  |  |   |    | |/ \   |   |   / \/  \|   | |/    |/ |  / |/ | /  | |/ | |/ \      |/ \|/ /  | /   |/ |/  |   | |/    /  | |/ |/ \/  \/ \|/  
  |  |  |_\_/|_/ \_/|/   |_|   |_/ \_/|/   \/\__/ \_/|_|__/  |__|_/  |  |_\_/|_|__|_|   |_/   |__/|__\_/|_\___|__|__/ \_/|_|__/     |_|__|__/\__/ \/|__o
                   /|                /|                      |\                              /|                  |\                     /|              
                   \|                \|                      |/                              \|                  |/                     \|             """
        )
        time.sleep(1.5)
        print("\n")
        print(
            r"""
                  _\<
                 (   >
                 __)(
           _____/  //   ___
          /        \\  /  \\__
          |  _     //  \     ||
          | | \    \\  / _   ||
          | |  |    \\/ | \  ||
          | |_/     |/  |  | ||
          | | \     /|  |_/  ||
          | |  \    \|  |     >_ )
          | |   \. _|\  |    < _|=
          |          /_.| .  \/
  *       | *   **  / * **  |\)/)    **
   \))ejm97/.,(//,,..,,\||(,wo,\ ).((// -  \)
"""
        )
        input("Press Any key to exit the game: ")
        sys.exit()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        explore_dungeons()


# Start the game
start_game()
