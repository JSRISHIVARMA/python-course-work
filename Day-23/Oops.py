'''class Flipkart:
    pass

rishi = Flipkart()
varma = Flipkart()
vijay = Flipkart()

#
class Flipkart:
    discount = 10
    products = ['laptop','phone','mouse','charger']

    @classmethod
    def showProducts (cls):
        print (cls.products)

    def login(self,username,password):
        self.username = username
        self.password = password
        print(f'welcome to the flipkart {self.username}')

    @staticmethod
    def banner():
        print("10% discount is going on flipkart, shop now!")


rishi = Flipkart()
rishi.login('rishi','rishi@123')
rishi.banner()
rishi.showProducts()

Flipkart.showProducts()
Flipkart.banner()

class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.followers = []
        print(f'Welcome to the Instagram, {self.username}')

rishi = Instagram('rishi','rishi@123')
'''
class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self.followers = []

    def getpassword(self):
        return self. __password
    
    def setpassword(self,newpassword):
        self. __password = newpassword
        
rishi = Instagram('rishi','rishi@123')

print("Before username:",rishi.username)
rishi.username = 'varma'
print("After username:",rishi.username)

print("Before username:",rishi.getpassword())
rishi.setpassword('varma@123')
print("After password:",rishi.getpassword())


