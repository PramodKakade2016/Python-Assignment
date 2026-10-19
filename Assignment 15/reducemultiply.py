from functools import reduce

Multiply = lambda no1 ,no2 : no1 * no2

def main():

    lst = []

    no = int(input("Enter number of elements: "))

    elements = input("Enter numbers separated by spaces: ").split()

    for i in range(no):
        lst.append(int(elements[i]))

    print("Original List:", lst)

    ret = reduce(Multiply, lst)

    print(f"Multiplication of all elements : {ret}")

if __name__ == "__main__":
    main()