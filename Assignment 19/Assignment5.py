from functools import reduce


def DataFilter(No):

    if No <= 1:
        return False

    for i in range(2,No):
        if No % i == 0 :
             return False
    return True 

DataMap = lambda no1  : no1 **2

DataReduce = lambda no1 , no2  : no1 if no1 > no2 else no2 

def main():

    lst = []
    No = int(input("enter the number of elements : "))

    for i in range(No):
        lst.append(int(input("Elements in List : ")))

    print(f"Orignal List : {lst}")

    Fdata = list(filter(DataFilter , lst))
    Mdata = list(map(DataMap , Fdata))
    Rdata = reduce(DataReduce , Mdata)
    
    print(f"Filter Data  = {Fdata}")
    print(f"Map Data  = {Mdata}")
    print(f"Reduce Data  = {Rdata}")

if __name__=="__main__":
    main()