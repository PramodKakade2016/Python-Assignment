def AreaRet(radius , pi=3.14159265339 ):
      
      return pi * radius**2

def main ():
    radi= int(input("Enter no length : "))
   
    Area = AreaRet(radi)

    print(f"Area of Circle :- {Area:.3f}" )
    

if __name__ == "__main__":
    main()