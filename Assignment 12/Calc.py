

def calc(no , no1):
        add  =  no + no1
        sub =  no - no1 
        mul= no *no1
        div  =no /no1

        return add ,sub ,mul , div
    

def main():
    no = int(input("enter no : "))
    no1 = int(input("enter no : "))
    ret = calc(no , no1)
    print (ret)

if __name__ == "__main__":
    main()

