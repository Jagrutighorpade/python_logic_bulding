#1
"""
def fibbo(no):
    t=0
    a=0
    b=1
    for i in range(no):
        t=a+b
        a=b
        b=t
        print(t,end=" , ")


def main():
    no=int(input("enter no="))
    fibbo(no)
if __name__=="__main__":
    main()"""

#2
"""
def big(no1,no2,no3):
    if no1>no2 and no1>no3:
        print(no1)
    elif no2>no3:
        print(no2)
    else:
        print(no3)
def main():
    no1=int(input("enter no="))
    no2=int(input("enter no="))
    no3=int(input("enter no="))
    big(no1,no2,no3)

if __name__=="__main__":
    main()"""

#3
"""
class xyz:
    def big(no1,no2):
        b=(no1-no2)
        print(b)
class xyz1(xyz):
    def big(no1,no2):
        c=(no1+no2)
        print(c)
def main():
    no1=int(input("enter no="))
    no2=int(input("enter no="))
    obj=xyz1
    obj.big(no1, no2)

if __name__=="__main__":
    main()"""

