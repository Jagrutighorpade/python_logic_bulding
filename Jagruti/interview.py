#1
"""
class lis_frq:
    def fun1():
        l1=[1,2,2,2,"a","a","b"]
        d2={}
        for i in l1:
            if i in d2:
                d2[i]=d2[i]+1
            else:
                d2[i]=1
        for k,v in d2.items():
            print(k,":",v)
def main():
    obj=lis_frq
    obj.fun1()
if __name__ == "__main__":
    main()"""


#2


"""
class lis_frq:
    def fun1():
        l1=[1,0,1,0,0,1,0]
        t=0
        for i in range(len(l1)):
            for j in range(i+1,len(l1)):
                if  l1[i]>l1[j]:
                    t=l1[i]
                    l1[i]=l1[j]
                    l1[j]=t
        print(l1)

def main():
    obj=lis_frq
    obj.fun1()
if __name__ == "__main__":
    main()"""

#3
"""
i = 0
def fun1():
    l1=[1,2,3,4,5]
    global i
    if  i<len(l1):
        print(l1[i]**2,end=" , ")
        i=i+1
        fun1()


def main():
    fun1()
if __name__ == "__main__":
    main()"""

#4
"""
def fun1():
    l1=[1,2,3,4,5]
    l2=list(map(lambda x : x**2,l1))
    print(l2)

def main():
    fun1()
if __name__ == "__main__":
    main()"""

#5
"""
def fun1():
    c=0
    for no in range(1,100):
        while no!=0:
            r=no%10
            if r==5:
                c=c+1
            no=no//10
    print(c)
def main():
    fun1()
if __name__ == "__main__":
    main()"""


#6
"""
def fun1():
    l1=[1,2,3,4,5,1,2]
    l2=[]
    l3=[]
    for i in l1:
        if i  not in l2:
            l2.append(i)
        else:
            l3.append(i)

    s1=set(l2)
    s2=set(l3)
    s3=s1.symmetric_difference(s2)
    l5=list(s3)
    print(l5)


def main():
    fun1()
if __name__ == "__main__":
    main()"""


#7
"""
def fun1():
    s="item_al10_item_b$20_item_cQ30"
    l1=list(s)
    for i in range(len(l1)-1):
        if l1[i]=='0':
            l1[i+1]=","
    for i in l1:
        print(i,end="")
def main():
    fun1()
if __name__ == "__main__":
    main()"""



#8
"""
def fun1(no):
    while no !=0:
        r=no%10
        no=no//10
        print(r,end="")

def main():
    no=312
    fun1(no)
if __name__ == "__main__":
    main()"""

#9
"""
def fun1(no):
    if no !=0:
        r=no%10
        no=no//10
        print(r,end="")
        fun1(no)


def main():
    no=312
    fun1(no)
if __name__ == "__main__":
    main()"""

#10
"""
def fun1():
    l1=[321,123,421,521,678]
    l2=[]
    for no in l1:
        a=str(no).replace("2","")
        l2.append(int(a))
    print(l2)

def main():
    fun1()
if __name__ == "__main__":
    main()"""

#11
"""
def fun1():
    l2="aabbbccccddddd"
    l1=list(l2)
    d2={}
    for i in l1:
        if ( i in d2):
            d2[i]=d2[i]+1
        else:
            d2[i]=1
    print(d2)

    for x,y in d2.items():
        print(x,end="")
        for j in range(1,y):
            print(j,end="")

def main():
    fun1()
if __name__ == "__main__":
    main()"""

#12
"""
def fun1():
    l1=[{'a':0,'b':0}, {'c':0},{'d':0}]
    #1
    l2=[]
    for i in l1:
        for j in i.keys():
            l2.append(j)
    print(l2)
    
    #2
    l3=[  j     for i in l1    for j in i.keys()  ]
    print(l3)
def main():
    fun1()
if __name__ == "__main__":
    main()"""

#13
"""
def fun1():
    s2="hello how are you"
    s3=s2.split()
    s1=list(s3)
    t=0
    si=0
    ei=len(s1)-1
    while  si <ei:
        t=s1[si]
        s1[si]=s1[ei]
        s1[ei]=t

        si=si+1
        ei=ei-1

    for i in s1:
        print(i,end=" ")


def main():
    fun1()


if __name__ == "__main__":
    main()"""


#14
"""
def fun1():
    l1=[3,9,7,5]
    l2=[4,6,1,8,2]
    l3=l1+l2
    print(l3)
    t=0
    for i in range(len(l3)):
        for j in range(i+1,len(l3)):
            if l3[i]>l3[j]:
                t=l3[i]
                l3[i]=l3[j]
                l3[j]=t
    print(l3)



def main():
    fun1()


if __name__ == "__main__":
    main()"""



