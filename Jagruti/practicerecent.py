# 1
"""
def main():
    l1=[11,[22,33],44,55]
    l1[1][0]=222
    print(l1)
if __name__=="__main__":
    main()"""


# 2
"""
def main():
    l1 = [11, 22, 33, 44, 55, 66]
    l2 = [i for i in l1 if i == 44 or i == 55]
    print(l2)
    l3 = []
    for i in l1:
        if i == 44 or i == 55:
            l3.append(i)
    print(l3)
if __name__ == "__main__":
    main()"""

#3
"""
def main():
    l1 = [11, 22]
    l2=[99,88]
    
    print("l1=",l1)
    print("l2=",l2)

    l3=l1
    l1=l2
    l2=l3

    print("l1=",l1)
    print("l2=",l2)

if __name__ == "__main__":
    main()"""

#4
"""
def main():
    l1=["orange",[10,20,30],[5,15,25]]
    print(l1[1][1])
if __name__ == "__main__":
    main()"""

#5
"""
def main():
    l1=[5,10,15,20,25,50,20]
    for i in range(len(l1)):
        if l1[i]==20:
            l1.insert(i,200)
            break
    print(l1)
if __name__ == "__main__":
    main()"""

#6
"""
def main():
    l1=[10,20,[300,400,[5000,6000],500],30,40]
    print(l1)
    l1[2][2].append(7000)
    print(l1)
if __name__ == "__main__":
    main()"""

#7
"""
def main():
    l1=[10,20,30,40,50]
    print(l1)

    #1
    l2=l1[::-1]
    print(l2)

    #2
    l3=[]
    for i in range(len(l1)-1,-1,-1):
        l3.append(l1[i])
    print(l3)

    #3
    t=0
    si=0
    ei=len(l1)-1
    while si<ei:
        t=l1[si]


        l1[si]=l1[ei]
        l1[ei]=t
        si=si+1
        ei=ei-1
    print(l1)



if __name__ == "__main__":
    main()"""

#8
"""
def main():
    l1=[34,54,67,89,11,43,94]
    

    print(l1)

    n   o=l1[4]
    print(no)

   # l1.remove(l1[4])
    for j in range(len(l1)):
        if j==4:
            l1.remove(l1[4])
    for i in range(len(l1)):
        if i ==2:
            l1.insert(2,no) or l1.append(no)
    print(l1)

if __name__ == "__main__":
    main()"""

#9
"""
def main():
    l1=[3,6,9,12,15,18,21]
    l2=[4,8,12,16,20,24,28]
    #1
    l3=[ l1[i] for i in range(len(l1)) if i%2!=0 ]
    for j in range(len(l2)):
        if j %2==0:
            l3.append(l2[j])
    print(l3)

#2
    l4=l1[1::2]
    l5=l2[::2]
    print(l4+l5)
if __name__=="__main__":
    main()"""


#10
"""
def main():
    #t1=([2,5,2,6,9],[3,7,3,1,2])
    #t1=([1,2,3,4,5],[9,8,7,6,5])
    t1=([4,3,4,4,5],[3,2,5,4,1])
    print("t1  = ",t1)
    l2=[]
    l3=[]

    l4=[]
    l5=[]
    for i in range(len(t1)):
        if i==0:
            l2.append(t1[0])
        else:
            l3.append(t1[1])
    print("l2  = " ,l2)
    print("l3  = ",l3)

    for i in l2:
        for x in range(len(i)):
             for y in range(len(i)):
                 if x!=y:
                    l4.append(int(str(i[x])+str(i[y])))
    print("l4  = ",l4)
    print()


    for i in l3:
        for x in range(len(i)):
             for y in range(len(i)):
                 if x!=y:
                    l5.append(int(str(i[x])+str(i[y])))
    print("l5  = ",l5)
    print()

    if max(l4)>max(l5):
        print( max(l4),">",max(l5),"=","True")
    else:
        print( max(l4),">",max(l5),"=","False")



if __name__=="__main__":
    main()"""

#2
"""
from functools import reduce
def  fun(name1,name2):
    #l1=[]
    # for i in name1:
    #     if i not in name2:
    #         l1.append(ord(i))
    # for j in name2:
    #     if j not in name1:
    #         l1.append(ord(j))
    #
    # print(l1)
    #
    # l2=(reduce(lambda x,y: x-y,l1))
    # print(l2)


     if len(name1)>=len(name2):
         for i in range(len(name1)):
            if (name1[i] not in name1 ):
                print(ord(name1[i])- ord(name2[i]))
        


def main():
    name1=str(input("enter  name ="))
    name2=str(input("enter  name ="))
    fun(name1,name2)
if __name__=="__main__":
    main()"""

