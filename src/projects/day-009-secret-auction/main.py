player_bids = {}
max_bid: int = 0
max_bidder: str = ""
while True:
    name: str = input("What is your name? ")
    bid: int = int(input("What is your bid? $"))
    player_bids[name] = bid
    if bid > max_bid:
        max_bid = bid
        max_bidder = name

    keep_going: str = input("Are there any other bidders? (yes/no): ")
    if keep_going == "no":
        print(f"The winner is {max_bidder} with a bid of {max_bid}.")
        break
    print("\033[H\033[J", end="")  # Clear the console
