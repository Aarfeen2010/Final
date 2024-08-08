import os
import msvcrt

pin = []
balance = 100000

print("\n\n\n\n\n\n\n\n\n\n")
print("\t\t\t\tEnter 4 digits pin")

# FIrst charcter
character = msvcrt.getch()
pin.append(character)
print("\n\n\n\t\t\t\t\t*", end="", flush=True)

# Second charcter
character = msvcrt.getch()
pin.append(character)
print("*", end="", flush=True)

# Third charcter
character = msvcrt.getch()
pin.append(character)
print("*", end="", flush=True)

# Fourth charcter
character = msvcrt.getch()
pin.append(character)
print("*", end="", flush=True)

print("\n\n\n\n")


class ATM:
    def check_balance():
        print("Your current balance is: ", balance, "rupees only")


    def deposit():
        global balance
        damount = int(input("Enter your deposit amount: "))
        damount += balance
        print("Successfully deposited.")


    def withdraw():
        global balance
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance:
            amount -= balance
            print("Transaction successful")
        else:
            print("Transaction unsuccessful")

        
    def main():

        print("Insert your card")
        confirm_pin = []

        print("\n\n\n\n\n")
        print("\t\t\t\tConfirm 4 digits pin")

        # FIrst charcter
        character = msvcrt.getch()
        confirm_pin.append(character)
        print("\n\n\n\t\t\t\t\t*", end="", flush=True)

        # Second charcter
        character = msvcrt.getch()
        confirm_pin.append(character)
        print("*", end="", flush=True)

        # Third charcter
        character = msvcrt.getch()
        confirm_pin.append(character)
        print("*", end="", flush=True)

        # Fourth charcter
        character = msvcrt.getch()
        confirm_pin.append(character)
        print("*", end="", flush=True)

        print("\n\n\n\n")

        if pin == confirm_pin:
            print("Enter 1 for balance inquiry")
            print("Enter 2 for Money withdrawal")
            print("Enter 3 for Money deposit")
            print("\n\n")

            option = int(input("Select an option(1/2/3): "))
            print("\n\n")

            if option == 1:
                ATM.check_balance()
            elif option == 2:
                ATM.withdraw()
            elif option == 3:
                ATM.deposit()
            else:
                print("Invalid option")
            
        else:
            print("Invalid pin. ")
            
        print("\n\n")

        
        print("Thank You, Visit Again")

atm = ATM()



if __name__ == "__main__":
    ATM.main() 

