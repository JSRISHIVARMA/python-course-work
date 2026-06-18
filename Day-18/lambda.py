'''syntax:

var = lambda: exp

add = lambda a,b: a+b

print(add(12,13))
print(add(22,33))

wish = lambda name: f'Welcome the python course {name}'

print(wish('rishi'))
print(wish('varma'))

gst = lambda price: price + price*0.18

print(gst(1000))
print(gst(600))
print(gst (89000))

greatest = lambda a,b: a if a>b else b

print(greatest(18,19))
print(greatest(2000,1900))
print(greatest(10,30))

iseven = lambda a: f"{a}-Even number" if a%2==0 else f"{a}-odd number"

print(iseven(4))
print(iseven(9))
print(iseven(15))

bill = lambda charge: charge if charge>99 else charge + 30
print(bill(150))
print(bill(45))
print(bill(15))

login = True
instock = True

status = lambda login,instock : ("You can buy product" if instock else "Product is out of stock") if login else "Login to buy a product"

print (status(login,instock))

l = [1,2,3,4,5,6,7]
res = list(map(lambda i:i**3,1))
print(res)

names = ['satya','rishi','varma']
t = list(map(lambda i:i.title(),names))
print(t)

l = [1,2,3,4,5,6,7,8,9,10,11,12]
res = list (filter(lambda i:i%2==0,1))
print(res)

l = [1,2,3,4,5,6,7]
res = list (filter(lambda i:i>5,1))
print(res)

l = [1,2,3,4,5,6,7]
res = list (filter(lambda i:i%3==0,1))
print(res)

from functools import reduce

l = [1,2,3,4,5,6,7,8,9,10,11,12]

s = reduce(lambda sum,i: sum+i,1)
p = reduce(lambda pro,i: pro*i,1)

print(s,p,m)
'''
from functools import reduce
l = [1,2,3,4,5,6,7,8,9,10,11,12]

s = reduce(lambda sum,i: sum+i,l)
p = reduce(lambda pro,i: pro*i,1)
m = reduce(lambda max,i: max if max>i else i,1)

d = {'subbu':50,'nagendra':40,'naresh':60,'dinesh':80,'sahith':70}

print(dict(sorted(d.items())))
print(dict(sorted(d.items(),key=lambda i:i[1])))

print(dict(sorted(d.items(),reverse= True)))
print(dict(sorted(d.items(),key=lambda i:i[1],reverse= True)))


























