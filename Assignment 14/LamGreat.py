'''
lamGreater = lambda no1 ,no2 : no1 > no2 

def main ():

    no1 = int(input("Enter the number : "))
    no2 = int(input("Enter the number two : "))
    ret = lamGreater(no1 ,no2)
    
    if ret == True:
        print(f"Number one {no1} is greater then {no2}")
    else:
        print(f"Number Two {no2} is greater then {no1}")
    

if __name__ == "__main__":
    main()
'''

lamGreater = lambda no1 ,no2 : no1 if no1 > no2 else no2

def main ():

    no1 = int(input("Enter the number : "))
    no2 = int(input("Enter the number two : "))
    ret = lamGreater(no1 ,no2)
    
    
    print(f"Number {ret} is greater ")
    

if __name__ == "__main__":
    main()