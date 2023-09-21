from word2vec_emb import load_nlp, compute_vord2vec
from similarity_metrics import euclidean_word2vec

import matplotlib.pyplot as plt
import random
from colorama import Fore, Style

# Define ANSI escape codes for green text
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'
BLUE = '\033[0;34m'

# Define main block
if __name__ == "__main__":
    
    while True:
    
        # Welcome the user
        input("Hello! Welcome to Word Similarity! (Press Enter to continue...)")

        # Ask the user for word
        input("First I need to know which word we'll be calculating similarity to!")
        word2guess = input("{}Which is the word?: {}"
                        .format(BLUE, RESET))
        
        nlp = load_nlp()
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
        
        # Ask for the number of players
        num_players = int(input("{}Now, enter the number of players:{} ".format(BLUE, RESET)))

        # Ask for the name of each player and their choice
        player_names = []
        player_choices = {}
        
        for i in range(num_players):
            name = input("{}Enter the name of player {}: {}"
                    .format(BLUE, i+1, RESET))
            choice = input("{}Enter the choice for player {}: {}"
                        .format(BLUE, name, RESET))
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

        # Display the list of players and their choices
        print("The current list of players and their choices is:")
        for name, choice in player_choices.items():
            print("{}: {}".format(name, choice[0]))
        
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

        # Check if any number is negative (for visualization purposes)
        has_negative_number = False
        for value in sorted_similarities.values():
            if value[1] < 0:
                has_negative_number = True
                break

        # Message showing winenr
        input("Let's see who the winner is!")

        winner = next(iter(sorted_similarities.keys()))
        print(f"Congratulations {Fore.GREEN}{winner}{Style.RESET_ALL}! You won!!")
        print("Let's take a look at the ranking:")

        # Message showing rank
        for i, (key, value) in enumerate(sorted_similarities.items()):
            print(f"{i+1}. {key} achieved {value[1]} with the word '{value[0]}'")

        # Ask user if they want to plot the rank
        plot = input("{}Do you want to plot the results? (Y/N):{}".format(BLUE, i+1, RESET))

        if plot == 'Y':
            x_labels = list(sorted_similarities.keys())
            numbers = [value[1] for value in sorted_similarities.values()]
            colors = [f'#{random.randint(0, 0xFFFFFF):06x}' for _ in range(len(x_labels))]

            plt.bar(x_labels, numbers, color=colors)
            
            # Set the plot title and axis labels
            if has_negative_number:
                plt.ylim([-1, 1])
            else:
                plt.ylim([0, 1])
            plt.title(f'Similarity with {word2guess}')
            plt.xlabel('Player')
            plt.ylabel('Similarity')

            plt.show()


        # Ask the participant if they want to play again
        play_again = input("{}Do you want to play again? (Y/N): {}"
                        .format(BLUE, RESET))
        if play_again.lower() != "y":
            break

    print("Thanks for playing!")