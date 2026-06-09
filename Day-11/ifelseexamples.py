'''data = {
    'rishi': {'status':True, 'python' :98, 'mysql': 90, 'flask' : 95},
    'suresh': {'status':True, 'python' :78, 'mysql': 85, 'flask' : 80},
    'ramesh': {'status':False, 'python' :None, 'mysql': None, 'flask' : None},
    'ravi': {'status':True, 'python' :62, 'mysql': 55, 'flask' : 65},
    'rajesh': {'status':True, 'python' :33, 'mysql': 25, 'flask' : 34},
}

name = input("Enter the name: ")

if name in data:
    if data[name]['status']:
        total = data[name]['python'] + data[name]['mysql'] + data[name]['flask']
        avg = total / 3
        if avg >= 90:
            print(f"congratulations {name}, you got first class!!!")
        elif avg >= 70:
            print(f"Good {name}, keep it up for next time !!")
        elif avg >= 35:
            print(f"{name}, you passed, but you need to work hard!")
        else:
            print(f"{name}, you are failed in the exam.")
    else:
        print(f"{name}, did,t write the exam.")
else:
    print("Name not found in the data.")

budget = int(input("Enter your budget: "))

if budget > 50000:
    print("You can go for the trip")
elif budget > 30000:
    print("You can go for pub)")
elif budget > 10000:
    print("You can go for shopping")
elif budget > 5000:
    print("You can go for a cafe")
elif budget > 2000:
    print("You can go for a movie")
elif budget > 500:
    print("You can recharge your mobile")

else:
    print("Take Rest") '''

hrs,mins = list(map(int, input("Enter the time (hours minutes): ").split()))  

if hrs >= 23 and 0 <= mins <= 59:
    print("Good Night")