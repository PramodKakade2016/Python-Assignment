def pattern (no):

    for i in range(no , 0 , -1):
        for a in range(i):
          print(i , end = " ")
        print()

def main():

    No = int(input("Enter Number : "))

    pattern(No)

if __name__ =="__main__":
    main()