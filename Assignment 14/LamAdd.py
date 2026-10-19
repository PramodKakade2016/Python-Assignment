Add  = lambda No1 ,No2 : No1+No2
        
    
def main ():
    No1 = int(input("Enter number :"))
    No2 = int(input("Enter number :"))

    ret = Add(No1 , No2)    # ret =(value % 2 == 0)

    print (f" addition  is {ret}")

if __name__ == "__main__":
    main()