'''
def countdigit(No):

   print("the digits are :  " , len(str(No)))
    
def main():

    No = int(input("Enter the number : "))
    countdigit(No)

if __name__=="__main__":
    main()
'''

def countdigit(no):

    count = 0
    while no > 0:
        no = no // 10
        count = count + 1

    print("count : " , count) 

def main():

    no = int(input("enter no "))
    countdigit(no)
    
if __name__=='__main__':
    main()   
