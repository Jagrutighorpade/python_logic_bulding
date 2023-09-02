 #-------1-----
#factorial
#with recursion
"""
i=1
mul=1
def fact(no):
    global i
    global mul
    if (i<=no):
        mul=mul*i
        i=i+1
        fact(no)
    return mul
def main():
    no=int(input("enter no="))
    print(fact(no))

if  __name__=="__main__":
    main()"""

#without recursion
"""
def fact(no):
    mul=1
    for i in range(1,no+1):
        mul=mul*i
    print(mul)
def main():
    no=int(input("enter no="))
    fact(no)
if  __name__=="__main__":
    main()"""

#------------2-------
#amstrong
"""
def amst(no):
    no1=no
    no2=no
    len1=0
    sum=0
    flag=0

    while no!=0:
        r=no%10
        len1=len1+1
        no=no//10

    while no1!=0:
        r1=no1%10
        sum=sum+(r1**len1)
        no1=no1//10

    if no2==sum:
        flag=1
    if flag==1:
        print("its a amstrong num")
    else:
        print("its not amstrong num")

def main():
    no=int(input("enter no="))
    amst(no)
if  __name__=="__main__":
    main()"""

#prime no
"""
def prim(no):
    flag=0
    if no==1:
        print("its not a prime no")
    elif no>1:
        for i in range(2,no):
            if no%i==0:
                flag=1
        if flag==1:
            print("its  not a prime num")
        else:
            print("its a prime")

def main():
    no=int(input("enter no="))
    prim(no)
if  __name__=="__main__":
    main()"""

#fibonacci
"""
def fibo(no):
    temp=0
    a=0
    b=1
    for i in range(no):
        temp=a+b
        a=b
        b=temp
        print(temp)
def main():
    no=int(input("enter no="))
    fibo(no)
if  __name__=="__main__":
    main()"""

#sum of array
#1 for loop
"""
def sum():
    l1=[1,2,3,4,5]
    sum=0
    for i in l1:
        sum=sum+i
    print("sum=" ,sum)

def main():
    sum()

if  __name__=="__main__":
    main()"""


#2 while loop
"""
def sum1():
    l1 = [1, 2, 3, 4, 5]
    i=0
    sum = 0
    while i<len(l1):
        sum+=l1[i]
        i=i+1
    return sum

def main():
     print("sum=",sum1())

if __name__ == "__main__":
     main()"""

#3 lambda
"""
from  functools import reduce
def sum1():
    l1 = [1, 2, 3, 4, 5]
    add= reduce(lambda  x,y : x+y  , l1)
    return add

def main():
     print("sum=",sum1())

if __name__ == "__main__":
     main()"""

#4 recusion
"""
i=0
sum=0
def sum1():
    l1 = [1, 2, 3, 4, 5]
    global sum
    global i

    if i< len(l1):
        sum=sum+l1[i]
        i=i+1
        sum1()
    return sum

def main():
     print("sum=",sum1())

if __name__ == "__main__":
     main()"""

#largest element in array
"""
def larg():
    l1=[22,66,12,5,72,33]
    max=0
    for i in l1:
        if i>max:
            max=i
    return max
def main():
     print("larger no of array=", larg())

if __name__ == "__main__":
     main()"""

#array rotation


#reverse array
"""
def rev():
    l1 = [1,2,3,4,5,6]
    temp=0
    start_idx=0
    end_idx=len(l1)-1

    while ( start_idx  < end_idx ):
         temp=l1[start_idx]
         l1[start_idx]=l1[end_idx]
         l1[end_idx]=temp

         start_idx=start_idx + 1
         end_idx=end_idx - 1

    print(l1)

def main():
     rev()

if __name__ == "__main__":
     main()"""


# start part shifted to the end
"""
def rev():
    l1 = [1,2,3,4,5,6]
    len1=len(l1)
    step=2
    for i in range(0,step):
        x=l1[0]
        for j in range(0,len1-1):
            l1[j]=l1[j+1]
        l1[len1-1]=x

    print(l1)

def main():
     rev()

if __name__ == "__main__":
     main()"""

