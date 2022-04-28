import sys, time
from attr import NOTHING

def numberFormat(num):
    return("{:,}".format(num))

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

int_error_message = ("please enter a vaild input! [Note: this should be lowercase only] \n")

def onions():
    coins = ("")
    try:
        amount = int(input('How many crates? ')) 
    except:
        print_slow(int_error_message)
        onions()

    large_crates = input(str('Large crates? [y/n] '))
    tuna_roll = input(str('Tuna roll? [y/n] '))
    print("")
    print(tuna_roll)
    print(large_crates)
    print("")

    if large_crates == ('y'):
        value = 10125
    else:
        if large_crates == ('n'): value = 3600
        else:
            print(int_error_message)
            onions()

    if tuna_roll == ('y'):
        coins = (value*amount)
        coins = coins + (7 / 100) * coins
    else:
        if tuna_roll == ('n'): print("")
        else:
            print(int_error_message)
            onions()


    print_slow(numberFormat(coins))