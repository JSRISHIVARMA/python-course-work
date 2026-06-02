#Methods of String
'''s = "Rishi varma"
print("Length of characters : ",len(s)) 
print("Sorting the string is :",sorted(s))
print("Maximum value of character is : ",max(s))
print("Minimum value of character is :",min(s))
print("Ascci Value of character 'a' is :",ord('a'))
print("Characters from numbers is : ",chr(2))'''

# case Methods
'''s = "Rishi varma"
print("uppe characters : ",s.upper())
print("lower is :",s.lower())
print("title character is : ",s.title())
print("casefold character is :",s.casefold())
print("swapcase character is :",s.swapcase())'''
#capitalizer also

#Alignments Methods
'''s = "Rishi varma"
print("center alignments characters : ",s.center(20,"*"))
print("ljust alignments characters : ",s.ljust(20,"*"))
print("rjust characters : ",s.rjust(20,"*"))
print("zfill characters : ",s.zfill(50))'''

#search and find methods
'''s = "Rishi varma"
print(s)
print("find the character of 'a' is  : ",s.find("a"))
print("rfind characters of 'V' : ",s.rfind("V"))
print("index characters of 'T' : ",s.index('T'))
print("rindex characters of 'a': ",s.rindex("a"))
print("counting characters of 'a': ",s.count("a"))'''

#Replace and modify
'''s = "Rishi varma"
print(s)
print("replace character of 'a' to 'A' is  : ",s.replace("a","A"))
print("translate characters of 'Tanuri' to 123456 : ",s.translate('Tanuri',123456))'''


#splitting and joining methods
'''s = "Rishi varma"
print(s)
print("splitting the characters with ',' is  : ",s.split(","))
print("splitting the characters with ',' in 2 is  : ",s.split(",",2))
print("Right splitting the characters with ',' in 2 is  : ",s.rsplit(",",2))
print("splittingline the characters with ',' in 2 is  : ",s.splitlines())
print("joining characters with '-' is  : ",'-'.join(s))
print("partitioning the characters into three parts is  : ",s.partition('#'))
print("Right partitioning the characters into three parts is  : ",s.rpartition('-'))'''

#Encoding and decoding Methods in strings
s = "Rishi varma 😀"
print(s)

print("encoding the characters  is  : ",s.encode())