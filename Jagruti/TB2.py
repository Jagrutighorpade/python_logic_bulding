#1  ---add  2 no
"""
def add_1():
    a=10
    b=20
    ans=a+b
    print(ans)
def main():
    add_1()
if __name__ == "__main__":
    main()"""

#2--max btwn 2 no
"""
def add_1(a,b):
    if a>b:
        print(a)
    else:
        print(b)
def main():
    a=int(input("enter no="))
    b=int(input("enter no ="))

    add_1(a,b)
if __name__ == "__main__":
    main()"""

#3----factorial
"""
def fact(a):
    mul=1
    for i in range(1,a+1):
        mul=mul*i
    print("factorial=",mul)
def main():
    a=int(input("enter no="))
    fact(a)
if __name__ == "__main__":
    main()"""

#4--simple intrest (3000,7,1)
"""
def SI(p,r,t):
    simple_in=(p*r*t)/100
    print(simple_in)
def main():
    p=int(input("enter principle="))
    r=int(input("enter intrest rate ="))
    t=int(input("enter time="))

    SI(p,r,t)

if __name__ == "__main__":
    main()"""

#5---compound intres (3000,5,3)
"""
def CI(p,r,t):
    A = p *  (pow ( ( 1+r/100),t) )
    comp_in= A-p
    print(comp_in)
def main():
    p=int(input("enter principle="))
    r=int(input("enter intrest rate ="))
    t=int(input("enter time="))

    CI(p,r,t)

if __name__ == "__main__":
    main()"""

#6-----chk amstrong no
"""
def ams(no):
    no1=no
    no2=no
    no3=no
    c=0
    sum=0
    flag=0
    while no1!=0:
        r=no1%10
        c=c+1
        no1=no1//10

    while no2!=0:
        r1=no2%10
        sum=sum+(r1**c)
        no2=no2//10

    if  no3==sum:
        flag=1
    if flag==1:
        print("yes")
    else:
        print("no")


def main():
    no=int(input("enter no="))
    ams(no)


if __name__ == "__main__":
    main()"""


#7--- area of cirle  (4)
"""
def area_c(PI,r):
    AC = PI*r**2
    print(AC)
    
    
def main():
    PI=3.14
    r=int(input("enter redius="))
    area_c(PI,r)


if __name__ == "__main__":
    main()"""


#8---- prime no in interval
"""
def prime(no1,no2):
        for no in range(no1,no2+1):
            if no>1:
                 for i in range(2,no):
                     if (no % i)==0:
                         break
                 else:
                     print(no)
def main():
    no1=int(input("enter no="))
    no2=int(input("enter no="))

    prime(no1,no2)

if __name__ == "__main__":
    main()"""

#9----chk prime no or not
"""
def prime(no1):
    flag=0
    if no1==1:
        print("its Not primeno")
    if no1>1:
        for i in range(2,no1):
            if no1%i==0:
                flag=1
    if flag==1:
        print("not")
    else:
        print("yes")


def main():
    no1=int(input("enter no="))

    prime(no1)

if __name__ == "__main__":
    main()"""

#10---nth fibbo
"""
def fibo(no1):
    t=0
    a=0
    b=1
    for i in range(0,no1):
        t=a+b
        a=b
        b=t
        print(t)

def main():
    no1=int(input("enter no="))

    fibo(no1)

if __name__ == "__main__":
    main()"""

#11----
""""
def fibo(no1):
    t=0
    a=0
    b=1
    flag=0
    for i in range(0,no1):
        t=a+b
        a=b
        b=t
        if t==no1:
            flag=1
    if flag==1:
        print("yes")
    else:
        print("no")

def main():
    no1=int(input("enter no="))

    fibo(no1)

if __name__ == "__main__":
    main()"""




#12------

#13 ---print ascii value
"""
def func(char):
    v=ord(char)
    print("ascii val of  ",char," is ", v)
def main():
    char=str(input("enter char="))

    func(char)

if __name__ == "__main__":
    main()"""

