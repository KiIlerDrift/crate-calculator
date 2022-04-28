from melon import melons
from pumpkin import pumkins
from raddish import raddishes
from onion import onions

options = ""

def menu():
    print("")
    print("█▀▄▀█ █▀▀ █▄░█ █░█ ▄")
    print("█░▀░█ ██▄ █░▀█ █▄█ ▄")
    print("")
    print(f"Please select a option from the list below:")
    print("")
    print(
    f"\n1. Melons"
    f"\n2. Pumpkins"
    f"\n3. Raddish"
    f"\n4. Onions"
    f"\n5. End"
    "\n ")
    globals() ['option'] = int(input("\nEnter your option 1-5 here: "))

menu()

while option != 0:
    if option == 1: melons() ; menu()
    elif option == 2: pumkins() ; menu()
    elif option == 3: raddishes() ; menu()
    elif option == 4: onions() ; menu()
    elif option == 5: exit()
