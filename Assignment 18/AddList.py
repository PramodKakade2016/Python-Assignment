def Add(no):

    total = 0

    for i in no :
        total = total + (i)

    return total

def main():

    lst = []

    element = int(input("Enter the number of elements in list : "))

    for i in range(element):
        lst.append(int(input("Enter the elements : ")))

    print(lst)
    '''
    total = 0
    
    for i in lst :
        total = total + (i)
    print("Add is ", total)
    '''

    ret = Add(lst)
    print("Addition is : " , ret)



if __name__ =="__main__":
    main()


