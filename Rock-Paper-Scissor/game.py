def game():
    choice={
        'Paper': 0,
        'Scissor':1,
        'Rock':2
    }
    for key,value in choice.items() :
        print(f'{key} : {value}')
    print()
    reverse={ 0: 'Paper', 1 : 'Scissor',2 : 'Rock'}
    
    userchoice=input("Enter Your Choice : ").capitalize()
    while userchoice not in choice: 
        print('Invalid Choice')
        userchoice=input("Enter Your Choice : ").capitalize()
    print()
    user=choice[userchoice]
    import random
    computer=random.choice([0,1,2])
    print(f"\nYou Choose : {reverse[user]}({choice[userchoice]})\nComputer choose : {reverse[computer]}({computer})")

    if user == computer:
        print("\n === It's a tie! ===\n")
        return -1
    elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
        print("\n  +++ You win! +++\n")
        return 1
    else:
        print("\n --- You lose! ---\n")
        return 0
    

print("\n=== Welcome to Rock,Paper & Scissor Game ===\n")
userscore=0
computerscore=0
tie=0
c='Y'
while True :
    score=game()
    if score==1: 
        userscore+=1
    elif score==0:
        computerscore+=1
    else :
        tie+=1
    c=input("Want to Play Again(Y/N) : ").strip().lower()
    print()
    if c=='n':
        break

print('\n ----  FINAL SCORES  ---- \n')
print(f'Computer Score : {computerscore}')
print(f'Your Score : {userscore}')
print(f'Tie Score : {tie}\n')

print('---- THANKS FOR PLAYING ----')


