from functools import reduce

#Minmum = lambda no1 , no2 : no1 if no1 < no2 else no2 # min(no1 ,no2)

def main ():

    lst = []
    no = int(input("Enter th number : "))

    for i in range(no):
        lst.append(int(input(f"Enter the element in list : ")))
    print (lst)    



    ret = reduce(lambda no1 , no2 : no1 if no1 < no2 else no2 , lst)

    print(f"Minmum of {lst} is {ret}")

if __name__ == "__main__":
    main()