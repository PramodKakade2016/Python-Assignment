CheckDivisible = lambda no: no % 3 == 0 and no % 5 == 0

def main():

    lst = []

    no = int(input("Enter number of elements: "))

    elements = input("Enter numbers separated by spaces: ").split()

    for i in range(no):
        lst.append(int(elements[i]))

    print("Original List:", lst)

    ret = list(filter(CheckDivisible, lst))

    print(f"Numbers divisible by 3 and 5: {ret}")

if __name__ == "__main__":
    main()