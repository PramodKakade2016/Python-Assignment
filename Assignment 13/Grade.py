def grade(no):
                
    if  no >= 75 :
        print("Distinction")
    elif no >= 60:
        print("First class")
    elif no >= 50:
        print("second class")
    elif no < 60:
        print("fail")
  

def main ():
    no= int(input("Enter no  : "))
   
    grade(no)  

if __name__ == "__main__":
    main()