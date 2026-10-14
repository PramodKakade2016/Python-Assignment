def Naturalno (no):
    print (f"No from starting of {no} are :-" , end =" ")
    for i in range(1, no+1):
       print (i , end =" ")       

def main ():
    no= int(input("Enter no : "))
    Naturalno(no)
    

if __name__ == "__main__":
    main()