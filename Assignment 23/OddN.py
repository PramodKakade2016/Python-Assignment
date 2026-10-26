import multiprocessing
import os 

def Odd(no):

    Total = 0

    for i in range(no):
        if i % 2 != 0:
            Total = Total + i
    print("Process Id is :" , os.getpid())
    print("Number is  :" ,no)
    print("Total of Odd number is  :" , Total)
    return Total

def main():

    Data = [1000000 ,2000000, 3000000, 4000000]
    result = []

    Pobj = multiprocessing.Pool()
    result = Pobj.map(Odd , Data)

    Pobj.close()
    Pobj.join()

    print("Resullt is ", result)

if __name__ =="__main__":
    main()