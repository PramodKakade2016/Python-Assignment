import MarvellousNum


def listprime(lst):

    total = 0

    for no in lst:
        if MarvellousNum.CheckPrime(no):
            total = total + no

    return total


def main():

    lst = []

    n = int(input("Enter number of elements: "))

    for i in range(n):
        no = int(input("Enter number: "))
        lst.append(no)

    print("List:", lst)

    result = listprime(lst)

    print("Addition of prime numbers:", result)


if __name__ == "__main__":
    main()