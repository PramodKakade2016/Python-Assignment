'''
def pattern (no):

   print(len(str(no)))

def main():

    No = int(input("Enter Number : "))

    pattern(No)

if __name__ =="__main__":
    main()
'''

def pattern (no):
   
    count = 0

    while no > 0 :
        dig = no % 10
        count = count + 1
        no = no // 10

    return count     

def main():

    No = int(input("Enter Number : "))

    ret = pattern(No)
    print(ret)

if __name__ =="__main__":
    main()