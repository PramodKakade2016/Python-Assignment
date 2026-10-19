
Square = lambda no : no**2

def main ():

    lst = []
    no = int(input("Enter th number : "))

    for i in range(no):
        lst.append(int(input()))
    print (lst)    



    ret = list(map(Square , lst))

    print(f"Square of {lst} is {ret}")

if __name__ == "__main__":
    main()