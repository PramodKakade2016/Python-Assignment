def pattern (no):

    for i in range(no , 0 , -1):
        print("* " *i)


def main():

    No = int(input("Enter Number : "))

    pattern(No)

if __name__ =="__main__":
    main()