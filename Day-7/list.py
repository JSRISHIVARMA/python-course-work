#stripping and trimming
'''s = "    Rishi     Varma    "
print("Removing of spaces in string elements : ",s.strip())
print("Removing of right spaces in string elements : ",s.rstrip())
print("Removing of left spaces in string elements : ",s.lstrip())'''

#string testing methods(Boolean results)
'''s = "    Rishi     Varma    "
print(s)
print("Checking starts with  : ",s.startswith("  "))
print("Checking ends with  : ",s.endswith("  "))
print("Checking alphabet or not : ",s.isalpha())
print("Checking all nums or not  : ",s.isalnum())
print("Checking title or not  : ",s.istitle())
print("Checking upper or not  : ",s.isupper())
print("Checking lower or not  : ",s.islower())
print("Checking space or not  : ",s.isspace())
print("Checking Identifier or not  : ",s.isidentifier())'''


#LIST (collection of elementsa and it is a immutable)
'''l  = [10,20,30,40,50]
a = [10,20,30,40,50]
print(l)
print("concatination of list : ",l+a)
print("Repetation of list : ",l*3)
print("3rd indexed value of list : ",l[3])
print("Slicing of first three elements of list : ",l[0:3])
print("Slicing of last three elements of list : ",l[2:5])
print("reverse of list : ",l[::-1])
print("reversed last 4 elements  of list : ",l[-1:-5:-1])'''

#modifing list
'''l  = [10,20,30,40,50]
A = [10,20,30,40,50]
a = l.append(60)
i = l.insert(6,70)
e = l.extend([80,90,100])
p = l.pop(9)
#d = del l[8]
c = l.clear()

print(l)
#print("adding 15 in 2nd index list : ",l[2]=15)
print("adding 15 in 2nd index list : ",l)
print("insert 70 in  list : ",l)
print("popping 100 from list : ",l)
#print("Deleting 90 from list : ",l)
print("Clearing the entire list : ",l)'''


#sorting and reversing a list
l  = [10,10,20,30,40,50]
n = l.copy()
'''print("sorted list : ",sorted(l))
print("reverse list : ",sorted(l,reverse = True))
print("index of 50 in list : ",l.index(50))
print("count of list : ",l.count(10))
'''
print("adding 200 to copied list ",n.append(200))
print("Copied list ",n)
print("original List = ",l)
print("size of  List = ",len(l))
print("sum of  List = ",sum(l))
print("maximum List = ",max(l))
print("minimum List = ",min(l))
print("any of true list = ",any(l))
print("all are true List = ",all(l))