def ChkPrime(No):

    if No <=1 :
        print("Not a prime no")
        return 
    

    for i in range(2 , int(No ** 0.5) + 1):
        if No % i == 0:
             print("Not a prime no")
             return
    print("prime No")     

def main():

    No = int(input("Enter the number : "))
    ChkPrime(No)

if __name__=="__main__":
    main()