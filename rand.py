import random

# main function that executes codes for toss
def main():

    fee = 0.001450354
    bankroll = 1000
    heads = 0
    tails = 0
    longest_head_streak = 0
    longest_tail_streak = 0
    current_streak = 0
    last_flip = None
    counter = 0
    
    while bankroll > 0:

        bet = round(random.uniform(0.05, 100), 1)
        print(f"Your random bet amount is: {bet:.2f} TON")

        flip = random.randint(0, 1)  # 0 for heads, 1 for tails

        if flip == 0 : # -
            bankroll -= bet * 0.95 - fee
            print(f"- Bankroll {bankroll:.2f}.")
            heads += 1
            if last_flip == 0:
                current_streak += 1
            else:
                current_streak = 1
            longest_head_streak = max(longest_head_streak, current_streak)
            last_flip = 0
        else: # +
            bankroll += bet - fee
            print(f"+ Bankroll {bankroll:.2f}.")
            tails += 1
            if last_flip == 1 :
                current_streak += 1
            else:
                current_streak = 1
            longest_tail_streak = max(longest_tail_streak, current_streak)
            last_flip = 1
        counter += 1
        print("Counter:", counter)
        if bankroll <= 0:
            print("Your bankroll is depleted! Game over.")
            break
    
    print("\nGame Over!")
    print("-:", heads)
    print("+:", tails)
    print("Longest - streak:", longest_head_streak)
    print("Longest + streak:", longest_tail_streak)

# calling the function
main()
