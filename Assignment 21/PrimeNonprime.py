import threading 


def Prime(no):
    print("Prime")
    for i  in no:
        if i < 2:
            continue
        prime = True
        for j in range(2,i):
                if i % j == 0 :
                    prime = False
        if prime:
            print(i)
    print("End Prime")

def NonPrime(no):

    print("NonPrime")
    for i  in no:
        if i < 2:
            continue
        prime = True
        for j in range(2,i):
                if i % j == 0 :
                    prime = False
        if not prime:
            print(i)
    print("End NonPrime")
def main():

    lst= []
    no = int(input("Enter the number of elements : "))

    for i in range(no):
        lst.append(int(input("Enter list elements")))

    t1 = threading.Thread(target=Prime , args=(lst ,))
    t1.start()
    t1.join()
    t2 = threading.Thread(target=NonPrime , args=(lst ,))
    t2.start()
    t2.join()

    print("Exit main")
if __name__ =="__main__":
    main()