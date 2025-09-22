import random

def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)
    return roll
while True:
  players=(input("Enter the number of players (2-4): "))
  if players.isdigit():   
   players=int(players)
   if (players>=2 and players<=4):
    break 
   else:     
     print("Must be between 2 to 4 !")

  else :
    print("Invalid ! Try again !")
  
max_score=50
players_scores=[0 for _ in range(players)]#puts 0 (score) for each player
#range will loop for (no. of players) times

while max(players_scores)<max_score:
    
    for player_idx in range(players):
         print("\n Player number ", player_idx + 1 , " turn has just started ! \n ")
         print("Your total score is : ",players_scores[player_idx],'\n')
         current_score=0
      
         while True:
             should_roll=input("Would you like to roll? Press 'y' for yes  ? ")
             if should_roll.lower()!= "y":              
               break
             value=roll()
             if value==1:
               print("You rolled a 1! Your turn over !")
               current_score=0
               break
             else:
                current_score+=value
                print("You rolled a : ",value)
             print("Your current score is : ",current_score)
         players_scores[player_idx]+=current_score
         print("Your total score is  : ", players_scores[player_idx])

max_score=max(players_scores)
winning_idx=players_scores.index(max_score)
print("Player number",winning_idx+1,"is the winner with the score of : ",max_score)

  
  