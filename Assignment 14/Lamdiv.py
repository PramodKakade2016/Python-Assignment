CheckEven  = lambda No : (No % 5 == 0)
        
    
def main ():
    No = int(input("Enter number :"))

    ret = CheckEven(No)    # ret =(value % 2 == 0)

    print (ret)

    if ret == True:
       print (f" The {No} is Divisible by 5 {ret}")
    else :
       print (f" The {No} is Divisible by 5 {ret}")


if __name__ == "__main__":
    main()