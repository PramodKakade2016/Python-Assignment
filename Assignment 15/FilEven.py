
CheckEven = lambda no : no % 2 == 0

def main ():

    lst = []
    no = int(input("Enter th number : "))

    for i in range(no):
        lst.append(int(input(f"Enter the element in list : ")))
    print (lst)    



    ret = list(filter(CheckEven , lst))

    print(f"EVen of {lst} is {ret}")

if __name__ == "__main__":
    main()