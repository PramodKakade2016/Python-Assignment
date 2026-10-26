import multiprocessing
import os 

def Factorial(no):

    Fact = 1
    for i in range(1 ,no):   
            Fact = Fact *i

    print("Process Id : " , os.getpid())
    print("Input Number : " ,no)
    print("Factorial is  : " ,Fact)

def main():

    Data = [10 , 20, 30, 40,15,21,18,63,69,14,9]

    pobj = multiprocessing.Pool()
    pobj.map(Factorial , Data)
    pobj.close()
    pobj.join()

    print("-------------Exit main-------------")
if __name__ =="__main__":
    main()