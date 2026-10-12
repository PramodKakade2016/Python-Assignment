def divisible(no):

    return  no%3 == 0 and no%5 == 0
      
def main():
    no = 15
    ret = divisible(no)
    if ret == True:
        print("Is divisible by 3 and 5 ")
    else :
        print("Not Divisible by 3 and 5")
if __name__ =="__main__":
    main()

    