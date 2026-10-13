def EvenNo(no):
    
    lst =[]

    for i in range(no+1):
        if i % 2 ==0:
            lst.append(i)
        
    return lst


def main():
    no = 10
    ret = EvenNo(no)
    print(*ret)   
    
if __name__=="__main__":
    main()