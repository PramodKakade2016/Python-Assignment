def perfect(no):
      total = 0
      for i in range(1 ,no):
           if no % i == 0 :
                total = total + i
      if total == no:
        print(f"The number {no} is :- Perfect" ) 
      else:
        print("Not Perfect ")           


def main ():
    no= int(input("Enter no  : "))
   
    perfect(no)

    print(f"------------------" )
    

if __name__ == "__main__":
    main()