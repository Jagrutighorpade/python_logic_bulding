"""
#----1
def rev(s):
    #1
    for i in range(len(s)-1,-1,-1):
        print(s[i],end="")

    print("\n")
    #2
    s1=s[::-1]
    print(s1)

def main():
    s="hello how are you"

    rev(s)
if __name__=="__main__":
    main()"""


#---2
"""
def lis(l1):
    l2=[ j     for i in l1     for j in i   ]
    print(l2)

def main():
    l1=[{'a':0,"b":0} ,{"c":0},{"d":0}]
    lis(l1)
if __name__=="__main__":
    main()"""


#-----3----yes
"""
s="[{)}]"
print(type(s))"""

#----4
"""
def cub(l1):
    #1
    l2=[i**3 for i in l1]
    print(l2)

    #2
    d1={i:i**3 for i in l1}
    print(d1)

def main():
    l1=[1,2,3,4,5,6,7,8,9,10]
    cub(l1)
if __name__=="__main__":
    main()"""


#---5
"""
def srt(A):
    t=0
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i]>A[j]:
                t=A[i]
                A[i]=A[j]
                A[j]=t
    print(A)

def main():
    A=[0,1,0,1,0,0,1,1,1,0]
    srt(A)
if __name__=="__main__":
    main()"""


#6


#7
"""
def eve(l1):
    l2=[]
    for i in l1:
        c=0
        for j in str(i):
            if int(j)%2==0:
                c=c+1
        if c==2:
            l2.append(i)
    print(l2)

def main():
    l1=[11,22,32,54,96,68,42]
    eve(l1)
if __name__=="__main__":
    main()"""

#8
"""
def fun(l1,no):
    l2=[]
    for  i in range(1,no+1):
        for j in l1:
            l2.append(j+str(i))
    print(l2)
def main():
    l1=["p","q"]
    no=5
    fun(l1,no)
if __name__=="__main__":
    main()"""

#9
"""
def rmv_dub(l1):
    t=0
    #sort
    for i in range(len(l1)):
        for j in range(i+1,len(l1)):
            if l1[i]>l1[j]:
                t=l1[i]
                l1[i]=l1[j]
                l1[j]=t

    #remove
    for i in range(len(l1)-1):
        for j in range(i+1,len(l1)-1):
            if l1[i]==l1[j]:
                l1.remove(l1[j])
    print(l1,id(l1))


def main():
    l1=[10,20,30,10,20]
    print(l1 ,id(l1))
    rmv_dub(l1)
if __name__=="__main__":
    main()"""

#10
"""
def main():
#1
    l1=[["Gfg","good"],["is","for"]]
    l2=[]
    for i in range(len(l1)-1):
        for  j in range(len(l1[i])):
            l2.append(l1[i][j]+l1[i+1][j] )
    print(l2)


#2
    # l3=list(l1[0])
    # l4=list(l1[1])
    # l5=[]
    #
    # for i,j in zip(l3,l4):
    #     l5.append(i+j)
    # print(l5)

if __name__=="__main__":
    main()"""


#11
"""
def fun(l1):
    l2=[]
    l3=[]
    for i in range(2,len(l1)):
    #     if i>=2:
    #         l2.append(l1[i])
    #     else:
    #         l3.append(l1[i])
    # print(l2+l3)

        l2.append(l1[i])
    print(l2)
def main():
    l1=[5,6,5,7,8,3]
    fun(l1)
if __name__=="__main__":
    main()"""

#12
"""
def main():
    no=10

if __name__=="__main__":
    main()"""



#13
"""
def  fun(no1,no2):
    for i in range(no1):
        for j in range(no2):
            print("*",end="  ")
        print("")
def main():
    no1=3
    no2=7
    fun(no1,no2)
if __name__=="__main__":
    main()"""

#14
"""
print(True+True) #2"""

#15
"""
def fun(l1):
    i=0
    max=0
    index1=0
    while i<len(l1):
        len(l1[i])>max
        max=len(l1[i])
        index1=i
        i=i+1
    print("max string=   ",l1[index1])

def main():
    l1=["apple" ,"banana","cherry","durian","elderberry"]
    fun(l1)
if __name__=="__main__":
    main()"""

