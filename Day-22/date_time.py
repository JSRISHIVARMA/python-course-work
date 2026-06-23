'''
from datetime import date,time,datetime

t = date.today()

print(t)
print("Year:", t.year)
print("Month:", t.month)
print("Date:", t.day)
print("Weekday from 0:", t.weekday())
print("Weekday from 1:", t.isoweekday())

from datetime import *

t = date(2026,13,30)

print(t)

from datetime import date,time,datetime,time

n = datetime.now()

print(n)
print("Year:", n.year)
print("Month:", n.month)
print("Day:", n.day)
print("Hour:", n.hour)
print("Minute:", n.minute)
print("Second:",n.second)


from datetime import date,time,datetime,timedelta

n = datetime.now()

print(n)
print(n.strftime('%d/%m/%y'))
print(n.strftime('%d/%m %y %H:%M:%S'))
print(n.strftime('%d/%m/%y %I:%M:%S %p'))
print(n.strftime('%d %b %y %I:%M:%S %p'))
print(n.strftime('%d %B %y %I:%M:%S'))
print(n.strftime('%a, %d % B, %y %I:%M:%S %p'))
print(n.strftime('%A, %d % B, %y %I:%M:%S %p'))

#timedelta
from datetime import date,time,datetime,timedelta

n = datetime.now()

n15 = n + timedelta(minutes=15)
n2 = n + timedelta(hours=2)
n7 = n + timedelta(days=60)

print(n15,n2,n7,sep='\n')

#exception handling
try:
    #a= int(input("Enter the age: "))
    #print(12/0)
    #print(b)
    #print(13+'14')
    d= {1:1,2:2,3:3,4:4}
    #print(d[5])
    l= [1,2,3]
    #print(l[10])
except ValueError:
    print("Enter the age in a digit[0-9] format")
except ZeroDivisionError:
    print("can't divide with zero")
except NameError:
    print("define the var")
except TypeError:
    print("Add the same datatypes")
except KeyError:
    print("Index is out of range")
else:
    print("Age: {n}")
finally:
    print("Thankyou")

try:
    #a= int(input("Enter the age: "))
    #print(12/0)
    #print(b)
    #print(13+'14')
    d= {1:1,2:2,3:3,4:4}
    #print(d[5])
    l= [1,2,3]
    #print(l[10])
except (ValueError, ZeroDivisionError, NameError, TypeError, KeyError) as a:
    print("Error Occured: {n}")
else:
    print("No Error Occured")
finally:
    print("Thankyou")

#Exceptin handling easy
try:
    #a= int(input("Enter the age: "))
    #print(12/0)
    #print(b)
    #print(13+'14')
    d= {1:1,2:2,3:3,4:4}
    #print(d[5])
    l= [1,2,3]
    #print(l[10])
except Exception as a:
    print("Error Occured: {n}")
else:
    print("No Error Occured")
finally:
    print("Thankyou")
'''
try:
    amount = int(input("Enter amount to Withdraw: "))
    if amount < 0:
        raise Exception("Enter the amount greater than zero")
    
except Exception as e:
    print("Error Occured: e")
else:
    print("No Error Occured")
finally:
    print("Thankyou")