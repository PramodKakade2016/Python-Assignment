def pattern(no):

    for i in range(no):
        print("* " *no)

def main():

    No = int(input("Enter Number : "))

    pattern(No)

if __name__ =="__main__":
    main()