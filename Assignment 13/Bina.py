def bina(no):
                
    return bin(no)

def main ():
    no= int(input("Enter no  : "))
   
    ret = bina(no)

    print(f"Binary equivalent of {no} is  {ret}" )
    

if __name__ == "__main__":
    main()