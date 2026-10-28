class Circle():

    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumferance = 0.0
        
    def Accept (self):

        self.Radius = float(input("Enter the Radius : "))
    
    def CalculateArea(self):

         self.Area= Circle.PI * self.Radius **2

    def CalculateCircumferance(self):

         self.Circumferance = 2 * Circle.PI * self.Radius

    def Display(self):

        print(f" Radius : {self.Radius} ")
        print(f" Area : {self.Area} ")
        print(f" Circumferance : { self.Circumferance} ")


class Arithmetic():


    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self):

        self.value1 = int(input("Enter the Number : "))
        self.value2 = int(input("Enter the Number : "))
    
    def Addition(self):
        return self.value1 + self.value2
    def substrcaction(self):
        return self.value1 - self.value2
    def Multiplaction(self):
        return self.value1 * self.value2
    def Division(self):

        try:
            return self.value1 / self.value2
        except ZeroDivisionError :
            return "Error : Divisoin by Zero is not Allowed."

    
    def Display(self):
        print(f"Addition : {self.Addition()}")
        print(f"substrcaction : {self.substrcaction()}")
        print(f"Multiplaction : {self.Multiplaction()}")
        print(f"Division : {self.Division()}")

def main():
    
    print("-"*40)   
    print("------Circle 1 -------")    
    c1 = Circle()
    c1.Accept()
    c1.CalculateArea()
    c1.CalculateCircumferance()
    c1.Display() 

    print("-"*40)
    print("------Circle 2 -------")   
    c2 = Circle() 
    c2.Accept()
    c2.CalculateCircumferance()
    c2.CalculateArea()
    c2.Display()

    print("="*50)
    print("----------------Arithematic 1-------------------------")
    A1 = Arithmetic()
    A1.Accept()
    A1.Display()

    print("="*50)
    print("----------------Arithematic 2-------------------------")
    A2 = Arithmetic()
    A2.Accept()
    A2.Display()

if __name__ =="__main__":
    main()