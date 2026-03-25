#The user has a brother who wants to play a video game with them. A list of the brother's games and their costs will be given to you. You then have to input a game of any choice.
#The user will have to input their money, the video game suggestion, and the suggested video game's genre.
#These games will have their own genres and costs, and the you will have to choose a game to play together when:
#The game aligns with his taste of genre at the time (the list of genres he's interested in will be given to you).
#The user can either input a game his brother owns, or a game the user owns. If the brother owns the game already, the user will have to pay for it.
#If the player is the only one who owns the game, the brother will have to pay for it.
#Neither person can go into debt, and you will be asked to choose another game.

brother1_games_genres = {"Lawnmowing Simulator": "Simulation", 
                         "Mario Kart 8": "Racing", 
                         "Terraria": "Sandbox",  
                         "Human: Fall Flat": "Puzzle", 
                         "Stardew Valley": "Simulation", 
                         "Super Mario Bros. Wonder": "Platformer", 
                         "Pikmin 4": "Adventure", 
                         "Minecraft": "Sandbox", 
                         "Pokemon Violet": "Adventure"}
brother1_games_cost = {"Lawnmowing Simulator": 28.96, 
                         "Mario Kart 8": 59.96, 
                         "Terraria": 14.5,  
                         "Human: Fall Flat": 28.93, 
                         "Stardew Valley": 16.98, 
                         "Super Mario Bros. Wonder": 59.99, 
                         "Pikmin 4": 79.95, 
                         "Minecraft": 29.99, 
                         "Pokemon Violet": 69.0}

print("Hello. Your brother would like to play a video game with you, but he is unsure of which one to play.")
print("Here are some games he already has:")
print("---------------------")
for game in brother1_games_genres:
  print(game)
print("---------------------")
print("If you want to play one of these, you will have to pay to buy it.")
librarydecision = input("Would you like to play one of the games in his library (Yes/No)? ").title()
if librarydecision == "Yes":
  gamefrombrolibrary = input("Alright, what game would you like to play? ").title()
  if gamefrombrolibrary in brother1_games_genres:
    def yourmoney(input(f"Alright. How much money is in your bank account {$xx.xx}? ")):
      if yourmoney < (brother1_games_cost[game]):
        print("You cannot play that game right now, as that game is 'MONEY GO HERE' and you would go into debt.)
else:
  print(".")