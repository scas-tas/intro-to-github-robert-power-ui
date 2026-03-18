brothers_games = ["Lawnmowing Simulator", "Mario Kart 8", "Terraria", 
                  "Human: Fall Flat", "Stardew Valley", 
                  "Super Mario Bros. Wonder", "Pikmin 4", "Minecraft", 
                  "Pokemon Violet"]

for game in brothers_games:
  print(f"game: {game}")

own_it = input("Check if I own this game: ")

if own_it.title() in brothers_games:
  print(f"You own {own_it.title()}.")
else:
  print("Game not found.")
