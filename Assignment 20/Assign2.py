import threading
import os

def FactEven(no):
    
    Total = 0 
    print("TId of ChKEven : " , threading.get_ident())

    for i in range(1, no+1):
       if no % i == 0:
         if i % 2 == 0:
           Total = Total + i
    print(Total)     


def FactOdd(no):
    
    Total = 0
    print("TId of ChKOdd : " , threading.get_ident())
       
    for i in range(1, no+1):
       if no % i == 0:
         if i % 2 != 0:
           Total = Total + i
    print(Total) 

def main():
    
    No = int(input("Enter the number : "))
    print("TId of Main : " , threading.get_ident())

    t1 = threading.Thread(target=FactEven , args=(No ,))
    t2 = threading.Thread(target=FactOdd , args=(No ,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from Main")

if __name__ =="__main__":
    main()
  