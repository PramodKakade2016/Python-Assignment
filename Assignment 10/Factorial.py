def factorial(no):
    
    fact =1

    for i in range(1,no+1):
        fact *=i
    return fact


def main():
    no = 5
    ret = factorial(no)
    print(ret)   
    
if __name__=="__main__":
    main()