#1
"""
def main():
    t1=([2,5,2,6,9],[3,7,3,1,2])
    #t1=([1,2,3,4,5],[9,8,7,6,5])
    #t1=([4,3,4,4,5],[3,2,5,4,1])
    for i in t1:
        print(sorted(i))






if __name__=="__main__":
    main()"""


#..........................itertors

#......exception hndling
"""
def fun(x,y):

   try:
        c=((x+y)/(x-y))
   except:
        print("0 devision error")
   else:
        print(c)


no2 = int(input("enter no2="))
no3 = int(input("enter no3="))
fun(no2,no3)"""

#genertor
"""
#1
def  fct(no):
    mul=1
    for i in range(no,1,-1):
        mul=mul*i
    yield mul

def main():
    no=int(input("enter no="))
    ans=fct(no)
    print(next(ans))
if __name__=="__main__":
    main()"""

#2
"""
def fun(no):
    squ=0
    for i in range(no):
        squ=i**2
        yield squ

def main():
    no=int(input("enter no="))
    for i in fun(no):
        print(i,end=" ")
if __name__=="__main__":
    main()"""

#3
"""
def fun1(no):
    for i in range(no):
        if i%2==1:
            yield i
def main():
    no=int(input("enter no="))
    for i in fun1(no):
        print(i,end=" ")
if __name__=="__main__":
    main()"""

#4
"""
def fun1(no):
    sum=0
    for i in range(no):
        sum=sum+i
        yield sum
def  main():
    no=int(input("enter no="))
    f=0
    for i in fun1(no):
        print(i,end=" ")
        print(" ")
        if i==no:
            f=1
    if f==1:
        print("yes present")
    else:
        print("not present")


if __name__=="__main__":
    main()"""


"""
def fun1(name):
    for i in range(len(name)+1):
        if i%2==1:
            print((chr(ord(name[i])-32)),end=" ")


def main():
    name=input("enter name=")
    fun1(name)
if __name__=="__main__":
    main()"""

#decorators--------------------
#1
"""
import time
def fun1(no):
    for x in range(2, no+1):
        if no > 2:
            for i in range(2,x):
                if x%i==0:
                    break
            else:
                yield x
def main():
    no=int(input("enter no="))
    for j in fun1(no):
        time.sleep(2)
        print(j)


if __name__=="__main__":
    main()"""

#class dic
"""
class avrage:
    @classmethod
    def stud(cls,d1):
        sum=0
        for i in d1.values():
            sum=sum+i
        avg=sum/len(d1)
        print(avg)


def main():
    d1={}
    size=int(input("enter dict size="))
    for i in range(size):
        name=input("enter student name=")
        value=int(input("enter student marks ="))
        d1[name]=value
        #d1.update({name:value})
    print(d1)
    avrage.stud(d1)


if __name__=="__main__":
    main()"""

#decorator
"""
def discount(addtocart):
    def inner():
        addsupercoin_Rs=15
        realprice=addtocart()
        total=realprice-addsupercoin_Rs
        return total
    return inner

def addtocart():
    product_price=int(input("enter amount of product Rs  ="))
    return product_price


addtocart =discount(addtocart)
print("after discount you need to pay Rs=" ,addtocart())"""



#2
"""
def discount1(product):
    def inner():
        realprice=product()
        if realprice>1000:
            Bank_name=input("enter bankname ICICI OR SBI  =")
            if Bank_name=="ICICI":
                total=realprice-(realprice//10)
                print("ICICI 10% discount = ", total)
                return total
            elif Bank_name=="SBI":
                total=realprice-(realprice//15)
                print("SBI 15% discount = ", total)
                return total
            # else:
                # return ("sorry your bank is not eliigible for discount")
        else:
            return realprice

    return inner()

def discount2(product):
    def inner():
        cupon = input("enter cupon =  ")
        b = product
        if b>1000:
            if cupon=="OFF100":
                total=b-100
                return total
        else:
            return b
    return inner

def product():
    productprice=int(input("eneter price rs ="))
    return productprice

product=discount2(discount1(product))
print("payable amount rs =",product())
#50====55=====10---------10*5=50-------50+5=55-------10"""