#14---sum of natural no
"""
def func(Nno):
    sum=0
    for i in range(1,Nno+1):
        sum=sum+(i**2)
    print(sum)


def main():
    Nno=int(input("enter natural no ="))

    func(Nno)

if __name__ == "__main__":
    main()"""

#15---cube of natural no
"""""
def func(Nno):
    sum=0
    for i in range(1,Nno+1):
        sum=sum+(i**3)
    print(sum)


def main():
    Nno=int(input("enter natural no ="))

    func(Nno)

if __name__ == "__main__":
    main()"""

#--------------------------LIST------------------------

#---------------------string---------

#1pallindrome or not
"""
def pallin(str1):
    l1=list(str1)
    l2=list(str1)
    t=0
    s=0
    e=len(l1)-1
    while s < e:
        t=l1[s]
        l1[s]=l1[e]
        l1[e]=t

        s=s+1
        e=s-1
    if l1==l2:
        print("yes")
    else:
        print("not")
def main():
    str1=str(input("enter name="))

    pallin(str1)

if __name__ == "__main__":
    main()"""

#2==#1

#-3---reverse word of string
"""
def pallin(str1):

    l1=list(str1.split())
    t=0
    s=0
    e=len(l1)-1
    while s < e:
        t=l1[s]
        l1[s]=l1[e]
        l1[e]=t

        s=s+1
        e=s-1
    for i in l1:
        print(i ,end="  ")

def main():
    str1=str(input("enter sentence="))

    pallin(str1)

if __name__ == "__main__":
    main()"""

#6----word frquency
"""
def fun(str1):
    l1=list(str1.split())
    d1={}
    for i in l1:
        if i  in d1:
            d1[i]=d1[i]+1
        else:
            d1[i]=1
    print(d1)

def main():
    str1=str(input("enter sentence="))

    fun(str1)

if __name__ == "__main__":
    main()"""


#7--sanke case to pascal case
"""
def fun(str1):
    a=str1.replace("_" , " ").title()
    a=a.replace(" ","")
    print(a)

def main():
    str1=str(input("enter sentence="))

    fun(str1)

if __name__ == "__main__":
    main()"""


#13=-----least frequent char in string
"""
def fun(str1):
    d1={}
    for i in str1:
        if i in d1:
            d1[i]=d1[i]+1
        else:
            d1[i]=1
    ans=(min(d1, key=d1.get))
    print(ans)

def main():
    str1=str(input("enter sentence="))

    fun(str1)

if __name__ == "__main__":
    main()"""

#14--- max frquency
"""
def fun(str1):
    d1={}
    for i in str1:
        if i in d1:
            d1[i]=d1[i]+1
        else:
            d1[i]=1
    ans=(max(d1, key=d1.get))
    print(ans)

def main():
    str1=str(input("enter sentence="))

    fun(str1)

if __name__ == "__main__":
    main()"""

#15 special char is present or not
"""
def fun(str1,char):
    flag=0
    for i in str1:
        if i==char:
            flag=1
    if flag==1:
        print("yes")
    else:
        print("not")


def main():
    str1=str(input("enter sentence="))
    char=str(input("enter char="))
    fun(str1,char)

if __name__ == "__main__":
    main()"""

#16----radom string
#17---word >7
"""
def fun(str1,no):
    l1=list(str1.split())
    for i in l1:
        if (len(i) >no):
            print(i,end="  ")



def main():
    str1=str(input("enter sentence="))
    no=int(input("enter no="))
    fun(str1,no)

if __name__ == "__main__":
    main()"""

#18....remove ith char
"""
def fun(str1,char):
    for i in str1:
        if i!=char:
            print(i,end="")

def main():
    str1=str(input("enter sentence="))
    char=str(input("enter char="))
    fun(str1,char)

if __name__ == "__main__":
    main()"""

#21--- uncommon words from2 string
"""
def fun(str1,str2):
    s1=set(str1.split())
    s2=set(str2.split())
    s3=s1.symmetric_difference(s2)
    for i in s3:
        print(i,end=" ")

def main():
    str1=str(input("enter sentence="))
    str2=str(input("enter sentence="))
    fun(str1,str2)

if __name__ == "__main__":
    main()"""

