'''
class Hotstar:
    def __init__(self,name):
        self.name = name
        print(f'Hi {name} ,welcome to the Hotstar')
    def login(self):
        print("You can login")
    def dashboard(self):
        print("You can see the dashboard items")
    def search(self):
        print("You can search")
    def languages(self):
        print("You select thr languages")
    def playcontrollers(self):
        print("You can pause and paly the video")
    def ads(self):
        print("Ads will run")
    def movies(self):
        print("You can limited access for movies")
    def sports(self):
        print("Limited time you can watch sports")
    def quality(self):
        print("limited quality")

rishi = Hotstar('rishi')
rishi.login()
rishi.dashboard()
rishi.search()
rishi.languages()
rishi.playcontrollers()
rishi.ads()
rishi.movies()
rishi.sports()
rishi.quality()

#premiumHotstar
class PremiumHotstar(Hotstar):
    def __init__(self,name):
        self.name = name
        print(f'Hi {name} ,welcome to the PremiumHotstar')
    def ads(self):
        print("Ads won't run")
    def movies(self):
        print("You can unlimited access for movies")
    def sports(self):
        print("you can watch sports")
    def quality(self):
        print("High quality")

rishi = PremiumHotstar('rishi')
rishi.ads()
rishi.movies()
rishi.sports()
rishi.quality()
'''
#operator overload
class Number:
    def __init__(self,n):
        self.n = n
    def __add__(self, other):
        return self.n + other.n
    def __sub__(self, other):
        return self.n - other.n
    def __mul__(self, other):
        return self.n * other.n
    def __truediv__(self, other):
        return self.n / other.n
    def __eq__(self, other):
        return self.n == other.n
    def __lt__(self, other):
        return self.n < other.n
    def __gt__(self, other):
        return self.n > other.n
    def __str__(self):
        return str (self.n)
    
n1 = Number(10)
n2 = Number(20)

print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)

print(n1==n2)
print(n1<n2)
print(n1>n2)
print(n1,n2)
    
    