import multiprocessing
import os

def Factorial(no):

    Fact = 1
    result = ""

    for i in range(1, no + 1):

        Fact = Fact * i

        if i == no:
            result = result + str(i)
        else:
            result = result + str(i) + "*"

    return (os.getpid(), no, result, Fact)


def main():

    Data = [16, 14, 17, 18]

    p = multiprocessing.Pool()

    result = p.map(Factorial, Data)

    p.close()
    p.join()

    for pid, no, expression, fact in result:
        print("Process Id :", pid)
        print("Input Number :", no)
        print(expression, "=", fact)
        print("----------------")


if __name__ == "__main__":
    main()