#22---replace dublicate occurance
"""
def func():
    str1="betty is a girl . betty is good in math . math is her fav sub."
    print(str1)

    Rplc={"betty":"she", "math" : "that"}

    l1=str1.split(" ")

    s1=set()

    for i,j in enumerate(l1):
        if j in Rplc:
            if j in s1:
                l1[i]=Rplc[j]
            else:
                s1.add(j)
    s1=" ".join(l1)
    print(str(s1))

def main():
    func()

if __name__ == "__main__":
    main()"""


#23--- replace multiple words with k
"""
def func():
    str1=str (input("enter string="))
    l1=["s" ,"h","y" ]
    r="k"
    for i in l1:
        str1=str1.replace(i,r)
    print(str1)
def main():
    func()

if __name__ == "__main__":
    main()"""


# 24---- permutation
"""
from itertools import permutations
def permu(str1):
    A=permutations(str1)
    l1=list(A)
    for i in l1:
        print("".join(i))
def main():
    str1=str(input("enter string1 ="))
    permu(str1)

if __name__ == "__main__":
     main()"""

#30== replace all occurance of substring
"""
def fun(str1):

    str2=str1.replace("a","#")
    print(str2)


def main():
    str1=str(input("enter main string="))
    fun(str1)

if __name__ == "__main__":
    main()"""

#=------------------dictionary-----

#1---extract uniq val from dict val
"""
def fun(d1):
    l1=[]
    l2=[]
    for i in d1.values():
        if i not in l1:
            l1.append(i)
        else:
            l2.append(i)
    print(l1)
    print(l2)

    s1=set(l1)
    s2=set(l2)
    s3=set(s1-s2)
    print("unique values=",s3)


def main():
    d1={"a":10, "b":11, "c":10, "d":13,"e":11, "f":14}
    fun(d1)

if __name__ == "__main__":
    main()"""

# 6 marging two list
"""
def fun(d1,d2):
    d3={**d1,**d2}
    print(d3)

    d1.update(d2)
    print(d1)


def main():
    d1={"a":10, "b":11, "c":10, "d":13,"e":11, "f":14}
    d2={"h":119, "g":12}

    fun(d1,d2)

if __name__ == "__main__":
    main()"""

#7---- key value in flat dict
"""
def fun(d1):
    l1=[]
    for i in d1.values():
        l1.append(i)
    print(l1)
    d1={ l1[0][i]: l1[1][i]  for i in range(len(l1)+1)  }
    print(d1)

def main():
    d1={"marks":[10,20,30]    ,"name":["namita","sita","gita"]}

    fun(d1)

if __name__ == "__main__":
    main()"""

#8---insertion at beginning
"""
from collections import OrderedDict
def fun(d1,a):
    d2=OrderedDict(d1)
    b=OrderedDict(a)

    final=OrderedDict(list(b.items())+list(d2.items()))
    print(final)

def main():
    d1={"a":10, "b":11, "c":10, "d":13,"e":11, "f":14}
    a={"k":77}

    fun(d1,a)

if __name__ == "__main__":
    main()"""

#9
#11 key val appened in list
"""
def fun(d1):
    l1=[]
    for i in d1.keys():
        l1.append(i)
    for j in d1.values():
        l1.append(j)
    print(l1)
def main():
    d1={"a":10, "b":11, "c":14}

    fun(d1)

if __name__ == "__main__":
    main()"""

#12---sort key and value list
"""
def main():
    d1={"a":[9,7,10], "v":[11,2], "c":[14,7,3]}
    d2={}
    for i in sorted(d1):
        d2[i]=sorted(d1[i])
    print(d2) 

if __name__ == "__main__":
    main()"""

#16... print anagram using list and dict
"""
def lis_1(l1):
    l2=[]
    for i in range(0,len(l1)):
        for j in range(i+1,len(l1)):
            if l1[i ] in l1[j] or l1[i ] in l1[j] [::-1]:
                l2.append([l1[i],l1[j]])
    print(l2)

def dict_1(l1):
    d2={}
    for i in l1:
        j=str(sorted(i))
        if j in d2:
            d2[j].append(i)
        else:
            d2[j]=[i]
    print(list(d2.values()))

def main():
    l1=['cat',  'dog' , 'fired',  'god',  'pat',  'tap',   'fired',  'tac','mnp',  'kop',  'subha', 'subha']
    lis_1(l1)
    dict_1(l1)

if __name__ == "__main__":
    main()"""


