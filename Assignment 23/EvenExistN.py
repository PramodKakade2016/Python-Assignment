import multiprocessing
import os 

def Evencount(no):

    Count = 0
    for i in range(1 ,no):  # 0 % 2 == 0 is true so we exclude 0 and started from 1 
        if i % 2 == 0:
            Count = Count + 1
    print("Parent Process Id : " , os.getppid())
    print("Process Id : " , os.getpid())
    print("Input Number : " ,no)
    print("Even number count is : " ,Count)

def main():
    print("Parent Process Id of Main : " , os.getppid())
    print("Process Id of Main : " , os.getpid())

    Data = [1000000 , 2000000, 3000000, 4000000]

    pobj = multiprocessing.Pool()
    pobj.map(Evencount , Data)
    pobj.close()
    pobj.join()

    print("-------------Exit main-------------")
if __name__ =="__main__":
    main()