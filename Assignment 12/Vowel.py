
def Vowel(ch):
    
    vowel =["a","e","i","o","u"]

    for i in vowel:
        if ch.lower() == (i):
            print("Vowel")
            return
    print("Constant")    

def main():
    
    while True :
        ch = input("Enter one character : ")

        if len(ch) == 1:
            break
        else :
            print("Enter Valid char")
    Vowel(ch)

if __name__=="__main__":
    main()
'''

def Vowel(ch):
    
    if ch.lower() in "aeiou":
        print("Vowel")
    else:
        print("Constant")    

def main():
    
    while True :
        ch = input("Enter one character : ")

        if len(ch) == 1:
            break
        else :
            print("Enter Valid char")
    Vowel(ch)

if __name__=="__main__":
    main()
'''    