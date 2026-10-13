def SumNatural(no):
    
    sum =0

    for i in range(1,no+1):
        sum +=i
    return sum


def main():
    no = 5
    ret = SumNatural(no)
    print(ret)   
    
if __name__=="__main__":
    main()