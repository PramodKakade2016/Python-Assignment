def Palindrom(no):

    rev = ""
    for i in no:
       rev = i + rev
    if no == rev:
        print("Palindrom")   
    else:
        print("Not Palindrom")    

    print(rev)
    return main()

def main():

    no = input("Enter No  : ")
    Palindrom(no)

if __name__ =="__main__":
    main()        


'''
 while No > 0:
        digit = No % 10
        rev = rev * 10 + digit
        No = No // 10
'''