
CheckOdd = lambda no : no % 2 != 0

def main ():

    lst = []
    no = int(input("Enter th number : "))

    elements = input(f"Enter the element in list : ").split() # while entering elements give space

    for i in range(no):
        lst.append(int(elements[i]))
    print (lst)    



    ret = list(filter(CheckOdd , lst))

    print(f"Odd of {lst} is {ret}")

if __name__ == "__main__":
    main()