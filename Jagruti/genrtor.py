
#1
"""
def gen(n):
    v=0
    while v<n:
        yield v
        v=v+1           #i++
def main():
    for i in gen(3):
        print(i)

if __name__=="__main__":
    main()"""

#2
"""
def gen(n):
    v=0
    while v<n:
        yield v
        v=v+1           #i++
def main():
    x=gen(3)
    try:
        print(next(x))
        print(next(x))
        print(next(x))
        print(next(x))
    except : #generic exception
        print("StopIteration value is  over")

if __name__=="__main__":
    main()"""

#3
"""
def  gen():
    yield 1
    yield 2
    yield 6
def main():
    for i in gen():
        print(i)
        
if __name__=="__main__":
    main()"""

#4
"""

def gen():
    yield 1
    yield 2
    yield 6


def main():
    x=gen()
    print(next(x))
    print(next(x))
    print(next(x))
if __name__ == "__main__":
    main()"""

#5
"""
def gen(l1):
    for i in l1:
        if i % 2 == 0:
            yield i
def main():
    l1=[1,2,3,4,5,6,7,8,9,0]
    for i in (gen(l1)):
            print(i)

if __name__ == "__main__":
    main()"""

#6(odd)
"""
def gen(l1):
    for i in l1:
        if i % 2 != 0:
            yield i
def main():
    l1=[1,2,3,4,5,6,7,8,9,0]
    for i in (gen(l1)):
            print(i)

if __name__ == "__main__":
    main()"""


#7(prime)
"""
def gen(no1,no2):
    for no in range(no1,no2):
        if   no>1 :
            for j in range(2,no):
                if no % j==0:
                    break
            else:
                yield no
def main():
    no1=1
    no2=20
    for j in (gen(no1,no2)):
            print(j)

if __name__ == "__main__":
    main()"""

#8 factorial
"""
def gen(no1):
    mul=1
    for i in range(no1,1,-1):
        mul=mul*i
    yield mul
def main():
    result=gen(5)
    print(next(result))

if __name__ == "__main__":
    main()"""

#factors
"""
def gen(no1):
    for i in range(1,no1):
        if no1%i==0:
            yield i
def main():
    no1=20
    for j in (gen(no1)):
            print(j)

if __name__ == "__main__":
    main()"""

#perfect no
"""
def gen(no):
    sum=0
    for i in range(1,int(no/2)+1):
        if no%i==0:
            sum=sum+i
    yield sum

def main():
    no=6
    sum=gen(no)
    if next(sum )== 6:
        print("its is perfect num")
    else:
        print("its not perfect")

if __name__ == "__main__":
    main()"""

#fibbonachi
"""
def gen(no1):
    a=0
    b=1
    temp=0
    for i in range(1,no1):
        temp=a+b
        a=b
        b=temp
        yield temp

def main():
    for j in (gen(10)):
            print(j)

if __name__ == "__main__":
    main()"""


