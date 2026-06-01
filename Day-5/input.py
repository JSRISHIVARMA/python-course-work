#split input formatting
'''V  = input("Enter names :").split()
print(V)
t = tuple(input("Enter tuple elements: ").split())
print(t)
s = set(input("Enter set elements : ").split())
print(s)
string = str(input("Enter string values : ").split(","))
print(string)
l = input().split(" ",2)
print(l)'''

#map Function (datatype,updateing)

# taking inputs int to list,tuple and set
'''l = list(map(int,input("Enter int values to list : ").split()))
print(l)

t = tuple(map(int,input("Enter int values to tuple : ").split()))

s = set(map(int,input("Enter int values to set : ").split()))

print(l)
print(t)
print(s)'''

#taking inputs Float to list,tuple,set

'''l = list(map(float,input("Enter float values to list : ").split()))

t = tuple(map(float,input("Enter float values to tuple : ").split()))

s = set(map(float,input("Enter float values to set : ").split()))

print(l)
print(t)
print(s)
'''
# assigning two or more values to variables bhy using  split methode

'''username,password = list(map(input("Enter float values to list : ").split()))
print(username)
print(password)

price,rating = tuple(map(float,input("Enter float values to tuple : ").split()))
print(username)
print(rating)
'''
# Eval method --> we can assign direst datatype with values
'''a = eval(input("enter eval list of a : "))
print(a,type(a))
b = eval(input("enter eval tuple of b : "))
print(b)
c = eval(input("enter eval set of c : "))
print(c)'''


#STRING
#1.Concatination(+)
'''a = "Tanuri"
b = "Vamsi"
print(a+b)''' #--> Concatinating a and b

#2.Repetation(*)
'''a = "Tanuri"
b = "Vamsi"
print(a*10)''' #--> Repeating 10 times

#3.Indexing (accessing each charact)
'''a = "Tanuri"
b = "Vamsi"
print(a[2])''' #--> accessing perticular characters in a string

#3.Slicing (accessing set of characters)
a = "Tanuri"
print(a[::-1]) #--> reversing a string