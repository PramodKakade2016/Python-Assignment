def RevNatural (no):
    print (f"No from Reversed of {no} are :-" , end =" ")
    for i in range(no , 0 , -1):
       print (i , end =" ")       

def main ():
    no= int(input("Enter no : "))
    RevNatural(no)
    

if __name__ == "__main__":
    main()