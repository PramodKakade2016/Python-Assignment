from functools import reduce

Add = lambda no1 , no2 : no1 + no2

def main ():

    lst = []
    no = int(input("Enter th number : "))

    for i in range(no):
        lst.append(int(input(f"Enter the element in list : ")))
    print (lst)    



    ret = reduce(Add , lst)

    print(f"Addition of {lst} is {ret}")

if __name__ == "__main__":
    main()