#15
"""
def fun():
    l1=[1,2,3,4,3,1,5]
    l2=[]
    for i in range(len(l1)):
        for j in range(i+1,len(l1)):
            if l1[i]==l1[j]:
                l2.extend([l1[i],l1[j]])

    s1=set(l1)
    s2=set(l2)
    s3=s1.difference(s2)
    l3=list(s3)

    l4=l3+l2
    print(l4)


def  main():
    fun()
if __name__=="__main__":
    main()"""


#16
"""
def fun():
    l1=['eat','tea','tan','ate','nat','bat','cat','ant']
    l2=[]
    c=0
    for i in range(len(l1)):
        for j in range(i+1,len(l1)):
            for k in l1[j]:
                if l1[i] in l1[j]:
                    c=c+1
    if c==3:
        l2.append([l1[j]])
    else:
        l2.append([l1[i]])
    print(l2)



def  main():
    fun()
if __name__=="__main__":
    main()"""

#17
"""
def fun():
    a=[8,4,5,2,1]
    d1={}
    t=0
    for i in  range(len(a)):
        for j in range(i+1, len(a)):
            if a[i]>a[j]:
                t=a[i]
                a[i]=a[j]
                a[j]=t
    l3={ a[x]: x        for x in range(len(a))  }
    print(l3)

def  main():
    fun()
if __name__=="__main__":
    main()"""

#18
"""
def fun():
    a=[['Gfg' ,'good'], ['is' ,'for ']]

    b=[]
    c=[]
    for i in range(len(a)):
        if i==0:
            b.extend(a[i])
        else:
            c.extend(a[i])

    d=[x+y    for x,y in zip(b,c)]
    print(d)


def  main():
    fun()
if __name__=="__main__":
    main()"""

#19
"""
def fun():
    l=[6,7,78,75,45,56]
    a=[]
    b=[]
    c=[]
    for i in l:
        if i <10:
            a.append(i)
        elif i<70:
            b.append(i)
        else:
            c.append(i)
    print(b+a +c)
def  main():
    fun()
if __name__=="__main__":
    main()"""


#20
"""
def fun():
    l1=['p','q']
    no=5
    l2=[]
    # for i in range(1,no+1):
    #     l2.extend("p"+,"q"+i)
    # print(l2)
    for j in range(1,(no+1)):
        for i in l1:
            l2.append(i+str(j))
    print(l2)

def main():
    fun()
if __name__=="__main__":
    main()"""


#21
"""
def fun():
    for no in range(25,35):
        print(int(str (no[0])) %2==0), (str(no([1])%2==0))

def main():
    fun()
if __name__=="__main__":
    main()"""



#22
"""
def fun():
    a=[1,1,2,2,3]
    d1={}
    for i in a:
        if i  in d1:
            d1[i]=d1[i]+1
        else:
            d1[i]=1
    print(d1)


def main():
    fun()
if __name__=="__main__":
    main()"""


#23
"""
def fun():
    l1=[1,2,3[4,5,6[7,8,9[10,11]]]]
    for i in l1:
        print(i)
        for j in i:
            print(j)



def main():
    fun()
if __name__=="__main__":
    main()"""

#24
"""
def fun():
    l1=[10,20,30,10,20]
    t=0

    print(l1)
    print(id(l1))

    for i in range(0,len(l1)):
        for j in range(i+1,len(l1)):
            if l1[i]>l1[j]:
                t=l1[i]
                l1[i]=l1[j]
                l1[j]=t
        print("---------------")

    for i in range(0, len(l1)):
        for j in range(i + 1, len(l1)-1):
            if l1[i]==l1[j]:
                l1.remove(l1[i])
    print(l1)
    print(id(l1))

def main():
    fun()
if __name__=="__main__":
    main()"""


#25
"""
no = 300
def fun():
    global no
    if no!=0:
        r=no%10
        print(r,end="")
        no=no//10

        fun()

def main():

    fun()

if __name__=="__main__":
    main()"""

#26
"""
def fun():
    str="AABEBCDD"
    c=0
    for i in range(len(str)):
        for j in range(i+1,len(str)):
            if str[i]==str[j]:
                c=c+1
    print(c)

def main():

    fun()

if __name__=="__main__":
    main()"""

#27
"""
def fun():
    str="aaaabbbccdq"
    d1={}
    for i in str:
        if i  in d1:
            d1[i]=d1[i]+1
        else:
            d1[i]=1
    for j,k in d1.items():
        print(j,k ,end="   ")
def main():

    fun()

if __name__=="__main__":
    main()"""

