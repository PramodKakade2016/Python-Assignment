import Arithmetic
'''
def main():

    No1 = int(input("Enter 1st Number : "))
    No2 = int(input("Enter 2nd Number : "))

    ret = Arithmetic.Arathimatic()

    print(ret(No1 ,No2))

if __name__ == "__main__":
    main()
'''
def main():

    No1 = int(input("Enter 1st Number : "))
    No2 = int(input("Enter 2nd Number : "))

    print("Addition is : " , Arithmetic.Addn(No1 ,No2))
    print("Substraction is : " , Arithmetic.Sub(No1 ,No2))
    print("Multiplication is : " , Arithmetic.Mult(No1 ,No2))
    print("Division is : " , Arithmetic.Div(No1 ,No2))

if __name__ == "__main__":
    main()
