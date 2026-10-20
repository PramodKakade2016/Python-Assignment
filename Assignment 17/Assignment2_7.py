def pattern (no):

    for i in range(1 , no+1):
        for a in range(1 , no+1):
          print(a , end = " ")
        print()

def main():

    No = int(input("Enter Number : "))

    pattern(No)

if __name__ =="__main__":
    main()