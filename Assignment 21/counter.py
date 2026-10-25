import threading 

count = 0
lock =threading.Lock()


def Incr(No):       
    
    global count 

    for i in range( No):
        lock.acquire()
        count = count + 1
        lock.release()

def main():

    
    global count

    t1 = threading.Thread(target=Incr , args=(10000000 ,))
    t2 = threading.Thread(target=Incr , args=(10000000 ,))

    t1.start()
    t2.start()

    t2.join()
    t1.join()
    print(count)

if __name__ =="__main__":
    main()