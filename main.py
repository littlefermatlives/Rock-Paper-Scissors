import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to Rock, Paper, Scissor Game!")
player1 = input("Enter Your choice : Rock -> R, Paper -> P, Scissor -> S\n")
#randomly select computers choice
random_integer = random.randint(1,3)
player2  = 'R'
if random_integer == 2:
    player2 = 'P'
elif random_integer == 3:
    player2 = 'S'



#printing choices made by computer and player


print("Your choice ->")
if(player1 == 'R'):
    print(rock)
elif player1 == 'S':
    print(scissors)
elif player1 == 'P':
    print(paper)
print('Computers Choice ->')
if(player2 == 'R'):
    print(rock)
elif player2 == 'S':
    print(scissors)
elif player2 == 'P':
    print(paper)



#Deciding who will win!
if player1 == 'R':
    if player2 == 'S':
        print("You Win!")
    elif player2 == 'P':
        print("You Lose!")
    elif player2 == 'R':
        print("Draw!")
elif player1 == 'S':
    if player2 == 'R':
        print("You Lose!")
    elif player2 == 'P':
        print("You Win!")
    else:
        print("Draw!")
elif player1 == 'P':
    if player2 == 'S':
        print("You Lose!")
    elif player2 == 'R':
        print("You Win")
    else : 
        print("Draw")
else : 
    print("Enter correct Choice")