# reminder of array
"""
def rem(no):
    l1 = [7,1,9]
    mul=1
    for i in l1:
        mul=mul*i  
    r=mul%no

    print("reminder=",(r))

def main():
     no=int(input("enter no ="))
     rem(no)

if __name__ == "__main__":
     main()"""



#interchange element (lst -1st)
"""
def rot():
     l1 = [1,2,3,4,5,6,7,8,9]
     print("orignal array=", l1)

     l1[0], l1[-1] = l1[-1], l1[0]
     print("rotated array=", l1)


def main():
     rot()


if __name__ == "__main__":
     main()"""

# swapping elem
"""
def rot():
     l1 = [22, 66, 12, 5, 72, 33]
     print("orignal array=",l1)
 
     l1[1],l1[4]=l1[4],l1[1]
     print("rotated array=",l1)
 
def main():
       rot()
 
if __name__ == "__main__":
      main()"""


 #remove nth char
"""
def rem(str1,no):
    l1=list(str1)
    for i in range(len(l1)-1):
        if i!=no:
            print(l1[i],end="")

def main():
    str1=str(input("enter name="))
    no=int(input("enter index no="))
    rem(str1,no)

if __name__ == "__main__":
     main()"""

# 14 --find length
"""
def length():
    l1=[1,2,3,4,5]
    len1=0
    for i in l1:
        len1=len1+1
    print("length=",len1)

def main():
    length()

if __name__ == "__main__":
     main()"""

#15--check elemnt exists in list
"""
def chk(no):
    l1=[22,33,56,88,10]
    flag=0
    
    for i in l1:
        if i==no:
            flag=1
            
    if flag==1:
        print("element is present ")
    else:
        print("element is  not present ")

def main():
    no=int(input("enter no="))
    chk(no)

if __name__ == "__main__":
     main()"""

#16---clear list
"""
def clr():
    l1=[1,2,3,4,5]

    #del l1[::]
    #l1.clear()
    #l1=[]
    
    while (len(l1)!=0):
        l1.pop()
        
    print(l1)
def main():
        clr()

if __name__ == "__main__":
     main()"""

#17 reverse reverse
"""
def rev():
    l1=[1, 5, "l", 22,  11.3, "z"]
    print("orignal list=",l1)
    
    # l1[::-1]
    
    temp=0
    start_idx=0
    end_idx=len(l1)-1

    while ( start_idx < end_idx):
        temp=l1[start_idx]
        l1[start_idx]=l1[end_idx]
        l1[end_idx] =temp

        start_idx=start_idx+1
        end_idx=end_idx-1

    print("reverselist=",l1)

def main():
     rev()

if __name__ == "__main__":
     main()"""

#18 cloning or copying list
"""
import copy
def cpy():

    l1=[1,2,3,4,5]
    
    #l2=l1
    #l2=l1.copy()
    #l2=copy.copy(l1)
    l2=copy.deepcopy(l1)
    
    print("l1=",l1)
    print("l2=",l2)

def main():
     cpy()

if __name__ == "__main__":
     main()"""

#19--count occurance of element
"""
def occ(no):
    l1=[1,2,3,1,2,3,4,5,3,6,4,4]
    count=0

    for i in l1:
        if i==no:
            count=count+1
    print(no,"=>","count=",count)

def main():
    no= int(input("enter no="))
    occ(no)

if __name__ == "__main__":
     main()"""

#20----sum of list ele
"""
def add():
    l1=[1,2,3,4,5,6]
    sum=0
    for i in l1:
        sum=sum+i
    print("sum=",sum)
def main():
    add()

if __name__ == "__main__":
     main()"""

#21--mul  of list ele
"""
def multi():
    l1=[1,2,3,4,5,6]
    mul=1
    for i in l1:
        mul=mul*i
    print("sum=",mul)
def main():
    multi()

if __name__ == "__main__":
     main()"""

# 22 ---smallest ele in list
"""
def small():
    l1=[11,2,3,4,5,6]
    min=9
    for i in l1:
        if i<min:
            min=i
    print(min)


def main():
    small()

if __name__ == "__main__":
     main()"""

