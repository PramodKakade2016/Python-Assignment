import threading
import os

def Order(no):
    
    print("TID of Order" , threading.get_ident())

    for i in range(1,no+1):
        print(i)

    print("Order End")     


def Reverse(no):
    
    print("TID of Reverse" , threading.get_ident())
       
    for i in range(no , 0, -1):
        print(i)
    print("Reverse End") 


def main():
    
    print("TID of Main" , threading.get_ident())

    no =int((input("Enter the String : ")))

    t1 = threading.Thread(target=Order , args=(no ,))
    t1.start()
    t1.join()
    t2 = threading.Thread(target=Reverse , args=(no ,))
    t2.start()
    t2.join()
    

    print("Exit from Main")

if __name__ =="__main__":
    main()