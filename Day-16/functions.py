'''
#functionf
def function_name (arg):
    #stmts
    return
    function_name (para)
#names
def wish(name):
    print (f'welcome to the python course {name} !')

wish('J')
wish('satya')
wish('rishi')
wish('varma')
#even
def iseven (num):
    if num%2==0:
        return f"{num}- Even Number"
    else:
        return f"{num}-Odd Number"
    
print(iseven(12))
print(iseven(12))

#factorial
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact

num = int(input("Enter the number: "))
print("Factorial:",factorial(num))

#prime numbers
def isprime(num) :
    for i in range(2,num//2):
        if num%i==0:
            return f"{num} - Not prime Number"
    return f"{num} - print Number"

num = int(input("Enter the number: "))
print(isprime(num))

#Arguments
def display(name,email,pwd):
    print("Name: ",name)
    print("Email: ",email)
    print("Password:" ,pwd)

display('rishi','rishi@gmail.com','rishi@2242')
display('rishi','rishi@2242','rishi@gmail.com')
display('rishi@2242','rishi','rishi@gmail.com')

#key word
def display(name,email,pwd):
    print("Name: ",name)
    print("Email: ",email)
    print("Password:" ,pwd)

display(name='rishi',email='rishi@gmail.com',pwd='rishi@2242')
display(name='rishi',pwd='rishi@2242',email='rishi@gmail.com')
display(pwd='rishi@2242',name='rishi',email='rishi@gmail.com')

#defalt  
def display(name,email,pwd=''):
    print("Name: ",name)
    print("Email: ",email)
    print("Password:" ,pwd)

display('rishi','rishi@gmail.com','rishi@2242')
display('rishi','rishi@2242')

#varable(var)
def display(*names):
    print("Name: ",names)

    
display('rishi','ravi','satish','subhash')
display('rishi','subhash','satish')
display('rishi')
display('rishi','ravi')
'''
def display(**names):
    print("Name: ",names)

    
display(k1='rishi',k2='ravi',k3='satish',k4='subhash')
display(k1='rishi')
display(k1='rishi',k2='ravi')
