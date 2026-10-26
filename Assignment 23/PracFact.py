import multiprocessing
import os 

def Factorial(no):

    Fact = 1
    for i in range(1 ,no+1):   
            Fact = Fact *i
            if i == no:
                 print(i , end ="")
            else:
                 print(i, end = "*") 
    print(" = " ,Fact)    

    print("Process Id : " , os.getpid())
    print("Input Number : " ,no)
    print("Factorial is  : " ,Fact)

def main():

    Data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    pobj = multiprocessing.Pool()
    pobj.map(Factorial , Data)
    pobj.close()
    pobj.join()

    print("-------------Exit main-------------")
if __name__ =="__main__":
    main()