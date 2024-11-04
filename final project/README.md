# Slot Machine Game
#### Video Demo:  <URL HERE>
#### Description:

A simple Python-based slot machine game where players can deposit money, place bets, and spin to win rewards!

This project simulates a slot machine with adjustable symbols, payouts, and betting options.



Features:-
1. Flexible Betting System: Players can choose the number of lines to bet on and the amount for each line.
2. Symbol Payouts: Each symbol has a specific payout value based on its rarity.
3. Winning Lines Calculation: The game checks each spin to see if there's a winning line and rewards accordingly.
4. Interactive Console: User-friendly prompts guide players through deposits, betting, and spinning.
5. Balance Tracking: Keeps track of player balance, allowing them to continue spinning as long as they have funds.



Installation:-
1. Clone the Repository
git clone https://github.com/username/slot-machine-game.git

2. Navigate to the Project Directory
cd slot-machine-game

3. Run the Game Make sure you have Python 3 installed, then run:
python slot_machine.py



How to Play:-
1. Deposit Funds: Enter an amount to start with.
2. Choose Lines: Select the number of lines to bet on (1-3).
3. Place Bet: Specify the bet amount for each line.
4. Spin: See if you hit any winning combinations!
5. Continue or Quit: After each spin, you can choose to keep playing or quit.



Controls:-
1. Enter to spin
2. q to quit



Game Rules:-
1. Symbols:
Each symbol has a predefined payout and frequency in the slot machine.
A pays 5x, B pays 4x, C pays 3x, and D pays 2x your bet amount.

2. Betting:
The number of lines you can bet on ranges from 1 to 3.
Bets per line can range from $1 to $100.
The total bet equals (number of lines) * (bet per line).

3. Winning:
To win, the same symbol must appear in all columns for a line.
Winnings are calculated based on the symbol payout and bet amount.



Code Overview:-
1. Constants:
MAX_LINES, MAX_BET, MIN_BET, ROWS, COLS - parameters that define betting limits and slot machine size.

2. Symbols:
symbol_count and symbol_value - dictionaries that define the number and value of each symbol.

3. Functions:
check_winnings(columns, lines, bet, values): Calculates winnings and tracks winning lines.
get_slot_machine_spin(rows, cols, symbols): Generates a random set of symbols for each column.
print_slot_machine(columns): Displays the slot machine grid.
deposit(): Prompts user for a deposit amount.
get_number_of_lines(): Gets the number of lines the player wants to bet on.
get_bet(): Retrieves the bet amount per line.
spin(balance): Processes the betting and spinning logic, updating the player balance.
main(): Main function that manages the game flow.



Example Usage:-
Initial Deposit
What would you like to deposit?
> 100

Placing Bets
Enter the number of lines to bet on (1-3)?
> 2

What would you like to bet on each line?
> 10

You are betting $10 on each line. Total bet is equal to: $20
A | C | D
B | B | D
C | C | C

You won $30.

You won on lines: 3

Current balance is $110

Press enter to play (q to quit).q

You left with $110
