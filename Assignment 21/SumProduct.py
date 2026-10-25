import threading 

Total = 0
Product = 1

def Max(no):       
      
    global Total 
    for i  in no:
       Total = Total + i
    print("Sum : " , Total)

def Min(no):

    global Product
    for i  in no:
       Product = Product * i
    print("product : " , Product)

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

    print(f"Result from Main Sum is {Total} and Product is {Product}")
    
if __name__ =="__main__":
    main()