import random

def main():
    def setup_player():
         """
        Prompts the user to create their player profile.

        Returns:
            dict: A dictionary containing player stats with the following keys:
                - "name" (str): Player's name (entered by user)
                - "health" (int): Starting health, set to 10 
                - "inventory" (list): Starts as an empty list
        Example:
            >>> setup_player()
            Enter your name: Ailene
            {'name': 'Ailene', 'health': 10, 'inventory': []}
        """
        
    player_name = input('Please enter your name:') #Ask the user for their name using input()
        
    start_dict = {
            'name': player_name, 
            'health': 10, 
            'inventory': []
        } #Initialize a dictionary with keys: "name", "health", and "inventory"

    return start_dict #Return the dictionary
       
        # Done. TODO: Ask the user for their name using input()
        # Done. TODO: Initialize a dictionary with keys: "name", "health", and "inventory"
        # Done. TODO: Return the dictionary


    def create_treasures():
         """
        Creates a dictionary of treasures, where each treasure has a value.

        Returns:
            dict: Example:
                {
                    "gold coin": 5,
                    "ruby": 10,
                    "ancient scroll": 7,
                    "emerald": 9,
                    "silver ring": 4
                }
        Tip:
            You can customize treasures or randomize the values using random.randint(3, 12).
        """
    treasures = {
                    "gold coin": 15, 
                    "silver coin": 10, 
                    "ruby": 5, 
                    "ancient scroll": 20, 
                    "emerald": 9, 
                    "silver ring": 4
            } #Create a dictionary of treasure names and integer values
        
    return treasures #Return the dictionary

        # Done. TODO: Create a dictionary of treasure names and integer values
        # Done. TODO: Return the dictionary


    def display_options(room_number):
        """
        Displays available options for the player in the current room.

        Args:
            room_number (int): The current room number.

        Output Example:
            You are in room 3.
            What would you like to do?
            1. Search for treasure
            2. Move to next room
            3. Check health and inventory
            4. Quit the game
        """
     
        print(f"""
            You are in room {room_number}. 
            What would you like to do? 
            1. Search for treasure 
            2. Move to next room 
            3. Check health and inventory 
            4. Quit the game'
            """) 
        # TODO: Print the room number and the 4 menu options listed above


    def search_room():
        """
        Simulates searching the current room.

        If the outcome is 'treasure', the player gains an item from treasures.
        If the outcome is 'trap', the player loses 2 health points.

        Args:
            player (dict): The player's current stats.
            treasures (dict): Dictionary of available treasures.

        Behavior:
            - Randomly choose outcome = "treasure" or "trap"
            - If treasure: choose a random treasure, add to player's inventory,
              and print what was found.
            - If trap: subtract 2 from player's health and print a warning.
        """
        result = random.choice(['treasure', 'trap'])

        if result == 'treasure':
            treasure_x = random.choice(list(treasures.keys()))
            player['inventory'].append(treasure_x)
            print(f'You found a {treasure_x}! It is worth {treasures[treasure_x]} points!')

        else: 
            player['health'] -= 2 #start_dict.update('health' -= 2)  
            print(f"It's a trap! Your health is now {player['health']}") 
        # TODO: Randomly assign outcome = random.choice(["treasure", "trap"])
        # TODO: Write an if/else to handle treasure vs trap outcomes
        # TODO: Update player dictionary accordingly
        # TODO: Print messages describing what happened


    def check_status(player):
        """
        Displays the player’s current health and inventory.

        Args:
            player (dict): Player stats including health and inventory.

        Example Output:
            Health: 8
            Inventory: ruby, gold coin
        or:
            Health: 10
            Inventory: You have no items yet.
        """
        print(f'Health: {start_dict['health']}')

        if player['inventory']:
            print(f'Inventory: {', '.join(player['inventory'])}')
        
        else:
            print('You have no items yet.')
        # TODO: Print player health
        # TODO: If the inventory list is not empty, print items joined by commas
        # TODO: Otherwise print “You have no items yet.”


    def end_game(player, treasures):
        """
        Ends the game and displays a summary.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary for item value lookup.

        Output:
            Prints player’s final health, inventory contents, and total score value.
        """
        final_score = sum(treasures[item] for item in player['inventory'])
        treasure_count = len('inventory')

        print(f'Your final health is {player['health']}.')
        print(f'Treasures collected: {', '.join(set(player['inventory']))}')
        print(f'You collected {treasure_count} items worth {final_score} points!')

        print(f'Thanks for playing, {player[name]}!')


        # TODO: Calculate total score by summing the value of collected treasures
        # TODO: Print final health, items, and total value
        # TODO: End with a message like "Game Over! Thanks for playing."


    def run_game_loop(player, treasures):
        """
        Main game loop that manages the rooms and player decisions.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary.

        Flow:
            - There are 5 rooms (use for loop range(1, 6))
            - Inside each room, use a while loop for player actions:
                1. Search room
                2. Move to next room
                3. Check status
                4. Quit
            - Health below 1 ends the game early.
        """
        for room_number in range(1, 6):
            while True:
                display_options(room_number)
                player_choice = int(input("What do you want to do? \n Choose \n 1. Search room \n 2. Move to next room \n 3. Check status \n  Quit"))
                if player_choice == 1:
                    search_room(player, treasures)
                    if player['health'] < 1:
                        print('You are dead. Game over!')
                    end_game(player, treasures)
                    return
                elif player_choice == 2:
                    if room_number <= 4:
                        print(f'Moving to room {room+1}...')
                    else:
                        print('There are no more rooms to explore!')
                    break
                elif player_choice == 3:
                    check_status(player)
                elif player_choice == 4:
                    print('Quit')
                end_game(player, treasures)
                return
                
            else: 
                print('Please choose a number between 1-4.')

        end_game(player, treasures)
        # TODO: Loop through 5 rooms (1–5)
        # TODO: Inside each room, prompt player choice using input()
        # TODO: Use if/elif to handle each choice (1–4)
        # TODO: Break or return appropriately when player quits or dies
        # TODO: Call end_game() after all rooms are explored


    # -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()
    run_game_loop(player, treasures)

if __name__ == "__main__":
    main()
