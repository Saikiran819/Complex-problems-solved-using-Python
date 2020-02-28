
class Node:
    def __init__(self, val):
        self.ch = val
        self.next = None

def compare(str1, str2):
    retval = 0
    
    if not str2 and not str1:
        print("Empty strings are passed\n")
    
    while (str1 and str2) and str1.ch == str2.ch:
        str1 = str1.next
        str2 = str2.next
    if (str1 and str2) and str1.ch > str2.ch:
        retval = 1
    elif(str1 and str2) and str1.ch < str2.ch:
        retval = 2
    
    if str1 and not str2:
        retval = 1
    if str2 and not str1:
        retval = 2
        
    return retval


str1 = Node('m')
str1.next = Node('a')
str1.next.next = Node('n')
str1.next.next.next = Node('h')
str1.next.next.next.next = Node('o')
str1.next.next.next.next.next = Node('l')
str1.next.next.next.next.next.next = Node('s')


str2 = Node('m')
str2.next = Node('a')
str2.next.next = Node('n')
str2.next.next.next = Node('h')
str2.next.next.next.next = Node('o')
str2.next.next.next.next.next = Node('l')
str2.next.next.next.next.next.next = Node('e')

ret = compare(str1, str2)
string1 = ""
string2 = ""

while str1:
    string1 += str1.ch
    str1 = str1.next
    
while str2:
    string2 += str2.ch
    str2 = str2.next

if ret == 0:
    print("Both strings are equal\n")
elif ret == 1:
    print("{0} is greater".format(string1))
else:
    print("{0} is greater".format(string2))