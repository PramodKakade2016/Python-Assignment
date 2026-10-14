def factor(no):
    print (f"Factor of the {no} are " , end = " ")
    for i in range(1, no+1):
        if no % i == 0:
            print (i , end = " ")
    

def main():
    no = int(input("enter no : "))
   # print (f"Factor of the {no} are ")
    factor(no)

if __name__ == "__main__":
    main()
