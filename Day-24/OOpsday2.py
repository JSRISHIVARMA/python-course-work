'''#property day-2
class Instagram:
    def __init__(self):
        self. __ = []

    @property
    def accessport(self):
        return self. __post
    
    @accessport.setter
    def accesspost(self,newpost):
        self. __post.append(newpost)

rishi = Instagram()

print(rishi.accessport)
rishi.accessport = 'class and object'
print(rishi.accessport)

#
class whatsapp1:
    def message(self):
        print("You can send message to people")

class whatsapp2(whatsapp1):
    def calls(self):
        print("You can do video/audio calls")

rishi = whatsapp1()
print("v1 - rishi")
rishi.message()

varma = whatsapp2()
print("v2 - varma")
varma.message
varma.calls()

#multipul 
class whatsapp1:
    def message(self):
        print("You can send message to people")

class whatsapp2:
    def calls(self):
        print("You can do video/audio calls")

class whatsapp3:
    def media(self):
        print("You can share photos/video")

class whatsapp4(whatsapp1,whatsapp2,whatsapp3):
    def status(self):
        print("You can share status-[22 hours]")


varma = whatsapp4()
print("v4 - varma")
varma.message()
varma.calls()
varma.media()
varma.status()

#multilevel

class whatsapp1:
    def message(self):
        print("You can send message to people")

class whatsapp2(whatsapp1):
    def calls(self):
        print("You can do video/audio calls")

class whatsapp3(whatsapp2):
    def media(self):
        print("You can share photos/video")

class whatsapp4(whatsapp3):
    def status(self):
        print("You can share status-[22 hours]")


varma = whatsapp4()
print("v4 - varma")
varma.message()
varma.calls()
varma.media()
varma.status()

#hi

class whatsapp1:
    def message(self):
        print("You can send message to people")

class whatsapp2(whatsapp1):
    def emojis(self):
        print("You can send messages with emojis to people")

class whatsapp3(whatsapp2):
    def stickers(self):
        print("You can send messages with stickers to people")

varma = whatsapp3()
print("v3 - varma")
varma.message()
varma.emojis()
varma.stickers()

#in
class whatsapp1:
    def message(self):
        print("You can send message to people")

class whatsapp2(whatsapp1):
    def emojis(self):
        print("You can send messages with emojis to people")

class whatsapp3(whatsapp1):
    def stickers(self):
        print("You can send messages with stickers to people")

class whatsapp4(whatsapp2,whatsapp3):
    def gif(self):
        print("You can send messages with gif to people")


varma = whatsapp4()
print("v4 - varma")
varma.message()
varma.emojis()
varma.stickers()
varma.gif()

#
class wpv1:
    def status(self):
        print("You can upload images/videos")

class wpv2(wpv1):
    def status(self):
        super().status()
        print("You can react and reply")

class wpv3(wpv2):
    def status(self):
        super().status()
        print("You can like and reshare")

varma = wpv3()
varma.status()


class wpv1:
    def status(self):
        print("You can upload images/videos")

class wpv2(wpv1):
    def status(self):
        super().status()
        print("You can react and reply")

class wpv3(wpv2):
    def status(self):
        super().status()
        print("You can like and reshare")

varma = wpv3()
varma.status()
'''