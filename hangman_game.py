from random import randint
c = 0
f = open("sowpods_dict.txt", "r")
for line in f:
    c+=1
def hang_man():
    global c
    global f
    word = ""
    
    found = False
    while not found:
        p = 1
        x = randint(1, c)
        f.close
        f = open("sowpods_dict.txt", "r")
        for line in f:
            if x == p and len(line[:-1]) > 8:
                word = line[:-1]
                found = True
                break
            p+=1
    f.close
    temp = list(word)
    done = False
    i = 0
    while not done:
        n = randint(1, len(temp))
        if temp[n-1] != "_":
            temp[n-1] = "_"
            i += 1
        if i == len(temp)-2:
            done = True
    done = False
    count = 0
    while not done:
        if count == len(temp) // 2:
            print("\nOops! Out of moves. You lost!\n:(\n")
            print("=======THE WORD IS=======\n")
            print(word)
            done = True
        else:
            print("======= HERE IS THE WORD =======\n")
            print(" ".join(temp))
            print("\n======= START GUESSING =======\n")
            print("\nYou have "+ str(len(temp)//2 - count)+ " lives ...")
            print("\nDo you have any word in your mind??\n")
            ch_done = False
            while not ch_done:
                choice = input("Enter YES or NO\n")
                if choice == "YES":
                    guess = input("Enter the word\n")
                    if guess == word:
                        print("\nHurray!! You won the game!\n:)\n")
                    else:
                        print("\nAlas!.. You lost!\n:(\n")
                        print("=======THE WORD IS=======\n")
                        print(word)
                    done = True
                    ch_done = True
                elif choice == "NO":
                    while True:
                        nxt = int(input("Enter the position to reveal a letter:\n"))
                        if nxt > len(temp):
                            print("Enter a value <= length of the letter\n")
                        elif temp[nxt-1] != "_":
                            print("The letter is already revealed. Please enter other position\n")
                        else:
                            temp[nxt-1] = word[nxt-1]
                            count += 1
                            break
                    ch_done = True
                else:
                    print("Please enter either YES or NO\n")
    print("\nWanna play again?\n")
    k = 1
    while k:
        dec = input("Enter YES or NO\n")
        if dec == "YES":
            hang_man()
        elif dec == "NO":
            print("Have a good day!!\n")
            k = 0
        else:
            print("Can't proceed! Enter YES or NO\n")
    return 0

hang_man()