# 23---largest no
"""
def larg():
    l1=[11,2,3,4,5,6]
    max=0
    for i in l1:
        if i>max:
            max=i
    print(max)

def main():
    larg()

if __name__ == "__main__":
     main()"""

#24---2nd largest no,----(disending )
"""
def larg_2():

    l1=[1,2,3,4,5,6]
    temp=0
    
    for i in range(0,len(l1)):
        for j in range(i+1,len(l1)):
            if l1[i]<l1[j]:
                temp=l1[i]
                l1[i]=l1[j]
                l1[j]=temp
    print(  "2nd largest no=",l1[1])

def main():
    larg_2()

if __name__ == "__main__":
     main()"""


#25 ---even no
"""
def eve():
     l1 = [1, 2, 3, 4, 5, 6,7,8,9]
     print("even no=")
     for i in l1:
         if i%2==0:
             print(i,end=" ")

def main():
     eve()


if __name__ == "__main__":
     main()"""


#26---odd
"""
def odd():
     l1 = [1, 2, 3, 4, 5, 6,7,8,9]
     print("odd no=")
     for i in l1:
         if i%2==1:
             print(i,end=" ")

def main():
     odd()


if __name__ == "__main__":
     main()"""

#27---even no in range
"""
def eve(no):
    print("even no=")
    for i in range(no):
         if i%2==0:
             print(i,end=" ")

def main():
    no=int(input("enter  range="))
    eve(no)


if __name__ == "__main__":
     main()"""




#28---odd no in range
"""
def  odd(no):
    print("odd no=")
    for i in range(no):
         if i%2==1:
             print(i,end=" ")

def main():
    no=int(input("enter  range="))
    odd(no)

if __name__ == "__main__":
     main()"""

#29---count even -odd no in list
"""
def count():
     l1 = [1, 2, 3, 4, 5, 6,7,8,9]
     c1=0
     c2=0
     for i in l1:
         if i%2==0:
             c1=c1+1
         else:
             c2=c2+1
     print("even no count=",c1)
     print("odd no count=", c2)

def main():
     count()


if __name__ == "__main__":
     main()"""

#30---print positive no in list
"""
def pstv():
     l1 = [1, -2, 3, -4, 5, 6,-7,8,-9]
     for i in l1:
         if i>0:
             print(i,end=" ")

def main():
     pstv()


if __name__ == "__main__":
     main()"""

#31---negative no in list
"""
def  ngtv():
     l1 = [1, -2, 3, -4, 5, 6,-7,8,-9]
     for i in l1:
         if i<0:
             print(i,end=" , ")

def main():
     ngtv()

if __name__ == "__main__":
     main()"""



#32---print positive no in range
"""
def pstv(no1,no2):
     for i in range(no1,no2):
         if i>0:
             print(i,end=" ,  ")

def main():
    no1=int(input("enter negative range="))
    no2=int(input("enter positive range="))

    pstv(no1,no2)


if __name__ == "__main__":
     main()"""



#33---print  negative no in range
"""
def  ngtv(no1,no2):
     for i in range(no1,no2):
         if i<0:
             print(i,end=" , ")

def main():
    no1=int(input("enter negative range="))
    no2=int(input("enter positive range="))

    ngtv(no1,no2)


if __name__ == "__main__":
     main()"""


#34--- count postive and negative no in list
#
# def count1(no1,no2):
#     c1=0
#     c2=0
#
#     while no1<no2:
#         if no1<0:
#             c1=c1+1
#         no1+=1
#     else:
#         c2=c2+1
#
#     no1=no1+1
#
#     print("negativetive no in range = ", c1)
#     print("postive no in range = ",c2)
"""
def  count(no1,no2):

    c3=0
    c4=0

    for i in range(no1,no2):
         if i<0:
             c3=c3+1
         else:
             c4=c4+1

    print("negativetive1 no in range = ", c3)
    print("postive1 no in range = ",c4)

def main():
    no1=int(input("enter negative range="))
    no2=int(input("enter positive range="))

    count(no1,no2)
    #(no1,no2)

if __name__ == "__main__":
     main()"""

