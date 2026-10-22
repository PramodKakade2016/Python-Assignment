power = lambda no1 , no2 : no1 * no2


def main():

    No1 = int(input("enter the number : "))
    No2 = int(input("enter the number : "))

    ret = power(No1 , No2)
    print(f"Multplication of {No1} x {No2} = {ret}")

if __name__=="__main__":
    main()