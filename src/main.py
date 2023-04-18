# Define ANSI escape codes for green text
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

# Define main block
if __name__ == "__main__":
    
    while True:
    
        # Welcome the user
        input("Hello! Welcome to 'Palabra del Día'! (Press Enter to continue...)")
        
        # Ask for the number of players
        num_players = int(input("{}Enter the number of players:{} ".format(GREEN, RESET)))


        # Ask for the name of each player and their choice
        player_names = []
        player_choices = {}
        for i in range(num_players):
            name = input("{}Enter the name of player {}: {}"
                    .format(GREEN, i+1, RESET))
            choice = input("{}Enter the choice for player {}: {}"
                        .format(GREEN, name, RESET))
            player_names.append(name)
            player_choices[name] = choice

        # Display the list of players and their choices
        print("The current list of players and their choices is:")
        for name, choice in player_choices.items():
            print("{}: {}".format(name, choice))

        # Ask the user if the list is correct
        correct = input("{}Is the list correct? (yes/no): {}"
                    .format(GREEN, RESET))

        # Allow the user to modify the list
        while correct.lower() == "no":
            # Ask the user which player they want to modify
            name_to_modify = input("{}Which player do you want to modify? (enter name): {}"
                            .format(GREEN, RESET))
            
            # Check if the entered name is valid
            if name_to_modify not in player_names:
                print("{}Error: That user does not exist.{}".format(RED, RESET))
                continue
            
            # Ask for the new choice for the player
            new_choice = input("Enter the new choice for player {}: ".format(name_to_modify))
            
            # Update the player_choices dictionary with the new choice
            player_choices[name_to_modify] = new_choice
            
            # Display the updated list of players and their choices
            print("The current list of players and their choices is:")
            for name, choice in player_choices.items():
                print("{}: {}".format(name, choice))
            
            # Ask the user if the list is correct
            correct = input("{}Is the list correct? (yes/no): {}"
                        .format(GREEN, RESET))

        print("The final list of players and their choices is:")
        for name, choice in player_choices.items():
            print("{}: {}".format(name, choice))

        # Ask the user for 'la palabra del día'
        word2guess = input("{}Which is the 'Palabra del Día': {}"
                        .format(GREEN, RESET))
        
        input("Thanks!! I have all the data :")

        ## Compute word2vec embeddings

        # Call word2vec function and return embedding of palabra del dia
        
        # Loop over user word choices

            # Call word2vec function and return embedding for a user

            # Call distance function and return distance
            # Store distance in the key of the users name in the previous dict

        # Rank outputs

        # Ask user if they want to plot the rank

            # If yes, plot rank

        # Ask user if they want to try with context

        # Ask again for names of players, word of choice and sentence for context

        
        ## Compute BERT embeddings

        # Call BERT function and return embedding of palabra del dia
        
        # Loop over user word choices

            # Call word2vec function and return embedding for a user

            # Call distance function and return distance
            # Store distance in the key of the users name in the previous dict

        # Rank outputs

        # Ask user if they want to plot the rank

            # If yes, plot rank

        # Ask the user if they want to play again

            # If yes, repeat all process
            # If not, say goodbye