#16
"""
def fun(main):
    def inner():
        try:
            a=main()
            b=10/a
        except ZeroDivisionError:
            print("ZeroDivisionError ")
        else:
            print(b)
    return inner()

def main():
    num=int(input("enter no= "))
    return num
result=fun(main)"""



#17
"""
class Table:
    def table_of(no):
        for i in range(1,11):
            print(no*i)
def main():
    no= int(input("enter no="))
    obj=Table
    obj.table_of(no)
if __name__=="__main__":
    main()"""


#18
"""
def main():
    #1
    with open(r"jag.txt","r") as f1:
        len1=len(f1.readline())
        print(len1)

    # #2
    # c=0
    # for i ,j in enumerate(f1):
    #     c=c+i
    #     print(c,end="")
if __name__=="__main__":
    main()"""

#19
'''
def fun(l1):
    l2=list(map(lambda x: {x: x*x,}, l1 ))
    print(l2)
def main():
    l1=[1,2,3,4]
    fun(l1)
if __name__=="__main__":
    main()'''

#20
"""
def gen(n):
    for i in range(1,n):
        yield i**2
def main():
    a=iter(gen(10))
    for j in a:
        print(j)
if __name__=="__main__":
    main()"""


#-----------------pravingiram,akash-------

#1
"""
def find_M(l1):
    max=0
    for i in l1:
        if i>max:
            max=i
    print(max)

def find_S(l1):
    min=9
    for i in l1:
        if i<min:
            min=i
    print(min)

def main():
    l1=[11,44,7,22,10,380,34]
    find_S(l1)
    find_M(l1)
if __name__=="__main__":
    main()"""

#2
"""
def calculator(no1,no2):
    print()
def main():
    no1=float(input("enter no="))
    no2=float(input("enter no="))
    calulator(no1,no2)

if __name__=="__main__":
    main()"""

#3
"""
def srt(l1):
    temp=0
    for i in range(len(l1)):
        for j in range(i+1,len(l1)):
            if l1[i]<l1[j]:
                temp=l1[i]
                l1[i]=l1[j]
                l1[j]=temp
    print(l1, "\n","2nd largest no=",l1[1])

def main():
    l1=[5,2,7,8,1,3,8,9,13]
    srt(l1)
if __name__=="__main__":
    main()"""


#5
"""
def rev(l1):
    #1
    l2=[l1[i] for i in range(len(l1)-1,-1,-1)]
    print(l2)

    #2
    temp=0
    si=0
    ei=len(l1)-1
    while si<ei:
        temp=l1[si]
        l1[si]=l1[ei]
        l1[ei]=temp

        si=si+1
        ei=ei-1
    print(l1)

def main():
    l1=[5,2,7,8,1,3,8,9,13]
    print(l1)
    rev(l1)
if __name__=="__main__":
    main()"""


#6
"""
def cnt(str1):
    srt1=list(str1)
    c1=0
    c2=0
    c3=0
    for i in str1:
        if i=="k":
            c1=c1+1
        elif i=="a":
            c2=c2+1
        elif i=="r":
            c3=c3+1

    print({"k":c1 ,"a":c2,"r":c3})

def main():
    str1="kaarthik"
    cnt(str1)
if __name__=="__main__":
    main()"""

#7
"""
def rev(str1):
    # l1=str1.split()
    # for i in range(len(l1)-1,-1,-1):
    #     print(l1[i],end=" ")


    word=" "
    rev=" "
    for i in str1:
        if ( i  !=" "):
            word=word+i
        else:
            rev=word+" "+rev
            word=" "
    print(rev)

def main():
    str1="my name is pravin"
    rev(str1+" ")
if __name__=="__main__":
    main()"""


#8
"""
def ptrn(no1):
    for i in range(1,no1):
        for j in range(1,i):
            print(j,end="  ")
        print("  ")

def main():
    no1=7
    ptrn(no1)
if __name__=="__main__":
    main()"""

