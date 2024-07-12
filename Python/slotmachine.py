import random


# Global constant
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100
ROWS = 3
COL = 3

#creating a dictionary of all the different symbols in the slot machine
symbol_count = {
  "A": 2,
  "B": 4,
  "C": 6,
  "D": 8
}

#function to get the slot machine spin 
def get_slot_machine_spin(rows, cols, symbols):
  #creating a list for all of our symbols
  all_symbols=[]
  #.items() gives you both the key and a value from the dictionary
  for symbol, symbol_count in symbol.items():
    #now add the symbols to the symbols list
    for _ in range(symbol_count):
      all_symbols.append(symbol)

  #storing the columns not the rows
  columns= []
  for col in range (cols):
    column=[]
    #to copy a list, you need a colon in the brackets, will not work without [] because it will just store the object, : is the splice symbol
    current_symbols = all_symbols[:]
    for row in range (rows):
      value = random.choice(all_symbols)

#Deposit function called when entering the deposit size
def deposit():
  while True:
    amount = input("Enter your deposit size: ")
    if amount.isdigit():
      amount = int(amount)
      if amount>0:
        print(f"Your deposit is {amount}")
        break
      else:
        print("Amount must be greater than 0.")
    else:
      print("Please enter a number")
  return amount

# line function
def get_number_0f_lines():
  while True:
    #Have to convert num to str as python cannot do string int conversion
    lines = input("Enter the number of lines to bet on (1-"+str(MAX_LINES) + ")?: ")
    if lines.isdigit():
      lines = int(lines)
      if lines>0 and lines<=MAX_LINES:
        print(f"Your lines are {lines}")
        break
      else:
        print("Please enter a number between 1 and "+str(MAX_LINES)+"")

    else:
      print("Please enter a number ")
  return lines

def get_bet():
  while True:
    #Have to convert num to str as python cannot do string int conversion
    betAmount = input("Enter the amount you want to bet for each line?")
    if betAmount.isdigit():
      betAmount = int(betAmount)
      if betAmount>MIN_BET and betAmount<=MAX_BET:
        print(f"Your bet amount is {betAmount}")
        break
      else:
        print("Please enter a number between "+str(MIN_BET)+" and "+str(MAX_BET)+"")

    else:
      print("Please enter a number ")
  return betAmount

# main called whenever they want to play again
def main():
  balance = deposit()
  lineNumber = get_number_0f_lines()
  while True:
    bet= get_bet()
    total_bet = bet*lineNumber

    if (total_bet> balance):
      print(f"Not enough money to bet on. Your cuurent balance is {balance}.Either change lines or ammount")
    else:
      break


  print(f"You are betting {bet} on {lineNumber} lines. Your total bet is {total_bet}")
main()