#35---remove multiple elemnt from  list
"""
def rmov(no):
    l1=[10,20,30,40,50,60]
    for i in range(0,no):
        #l1.pop(i)
       # l1[i]
        l1.remove(l1[i])

    print(l1)


def main():
    no=int(input("how many elem u want remove="))

    rmov(no)

if __name__ == "__main__":
     main()"""

#36---remove empty tuple from list
"""
def rmov():
    l1=[(10,20),(30),(),40,50,(),60]
    for i in l1:
        if i!=():
            print(i,end=" ,")
def main():

    rmov()

if __name__ == "__main__":
     main()"""

# 37-----duplicate elemnt in list
"""
def dub():
    l1=[1,2,3,1,4,5,4,6,7,9]
    Ndub=[]
    dub=[]

    for i in l1:
        if i not in Ndub:
            Ndub.append(i)
        else:
            dub.append(i)
            
    print("orginal=",l1)
    print("dube=",dub)
    print("Notdube=",Ndub)

def main():

    dub()

if __name__ == "__main__":
     main()"""

#38--cumulative sum
"""
def add():
    l1=[1,2,3,4,5,6]
    l2=[]
    sum=0
    for i in l1:
        sum=sum+i
        l2.append(sum)
    print("orignal list=",l1)
    print("sum list =",l2)
def main():
    add()

if __name__ == "__main__":
     main()"""

#39

#40----pallindrom
"""
def palin():
    str1= str(input("enter name="))
    
    l1=list(str1)
    l2=list(str1)

    temp=0
    s_i=0
    e_i=len(l2)-1

    flag=0

    while (s_i < e_i) :
        temp=l2[s_i]
        l2[s_i]=l2[e_i]
        l2[e_i]=temp

        s_i=s_i+1
        e_i=e_i-1

    if l1==l2:
        flag=1
    if flag==1:
        print("Its a pallindrom")
    else:
        print("its not pallindrom")

def main():
    palin()

if __name__ == "__main__":
     main()"""

# 41----remove i'th  char in string
"""
def rem(str1,no):
    l1=list(str1)
    for i in range(len(l1)):
        if i!=no:
            print(l1[i],end="")

def main():
    str1=str(input("enter string="))
    no=int(input("enter no="))
    rem(str1,no)

if __name__ == "__main__":
     main()"""

#42---
"""
# 1---find substring is present in given string
#1
def subs(str1,str2):
    flag=0
    if str2 not in str1:
        flag=1

    if flag==1:
        print("sub string is NOT present in main string")
    else:
        print("sub string is Present in main string")

#2 comp
    ans=["yes" if str2 in str1 else "no"]
    print(ans)

# using find
    if (str1.find(str2)==-1):
        print("NO")
    else:
        print("YES")


#.....find lenght of string
def length(str1):
    c=0
    for i in str1:
        c=c+1
    print("lenght of str1=",c)

def main():
    str1=str(input("enter main string="))
    str2=str(input("enter sub string ="))
    subs(str1,str2)
    length(str1)


if __name__ == "__main__":
     main()"""


# 43---even length word
"""
def  eve_len(str1):

    s=str1.split(" ")
    for i in s:
        if len(i)%2==0:
            print(i,end=" , ")

#using lambda
    l=list(filter(lambda x: len(x)%2==0 ,s))
    print(l)

#list  comp
    print([i   for i in s    if len(i)%2==0 ])

def main():
    str1=str(input("enter main string="))
    eve_len(str1)


if __name__ == "__main__":
     main()"""


#44--
"""
def chk_v(str1):
    vowel="AEIOUaeiou"
    
    if vowel not  in str1:
        print("cant accept string")

    else:
        print("string accepted=", str1 )


def main():
    str1=str(input("enter main string="))
    chk_v(str1)


if __name__ == "__main__":
     main()"""

#45-----  count common char in two string
"""
def chk(str1,str2):
    s1=set(str1)
    s2=set(str2)
    s3=s1 & s2
    print("common char =",len(s3))
def main():
    str1=str(input("enter string="))
    str2=str(input("enter string="))

    chk(str1,str2)


if __name__ == "__main__":
     main()"""

