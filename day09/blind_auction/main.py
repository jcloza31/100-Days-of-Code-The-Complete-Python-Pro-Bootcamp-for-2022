from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
intro = "Welcome to the secret auction program."
print(intro)

bid_is_open = True
bidder = {}
while bid_is_open:
    name = input("What is your name?: ")
    bid = int(input("What's your bid? $"))
    bidder[name] = bid
    other_bidder = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    clear()
    if other_bidder == "no":
        bid_is_open = False
        winner = ""
        winning_bid = 0
        for bid in bidder:
            bidder_name = bid
            if bidder[bid] > winning_bid:
                winner = bidder_name
                winning_bid = bidder[bid]
        print(f"The winner is {winner} with a bid of ${winning_bid}.")
    elif other_bidder == "yes":
        continue
    else:
        print("You have entered an invalid response. We will ask you to input another bidder. ")

# print(bidder)
        
