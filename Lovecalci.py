print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your codebelow this line 👇
true=0
love=0
for x in name1:
  if (x=="T" or x=="t") or (x=="R" or x=="r") or (x=="U" or x=="u") or (x=="E" or x=="e"):
    true+=1
  if (x=="L" or x=="l")or (x=="O" or x=="o") or (x=="V" or x=="v") or (x=="E" or x=="e"):
    love+=1
for x in name2:
  if (x=="T" or x=="t") or (x=="R" or x=="r") or (x=="U" or x=="u") or (x=="E" or x=="e"):
    true+=1
  if (x=="L" or x=="l")or (x=="O" or x=="o") or (x=="V" or x=="v") or (x=="E" or x=="e"):
    love+=1
percentage=int(str(true)+str(love))
if percentage<=10 or percentage>=90:
  print(f"Your score is {percentage}, you go together like coke and mentos")
elif percentage>=40 and percentage<=50:
  print(f"Your score is {percentage}, you are alright together.")
else:
  print(f"Your score is {percentage}.")

