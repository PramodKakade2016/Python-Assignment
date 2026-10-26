import multiprocessing
import os 

def Even(no):

    Total = 0

    for i in range(no):
        if i % 2 == 0:
            Total = Total + i
    print("Process Id is :" , os.getpid())
    print("Number is  :" ,no)
    print("Total of Even number is  :" , Total)
    #return Total

def main():

    Data = [1000000 ,2000000, 3000000, 4000000]
    result = []

    Pobj = multiprocessing.Pool()
    Pobj.map(Even , Data)
    Pobj.close()
    Pobj.join()

    #print("Resullt is ", result)

if __name__ =="__main__":
    main()