#strings, list, tuple, set, dictionary
'''s= 'python programming'
for ch in s:
    print(ch)  

l =['suger','milk','bread']     
for item in l:
    print(item)  

t = ('1.intro','2.data types','3.operators')     
for item in t:
    print(item) 

s = {'laptop','mobile','tablet','charger'}
for item in s:
    print(item) 

d= {'name':'python','type':'programming language','version':3.10}
for key in d:
    print(key,d[key]) 

#range (start,stop+1,step) => (0,n,1)

for i in range(1,11):
    print(i)


for i in range(1,51,2):
    print(i)


for i in range(5,101,5):
    print(i)

for i in range(20,0,-1):
    print(i)    

for i in range(30,2,-3):
    print(i)

for i in range(6):
    print(i)

for i in range(1,50,2):
    print(i)

s= 'looping statements'
for i in range (len(s)):
    print(i,s[i])

l = [7,2,4,1,5,3,6]
for i in range(len(l)):
    print(i,l[i]) 

l = (7,2,4,1,5,3,6)
for i in range(len(l)):
    print(i,l[i])


s = 'looping'
for i in enumerate(s):
    print(i[0],i[1])

l = (7,2,4,1,5,3,6)
for i in enumerate(l):
    print(i[0],i[1])

l = [7,2,4,1,5,3,6]
for i in enumerate(l):
    print(i[0],i[1])

for i in range (10):
    pass

for i in range (10):
    if i == 5:
        break
    print(i)

for i in range (10):
    if i == 5:
        continue
    print(i)

l = [56,76,32,3,34,2,3,4,97,45,67,89,23,45,67,89]
for i in l:
    if i%2 == 0:
        print(i)

d = {'laptop':0,'mobile':1,'tablet':2,'charger':3}

for key in d:
    if d[key] :

        print(key,d[key])


t = (9,2,13,4,5,6)
for i in range(len(t)):
    print(i*t[i])

#upper case
name = { 'rishi' , 'suresh' , 'ramesh' , 'suresh' }
for i in name:                         
    print(i.upper())'''