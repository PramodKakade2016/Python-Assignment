CheckEven = lambda no: no % 2 == 0

def main():

    lst = []

    no = int(input("Enter number of elements: "))

    elements = input("Enter numbers separated by spaces: ").split()

    for i in range(no):
        lst.append(int(elements[i]))

    print("Original List:", lst)

    ret = list(filter(CheckEven, lst))

    print(f"Even numbers: {ret}")
    print(f"Count of even numbers: {len(ret)}")

if __name__ == "__main__":
    main()