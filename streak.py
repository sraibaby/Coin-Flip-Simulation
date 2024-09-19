import random
# main function that executes codes for toss
def main():
    # user input
    num = int(input("Enter the number of flips: "))
    
    bankroll = 9.6
    heads = 0
    tails = 0
    longest_head_streak = 0
    longest_tail_streak = 0
    current_streak = 0
    last_flip = None
    
    for i in range(num):

        bet = round(random.uniform(0.8, 1.2), 1)
        print(f"Your random bet amount is: {bet:.2f} TON")

        # flip of coin
        flip = random.randint(0, 1)
        
        if flip == 0:
            print("You got head")
            heads += 1
            if last_flip == "head":
                current_streak += 1
            else:
                current_streak = 1
            longest_head_streak = max(longest_head_streak, current_streak)
            last_flip = "head"
        else:
            print("You got tail")
            tails += 1
            if last_flip == "tail":
                current_streak += 1
            else:
                current_streak = 1
            longest_tail_streak = max(longest_tail_streak, current_streak)
            last_flip = "tail"
    
    print("HEADS:", heads)
    print("TAILS:", tails)
    print("Longest head streak:", longest_head_streak)
    print("Longest tail streak:", longest_tail_streak)

# calling the function
main()
