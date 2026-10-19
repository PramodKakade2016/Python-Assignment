from functools import reduce

Maximum = lambda no1 , no2 : no1 if no1 > no2 else no2 # max(no1 ,no2)

def main ():

    lst = []
    no = int(input("Enter th number : "))

    for i in range(no):
        lst.append(int(input(f"Enter the element in list : ")))
    print (lst)    



    ret = reduce(Maximum , lst)

    print(f"Maximum of {lst} is {ret}")

if __name__ == "__main__":
    main()