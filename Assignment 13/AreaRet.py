def AreaRet(length , breadth):
      
      return length * breadth

def main ():
    length= int(input("Enter no length : "))
    breadth = int(input("Enter breadth : "))
    Area = AreaRet(length , breadth)

    print(f"Area of Rectangle :- {Area}" )
    

if __name__ == "__main__":
    main()