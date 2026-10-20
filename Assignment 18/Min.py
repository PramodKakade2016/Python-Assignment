def min(no):

    min = no[0]

    for i in range(len(no)):
        if min > no[i]:
            min= no[i]
    return min

def main():

    lst = []

    element = int(input("Enter the number of elements in list : "))

    for i in range(element):
        lst.append(int(input("Enter the elements : ")))

    print(lst)

    ret = min(lst)
    print("Minimum is : " , ret)



if __name__ =="__main__":
    main()


