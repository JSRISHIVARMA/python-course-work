'''n = 10
def display():
    n = 10
    print ("Inside:",n)

display()
print("Outside:" ,n)

#global
def display():
    global n
    n = 10
    print ("Inside:",n)

display()
print("Outside:" ,n)

#w
def display(n):
    #global n
    n += 10
    print ("Inside:",n)

n = 10
display(n)
print("Outside:" ,n)

#using globle
def display():
    global n
    n += 10
    print ("Inside:",n)

n = 10
display()
print("Outside:" ,n)

#nonlocal
def display():
    n = 10
    def inner():
        nonlocal n
        n+=10
        print("Inner function:" ,n)

    print("Outer function:", n)

#functions -> veriable
s='python'
print(len(s))

len=5
print(len(s))

#int float complex str list tuple set dict bool
#int float complex str list tuple bool
#list set dict

def update(n):
    n = False
    print("Inside:",n)

n=True
update(n)
print("Outside:",n)

def update(n):
    n +=6
    print("Inside:",n)

n=2+4j
update(n)
print("Outside:",n)


def update(n):
    n = [1,2,3,4,5]
    print("Inside:",n)

n=[1,2,3,4,5]
update(n)
print("Outside:",n)


def update(n):
    n = {1,2,3,4,5}
    print("Inside:",n)

n={1,2,3,4,5}
update(n)
print("Outside:",n)

#set
def update(n):
    n.add(5)
    print("Inside:",n)

n={1,2,3,4,5}
update(n)
print("Outside:",n)
#Recursive function

def func():
    if basecondi:
        return
    func()


def func(num):
    if num == 0:
        return
    #print(num,end=' ')
    func(num-1)
    print(num,end=' ')

func(5)

#sum of digits 
def sumofdigits(n):
    if n==0:
        return 0
    return n+sumofdigits(n-1)

print(sumofdigits(5))

#factorial
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
n=int(input())
print(fact(5))

#power of A and B
def power(base,pow):
    if pow==0:
        return 1
    return base * power(base,pow-1)

print(power(2,4))
print(power(3,3))
'''
#reverse of the string
def reverseofstr(s,ind):
    if ind == 0:
        return s[0]
    return s[ind] +reverseofstr(s,ind-1)

l="Python Programming"
print(reverseofstr(l,len(l)-1))
