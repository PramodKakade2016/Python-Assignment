CheckEven  = lambda No : (No % 2 != 0)
        
    
def main ():
    No = int(input("Enter number :"))

    ret = CheckEven(No)    # ret =(value % 2 == 0)

    #print (ret)

    if ret == True:
       print (f"Its Odd Number {ret}")
    else :
       print (f"Its odd Number {ret}")


if __name__ == "__main__":
    main()