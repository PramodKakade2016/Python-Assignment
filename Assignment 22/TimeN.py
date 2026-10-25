import multiprocessing
import os
import time 

def Prime(no):
    print("process is running : " , os.getpid())
    Total = 0
    for i in range(no):
         Total = Total + i*5
    return Total

def main():

    lst = [1000000 , 2000000 ,30000000 ,4000000]

    ret =[]
    start_time = time.perf_counter()
    p1 = multiprocessing.Pool()
    ret = p1.map(Prime , lst)
    p1.close()
    p1.join()
    End_time = time.perf_counter()


    print(ret)
    print(f"Time Required : {End_time  - start_time:.4f}")

if __name__ == "__main__":
    main()


