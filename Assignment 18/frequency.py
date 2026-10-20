def min(no , a):

    mcount = 0    
    
    for i in range(len(no)):
        count = 0
        for j in range(len(no)):
            if no[j] == a == no[i]:
               count = count + 1
        if count > mcount:
            mcount = count

    return mcount

def main():

    lst = []

    element = int(input("Enter the number of elements in list : "))

    for i in range(element):
        lst.append(int(input("Enter the elements : ")))

    print(lst)

    a = int(input("Enter the number of elements in list : "))

    ret = min(lst , a)
    print(f"frequency of {a} repeted no : {ret} ")



if __name__ =="__main__":
    main()


