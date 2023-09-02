#1
"""
def exc():
    no1=10
    no2=0
    l1=[1,2,3]
    try:
        d=(no1 + no2)
        e=(no1 - no2)
        print(e)
        print(d)
        #
        # a=(no1 * no2)
        # b=(no1 / no2)
        # print(a)
        # print(b)

        print(l1[5])
    except IndexError :
        print("index is not found ")

    except ZeroDivisionError:
        print("when we multiply or devided with 0 we get zero ")

def main():
    exc()

if __name__=="__main__":
    main()"""

#2
"""
def exc():
    try:
        no1=int(input("enter no ="))
        if no1%2==0:
            print(no1)
        else:
            print(no1)
    except :
        print("enter no not charactor")

def main():
    exc()

if __name__=="__main__":
    main()"""

#4
"""
def exc():
    try:
        a=10
        b="0"
        e=a+b
        d=a/b
        print(e)
        print(d)
    except   ZeroDivisionError:
        print("cant devied wirh zero")
    except:
        print(" unsupported operation")

def main():
    exc()

if __name__=="__main__":
    main()"""

#5
"""
def exc():
    try:
        a=10
        b=0
        d=a/b
        print(d)

    except TypeError:
        print(" unsupported operation")
    except   ZeroDivisionError:
        print("cant devied wirh zero")

def main():
    exc()

if __name__=="__main__":
    main()"""

# try except else
"""
def exc():
    try:
        a=int(input("enter 1st no="))
        b=int(input("enter 2nd no="))
        d=a/b

    except ValueError:
        print(" unsupported operation")
    except   ZeroDivisionError:
        print("cant devied wirh zero")
    else:
        print("ans =",d)

def main():
    exc()

if __name__=="__main__":
    main()"""

#

def exc():
    try:
        a=int(input("enter no upto 10="))
        if a>10:
            raise ValueError(a)
    except ValueError:
        print(" unsupported no")
    else:
        print("u enter write input",a)

def main():
    exc()

if __name__=="__main__":
    main()
