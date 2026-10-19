Cube = lambda no : no**3

def main ():

    no = int(input("Enter th number : "))
    ret = Cube(no)

    print(f"Cube of {no} is {ret}")

if __name__ == "__main__":
    main()