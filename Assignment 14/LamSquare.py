Square = lambda no : no**2

def main ():

    no = int(input("Enter th number : "))
    ret = Square(no)

    print(f"Square of {no} is {ret}")

if __name__ == "__main__":
    main()