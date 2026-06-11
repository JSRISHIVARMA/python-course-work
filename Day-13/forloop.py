''''pin = 2242
for i in range (5) :
    e_pin = int(input("Enter the pin:"))
    if e_pin == pin:
        print("unlock the phone")
        break
    else:
        print("Incorrect pin")
else:
    print("Try again ,after 60 seconds")

l = [2,3,5,6,8,10,34,12]
search = int(input("Enter the element: "))

for i in range(len(l)):
    if l[i] == search: 
       print(f'{search} is found at index-{i}')
    break
else:
    print(f'{search} is not found')


password = input ("Enter the password: ")
if len (password) >=8:
    s=set ()
    for i in password:
        if i.isupper ():
            s.add('u')
        elif i.islower():
            s.add('l')
        elif i.isdigit():
            s.add('d')
        else:
            s.add('s')

    if len(s) == 4:
        print ("Strong Password")
    else:
        print("Week Password")

else:
    print("Week Password")

#ASSETS --->Dbugging
status = None
assert status != None, "You need to update the status"
print (status)

name = 'abc'
batch= 55
age = 21
assert (name!=None and batch!=None and age!=None), "You need to update the data"
print (name,batch,age) 

#while loops
i = 1
while i<11:
    print(i)
    i+=1

i=2
while i<21:
    print (i)
    i+=2

i=10
while i>0:
    print(i)
    i-=1

i=5
while i<51:
    print(i)
    i+=5

l = [1,2,4,5,6,7,3,9]
i=0
while i<len(l[i])
i+=1

l = 'python programming'
i=0
while i<len(l[l]):
    print(l[i])
    i+=1

l= (1,2,3,45,5,6,3)
i=0
while i<len(l):
    print(l[i])
    i+=

#remove errors
l= [1,0,0,2,3,4,0,0,0,2,0,0,1,0,3,50,2,0,64,23,0,0,0,0,12,3,34]

while 0 in l:
    l.remove(0)

print (l) 


#candycrush moves
moves = 30
while moves>1:
    status = input("[w] in or [c] ontinue: ") .upper()
    if status == 'w':
       print ("You won the game")
       break

    moves-=1
    print(f'{moves} moves are left')

else:
    print("Game Over")
'''