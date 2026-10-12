def ChkGreater (no1 , no2):

    if no1 >no2 :
        return no1
    else :
        return no2 

def main():
    no1 = 10
    no2 = 20
    ret = ChkGreater(no1 ,no2)

    print("The Greater no is : " , ret)

if __name__ =="__main__":
    main()