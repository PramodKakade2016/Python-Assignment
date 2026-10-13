'''
def countdigitsum(No):
    sum=0
    for i in str(No):
       sum = sum + int(i)
    return sum
def main():

    No = int(input("Enter the number : "))
    ret = countdigitsum(No)
    print("the sum " , ret)

if __name__=="__main__":
    main()
=================================================================

def countdigitsum(No):
    summ=0
    for i in No:
     summ = summ + int(i)
    return summ

def main():

    No = (input("Enter the number : "))
    ret = countdigitsum(No)
    print("the sum " , ret)

if __name__ == "__main__":
    main()
'''

def countdigsum(no):
    summ =0

    while  no > 0:
      dig= no % 10 
      summ = summ + dig
      no = no // 10
    return summ
def main():
   no = int(input("NO plz"))
   ret =countdigsum(no)
   print ("summ dig ", ret)
if __name__ =="__main__":
   main()
  

