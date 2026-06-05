#Dictionary (It is a container to store the Key,Value pairs)
'''
1)It is a mutable datatype
2)It is a heterogenious
3)It is Odered datatype
4)Key need to immutable and uniqe
5)Values can be anything
6)In dict values consists of duplicates and keys must be uniqe or not duplicate
'''
#Properties and operations of dictionaries
'''d = {1:2,2:3,3:4,4:5,5:6,6:7}
print("Type of a dictionary is :",type(d))
print("dictionary is :",d)
a = d[1] = "Rishi"
print("Changing of first key as 'Rishi' dictionary is :",d)
print("Accessing 1st value in given dictionary is :",d[1])

print("Getting unavailable if key is not in dictionary Using '.get()' is :",d.get("varma","User not available"))

print("Getting available value if key is in dictionary Using '.get()' is :",d.get(2,"User not available"))

print("Getting available value if key is in dictionary Using '.get()' is :",d.get(2,"User not available"))
print( "checking 1 in dictionary is :",1 in d)'''

#methods of Dictionaries
'''d = {1:2,2:3,3:4,4:5,5:6,6:7}
print("Type of a dictionary is :",type(d))
print("dictionary is :",d)
print("Accessing keys in dictionary is :",d.keys())
print("Accessing values in dictionary is :",d.values())
print("sorted in dictionary is :",sorted(d))
print("min of dictionary is :",min(d))
print("max in dictionary is :",max(d))
print("size in dictionary is :",len(d))'''

#Modifications in dictionaries
'''d = {1:2,2:3,3:4,4:5,5:6,6:7}
u = d.update({"FName":"varma","LName":"Rishi"})
print("Updating multiple items in dictionary is :",d)
print("poping last item in dictionary is :",d.popitem())
#D = del d[1]
#print("Deleting 1st key items in dictionary is :",d)
c = d.clear()
print("Clearing items in dictionary is :",d)
print("Setting default of 'Rishi' is 0 in dictionary is :",d.setdefault("Rishi",0))'''


#Simple if -->Having only one conditions

'''v = "Rishi varma"
if "Rishi" in v:
    print("Found")

if v[0] == v:
    print("Yes")'''

#if else -->Having only two conditions
'''
details = ("Rishi","22424222")

a = input("Enter Username and password  here :").split()

if a == details:
    print("Login Successfull")
else:
    print("Invalid Creadantials")'''

#if-elif-else -->Having morethen three conditions
'''
num = int(input("Enter a number : "))
if num<0:
    print("Negitive")
elif num>0:
    print("Positive")
else:
    print("Zero")'''

#if-elif-else -->Having  conditions inside condition

products ={
    "apple":10,
    "mango":0,
    "banana":20,
    "goa":5,
    "sapota":100
    }
product = input("Enter the product here : ")

if product in products:
    if products[product] != 0:
        print(f"{product} is avalable")
    else:
        print(f"{product} is out of stock")
    
else:
    print(f"{product} is not avalable")