#The user has three siblings: a brother, another brother, and a sister. Using a dictionary for every person including themself, they will assign a list of games to each dictionary.
#These games will have their own genres, platform compatibility and multiplayer compatibility listed, and the four siblings (including them) will have to choose a game to play together when:
#The time is between 9AM and 10PM (thats when everyone is awake)
#The game aligns with everyones taste of genre at the time (depending on the users input of their specified taste from a group of options)
#This means the user will have to code that the majority of the siblings have no problem with the game chosen (at least three, including the user)
#If its a draw, another game will have to be chosen (or the code restarts and different information is inputted by the user for the users taste in games)
#If someone does not have the game in their library already, they must buy it. Everyone has their own specified amount of money
#, though the user will not have to input any amount of money for themselves (why would they be choosing a game that they havent bought yet?)
#The game is available on the correct platform (everyone has their own platform, so the game has to be available for purchase on all of them.)
#Possible genres: Puzzle, Action-Adventure, Arcade, Shooter, Platformer, Sandbox, Action RPG, Turn-Based Strategy.


brother1_games_genres = {"Lawnmowing Simulator": "Simulation", 
                         "Mario Kart 8": "Racing", 
                         "Terraria": "Sandbox",  
                         "Human: Fall Flat": "Puzzle", 
                         "Stardew Valley": "Simulation", 
                         "Super Mario Bros. Wonder": "Platformer", 
                         "Pikmin 4": "Adventure", 
                         "Minecraft": "Sandbox", 
                         "Pokemon Violet": "Adventure"}

for game in brother1_games_genres:
  print(f"Game: {game}")

your_games = input("What games do you own? ")

if own_it.title() in brother1_games_genres:
  print(f"You own {own_it.title()}.")
else:
  print("Game not found.")
