import random
rock=''' 
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
'''

paper='''
             _
         _  / |
        / \ | | /\ 
        \ \| |/ /
         \ Y | /___
       .-.) '. `__/
      (.-.   / /
          | ' |
          |___|
         [_____]
         |     | 
'''
scissors='''
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
'''
game_images=[rock,paper,scissors]
play="y"
while(play.lower()=="y"):
    comp_choice=random.randint(1,3)
    user_choice = input("Enter 1 for rock, 2 for paper, 3 for scissors:\n")
    user_choice=int(user_choice)
    if(1<=user_choice<=3):
        print("You chose:\n",game_images[user_choice-1])
        print("Computer chose:\n",game_images[comp_choice-1])
        if(comp_choice==user_choice):
            print("Draw!!!")
        elif(comp_choice==1 and user_choice==2):#rock vs paper
            print("User wins")
        elif(comp_choice==2 and user_choice==3):#paper vs scissors
            print("User wins")
        elif(comp_choice==3 and user_choice==1):#rock vs scissors
            print("User wins")
        else:
            print("Computer wins")
        play=input("Do you wish to play again? If yes please press 'y':\n")
    else:
        print("Invalid choice,please enter a no. between 1 and 3")
print("Thanks for playing")
    
