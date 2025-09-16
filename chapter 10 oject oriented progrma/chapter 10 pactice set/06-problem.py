from random import randint

class train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo
    def book(self, fro, to):
        print(f" Ticket is booked in train no: {self.trainNo} From {fro} to {to}")

    def getStaus(self):
        print(f"Train is runing SuccesFuly and Train No:-{self.trainNo}")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} From {fro} to {to} is {randint(22,55)}")


t = train(1234567)
t.book("Howrah","Amta")
t.getStaus()
t.getFare("Howrah", "Amta")