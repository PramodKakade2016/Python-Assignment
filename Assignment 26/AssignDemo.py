class Demo ():

    Value = 0

    def __init__(self ,A ,B):
        self.No1 = A
        self.No2 = B
    def fun(self):
        print(self.No1)
        print(self.No2)

    def gun(self):
        print(self.No1)
        print(self.No2)

Dobj1 = Demo(11 ,21)
Dobj2 = Demo(51 ,101)

Dobj1.fun()
Dobj2.fun()
Dobj1.gun()
Dobj2.gun()
    
    