#17---kth no repeating char using list comp and Orderdict
"""
from  collections import OrderedDict
def func(str1,k):
    d1=OrderedDict.fromkeys(str1,0)

    for i in str1:
        d1[i]=d1[i]+1
    print(d1)
    non_R=[k for k , v in d1.items() if v==1]

    print(non_R)
    if len(non_R)<k:
        return "less than k"
    else:
        return non_R[k-1]


def main():
    str1=str(input("enter string="))
    position=1
    print( func(str1,position) )

if __name__ == "__main__":
    main()"""

#18---binary representation is angram or not(17,18)
"""
def func(no1,no2):
    l1=[]
    l2=[]
    flag=1
    while(no1!=0):
          irem=no1%2
          no1=no1//2
          l1.append(irem)
    l3=sorted(l1)
    print(l3)
    while (no2 != 0):
        irem2= no2 % 2
        no2 = no2 // 2
        l2.append(irem2)
    l4=sorted(l2)
    print(l4)
    for i in range(len(l1)):
        if l3[i]!=l4[i]:
            flag=0
    if flag==0:
        print("no")
    else:
        print("yes")



def main():
    no1=int(input("enter binary no1="))
    no2=int(input("enter binary no2="))
    func(no1,no2)


if __name__ == "__main__":
    main()"""

#25---dict,set counter to chk frquency
"""
from collections import Counter
def func(str1):
    d1=Counter(str1)
    print(d1)

    s1=set(d1.values())
    print(s1)

    l1=list(s1)
    print(l1)
    if len(l1)>2:
        print("no")
    elif len(l1)==2 and l1[1]-l1[0]>1:
        print("no")
    else:
        print("yes")

def main():
    str1=str(input("enter string="))
    func(str1)


if __name__ == "__main__":
    main()"""

#26----scraping and finding order words in dict

#27------possible words using char
"""
def fun(words,char):
    for i in char:
        for j in char:
            for k in char:
                sum=(i+j+k)
                for m in words:
                    if  m==sum:
                        print(m)
def main():
    words=['top' , 'cat', 'mat' ,'hat']
    char=['p','o','t','h']
    fun(words,char)

if __name__ == "__main__":
    main()"""


#...extract key from val
"""
def func(d1):
    k1=list(d1.keys())
    v1=list(d1.values())
    ans=v1.index(13)
    print(k1[ans])
def main():
    d1={"a":10, "b":11, "c":10, "d":13,"e":11, "f":14}
    func(d1)

if __name__ == "__main__":
    main()"""

#------tuple-----
#1
"""
def func(t1):
    print(t1.__sizeof__(),"bytes")
def main():
    t1=(1,2,3,4,5)
    func(t1)

if __name__ == "__main__":
    main()"""

#3-- list of tuple having no and its cube
"""
def func(l1):
    l2=[]
    for i in l1:
        l2.append((i,i**3))
    print(l2)
def main():
    l1=[1,2,3,4,5]
    func(l1)

if __name__ == "__main__":
    main()"""

#--4--- adding tuple to list and vice varsa
"""
def func(l1,t1):
    t2=(tuple(l1)+t1)
    print(t2)

    l2=l1+list(t1)
    print(l2)

    l1.extend(t1)
    print(tuple(l1))
    
def main():
    l1=[1,2,3,4,5]
    t1=(6,7,8,9)
    func(l1,t1)

if __name__ == "__main__":
    main()"""

# 5----closest pair of kth index
"""
def   func(l1,t1,k):
    for i in l1:
        for j in  i:
            for k in t1:
                if j==k:
                    print(i)

def main():
    # l1=[(1,2), (3,4) ,(5,6)]
    # t1=(6,7)
    #k=1

    # l1=[(3,4,9),(5,6,7)]
    # t1=(1,2,5)
    # k=3

    l1=[(1,21), (13,24) ,(5,16),(19,23),(44,88)]
    t1=(17,23)
    k=1

    func(l1,t1,k)

if __name__ == "__main__":
    main()"""

