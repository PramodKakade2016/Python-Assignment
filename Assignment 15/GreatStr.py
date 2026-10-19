
GreatStr = lambda Name : len(Name) > 5 

def main ():

    lst = []
    no = int(input("Enter th number : "))

    for i in range(no):
        lst.append(input(f"Enter the element in list : "))
    print (lst)    



    ret = list(filter(GreatStr , lst))

    print(f"Element Greater than length are of {lst} is {ret}")

if __name__ == "__main__":
    main()