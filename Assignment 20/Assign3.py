import threading
import os

def FactEven(no):

    Total = 0
    for i in no:
        if i % 2 == 0:
         Total = Total + i
    print(Total)     


def FactOdd(no):
    
    Total = 0
       
    for i in no:
        if i % 2 != 0:
           Total = Total + i
    print(Total) 

def main():
    
    lst = []
    No = int(input("enter the number of elements : "))

    for i in range(No):
        lst.append(int(input("Elements in List : ")))

    print(f"Orignal List : {lst}")

    t1 = threading.Thread(target=FactEven , args=(lst ,))
    t2 = threading.Thread(target=FactOdd , args=(lst ,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from Main")

if __name__ =="__main__":
    main()