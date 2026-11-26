# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `uv run python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# Function for ... (displaying the board?)
def print_grid(grid: list):
    print_grid_line(grid,0, 1, 2)
    print("___|___|___")
    print_grid_line(grid,3, 4, 5)
    print("___|___|___")
    print_grid_line(grid,6, 7, 8)

# Function for... (choosing a player?)
def print_grid_line(grid: list, a: int, b: int, c: int):
        print(f" {grid[a]} | {grid[b]} | {grid[c]} ")

def validate_input(inp, grid: list, symbols: dict):
    if inp in grid  and not inp in symbol.values() :
        return True
    else:
         print("Please enter a valid input.")
         return False

def check_for_win(fields, wc: set):
    for w in winning_combinations:
        if w <= set(fields):
            return True
    return False



active_player = "p1"

symbol = {"p1": "O",
          "p2": "X"}

game_continue = True
input_val = None
valid_input = False

winning_combinations = (set("123"), set("456"), set("789"), 
                        set("147"), set("258"), set("369"), 
                        set("159"), set("357"))

# Tic-tac-toe game
if __name__ == "__main__":
    # Start a new round of Tic-tac-toe
    while game_continue:

        fields_chosen = {"p1": "",
                         "p2": ""}
        grid = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        game_going = True
        
        print("Welcome to a new round of Tic-Tac-Toe!")
        while game_going:
            print(f"It's {active_player}'s turn")
            print_grid(grid)

            while not valid_input:
                input_val = input("Enter field you want to choose: ")
                valid_input = validate_input(input_val, grid, symbol)
            grid[int(input_val) - 1] = symbol[active_player]
            fields_chosen[active_player] += input_val

            if check_for_win(fields_chosen[active_player], winning_combinations):
                print(f"\n~~~~~~~\n{active_player} won!\n~~~~~~~\n")
                print_grid(grid)
                game_continue = True if input("\nAnother Game? Enter 'Y' to continue.") == "Y" else False
                game_going = False
            elif len(fields_chosen["p1"] + fields_chosen["p2"]) == 9:
                print(f"\nThat's a draw!\n")
                print_grid(grid)
                game_continue = True if input("\nAnother Game? Enter 'Y' to continue.") == "Y" else False
                game_going = False
            
            valid_input = False
            active_player = "p2" if active_player == "p1" else "p1"
            print("\n")
