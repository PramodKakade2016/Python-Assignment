def pattern (no):
   
    Digsum = 0

    while no > 0 :
        dig = no % 10
        Digsum = Digsum + dig
        no = no // 10

    return Digsum     

def main():

    No = int(input("Enter Number : "))

    ret = pattern(No)
    print(ret)

if __name__ =="__main__":
    main()