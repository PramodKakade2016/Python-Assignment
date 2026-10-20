def Factorial(no):

    fact = 1

    for i in range(1 ,no+1):
        fact = fact * i
    return fact

def main():

    No = int(input("Enter Number : "))

    ret = Factorial(No)
    print ("Factorial is : " , ret)

if __name__ =="__main__":
    main()