#6 join tuple if similar initial
"""
def func(l1):
    l2=[]
    for  i in range(len(l1)):
        for j in range(i+1,len(l1)):
                    if l1[i][0]=l1[j][0]:
                        l2.append(l1[i])
    print(l2)

def main():

    l1=[(5,6), (5,7) ,(5,8),(19,23),(44,88)]

    func(l1)

if __name__ == "__main__":
    main()"""


#7...extract digit from digit
"""
def func(l1):
    l2=[]
    for i in l1:
        for no in i:
            while no!=0:
                r=no%10
                no=no//10
                l2.append(r)
    print(l2)
def main():

    l1=[(19,23),(45,87)]

    func(l1)

if __name__ == "__main__":
    main()"""


#8----two tuple multiple pair
"""
def func(t1,t2):
    l1=[(x,y)  for x in t1  for y in t2]
    l2=l1+[(m,n)  for m in t2  for n in t1]
    print(l2)

def main():

    t1=(1,2)
    t2=(3,4)

    func(t1,t2)

if __name__ == "__main__":
    main()"""


#9--- remove tuple of k len
"""
def func(t1,len_1):
    l2=[]
    for i in t1:
        if  len(i)!=len_1:
            l2.append(i)
    print(l2)

def main():

    t1=[(1,2),(1,2,3,4), (3,4,5),(4,6),(8,9,0)]
    len_1=4
    func(t1,len_1)

if __name__ == "__main__":
    main()"""


#sor tuple
"""
def func(l1):
    # l2=sorted(l1,key=lambda l1:l1[1])
    # print(l2)

    t=0
    e=len(l1)
    for i in range(0,e):
        for j in range(i+1,e):
            if l1[i][1] > l1[j][1]:
                t=l1[i]
                l1[i]=l1[j]
                l1[j]=t
    print(l1)

def main():
    l1=[(5,96), (5,77) ,(5,8),(19,23),(44,88)]
    func(l1)


if __name__ == "__main__":
    main()"""



#11-----order tuple using external list
"""
def func(l1):
    l2=sorted(l1,key=lambda l1:l1[0])
    print(l2)

    t=0
    e=len(l1)
    for i in range(0,e):
        for j in range(i+1,e):
            if l1[i][0] > l1[j][0]:
                t=l1[i]
                l1[i]=l1[j]
                l1[j]=t
    print(l1)

def main():
    l1=[("p",96), ("x",77) ,("u",8),("a",23),("b",88)]
    func(l1)


if __name__ == "__main__":
    main()"""

#---flatten lt of l in t
"""
def func(l1):
    l2=[]
    for i in l1:
        for j in i:
            l2.append(j)
    print(l2)
def main():
    l1=([1,2,3,4],[5,6])
    func(l1)


if __name__ == "__main__":
    main()"""


# tuple to dict
"""
def func(t1):
    l1=[{  "key": i[0] ,  "val": i[1]  , "id":i[2]  }  for i in t1]
    print((l1))

def main():
    t1=((1,"a",2),  (3,"b",4),  (5,"c",6))
    func(t1)


if __name__ == "__main__":
    main()"""

#-------------------------searching and sorting-----
#1----linear search
"""
def func(l1,no):
    for i in range(len(l1)):
        if l1[i]==no:
            print("index=",i)

def main():
    l1=[1,2,3,10,45,67,89]
    no=int(input("enter no="))
    func(l1,no)


if __name__ == "__main__":
    main()"""



#2---binary search
#3-----

#-------------- funcation-------
#1---max no
"""
def func(l1):
    max=0
    for i in l1:
        if i >max:
            max=i
    print(max)

def main():
    l1=[]
    for i in range(3):
        l1.append(int(input("enter item=")))
    func(l1)


if __name__ == "__main__":
    main()"""


