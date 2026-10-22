power = lambda no : no **2


def main():

    No = int(input("enter the number : "))

    ret = power(No)
    print(f"Power of {No} is {ret}")

if __name__=="__main__":
    main()