#9
"""
def cnt(str1):
    d1={}
    for i in str1:
        if i in d1:
            d1[i]=d1[i]+1
        else:
            d1[i]=1
    for i,j in d1.items():
        print(str(j)+i , end="")

def main():
    str1="abaaabbcdd"
    cnt(str1)
if __name__=="__main__":
    main()"""

#10
"""
def main():
    l1=[1,2,4,6,7,9]
    l2=[]
    for i in range(1,10):
        if i not in l1:
            l2.append(i)

    min=9
    for x in l2:

        if x < min:
            min=x
    print(min)
if __name__=="__main__":
    main()"""

#11
"""
def cmn(l1,l2):
    #1
    l3=[]
    for i in l1:
        for j in l2:
            if i==j:
                l3.append(j)
    print(l3)

    #2
    s1=set(l1)
    s2=set(l2)
    s3=s1.intersection(s2)
    print(list(s3))

def main():
    l1=[1,2,3,4]
    l2=[2,4,8,9]
    cmn(l1,l2)
if __name__=="__main__":
    main()"""


#12
"""
def srt(l1):
    temp=0
    for i in range(len(l1)):
        for j in range(i+1,len(l1)):
            if len(l1[i])>len(l1[j]):
                temp=l1[i]
                l1[i]=l1[j]
                l1[j]=temp
    print(l1)

def main():
    l1=["apple","banana","orange","pear"]
    srt(l1)
if __name__=="__main__":
    main()"""




#calculator
"""
def main():
    while (True):
        print("1) Press 1 for Addition ")
        print("2) Press 2 for Substracrion ")
        print("3) Press 3 for Multiplication ")
        print("4) Press 4 for Division ")
        print("5) Press 5 for  even ")
        print("6) Press 6 for  Square ")
        print("7)Press 7 for Cube ")
        print("8 Press 8 for pllindrom ")
        print("9) EXIT")

        choice=int(input("enetr your choice = "))

        if  choice==1:
            l1 = []
            sum = 0
            no1=int(input("enter how many nunber you want add = "))
            for i in range(no1):
                l1.append(float(input("enetr no=")))
            for j in l1:
                sum=sum+j
            print("sum=",sum)

        elif choice==2:
            no1=float(input("enter 1st no="))
            no2=float(input("enter 2st no="))
            print("sub=",no1-no2)

        elif choice==3:
            l2=[]
            mul=1
            no1=int(input("enter how many nunber you want mul = "))
            for i in range(no1):
                l2.append(float(input("enetr no=")))
            for j in l2:
                mul=mul*j
            print("mul=",mul)


        elif choice==4:
            no1=float(input("enter 1st no="))
            no2=float(input("enter 2st no="))
            print("div=",no1/no2)

        elif choice==5:
            no1=float(input("enter no ="))
            if no1%2==0:
                print("it is even")
            else:
                print("its odd ")

        elif choice==6:
            no1=float(input("enter no ="))
            print("square=",no1**2)

        elif choice==7:
            no1=float(input("enter no ="))
            print("square=",no1**3)

        elif choice==8:
            no1=float(input("enter big no ="))
            no2=no1
            p=0
            while no1 !=0:
                r=no1%10
                p=p*10+r
                no1=no1//10
            if no2==p:
                print("its pallindrome ")
            else:
                print("its not pallindrome")





        elif choice==9:
            print("Thank for using calculator")
            return
        else:
            print("----Invlid Input-----")



if __name__=="__main__":
    main()"""


#13
"""
def func(d):
    for i ,j in d.items():
        c=0
        for k in  j:
            c=c+k
        if c==9:
            print(i,end=",")

def main():
    d={"a":[2,3,4],"b":[2,4,5,6],"c":[2,3,4],"d":[9],"e":[1,3,5]}
    func(d)



if __name__=="__main__":
    main()"""


