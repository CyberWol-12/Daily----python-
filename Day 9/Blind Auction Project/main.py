 # TODO-1: Ask the user for input



# TODO-2: Save data into dictionary {name: price}
def find_highest_bidder (bidding_dictionary):
    winner = ""
    highest_paid = 0
    max(bidding_dictionary)
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_paid:
            highest_paid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_paid}")




bids = {}
continue_bidding = True


while continue_bidding:
    name = input("what is your name?:\n")
    price = int(input("What is your bid?: \n$"))

    bids[name] = price
    should_continue = input("Are there is another bid? Type yes or no.\n").lower()

    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 5)

# TODO-4: Compare bids in dictionary



