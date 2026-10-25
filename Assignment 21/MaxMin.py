import threading 


def Max(no):       
    #print(max(no))  simple way 
    print("Max")
    Max = no[0]
    for i  in no:
        if i > Max:
            Max = i 
    print(Max)

def Min(no):
   # print(min(no)) insted of below logic we can use 

    print("Min")
    Min = no[0]
    for i  in no:
        if i < Min:
            Min = i 
    
    print(Min)

def main():

    lst= []
    no = int(input("Enter the number of elements : "))

    for i in range(no):
        lst.append(int(input("Enter list elements")))

    t1 = threading.Thread(target=Max , args=(lst ,))
    t1.start()
    t1.join()
    t2 = threading.Thread(target=Min , args=(lst ,))
    t2.start()
    t2.join()

    print("Exit main")
if __name__ =="__main__":
    main()