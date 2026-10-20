def max(no):

    max = no[0]

    for i in range(len(no)):
        if max < no[i]:
            max= no[i]
    return max

def main():

    lst = []

    element = int(input("Enter the number of elements in list : "))

    for i in range(element):
        lst.append(int(input("Enter the elements : ")))

    print(lst)

    ret = max(lst)
    print("Maximum is : " , ret)



if __name__ =="__main__":
    main()


