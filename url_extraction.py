#Extracting url from a string or paragraph.
import re

text = input("Enter the text:\n")
pat = r"http(s)?(:)//([a-zA-Z]+(\.)[a-zA-Z]+((\.)[a-zA-Z]+)*)(/([a-zA-Z]+[0-9]*[!@#$%^&*+=<>,.?]*[a-zA-Z]*[0-9]*))*"
url = re.search(pat, text)
print("URL:", url.group())
