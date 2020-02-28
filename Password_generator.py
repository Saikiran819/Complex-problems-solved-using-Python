from random import randint

def pwd_gen():
    l = int(input("Enter the length of the password you want\n"))
    n_let = int(input("Enter the no.of letters you want\n"))
    dec = input("Enter YES or NO? for atleast one upper case chars\n")
    n_nums = int(input("Enter the no.of numbers you want\n")) 
    spl_dec = input("Enter YES or NO? for atleast one special characters\n")
    
    if (n_let + n_nums > l and spl_dec == "NO") or (n_let + n_nums + 1 > l and spl_dec == "YES"):
        print("Your choices exceed the length. Please enter valid values\n")
        pwd_gen()
    else:
        pwd = ['.']*l
        spl = ['!', '@', '#', '$', '%', '&', '*', '?']
        if dec == "NO":
            for i in range(n_let):
                n = chr(randint(97,122))
                j = randint(0, l-1)
                while pwd[j] != '.':
                    j = randint(0, l-1)
                pwd[j] = n
        else:
            k = int(n_let*0.6)
            for i in range(k):
                n = chr(randint(97,122))
                j = randint(0, l-1)
                while pwd[j] != '.':
                    j = randint(0, l-1)
                pwd[j] = n
            for i in range(n_let - k):
                n = chr(randint(65,90))
                j = randint(0, l-1)
                while pwd[j] != '.':
                    j = randint(0, l-1)
                pwd[j] = n
        for i in range(n_nums):
            n = randint(0,9)
            j = randint(0, l-1)
            while pwd[j] != '.':
                j = randint(0, l-1)
            pwd[j] = str(n)
        
        if spl_dec == "YES":
            for i in range(len(pwd)):
                if pwd[i] == '.':
                    s = randint(0, len(spl)-1)
                    pwd[i] = spl[s]
        return "".join(pwd)
    
pwd = pwd_gen()
print(pwd)