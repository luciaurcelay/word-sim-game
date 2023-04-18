from word2vec_emb import load_nlp, compute_vord2vec
from similarity_metrics import euclidean_word2vec

import matplotlib.pyplot as plt
import random

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
        nlp = load_nlp()
        for i in range(num_players):
            name = input("{}Enter the name of player {}: {}"
                    .format(GREEN, i+1, RESET))
            choice = input("{}Enter the choice for player {}: {}"
                        .format(GREEN, name, RESET))
            correct_embedding = False
            while correct_embedding == False:
                # Compute embedding
                embedding = compute_vord2vec(choice, nlp)
                # print(embedding)
                if all(val == 0 for val in embedding):
                    print("{}This word is invalid! Please try again.{}".format(RED, RESET))
                    choice = input("Enter new word: ")
                    continue
                correct_embedding = True

            player_names.append(name)
            player_choices[name] = (choice, embedding)

        # print(player_choices)   

        # Display the list of players and their choices
        print("The current list of players and their choices is:")
        for name, choice in player_choices.items():
            print("{}: {}".format(name, choice[0]))

        '''# Ask the user if the list is correct
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
            
            # Check if words have embeddings associated
            input("Perfect! Let's check whether the words are valid...")

            # Extract word2vec embedding from all the words
            nlp = load_nlp()
            
            for name in player_names:
                correct_embedding = False
                while correct_embedding == False:
                    # Compute embedding
                    embedding = compute_vord2vec()
                    if embedding != None:
                        # Save in dictionary
                        player_choices[name] = embedding
                        correct_embedding = True
                    else:

        print("The final list of players and their choices is:")
        for name, choice in player_choices.items():
            print("{}: {}".format(name, choice))'''

        # Ask the user for 'la palabra del día'
        input("Okay, now is time to look up which the 'Palabra del Día is!")
        word2guess = input("{}Which is the 'Palabra del Día'?: {}"
                        .format(GREEN, RESET))
        
        correct_embedding = False
        while correct_embedding == False:
            # Compute embedding
            pdd_embedding = compute_vord2vec(word2guess, nlp)
            # print(embedding)
            if all(val == 0 for val in pdd_embedding):
                print("{}This word is invalid! Please try again.{}".format(RED, RESET))
                word2guess = input("Enter new word: ")
                continue
                
            correct_embedding = True
        
        input("Thanks! I have all the data I need...")
        
        # Call similarity function and return distance
        similarities = {}
        for name, choice in player_choices.items():
            similarity = euclidean_word2vec(pdd_embedding, choice[1], nlp)
            similarity = round(similarity, 3)
            similarities[name] = (choice[0], round(similarity, 3))

        # Sort keys by number in tuple
        sorted_keys = sorted(similarities, key=lambda x: similarities[x][1], reverse=True)

        # Create new dictionary with sorted keys
        sorted_similarities = {key: similarities[key] for key in sorted_keys}

        # Message showing winenr
        input("Let's see who the winner is!")

        winner = next(iter(sorted_similarities.keys()))
        input(f"Congratulations {winner}! You won!!")
        input("Let's take a look at the ranking:")

        # Message showing rank
        for i, (key, value) in enumerate(sorted_similarities.items()):
            print(f"{i+1}. {key} achieved {value[1]} with the word '{value[0]}'")

        # Ask user if they want to plot the rank
        plot = input("{}Do you want to plot the results? (Y/N):{}".format(GREEN, i+1, RESET))

        if plot == 'Y':
            x_labels = list(sorted_similarities.keys())
            numbers = [value[1] for value in sorted_similarities.values()]
            colors = [f'#{random.randint(0, 0xFFFFFF):06x}' for _ in range(len(x_labels))]

            plt.bar(x_labels, numbers, color=colors)
            
            # Set the plot title and axis labels
            plt.ylim([-1, 1])
            plt.title(f'Similitud con {word2guess[0]}')
            plt.xlabel('Participante')
            plt.ylabel('Similitud')

            plt.show()


        # Ask the participant if they want to play again
        play_again = input("{}Do you want to play again? (Y/N): {}"
                        .format(GREEN, RESET))
        if play_again.lower() != "y":
            break

    print("{}Thanks for playing!{}".format(GREEN, RESET))