import multiprocessing
import os

def Factr(no):
    print("process is running : " , os.getpid())
    fact = 1
    for i in range(1, no):
            fact = fact * i
    print("Process ID :", os.getpid())
    print("Number     :", no)
    print("Factorial  :", fact)
    print("-----------------------")

    return fact

def main():

    lst = [10 ,20, 30 ,50 ,7 , 8 , 27]

    ret =[]

    p1 = multiprocessing.Pool()
    ret = p1.map(Factr , lst)
    p1.close()
    p1.join()

    print(ret)

if __name__ == "__main__":
    main()


