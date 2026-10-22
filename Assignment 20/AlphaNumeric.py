import threading
import os

def Small(no):
    
    Total = 0
    print("TID of Small" , threading.get_ident())

    for i in no:
        if i.islower():
          Total = Total + 1
    print(Total)     


def Capital(no):
    
    print("TID of Capital" , threading.get_ident())
    
    Total = 0
       
    for i in no:
        if i.isupper() :
           Total = Total + 1
    print(Total) 

def Number(no):

    print("TID of Number" , threading.get_ident())
    
    Total = 0
       
    for i in no:
        if i.isnumeric() :  #i.isdigit():  Also works
           Total = Total + 1
    print(Total) 

def main():
    
    print("TID of Main" , threading.get_ident())

    no =(input("Enter the String : "))

    t1 = threading.Thread(target=Small , args=(no ,))
    t2 = threading.Thread(target=Capital , args=(no ,))
    t3 = threading.Thread(target=Number , args=(no ,))
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Exit from Main")

if __name__ =="__main__":
    main()