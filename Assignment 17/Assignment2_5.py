def CheckPrime(no):
    
    if no <= 1 :
       return False 

    for i in range(2 ,no):
       if no % i == 0:
         return False
    return True

def main():

    No = int(input("Enter Number : "))

    ret = CheckPrime(No)

    if ret == True:
        print (f"The {No} is Prime Number")

    else:
       print (f"The {No} is Composite Number")

if __name__ =="__main__":
    main()