#28
"""
c=0
l2=[]
def fun():
    l=[1,1,1,0,0,1,1,0,1,1,1,1,1]
    global c
    global l2
    for i in l:
        if i!=0:
            c=c+1
            l2.append(c)
        else:
            c=0
            l2.append(0)
    s=l2.sort()
    print(l2[-1])


def main():

    fun()

if __name__=="__main__":
    main()"""

#29
"""
def fun():
    arr=[1,2,3,4,5]
    l2=[]
    l3=[]
    l4=[]
    for i in arr:
        if i<3:
            l2.append(i)
        elif i>2 and i<5:
            l3.append(i)
        else:
            l4.append(i)
    print(l2[::-1]+l3[::-1]+l4)


def main():

    fun()

if __name__=="__main__":
    main()"""

#30
"""
def fun():
    d1={'a':100 ,'b':200 ,'c':300}
    d2={'a':300 ,'b':200 ,'d':400}
    d3=dict(d1)
    d3.update(d2)
    print(d3)
    for i ,j in d1.items():
        for x,y in d2.items():
            if i==x:
                d3[i]=(j+y)
            else:
                pass
    print(d3)

def main():

    fun()

if __name__=="__main__":
    main()"""


#31
"""
def fun():
    #3
    a="madam"
    b=a[::-1]
    if a==b:
        print("yes")
    else:
        print("no")


    #2
    c=list(a)
    d=[]
    for i in range(len(c)-1,-1,-1):
        d.append(c[i])
    if c==d:
        print("yes")
    else:
        print("no")

    #3
    c=list(a)
    s=0
    e=len(c)-1
    f=0
    while s<e:
        if c[s]!=c[e]:
            f=1
        s=s+1
        e=e-1

    if f==0:
        print("yyyes")
    else:
        print("no")


def main():

    fun()

if __name__=="__main__":
    main()"""




#





#31
"""
def fun():
    str1=list("mafiamafia")
    f=0

    s=0
    e=len(str1)-1


    s1=0
    e1=len(str1)-1
    while s<e:
        str1[s]=str1[e]

        s=s+1
        e=e-1
    print(str1)

    while s1<e1:
        if str1[s1]!=str1[e1]:
            f=1

        s1=s1+1
        e1=e1-1


    if f==0:
        print("yes")
    else:
        print("no")


def main():

    fun()

if __name__=="__main__":
    main()"""


#32
"""
def fun(str1):
    f=0
    i=0
    e=len(str1)-1
    while i<e:
        if str1[i]!=str1[e]:
            f=1
        i=i+1
        e=e-1
    if f==1:
        print("symetric")
    else:
        print("pallindrome")


def main():
    str1=input("enter string=")
    fun(str1)

if __name__=="__main__":
    main()"""

#33
"""
def fun(str1):
    mid=len(str1)//2
    print(str1[mid])
    s=0
    e=len(str1)
    f=0
    while s < mid and  mid<e :
        if str1[s]!=str1[mid ]:
            f=1
        s=s+1
        mid=mid+1
    if f==1:
        print("not symetric")
    else:
        print("yes symetric")

def main():
    str1=input("enter string=")
    fun(str1)

if __name__=="__main__":
    main()"""

#34
"""
def fun(str1):
    str2=str1.split()
    for i in range(len(str2)-1,-1,-1):
        print(str2[i] ,end=" ")

def main():
    str1=input("enter string=")
    fun(str1)

if __name__=="__main__":
    main()"""

#35
"""

def fun(str1):
    a=str1.replace('s',' ')
    b=str1[:2]+str1[3:]
    #if i !==2
    print(a)
    print(b)

def main():
    str1=input("enter string=")
    fun(str1)

if __name__=="__main__":
    main()"""


#36
"""
def fun(str1):
    c=0
    for i in str1:
        if i!=" ":
            c=c+1
    print(c)

def main():
    str1=input("enter string=")
    fun(str1)

if __name__=="__main__":
    main()"""

#37
"""
def fun(str1):
    for i in str1.split():
        if len(i)%2==0:
            print(i)

def main():
    str1=input("enter string=")
    fun(str1)

if __name__=="__main__":
    main()"""

#38
"""
def fun(str1):
    len1=len(str1)//2
    for i in range(len(str1)):
        if i <len1:
            print(str1[i],end="")
        else:
            a=str1[i]
            cap=ord(a)-32
            print(chr(cap),end="")


def main():
    str1=input("enter string=")
    fun(str1)

if __name__=="__main__":
    main()"""