#sort
"""
def srt(l1):
    t=0
    for i in range(len(l1)):
        for j in range(0 ,len(l1)-1-i):
            if l1[j]>l1[j+1]:
                temp=l1[j]
                l1[j]=l1[j+1]
                l1[j+1]=temp
    print(l1)


def main():
        l1=[9,8,3,5,6,2]
        srt(l1)

if __name__ == "__main__":
    main()"""


#extra
"""
def func(l1):
    icnt1=0
    icnt2=0
    icnt3=0
    icnt4=0
    icnt5 = 0
    icnt6 =0
    f=0
    for i in l1:
        if i=="(":
            icnt1+=1
        elif i ==")":
            icnt2+=1
        elif i =="[":
            icnt3+=1
        elif i =="]":
            icnt4+=1
        elif i =="{":
            icnt5+=1
        elif i =="}":
            icnt6+=1
    if icnt1==icnt2 and icnt3==icnt4 and icnt5==icnt6:
        print("yes brackets are balanecd")
    else:
        print("no")


def main():
    l1=input("enter expression = ")
    func(l1)

if __name__ == "__main__":
    main()"""


#14
"""
def func(l1,no):
    c=0
    for i in range(len(l1)):
        for j in range(i+1,len(l1)):
            c=l1[i]+l1[j]
            if no==c:
                print(i,j)


def main():
    l1=[2,10,30,40]
    no=int(input("enetr no= "))
    func(l1,no)

if __name__ == "__main__":
    main()"""

#8
"""
i = 0
max = 0
def rcr(l1):
    global i
    global max
    if i<len(l1):
        if l1[i] >max:
            max=l1[i]

        i=i+1
        rcr(l1)
    return max

def main():
    l1=[-1,3,5,6,99,12,2]
    print( rcr(l1))

if __name__ == "__main__":
    main()"""

#5
"""
def fun(l1):
    for j in l1:
        # for i in range(1,27):
        #     if ord(j)==96+i:
        #         print(i,end=" ")
        # for k in range(27,53):
        #     if ord(j)==38+k:
        #          print(k,end=" ")


        if ord(j)>=ord("a") and ord(j)<=ord("z"):
            print(ord(j)-70,end=" ,")
        elif ord(j)>=ord("A") and ord(j)<=ord("Z"):
            print(ord(j)-64,end=" , ")


def main():
    l1=["A","p","l","r","P","m","a"]
    fun(l1)

if __name__ == "__main__":
    main()"""


#
"""
def fun(str1):
    l1=list(str1)
    si=0
    ei=len(l1)-1
    while si<ei:
        if l1[si]==l1[ei]:
            print(l1[si])
        si=si+1
        ei=ei-1

def main():
    str1="formadammadamfor"
    fun(str1)

if __name__ == "__main__":
    main()"""


#
"""
def fun(l1):
    l2=[]
    min=9
    for i in l1:
        l2.append(len(i))
    for j in l2:
        if j<min:
            min=j

    for i in range(min):
        if l1[0][i]==l1[1][i]==l1[2][i]:
            print(l1[0][i],end="")
def main():
    l1=["flower","flow","flight"]
    #l1=["dog","rececar","car"]
    fun(l1)

if __name__ == "__main__":
    main()"""

#@3
"""
def fun(l1):
    while True:
        print("________________________________________________________________")
        print("Press 1 Searching for 90 ")
        print("Press 2 Frequency of element inarray ")
        print("Press 3 finding a pair whose sum is equal to 100 ")
        print("Press 4 Deleting dublicate ")
        print("press 5 EXIT")

        print("------------------------------------------------------------------------------")

        Option= int(input("eneter your choice = "))

        print("------------------------------------------------------------------------------")

        #1
        if Option==1:
            for i in range(len(l1)):
                if l1[i]==90:
                    print("90 is present on index no=",i)

        #2
        elif Option==2:
            d1={}
            for i in l1:
                if i in d1:
                    d1[i]=d1[i]+1
                else:
                    d1[i]=1
            print(d1)

        #3
        elif Option==3:
            sum=0
            for i in range( len(l1)):
                for j in range(i+1,len(l1)):
                    sum=l1[i]+l1[j]
                    if sum==100:
                        print((l1[i],l1[j]),end=" ")

        #4
        elif Option==4:
            l2=[]
            for i in l1:
                if i not in l2:
                    l2.append(i)
            print(l2)

        #5
        elif Option==5:
            print("THANK YOU")
            return



def main():
    l1=[10,20,30,40,30,20,60,90]
    fun(l1)

if __name__ == "__main__":
    main()"""

