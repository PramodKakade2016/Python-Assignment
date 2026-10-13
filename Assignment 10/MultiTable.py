def multiTable(no):
    
    table =[]

    for i in range(1,11):
        t = i*no
        table.append(t)
    return table


def main():
    no = 2
    ret = multiTable(no)
    print(*ret)
'''   print(ret[1])

    result = " , ".join(map(str ,ret))
    print("join mult is :" , result)

    for table, value in enumerate(ret , start=1):
        print(f"{table} * {no} = {value}")

    for i in range(len(ret)):
        print(f" {i+1}*{no}={ret[i]}")
'''      
    
if __name__=="__main__":
    main()