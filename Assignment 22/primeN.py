import multiprocessing
import os

def Prime(no):
    print("process is running : " , os.getpid())
    Count = 0
    for i in range(no):
         if i < 2:
             continue
         prime = True 
         for j in range(2, i):
             if i % j == 0:
                 prime = False
         if prime:         
            Count = Count + 1
    return Count

def main():

    lst = [10000 , 20000 ,30000]

    ret =[]

    p1 = multiprocessing.Pool()
    ret = p1.map(Prime , lst)
    p1.close()
    p1.join()

    print(ret)

if __name__ == "__main__":
    main()


