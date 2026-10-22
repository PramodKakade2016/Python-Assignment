import threading
import os

def ChkEven():
    no = 2
    print("TId of ChKEven : " , threading.get_ident())

    for i in range(10):
        print(no)
        no += 2


def ChkOdd():
    
    no = 1
    print("TId of ChKOdd : " , threading.get_ident())
    for i in range(10):
        print(no)
        no +=2

def main():

    No = int(input("Enter the number : "))
    print("TId of Main : " , threading.get_ident())

    t1 = threading.Thread(target=ChkEven)
    t2 = threading.Thread(target=ChkOdd)
    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ =="__main__":
    main()
  