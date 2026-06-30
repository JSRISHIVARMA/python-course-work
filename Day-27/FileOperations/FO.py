'''
file = open('Sample.txt','r')

print(file.read())
file.seek(0)
print(file.readline())
file.seek(0)
print(file.readlines())

file.close()
#try 
try:
    file = open('Sample.txt','r')
except FileNotFoundError:
    print("File is not there")
else:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    file.close()

#
with open('Sample.txt','r') as file:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    file.close()


with open('Sample.txt','a') as file:
    file.write('\nrishi\nvarma\nsatya')

with open('Samples.txt','a') as file:
    file.write('\nrishi\nvarma\nsatya')

with open('Sample.txt','w') as file:
    file.write('\nrishi\nvarma\nsatya')

#Read and write with r+
with open('demo.txt','w+') as file:
    file.write('varma\nrishi\nsatya')
    file.seek(0)
    print(file.read())

import os

#os.mkdir('Sample')
os.rmdir('Sample')

import re

pattern = '[abc]'
text = 'codegnan'

res = re.match(pattern,text)

print(res.group() if res else "No Match Found")

#search
import re

pattern = '[a-z]'
text = 'Python verson 3.11'

res = re.search(pattern,text)

print(res.group() if res else "No Match Found")

#finally 
import re

pattern = '[0-9]'
text = 'Python verson 3.11'

res = re.findall(pattern,text)

print(res)

#print(res.group() if res else "No Match Found")


#using finditer
import re

pattern = '[0-9]'
text = 'Python verson 3.11'

res = re.finditer(pattern,text)
for i in res:
    print(i.group(),i.start())

#print(res)
#print(res.group() if res else "No Match Found")

import re

pattern = '[a-z] {9}'
text = 'abcdefghi'

res = re.fullmatch(pattern,text)
#for i in res:
 #   print(i.group(),i.start())

#print(res)
#print(res.group() if res else "No Match Found")
print(res.group() if res else "No Match Found")
'''
import re

pattern = r'[0-9]{2}'
text = 'python: 34 mysql : 78 java : 55 html: 45'

res = re.sub(pattern, '**',text)

print(res)