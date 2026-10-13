def ReverseNo(no):

    rev = ""
    for i in no:
       rev = i + rev

    print(int(rev))

def main():

    no = input("Enter No  : ")
    ReverseNo(no)

if __name__ =="__main__":
    main()        


'''
 while No > 0:
        digit = No % 10
        rev = rev * 10 + digit
        No = No // 10
'''