#46----count no vowel and remove dublicate
"""
#vowel count
def chk(str1):
    vowel={"a","u","i","e","o"}
    c=0
    for i in str1:
        if i in vowel:
            c=c+1
    print("count of vowel=",c)

#remove dublicate
def dub(str1):
    l1=[]
    for i in str1:
        if i not in l1:
            l1.append(i)
    for j in l1:
        print(j,end="")

def main():
    str1=str(input("enter main string="))

    chk(str1)
    dub(str1)


if __name__ == "__main__":
     main()"""

#49----split and join string
"""
def split_1(str1):
    str2=str1.split()
    print(str2)

def join_2():
    l1=["aassbb","agsgx","hsya"]
    str3= " @  ".join(l1)
    print(str3)

def main():
    str1=str(input("enter main string="))

    split_1(str1)
    join_2()


if __name__ == "__main__":
     main()"""

#50--- string binary or not
"""
def chk(str1):
    s=set(str1)
    b={"0","1"}
    flag=0

    if  s==b  or  s=={"0"} or s=={"1"}:
        flag=1

    if flag==1:
        print("its  a binary string")
    else:
        print("its not  a binary string")


def main():
    str1=str(input("enter main string="))

    chk(str1)


if __name__ == "__main__":
     main()"""

#51----close match
"""
from  difflib import get_close_matches

def chk(word):
    l1=["apple","banana","berry","papaya","orange"]
    match=get_close_matches(word,l1)
    print(match)

def main():
    word=str(input("enter word="))

    chk(word)

if __name__ == "__main__":
     main()"""

#52---uncommon word from two string
"""
def chk(str1,str2):
    s1=str1.split()
    s2=str2.split()
    l1=[]
    for i in s1:
        if i not in s2:
            l1.append(i)
    for j in s2:
        if j not in s1:
            l1.append(j)
    print(list(set(l1)))


def main():
    str1=str(input("enter string1 ="))
    str2=str(input("enter string2 ="))

    chk(str1,str2)


if __name__ == "__main__":
     main()"""


#53----swap commas and dot
"""
def swap(str1):
    str2=str1.maketrans(". ,"  , ", .")
    print(str1.translate(str2))

def main():
    str1=str(input("enter string1 ="))
    swap(str1)

if __name__ == "__main__":
     main()"""

#54----permutation
"""
from itertools import permutations
def permu(str1):
    A=permutations(str1)
    for perm in list(A):
        print("".join(perm))
def main():
    str1=str(input("enter string1 ="))
    permu(str1)

if __name__ == "__main__":
     main()"""

#55


 # 56--string slicing rotate
"""
def rot(s,d):
    L=s[0 : d]
    l=s[d : ]

    R=s[0 : len(s)-d]
    r=s[len(s)-d  : ]

    print("left=",(l+L))
    print("right=",(r+R))

def main():
    str1="studytonight"
    d=4
    rot(str1,d)

if __name__ == "__main__":
     main()"""

#57----

#58---dublicate element in dict format
"""
def dub(str1):
    d1={}
    for i in str1:
        if i in d1:
            d1[i]=d1[i]+1
        else:
            d1[i]=1
    print(d1)
def main():
    str1=str(input("enter string1 ="))
    dub(str1)
if __name__ == "__main__":
     main()"""

#59----sort dict key or val----handling missing key
"""
#key sort
def sort_k(d1):
    #1
    d2= sorted(d1.items())
    print(d2)

    #2
    d3=sorted(d1.items() ,key=lambda x: x[0])
    print(d3)

    #3
    for i in sorted(d1.keys()):
        print({i: d1[i]},end=" ")

#value sort
def sort_v(d1):
    #1
    print("\r")
    d4=sorted(d1.items() ,key=lambda x: x[1])
    print("d4=",d4)

    #3
    for i in sorted(d1.values()):
        print(i,end=",")

#missing value
def miss(d1):
    print("\r")
    #1--setdefault()
    m1=d1.setdefault("ram",12)
    print("m1 missing value=",m1)

    m2=d1.setdefault("sita",12)
    print("m2 missing value=",m2)

    #2 get()

    m3=d1.get("ram",13)
    print("m3 missing value=",m3)

    m4=d1.setdefault("minu",14)
    print("m4 missing value=",m4)

    #3 slicing
    print(d1["sita"])

    d1["gita"]=8
    print(d1["gita"])

    print((d1))

    #3 get


def main():

    d1={"ram":11 ,  "sham":9,   "pooja":15,  "rahul":12}

    sort_k(d1)
    sort_v(d1)
    miss(d1)
if __name__ == "__main__":
     main()"""



