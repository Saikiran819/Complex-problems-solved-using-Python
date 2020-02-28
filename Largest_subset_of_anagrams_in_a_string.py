from collections import Counter

def maxAnagramSize(string):
    string = string.split(" ")
    
    for i in range(len(string)):
        string[i] = ''.join(sorted(string[i]))
        
    freqDict = Counter(string)
    print(freqDict)
    print(max(freqDict.values()))

maxAnagramSize(input("Enter a string:\n"))