def OddNo(no):

    for i in range(1 ,no+1 ,2):
        if i % 2 !=0:
            print(i , end =" ")

def main():
    no = 10
    print("odd numbers are : " ) 
    OddNo(no)
    
    
if __name__=="__main__":
    main()