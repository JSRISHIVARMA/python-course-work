'''s = 'python'
for i in s:
    for j in s:
        print(i,j)

s = 'python'

for i in range(len(s)):
    for j in range(i+1,len(s)):
        print(s[i],s[j],sep='',end=' ')

#sum
l = [[1,2,3],[4,5,6],[7,8,9],[10,12,13],[30,40,50]]
sum = 0
for i in l:
    for j in i:
        sum +=j

print(f'sum = {sum}')


d = {
    '1234' : {'pin':'4567','balance':2300},
    '2345' : {'pin':'9876','balance':5300},
    '1345' : {'pin':'5678','balance':6300},
    '4567' : {'pin':'9876','balance':7300}
    
}

for i in d:
    print('Account number:',i)
    print('pin number:',d[i] ['pin'])


#patterns
for row in range(5):
    for col in range(5):
        print(col,end=' ')
    print()

n= int(input("Enter the size: "))
for row in range(n):
    for col in range(n) :
        print('*',end =' ')
    print()


n = int(input())
for row in range(n):
    for col in range(n):
        print(col%2,end=' ')
    print()

n = int(input())
for row in range(n):
    for col in range(row+1):
        print('*',end='')
    print()

n = int(input())
for i in range(n):
    for j in range(n-i):
        print('*',end='')
    print()

n = int(input())
for i in range(n):
    for sp in range(n-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()

n = int(input())
for i in range(n):
    for sp in range(i):
        print(' ',end=' ')
    for j in range(n-i):
        print('*',end=' ')
    print()

n = int(input())
for i in range(n):
    for j in range(n):
        print((i+j)%2,end=' ')
    print()

n = int(input("Enter the size: "))
c = 1
for i in range(n):
    for j in range(i+1):
        print(str(c).zfill(2),end=' ')
        c+=1
    print()

n = int(input("Enter the size: "))
c = 1
for i in range(n):
    for j in range(i+1):
        print(str(c).zfill(3),end=' ')
        c+=1
    print()
'''