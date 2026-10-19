lamMax = lambda no1 ,no2 ,no3: max(no1 ,no2 ,no3)   # a if a > b and a > c else (b if b > c else c)
         
def main ():

    no1 = int(input("Enter the number One: "))
    no2 = int(input("Enter the number Two : "))
    no3 = int(input("Enter the number Third : "))
    ret = lamMax(no1 ,no2 ,no3)
    
    
    print(f"Number {ret} is greater ")
    

if __name__ == "__main__":
    main()