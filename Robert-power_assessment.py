# You have a brother who wants to play a video game with you. A dictionary containing the games he already owns is here, plus the costs of each:
brother_games_cost = {"Lawnmowing Simulator": 29, 
                         "Mario Kart 8": 60, 
                         "Terraria": 15,  
                         "Human: Fall Flat": 29, 
                         "Stardew Valley": 17, 
                         "Super Mario Bros. Wonder": 60, 
                         "Pikmin 4": 80, 
                         "Minecraft": 30, 
                         "Pokemon Violet": 69}

# And here is how much money your brother has (or how much he's willing to spend on a video game, at least).
brothermoney = 50

# Here, we're defining the process of confirming your game selection (the code of which you can see after these two functions), but only IF you choose to select an option out of your brother's list of games.
def brothergameconfirmation(gamechoice):
  # This identifies whether or not the game you choose is in your brother's game list already, considering that earlier, you would have gotten the specific options to select a game from his library or an unrelated game, foreign to the pre-existing library.
  if gamechoice in brother_games_cost:
    # An input of the money you have to determine if you have enough to purchase the game in his library, always assuming you don't have it already.
    # There is also some more lines of code here to account for answers that cannot be processed as integers, so that it is impossible to get an error when running this code.
    while True:
      try:
        # This is the money input, which is then translated into an integer if the input allows (follows the value format).
        yourmoney = int((input("How much money are you willing to pay for a game ($xx)? ")))
        break
      # This takes care of any value errors (e.g. inputting anything that isn't a value) and allows the user to repeat the question again to avoid stopping the program prematurely.
      except ValueError:
        print("Only enter the number of dollars, with no sign beforehand.")

    # Determines the next move based on how much money you have. Here, this path is for when you have less money than the amount that the game requires to play.
    if yourmoney < (brother_games_cost[gamechoice]):
      print(f"You cannot play that game right now, as that game is ${brother_games_cost[gamechoice]}. Please choose another.")
      # Allows a loop for when your option was rejected - now you can choose another game that hopefully meets the criteria.
      gamefrombrolibrary = input("What game would you like to play? ").title()
      return(brothergameconfirmation(gamefrombrolibrary))
    else:
      # This is used if you did indeed have enough money to buy and play the game in your brother's library.
      return(f"Congratulations! You and your brother can now both play {gamechoice} together. Have fun!")
  else:
    # This part is printed if your input for a game in the library doesn't match any of the games in the library.
    print("That game is not already in your brother's library. Please choose another.")
    # Allows a loop for when you option is rejected - you can now try again.
    gamefrombrolibrary = input("What game would you like to play? ").title()
    return(brothergameconfirmation(gamefrombrolibrary))

# Here, we're defining the process of confirming your game selection (the code of which you can see after these two functions), but only IF you choose to select a game that your brother does not have yet.
def mygameconfirmation(gamechoice):
  # Here, you must input how much money your game costs.
  print("You will not have to pay for this one, however, your brother will. He's willing to spend $50.")
  # Again, more code to ensure the correct mode of input, as mentioned in the previous function.
  while True:
      try:
        # This is where you input the cost of your game, and your answer is converted into an integer (if possible)
        mygamecost = int(input(f"How much money does it take to play {gamechoice} ($xx)? "))
        break
      # There will not be any errors if you enter anything that cannot function with the code above, as it will instead ask you to try again.
      except ValueError:
        print("Only enter the number of dollars, with no sign beforehand.")
  # Now, we decide whether your brother has enough money to purchase and play the game.
  if mygamecost <= brothermoney:
    # If he does have the money (the cost is lower or equal to the amount of money your brother is willing to spend), then the code ends successfully.
    return(f"Congratulations! He has the money, and you and your brother can now both play {gamechoice} together. Have fun!")
  else:
    # If he doesn't have the money, then you are allowed to put in another input, and choose a different game that you already own, hoping it meets the criteria.
    print("Your brother does not have the funds for that purchase. Please choose another.")
    gamefrommylibrary = input("What game would you like to play? ").title()
    return(mygameconfirmation(gamefrommylibrary))
  
# This function represents the first decision that the user makes - where they'd like to select a game from.
def decisionprocess(decisioninput):
  if decisioninput == "Yes":
    # The game choice you make here is the game you're trying to find.
    gamefrombrolibrary = input("Alright, what game would you like to play? ").title()
    # Connects to the appropriate function for both valid options.
    return(brothergameconfirmation(gamefrombrolibrary))
  elif decisioninput == "No":
    gamefrommylibrary = input("Alright, what game would you like to play? ").title()
    return(mygameconfirmation(gamefrommylibrary))
  # Any other input that isn't 'yes' or 'no' is accounted for, and the user will be asked to try again, to avoid any errors and to allow the code to continue.
  else:
    print("Your brother is decisive, and would rather you give 'yes' or 'no' as an answer.")
    decisioninput = input("Would you like to play one of the games in his library (Yes/No)? ").title()
    return(decisionprocess(decisioninput))


# Here's what's actually shown to the user as the code progresses, starting off with the introduction.
print("Hello. Your brother would like to play a video game with you, but he is unsure of which one to play.")
print("Here are some games he already has, plus how much they each cost:")
print("---------------------")
# Prints the dictionary of the brother's library of games with the costs, with one game + cost represented per line before moving onto the next line.
for game, cost in brother_games_cost.items():
  print(f"{game}: ${cost}")
print("---------------------")
print("If you want to play one of these, you will have to pay to buy it.")
# The answer you give is put in title format to allow for the proceeding few lines to work no matter what case you use for your answer.
librarydecision = input("Would you like to play one of the games in his library (Yes/No)? ").title()
# This function, as shown above, represents the 'Yes' or 'No' decision for your choice of the option to play a game that he already has.
# This also functions as a channel to the rest of the code, as this function also contains the other functions, which themselves lead to a satisfactory end of the program.
print(decisionprocess(librarydecision))