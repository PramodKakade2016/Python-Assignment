import multiprocessing
import os

def square(no):
    print("process is running : " , os.getpid())
    summ = 0
    for i in range(1, no):
         summ = summ + (i ** 2)
    return summ

def main():

    lst = [10000000 , 2000000 ,30000000]

    ret =[]

    p1 = multiprocessing.Pool()
    ret = p1.map(square , lst)
    p1.close()
    p1.join()

    print(ret)

if __name__ == "__main__":
    main()


