import re
'''p = r'h.t\b'
t = 'hot hit hoo haa hbb host hate hourse'
r = re.findall(p,t)
print(r)'''

'''p = r'^h'
t = 'hot hit hoo haa hbb host hate hourse'
r = re.findall(p,t)
print(r)'''

'''p = r't$'
t = 'hot hit hoo haa hbb host hate hourse'
r = re.findall(p,t)
print(r)'''

'''p = r'to*'
t = 'to too hoo toa  toooooo'
r = re.findall(p,t)
print(r)'''

'''p = r'[a-z]{3,4}'
t = 'to too hoo toa  toooooo'
r = re.findall(p,t)
print(r)

p = r'(vamsi)'
t = 'tanuri vamsi'
r = re.findall(p,t)
print(r)


#valid Email or not
p = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

t = input("Enter the Text :")
r = re.fullmatch(p,t)
print("Valid format" if r else "Invalid format")

#valid Mobile number or not
p = r'^[6-9]\d{9}$'
t = input("Enter the Mobile Number :")
r = re.fullmatch(p,t)
print("Valid format" if r else "Invalid format")
'''
#valid password or not
p = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
t = input("Enter the Password :")  
r = re.fullmatch(p,t)
print("Valid format" if r else "Invalid format")