#39
"""
def fun(str1):
    l2=str1.split()
    print(l2)
    for substr in l2:
        for j in range(len(substr)):
            if  j!=0 and j!=len(substr)-1 :
                print(substr[j],end="")
            else:
                a=substr[j]
                cap=ord(a)-32
                print(chr(cap),end="")

def main():
    str1=input("enter string=")
    fun(str1)

if __name__=="__main__":
    main()"""

#40
"""
def fun(str1):
    l1=list(str1)
    for i in range(len(l1)):
        if i==0:
            l1[i]=chr(ord(l1[i])-32)
        if  i==len(l1)-1:
            l1[i] = chr(ord(l1[i]) - 32)

        if  l1[i]==" ":
            l1[i-1]=chr(ord(l1[i-1])-32)
            l1[i+1]=chr(ord(l1[i+1])-32)


    for j in l1:
        print(j,end="")

def main():
    str1=input("enter string=")
    fun(str1)

if __name__=="__main__":
    main()"""


#41
"""
def fun():
    l1=[20,15,18,30,10]
    l2=[]
    l3=[]
    for i in range(len(l1)):
        if i >len(l1)//2:
            l2.append(l1[i])
        else:
            l3.append(l1[i])
    print(l2+l3)

def main():
    fun()

if __name__=="__main__":
    main()"""

#42
"""
def fun(a1):
    f1=0
    f2=0
    f3=0
    d="0987654321"
    a="abcdefghijklmnopqrstuvwxyz"
    for i in a1:
        if i in d:
            f1=1
        if i in a:
            f2=1

        if f1 and f2:
            f3=1

    if  f3==1:
        print("T")
    else:
        print("f")

def main():
    a=input("enter string = ")
    fun(a)

if __name__=="__main__":
    main()"""

#43
"""
def fun():
    c=0
    a=int(input("entr no="))
    b=int(input("entr no="))
    for i in range(a,b):
        a=str(i)
        for j in range(0 ,len(a)):
            for k in range(j+1,len(a)):
                if  a[j]==a[k]:
                    print(i)
                    c=c+1
                    break

    print("similsr=",c)
    print("diffent=",b-c)



def main():
    fun()

if __name__=="__main__":
    main()"""

#44
"""
for i in "fghhghjxk123j":
    if i>='a' and i<='z':
        print(i)"""

#45
"""
def fun(str1):
    str1.lower()
    f1=0
    f2=0
    f3=0
    f4=0
    f5=0
    for i in str1:
     if i=="a" :
         f1=1

     elif i=="e" :
         f2=1

     elif i=="u" :
         f3=1
     elif i=="i" :
         f4=1

     elif i=="o":
         f5=1

    f=f1 and f2 and f3 and f4 and f5

    if    f==1:
        print("accept")
    else:
        print("no")



def main():
    str1=input("enter string=")
    fun(str1)

if __name__=="__main__":
    main()"""
#

#45
"""
def fun(str1):
     s1=set((str1.lower()))
     s2={"a","e","u","i","o"}
     s3=s1.intersection(s2)
     l1=len(s2)
     l2=len(s3)

     if  l1==l2:
        print("accept")
     else:
        print("no")



def main():
    str1=input("enter string=")
    fun(str1)

if __name__=="__main__":
    main()"""

#46
"""
def fun(str1,str2):
    #
    # if str1 not in str2:
    #     print("no")
    # else:
    #     print("yes")

    str1=list(str1)
    str2=list(str2)

    t1=0
    t2=0
    f=0
    for i in range(len(str1)):
        for j in range(i+1,len(str1)):
            if str1[i]>str1[j]:
                t1=str1[i]
                str1[i]=str1[j]
                str1[j]=t1


    print(str1)

    for i in range(len(str2)):
        for j in range(i+1,len(str2)):
            if str2[i]>str2[j]:
                t2=str2[i]
                str2[i]=str2[j]
                str2[j]=t2
    print(str2)
    if str1!=str2:
        f=1

    if f==1:
        print("no")
    else:
        print("yes")





def main():
    str1=input("enter string=")
    str2=input("enter string=")

    fun(str1,str2)

if __name__=="__main__":
    main()"""


#47...sorting
"""
def fun(str1):
    l1=list(str1)
    t=0

    for i in range(len(l1)):
            for j in range(i+1,len(l1)):
                if l1[i]>l1[j]:
                    t=l1[i]
                    l1[i]=l1[j]
                    l1[j]=t

    for j in l1:
        print(j,end="")


def main():
    str1=input("enter string=")

    fun(str1)

if __name__=="__main__":
    main()"""


#49
"""
def fun():
    d1={"ravi":2,"kvi":3,"kavita":7}
    l1=[]
    for i in sorted( d1.keys()):
        l1.append(i)
    print(l1)

def main():

    fun()

if __name__=="__main__":
    main()"""