#extra-----remove dublicate
"""
def fun(l1):
    l1.sort()

    for j in range(-1,len(l1)-1):

        if l1[j]!=l1[j+1]:

            print(l1[j+1],end=" ")


def main():
    l1=[10,20,30,40,30,20,60,90,80,60]
    fun(l1)

if __name__ == "__main__":
    main()"""

#2
"""
def fun(l1,no):
    # for i in range(len(l1)):
    #     if i>no:
    #         l1[no]=l1[i]
    #         no=no+1
    #
    # for i in range(len(l1)-1):
    #     print(l1[i],end=" ")

    for i in range(len(l1)):
        if i==no:
            pass
        else:
            print(l1[i],end=" ")


def main():
    l1=[10,20,30,40,50,60,70]
    no=int(input("entrt no="))
    print(l1)
    fun(l1,no)

if __name__ == "__main__":
    main()"""


#3
"""
def fun(l1):
    for no in l1:
        if no >1 :
            for i in range(2,no):
                if (no%i)==0:
                    break
            else:
                print(no,end=" ")


def main():
    l1=[1,6,13,25,29,43,47]
    fun(l1)

if __name__ == "__main__":
    main()"""

#4
"""
def fun(no):
    no1=no
    l2=[]
    for i in range(2,no):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            l2.append(i)
    print(l2)

    for x in range(len(l2)):
        for y in range(len(l2)):
            if l2[x]+l2[y]==no1 and  l2[x]!=3:
                print([l2[x],l2[y]],end=" , ")



def main():
    no=int(input("enter no= "))
    fun(no)

if __name__ == "__main__":
    main()"""


## =======
"""
def marks(l1):
    min=l1[0][0]
    for x in l1:
        for z in range(len(x)):
            if x[z]<min:
                min=x[z]
        break
    print(min)


    for m in l1:
        for n in range(len(m)):
            if min==m[n]:
                idx=n
                print(idx)
        break

    l3=[]
    for i in l1:
        sum = 0
        for j in range(len(i)):
            if  j!=idx:
                sum=sum+i[j]
        l3.append(sum)
    print(l3)

def main():
    no1=int(input("enter no of student ="))
    no2=int(input("enter no of marks ="))
    l1=[]
    for i in range(no1):
        l2=[]
        for j in range(no2):
            l2.append(int (input()))
        l1.append(l2)

    print(l1)

    marks(l1)


if __name__=="__main__":
    main()"""

#
"""

def main():
    A=0
    B=1
    t=0
    d3={"A":0,"B":1,}
    for i in range(24):
        t=A+B
        A=B
        B=t
        d3.update({chr(67+i) : t} )

    name=input("enter name in capital= " )
    sum=0
    for i in name:
        i=chr(ord(i)-32)
        for k in d3:
            if i==k:
                sum=sum+d3[k]
    print(sum)





if __name__=="__main__":
    main()"""

#
"""
t1=(1,2,3,4,5)
l1=[*t1,]
print(l1)


t1=(1,2,3,4,5)
l1=(*t1,)
print(l1)"""

#f string
"""
def main1(a,b):
    a="my name is {} and my contact no is {}"
    print(a.format(a,b))

def main():
    name="raj"
    num=9876543321
    print(f"my name is {name} and my contact no is {num}")

    main1("priya" ,25000)
if __name__=="__main__":
    main()"""


#
"""
l1=[1,2,3,4,5,6,7,8]
print(l1[::3])"""

#
"""
l1=["hello ","take"]
l2=["dear","sir"]
l3=[]
l4=[ i+j for i in l1 for j in l2 ]
print(l4)
for i in l1:
    for  j in l2:
        l3.extend([i+j])
print(l3)"""














