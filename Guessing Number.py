import random
account_balance = 100
print(account_balance)
Cab = ()
pay_for_each_game = 5
win = 0
lose = 0
while True:
    computer = random.randint(1,100)
    print("We already have a number , it's your turn" )
    level = int(input("Choose your level [1,2,3]: "))
    while level < 1 or level > 3:
        print("Have something wrong!! Please try again.")
        print("---------------------------------------")
        level = int(input("Choose your level [1,2,3]: "))
    times = 10 if level == 1 else 5 if level == 2 else 3
    is_win = False
    for time in range(times):
        your_number = int(input("Enter your number " + str(time + 1) + ": "))
        if your_number == computer:
            print("You win!!")
            is_win = True
            win += 1
            w = 5*3* win if level == 2 else 5*5*win if level ==3 else  5*win
            print(f"You won {win} times.")
            print(f"You will receive : {w}$")
            Cab = account_balance + w
            print(f"Your current balance is : {Cab}")
            break
        else:
            if your_number < computer:
                print("Too low")
            else:
                print("Too high")
        if is_win and time +1 >= times:
            print("You win!")
        if time +1 >= times:
            print("----------------------------")
            print("You lose!")
            lose += 1
            l =5*5*lose if level == 3 else 5*3*lose if level == 2 else 5*lose
            Cab = account_balance - l
            print(f"You lose {lose} times.")
            print(f"Oh no! You lost {l}$ and your current balance is :{Cab}$ ")


    print("----------------------------")


    cont = input("Continue? [y/n]: ")
    if cont == "n" or cont == "N" or Cab ==0 or Cab <=0:
        print(f"Your current account balance is : {Cab}$")
        break




