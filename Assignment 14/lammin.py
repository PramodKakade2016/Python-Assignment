'''
lamMin = lambda no1 ,no2 : no1 if no1 < no2 else no2

def main ():

    no1 = int(input("Enter the number : "))
    no2 = int(input("Enter the number two : "))
    ret = lamMin(no1 ,no2)
    
    
    print(f"Number {ret} is Smaller ")
    

if __name__ == "__main__":
    main()
'''    

lamMin = lambda no1 ,no2 : min(no1 ,no2)

def main ():

    no1 = int(input("Enter the number : "))
    no2 = int(input("Enter the number two : "))
    ret = lamMin(no1 ,no2)
    
    
    print(f"Number {ret} is Smaller ")
    

if __name__ == "__main__":
    main()