#2...sum of all no of list
"""
def func(l1):
    sum=0
    for i in l1:
        sum=sum+i
    print(sum)

def main():
    l1=[10,20,30,40]
    func(l1)

if __name__ == "__main__":
    main()"""

#3-----multiplication of list
"""
def func(l1):
    mul=1
    for i in l1:
        mul=mul*i
    print(mul)

def main():
    l1=[1,20,-3,4]
    func(l1)

if __name__ == "__main__":
    main()"""

#4---reverse string
"""
def func(str1):
    l1=list(str1)
    t=0
    s=0
    len1=len(l1)-1
    while s<len1:
        t=l1[s]
        l1[s]=l1[len1]
        l1[len1]=t
        s=s+1
        len1=len1-1
    for i in l1:
        print(i,end="")


def main():
    str1="abcd1234"
    func(str1)

if __name__ == "__main__":
    main()"""

#5----- factorial
"""
def fun(no):
    mul=1
    for i in range(1,no+1):
        mul=mul*i
    print(mul)
def main():
    no=int(input("enter no="))
    fun(no)

if __name__ == "__main__":
    main()"""

#6...no falls in given range
"""
def fun(no1,no2,chk_no):
    if no1<no2:
        if no1<= chk_no and no2 >=chk_no:
            print("yes")
        else:
            print("no")
    elif no1>no2:
        if no1>= chk_no and no2 <=chk_no:
            print("yes")
        else:
            print("no")
def main():
    no1=int(input("enter start range="))
    no2=int(input("enter end range="))
    chk_no=int(input("enter no="))

    fun(no1,no2,chk_no)

if __name__ == "__main__":
    main()"""

# 7---find uppercase char and lower case char
"""
def func(str1):
    c1=0
    c2=0
    for i in str1:
        if ord(i)<97:
            c1=c1+1
    print("upper=",c1)

    for j in str1:
        if ord(j) >= 97:
            c2 = c2 + 1
    print("lower=", c2)


def main():
    str1= str(input("enter string="))
    func(str1)

if __name__ == "__main__":
    main()"""

#----
"""
def func(s1):
    c1=0
    c2=0
    for i in range(len(s1)):
        if ord(s1[i])<97:
            c1=c1+1

        elif ord(s1[i]) >= 97:
                c2 = c2 + 1

    print("upper=",c1)
    print("lower=", c2)


def main():
    str1= str(input("enter string="))
    func(str1)

if __name__ == "__main__":
    main()"""


#8----
"""
def func(l1):
    l2=[]
    for i in l1:
        if i not in l2:
            l2.append(i)
    print(l2)
def main():
    l1=[1,2,44,5,1,2]
    func(l1)

if __name__ == "__main__":
    main()"""

#9-------prime or not
"""
def func(no):
    flag=1
    if no==1:
        print("not prime")
    elif no>1:
        for i in range(2,no):
            if no%i==0:
                flag=0
        if flag==0:
            print("not")
        else:
            print("yes")

def main():
    no=int(input("enetr no="))
    func(no)

if __name__ == "__main__":
    main()"""


# string is palindrom or not
"""
def func(str1):

    l1=list(str1)
    l2=list(str1)
    t=0
    s=0
    e=len(l1)-1

    while s<e:
        t=l1[s]
        l1[s]=l1[e]
        l1[e]=t

        s=s+1
        e=e-1

    if l1==l2:
        print("yes")
    else:
        print("no")




def main():
    str1=str(input("enetr str="))
    func(str1)

if __name__ == "__main__":
    main()"""


 #----panagram or not
"""
def func(str1):
    str2=(str1.lower())
    alpha=("abcdefghijklmnopqrstuvwxyz")
    for i in alpha:
        if i not in str2:
            return 1


def main():
    str1=str(input("enetr str="))
    x=func(str1)
    if x==1:
        print("not")
    else:
        print("yes")

if __name__ == "__main__":
    main()"""

#----
def fun(str1):
    str2=str1.maketrans(" ","- ")
    for i in sorted(str2):
        print(i,end=" ")
def main():
    str1="green-red-yellow-black-white"
    fun(str1)

if __name__ == "__main__":
    main()
