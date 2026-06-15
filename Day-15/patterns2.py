'''n= int(input("Enter the size: "))
m= n//2
for i in range(n):
    if i<=m:
     for j in range(i+1) :
        print('*',end =' ')
    else:
       for j in range(n-i):
          print('*',end=' ')
    print()

n= int(input("Enter the size: "))
m= n//2
for i in range(n):
    if i<=m:
        print('* '*(i+1),end =' ')
    else:
       print('* '*(n-i),end=' ')
    print()

n= int(input("Enter the size: "))
m= n//2

for i in range(n):
    if i<=m:
        print('  '*(m-i),end=' ')
        print('* '*(i+1),end =' ')
    else:
       print('  '*(i-m),end=' ')
       print('* '*(n-i),end=' ')
    print()

n= int(input("Enter the size: "))
m= n//2

for i in range(n):
    if i<=m:
        #print(' '*(m-i),end=' ')
        print(' '*(m-i),'* '*(i+1),end =' ')
    else:
       #print(' '*(i-m),end=' ')
       print(' '*(i-m),'* '*(n-i),end=' ')
    print()

n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i == n//2 or j == n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or j == i or i+j == n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n = int(input("Enter the size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==n-1 or i == m :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n = int(input("Enter the size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i == m or j==0 or j==n-1 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


n = int(input("Enter the size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


n = int(input("Enter the size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n = int(input("Enter the size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i == m or j==0 or j==n-1 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n = int(input("Enter the size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i == m or j==0 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#pattern G
'''
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or (i==n-1 and j<=n//2) or (j==n//2 and i>=n//2) or (i==n//2 and j>n//2) or (j==n-1 and i>n//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

#pattern H
'''
for i in range(n):
    for j in range(n):
        if j==0 or j==(n-1) or i==n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

#pattern I
'''
for i in range(n):
    for j in range(n):
        if i==0 or j==n//2 or i==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


#pattern J

for i in range(n):
    for j in range(n):
        if i==0 or j==n//2 or (i==(n-1) and j<n//2) or (j==0 and i>n//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

n = int(input("Enter a number to print J: "))

for row in range(n):
    for col in range(n):

        if row == 0:                      # Top horizontal line
            print("*", end=" ")

        elif col == n//2 and row < n-1:   # Vertical line
            print("*", end=" ")

        elif row == n-1 and col <= n//2:  # Bottom horizontal line
            print("*", end=" ")

        elif col == 0 and row >= n//2:    # Left side curve
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()
#print K Pattern

n = int(input("Enter a number to print J : "))
m = n//2
for row in range(n):
    for col in range(n):
        if col == 0 or (row == m and row <=0) :
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

#print L Pattern

n = int(input("Enter a number to print L : "))
m = n//2
for row in range(n):
    for col in range(n):
        if col == 0 or row == n-1 :
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

#print M Pattern

n = int(input("Enter a number to print N : "))
m = n//2
#c_m = (row+col==4)//2
for row in range(n):
    for col in range(n):
        c_m = (row+col==4)//2
        if col == 0 or col == n-1 or row<c_m or row == col :
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

#print O Pattern

n = int(input("Enter a number to print O : "))
m = n//2
#c_m = (row+col==4)//2
for row in range(n):
    for col in range(n):
        c_m = (row+col==4)//2
        if col == 0 or col == n-1 or row==0 or row == n-1 :
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()
#print P Pattern

n = int(input("Enter a number to print P : "))
m = n//2
#c_m = (row+col==4)//2
for row in range(n):
    for col in range(n):
        c_m = (row+col==4)//2
        if col == 0 or (col == n-1 and row<=m) or row==0 or row == m  :
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()
#print q Pattern

n = int(input("Enter a number to print q : "))
m = n//2
#c_m = (row+col==4)//2
for row in range(n):
    for col in range(n):
        c_m = (row+col==4)//2
        if col == n-1 or (col == 0 and row<=m) or row==0 or row == m  :
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()
#print R Pattern

n = int(input("Enter a number to print r : "))
m = n//2
#c_m = (row+col==4)//2
for row in range(n):
    for col in range(n):
        c_m = (row+col==4)//2
        if col == n-1 or col == 0 or row==0 or row == m:
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()
#print T Pattern

n = int(input("Enter a number to print T : "))
m = n//2
#c_m = (row+col==4)//2
for row in range(n):
    for col in range(n):
        c_m = (row+col==4)//2
        if col == m or row==0:
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

#print S Pattern

n = int(input("Enter a number to print S : "))
m = n//2
#c_m = (row+col==4)//2
for row in range(n):
    for col in range(n):
        c_m = (row+col==4)//2
        if row == 0 or row==n-1 or row == m or (col==0 and row <= m) or (col==n-1 and row >= m):
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

#print U Pattern

n = int(input("Enter a number to print U : "))
m = n//2
#c_m = (row+col==4)//2
for row in range(n):
    for col in range(n):
        c_m = (row+col==4)//2
        if row == n-1 or col==0 or col==n-1 :
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

#print X Pattern

n = int(input("Enter a number to print X : "))
m = n//2
#c_m = (row+col==4)//2
for row in range(n):
    for col in range(n):
        c_m = (row+col==4)//2
        if row+col == 4 or row == col :
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

#print Z Pattern

n = int(input("Enter a number to print X : "))
m = n//2
#c_m = (row+col==4)//2
for row in range(n):
    for col in range(n):
        c_m = (row+col==4)//2
        if row == 0 or row == n-1 or row+col == 4 :
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()
'''




