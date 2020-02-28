

string = input("Enter a word:\n")

string = list(string.split(" "))

for var in string:
    sort = ''
    sort = ''.join(sorted(var))
    
    if sort == var:
        print('\''+var+'\'' + " is a ordered string\n")
    else:
        print('\''+var+'\'' + " is an unordered string\n")