import random


class Comunicator:
    privateKey = -1
    buff = -1
    textBuff = ""

    def __init__(self):
        self.choosePrivateKey()

    def choosePrivateKey(self):
        self.privateKey = random.randint(0, 9)

    def shakeSymKey(self, others):
        if self.privateKey == -1:
            return -1
        tempSeed = -1
        tempSeed = random.randint(0, 9)
        others.buff = self.privateKey ^ tempSeed
        reciv = others.processShake() ^ tempSeed
        others.processSecondShake(reciv)
        print("client key:" + str(self.privateKey))

    def processShake(self):
        if self.buff == -1:
            return -1
        if self.privateKey == -1:
            return -1
        return self.buff ^ self.privateKey

    def processSecondShake(self, halfKey):
        if self.buff == -1:
            return -1
        if self.privateKey == -1:
            return -1
        self.privateKey = self.privateKey ^ halfKey
        print("serverKey:" + str(self.privateKey))

    def sendencText(self, msg: str, others):
        if self.privateKey == -1:
            return -1
        buff = ""
        for i in msg:
            buff = buff + chr(ord(i) ^ self.privateKey)
        others.textBuff = buff
        print("enc: " + buff)

    def decText(self):
        if self.privateKey == -1:
            return -1
        buff = ""
        for i in self.textBuff:
            buff = buff + chr(ord(i) ^ self.privateKey)
        self.textBuff = buff
        print("dec: " + self.textBuff)


a = Comunicator()
b = Comunicator()
a.shakeSymKey(b)
print(a.privateKey)
print(b.privateKey)
a.sendencText("abcd", b)
b.decText()
