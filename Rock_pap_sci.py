from random import randint

def rock_paper_scissors():
    
    n = input("Rock, Paper or Scissors\n")
    m = randint(0,2)
    comps_list = ["Rock", "Paper", "Scissors"]
    comps_choice = comps_list[m]
    found = False
    if n in comps_list:
        
        while not found:
            if comps_choice == n:
                print("Oops! It's a TIE. Let's try again\n")
                n = input("Rock, Paper or Scissors\n")
                comps_choice = comps_list[randint(0,2)]
                while n not in comps_list:
                    print("Please enter a valid value\n")
                    n = input("Rock, Paper or Scissors\n")
            else:
                if comps_choice == "Rock":
                    if n == "Scissors":
                        print("You lost!:(\nYou are killed by my Rock\n")
                    else:
                        print("You Won!:)\nYou killed my Rock\n")
                elif comps_choice == "Scissors":
                    if n == "Paper":
                        print("You lost!:(\nYou are cut by my Scissors\n")
                    else:
                        print("You Won!:)\nYou killed my Scissors\n")
                elif comps_choice == "Paper":
                    if n == "Rock":
                        print("You lost!:(\nYou are killed by my Paper\n")
                    else:
                        print("You Won!:)\nYou cut my Paper\n")
                found = True
            
        print("Wanna play again?\n")
        k = 1
        while k:
            dec = input("Enter YES or NO\n")
            if dec == "YES":
                rock_paper_scissors()
            elif dec == "NO":
                print("Have a good day!!\n")
                k = 0
            else:
                print("Can't proceed!\n")
        return 0

    else:
        print("Please enter a valid value\n")
        rock_paper_scissors()

rock_paper_scissors()