#60--- key having multiple input
"""
def  mult(a,b,c):
    d1={}
    d1["a+b+c"]=[a+b+c ,a+b-c]
    print(d1)

def main():
    a, b , c = 2 , 3 ,4
    mult(a,b,c)

if __name__ == "__main__":
     main()"""

#61------sum of all items
"""
from functools import reduce
def sum_item():
    d1={"ram":11 ,  "sham":9,   "pooja":15,  "rahul":12}
    sum=0
    for i in d1.values():
         sum=sum+i
    print(sum)

    add=reduce(lambda x,y: x+d1[y],d1,0)
    print(add)
def main():
    sum_item()

if __name__ == "__main__":
     main()"""

#62------remove key .....
"""
#remove key
def rmv():
    d1={"ram":11 ,  "sham":9,   "pooja":15,  "rahul":12}

    del d1["ram"]
    print(d1)

    d1.pop("sham")
    print(d1)

    d1.popitem()
    print(d1)

 
 def main():
     rmv()


 if __name__ == "__main__":
     main()
 """


#63---- sort list of dict
"""
from operator import itemgetter
def sort_v():
     Ld = [{"name": "pooja", "age": 14},
           {"name": "gita", "age": 19},
           {"name": "sita", "age": 1}]

    #lambda
     d2 = sorted(Ld, key=lambda x: x["name"])
     print("L sorted by name=", d2)

     d3 = sorted(Ld, key=lambda x: x["age"])
     print("L sorted by age=", d3)

    #itemgetter
     d4= sorted(Ld, key= itemgetter("age"))
     print("i sorted by age=",d4)

     d5= sorted(Ld, key= itemgetter("name"))
     print("i sorted by name=",d5)



def main():
     sort_v()


if __name__ == "__main__":
     main()"""


#64---marging two dict create grade calculator
"""
def grd_c():
     girls={"pooja":75  ,  "sita":85, "gita":66 ,"aati":56}
     boys={"rahul ":95  ,  "sita":39, "gita":80 ,"aati":78}
     marks={**girls,**boys}
     print(marks)
     for k,m in  (marks.items()):
         if m>90 :
             print(k,"is pass with A+ grade",m)
         elif m>=80 and m<90:
             print( k,"is pass with b+ grade",m)
         elif m >=70 and m <= 80:
             print(k, " is pass with c+ grade",m)
         elif m >= 60 and m <=70:
             print( k," is pass with d+ grade",m)
         elif m >=50 and m <= 60:
             print( k,"is PASS",m)
         else:
             print(k, " is  FAIL ",m)


def main():
     grd_c()


if __name__ == "__main__":
     main()"""

# 65---orderdict()
"""
from collections import OrderedDict
def ord():
    str1= "engineers rocks"
    str2="er"
    d1=OrderedDict.fromkeys(str1)
    i=0
    for k,v in d1.items():
        if (k == str2[i]):
            i=i+1
        if (i == (len(str2))):
                return "True"
    return "False"
def main():
     print(ord())


if __name__ == "__main__":
     main()"""

#66------
#67---remove dublicate words
"""
def dub():
    str1=" happy happy new year year 2023"
    str2=str1.split()
    l1=[]
    for i in str2:
        if i not in l1:
            l1.append(i)
    for j in l1:
        print(j,end=" ")
def main():
     dub()

if __name__ == "__main__":
     main()"""

#69 list of tuple in dict
def conv():
    l1=[("a",10),  ("b",20) ,  ("c",30) ,  ("d",40)]

    d1=dict(l1)
    print(d1)

    d2={l1[i][0]:l1[i][1]  for i in range(len(l1))}
    print(d2)
def main():
     conv()

if __name__ == "__main__":
     main()
















