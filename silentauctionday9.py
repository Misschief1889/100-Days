from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.

print(art.logo)
print("Welcome to the secret auction program!")
item_bids = {}

additional_bidders = 0

def get_key(val):
    for key, value in item_bids.items():
         if val == value:
             return key

def auction_program():
  print("\nWhat is your name?")
  bidder_name = str(input())
  print("\nWhat's your bid?")
  total_bid = int(input())
  item_bids[bidder_name] = total_bid
  

auction_program()
print(item_bids)
print("\nAre there any other bidders?")
additional_bidders = input()

highest_bid = 0

while additional_bidders == "yes":
  clear()
  auction_program()
  print("\nAre there any other bidders?")
  additional_bidders = input()
else:
  for value in item_bids.values():
    if value > highest_bid: 
      highest_bid = value
  
winner_name = get_key(highest_bid)


print("The winner is " + str(winner_name) + " with a bid of " + str(highest_bid) + ".")
