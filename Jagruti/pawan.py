# #1)
# def  factoril1(no):
#     mul=1
#     for i in range(1,no+1):
#         mul=mul*i
#     print(mul)
#
# def main():
#     no=int(input("enter no="))
#     factoril1(no)
#     #factoril2(no)
#
#
# if __name__=="__main__":
#     main()

#11)
"""
mul1 = 1
n=1
def  factoril2(no):
    global mul1
    global n
    if no+1!=n:
        mul1=mul1*n
        n=n+1
        factoril2(no)
    return mul1
def main():
    no=int(input("no="))
    print(factoril2(no))

main()"""

#2'
"""
def armstrong(no):
    no1=no
    l1=len(str(no))
    sum=0
    while no!=0:
        r=no%10
        sum=sum+(r**l1)
        no=no//10

    if no1==sum:
        print(no1,"=",sum,",,,,,,,,,,,,its armstromg")
    else:
        print(no1,"!=",sum,",,,,,,,,,,not armstrong")

def main():
    no=int(input("enter no="))
    armstrong(no)
if __name__=="__main__":
    main()"""

#3
"""
def prime(l1):
    for i in l1:
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                print(i)

def main():
    l1=[11,12,13,14,15,16,17,18,19,20]
    print(l1)
    prime(l1)
if __name__=="__main__":
    main()"""

#3
"""
def fun1(no1,no2):
    for i in range(no1,no2):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                print(i)

def main():
    no1=int(input("enter no="))
    no2=int(input("enter no="))

    fun1(no1,no2)
if __name__=="__main__":
    main()"""

#4
"""
def fun1(no):
    a=0
    b=1
    t=0
    for i in range(no):
        t=a+b
        a=b
        b=t
        print(t)
def main():
        no=int(input("enter no="))
        fun1(no)

if __name__=="__main__":
    main()"""

#5
"""
def fun1(l1):
    #1
    sum=0

    for i in l1:
        sum=sum+i
    print(sum)

    #2
    from functools import reduce
    l2=reduce((lambda x,y: x+y),l1)
    print(l2)

    #3
    sum1=0
    no=len(l1)
    i=0
    while no>i:
        sum1=sum1+l1[i]
        i=i+1
    print(sum1)

def main():
    l1=[1,2,3,4,5,6,7,8,9]
    fun1(l1)
if __name__=="__main__":
    main()"""

#6
"""
def fun1(l1):
    max=l1[0]
    for i in l1:
        if i>max:
            max=i
    print(max)
def main():
    l1=[1,2,3,4,5,6,77,8,9]
    fun1(l1)
if __name__=="__main__":
    main()"""

#8#9
"""
def fun1(l1,no):
    l2=[]
    l3=[]
    for i in range(len(l1)):
        if i<no:
            l2.append(l1[i])
        else:
            l3.append(l1[i])

    print(l3+l2)


def main():
    l1=[1,2,3,4,5,6,7]
    no=int (input("enter no="))
    print(l1)
    fun1(l1,no)
if __name__=="__main__":
    main()"""

#1 0
"""
def fun1(l1,no):
    mul=1
    for i in l1:
        mul=mul*i

    ans=mul%no
    print("ans =",ans)

    #2

    from functools import reduce
    ans1=reduce((lambda x,y: x*y),l1)
    print("ans1=",ans1%no)


def main():
    l1=[100,10,5,25,35,14]
    no=int (input("enter no="))
    print(l1)
    fun1(l1,no)
if __name__=="__main__":
    main()"""

#11
"""
def fun1(l1):
    t=l1[0]
    l1[0]=l1[len(l1)-1]
    l1[len(l1)-1]=t

    print(l1)

def main():
    l1=[1,2,3,4,5,6,7]
    print(l1)
    fun1(l1)
if __name__=="__main__":
    main()"""


#12
"""
def  fun1(l1,position1,position2):
    t=l1[position1]
    l1[position1]=l1[position2]
    l1[position2]=t

    print(l1)


def main():
    l1=[21,22,23,24,25,26,27]
    print(l1)

    position1=int(input("enter no="))
    position2=int(input("enter no="))

    fun1(l1,position1,position2)

if __name__=="__main__":
    main()"""

#13
"""
def  fun1(l1,word,n):
    

def main():
    l1=["geeks","for ","geeks"]
    word="geeks"
    n=2
    
    fun1(l1,word,n)
    
if __name__=="__main__":
    main()"""

#14
"""
def fun1(l1):
    #1
    print(len(l1))

    #2
    c=0
    for i in l1:
        c=c+1
    print(c)



def main():
    l1 = ["geeks", "for ", "geeks"]
    fun1(l1)


if __name__ == "__main__":
    main()"""

#15
"""
def  fun1(l1,no):
    #1
    f=0
    for i in l1:
        if i==no:
            f=1

    if f==1:
        print("yes")
    else:
        print("no")

    #2
    if no in l1:            #not in
        print("yessss")
    else:
        print("nooo")

def main():
    l1=[21,22,23,24,25,26,27]
    no=int(input("enter no="))

    fun1(l1,no)


if __name__ == "__main__":
    main()"""

#16
"""
def fun1(l1):
    #2
    l2=l1
    l2.clear()
    print("l2=",l2)

    #3
    l3=l1
    for i in l3:
        l3.remove(i)
    print("l3=",l3)

    #4
    l4=l1
    for i in range(len(l1)):
        l4.pop(i)
    print("l4=",l4)

    #5

    l5=l1
    for i in l1:
        del [i]
    print("l5=",l5)


def main():
    l1=[21,22,23,24,25,26,27]
    print(l1)

    fun1(l1)


if __name__ == "__main__":
    main()"""

#17
"""
def fun1(l1):
    i=0
    t=0
    ei=len(l1)-1
    while i<ei:
        t=l1[i]
        l1[i]=l1[ei]
        l1[ei]=t

        i=i+1
        ei=ei-1

    print(l1)
def main():
    l1=[1,2,3,4,5,6,7,8,9]
    print(l1)

    fun1(l1)


if __name__ == "__main__":
    main()"""

#18
"""
def fun1(l1):
    l2=l1.copy()
    print("l2=",id(l2),"=",l2)

    l3=list(l1)
    print("l3=",id(l3),"=",l3)

    l4=l1[:]
    print("l4=",id(l4),"=",l4)

    import copy
    l5=copy.copy(l1)
    print("l5=",id(l5),"=",l5)

    l6=copy.deepcopy(l1)
    print("l6=",id(l6),"=",l6)



def main():
    l1=[1,2,3,4,5,6,7,8,9]
    print("l1=",id(l1),"=",l1)

    fun1(l1)


if __name__ == "__main__":
    main()"""

#19
"""
def fun1(l1,no):
    c=0
    for i in l1:
        if no==i:
            c=c+1
    print(c)

def main():
    l1=[15,6,7,10,12,20,10,28,10]
    no=int(input("enter no="))

    fun1(l1,no)


if __name__ == "__main__":
    main()"""

#20
"""
def fun1(l1):


    sum2=0
    for i in l1:
        sum2=sum2+i
    print(sum2)

    from functools import reduce
    sum1=reduce((lambda a,b:a+b),l1)
    print(sum1)

    print(sum(l1))


def main():
    l1=[10,20,30]

    fun1(l1)


if __name__ == "__main__":
    main()"""

#21
"""
j=0
mul4=1
def fun1(l1):
    global j,mul4
    if j <len(l1):
        mul4=mul4*l1[j]

        j=j+1
        fun1(l1)
    return (mul4)



def fun2(l1):
    mul1=1
    for i in l1:
        mul1=mul1*i
    print(mul1)

    from functools import reduce
    mul2=reduce((lambda a,b:a*b),l1)
    print(mul2)

    i=0
    mul3=1
    while i<len(l1):
        mul3=mul3*l1[i]

        i=i+1
    print(mul3)


def main():
    l1=[10,20,30]

    print(fun1(l1))
    fun2(l1)


if __name__ == "__main__":
    main()"""

#22
"""
def fun1(l1):
    min=l1[0]
    for i in l1:
        if i<min:
            min=i
    print(min)
def main():
    l1=[10,202,30,3,998,65,]
    fun1(l1)

if __name__ == "__main__":
    main()"""

#23
"""
def fun1(l1):
    max=l1[1]
    for i in l1:
        if i >max:
            max=i
    print(max)
def main():
    l1=[10,202,30,3,998,65,]
    fun1(l1)

if __name__ == "__main__":
    main()"""


#24
"""
def  fun1(l1):
    t=0
    ei=len(l1)
    for i in range(ei):
        for j in  range(i+1,ei):
            if l1[i]<l1[j]:
                t=l1[i]
                l1[i]=l1[j]
                l1[j]=t
    print("2nd largest no=" ,l1[1])
def main():
    l1=[99,45,987,123,65,34,8]
    print(l1)
    fun1(l1)

if __name__ == "__main__":
    main()"""


#25
"""
def fun1(l1):
    for i in l1:
        if i%2==0:
            print(i, end=" ,")

def main():
    l1=[1,2,3,4,5,6,7,8,9]
    print(l1)
    print("even=")
    fun1(l1)

if __name__ == "__main__":
    main()"""

#26
"""
def fun1(l1):
    for i in l1:
        if i%2==1:
            print(i, end=" ,")

def main():
    l1=[1,2,3,4,5,6,7,8,9]
    print(l1)
    print("odd=")
    fun1(l1)

if __name__ == "__main__":
    main()"""

#27
"""
def fun1(no):
    for i in range(no):
        if i%2==0:
            print(i, end=" ,")

def main():
        no=int(input("enter no="))
        print("even=")
        fun1(no)

if __name__ == "__main__":
    main()"""

#28
"""
def fun1(no):
    for i in range(no):
        if i%2==1:
            print(i, end=" ,")

def main():
        no=int(input("enter no="))
        print("odd=")
        fun1(no)

if __name__ == "__main__":
    main()"""

#29
"""
def fun1(l1):
    c1=0
    c2=0
    for i in l1:
        if i%2==0:
            c1=c1+1
        else:
            c2=c2+1
    print("amount of even no=",c1,"..........","amount of odd no =",c2)
def main():
    l1=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    print(l1)
    fun1(l1)

if __name__ == "__main__":
    main()"""

#30
"""
def fun1(l1):
    for i in l1:
        if i<0:
            print(i,end=" ,")
def main():
    l1=[1,-2,3,-4,5,-6,7,-8,9]
    print(l1)
    fun1(l1)

if __name__ == "__main__":
    main()"""

#31
"""
def fun1(l1):
    for i in l1:
        if i>=0:
            print(i,end=" ,")
def main():
    l1=[0,1,-2,3,-4,5,-6,7,-8,9]
    print(l1)
    fun1(l1)

if __name__ == "__main__":
    main()"""


#32
"""
def fun1(si,ei):
    for i in range(si,ei):
        if i>=0:
            print(i,end=" ,")
def main():
    si=int(input("enter no="))
    ei=int(input("enter no="))

    fun1(si,ei)

if __name__ == "__main__":
    main()"""

#33
"""
def fun1(si,ei):
    for i in range(si,ei):
        if i<0:
            print(i,end=" ,")
def main():
    si=int(input("enter no="))
    ei=int(input("enter no="))

    fun1(si,ei)

if __name__ == "__main__":
    main()"""

#34
"""
def fun1(l1):
    c1=0
    c2=0
    for i in l1:
        if i>=0:
            c1=c1+1
        else:
            c2=c2+1
    print("count of +ve no=",c1,",,,,,,,,","count of -ve no=",c2)
def main():
    l1=[0,1,-2,3,-4,5,-6,7,-8,9]
    print(l1)
    fun1(l1)

if __name__ == "__main__":
    main()"""

#35
"""
def fun2(l1):
    l2=l1[0:3]
    for i in l2:
        if i in l1:
             l1.remove(i)
    print(l1)
def fun1(l1):
    no1=-2
    no2=-8
    for  i in l1:
        if i == no1:
            l1.remove(i)
        elif  i== no2:
            l1.remove(i)
    print(l1)

def main():
    l1=[0,1,-2,3,-4,5,-6,7,-8,9]
    print(l1)
    fun1(l1)
    fun2(l1)

if __name__ == "__main__":
    main()"""


#36
"""
def fun1(l1):
    for i in l1:
        if i==():
            l1.remove(i)
    print(l1)

def main():
    l1=[(),0,1,-2,(","),(),3,-4,5,-6,7,(),-8,9,(",")]
    print(l1)
    fun1(l1)

if __name__ == "__main__":
    main()"""

#37
"""
def fun1(l1):
    l2=[]
    for i in range(len(l1)):
        for j in range(i+1,len(l1)):
            if l1[i] ==l1[j] and l1[i] not in l2:
                l2.append(l1[i])
                break
    print(l2)

def main():
    l1=[10,20,30,20,20,30,40,50,-20,60,60,-20,-20]
    print(l1)
    fun1(l1)

if __name__ == "__main__":
    main()"""

#38
"""
def fun1(l1):
    l2=[]
    sum=0
    for i in l1:
        sum=sum+i
        l2.append(sum)
    print(l2)

def main():
    l1=[10,20,30,40,50]
    print(l1)
    fun1(l1)

if __name__ == "__main__":
    main()"""

#39
"""
def fun1(l1,l2):
    l3=[]
    l4=[]
    l5=[]
    for i ,j in zip(l1,l2):
        if j==0:
            l3.append(i)
        elif j==1:
            l4.append(i)
        else:
            l5.append(i)
    print(l3+l4+l5)



def main():
    l1=["a","b","c","d","e","f","g","h","i"]
    l2=[  0,  1,    1,  0,   1,  2,  2,   0,  1]

    print(l1)
    print(l2)


    fun1(l1,l2)

if __name__ == "__main__":
    main()"""

#40
"""
def fun1(str1):
    l1=str1
    l2=[]
    f=0
    for i in range(len(l1)-1,-1,-1):
        l2.append(l1[i])

    for i,j in zip(l1,l2):
        if i!=j:
            f=1
    if f==1:
        print("no")
    else:
        print("yes")


def main():
    str1=str(input("enter string="  ))
    fun1(str1)

if __name__ == "__main__":
    main()"""


#41
"""
def fun3(str1,i):
    l5=list(str1)
    for m in range(len(l5)):
        if m==i:
            l5.pop(i)
    for y in l5:
        print(y,end="")

def fun2(str1,i):
    l1=list(str1)
    for j in range(len(l1)):
        if j==i:
            l1.remove(l1[j])
    for x in l1:
        print(x,end="")
    print("\n")

def fun1(str1,i):
    for j in range(len(str1)):
        if i==j:
            str2=str1.replace(str1[i],"")
    print(str2)
def main():
    str1=str(input("enter string="  ))
    i=int(input("enter no="))
    fun1(str1,i)
    fun2(str1,i)
    fun3(str1,i)


if __name__ == "__main__":
    main()"""

#42
"""
i=0
c2=0
def fun4(str1):
    global i,c2
    if i<len(str1):
        c2=c2+1
        i=i+1
        fun4(str1)
    return c2
def fun3(str3):
    print("len2=",len(str3))
    i=0
    c1=0
    while i<len(str3):
        c1=c1+1
        i=i+1
    print("len3=",c1)
def fun2(str2):
    c=0
    for i in str2:
        c=c+1
    print("len1=",c)
def fun1(str1,str2):
    f=0
    if str2 not in str1:
        f=1
    if f==1:
        print("not")
    else:
        print("yes")

def main():
    str1="geeks for geeks"
    str2=str(input("enter string="  ))
    fun1(str1,str2)
    fun2(str1)
    fun3(str1)
    print("len4=",fun4(str1))


if __name__ == "__main__":
    main()"""

#43
"""
def fun1(str1):
    str1=str1.split()
    for i in str1:
        if len(i)%2==0:
            print(i ,end="   ")

def main():
    str1=str(input("enter string="  ))
    fun1(str1)


if __name__ == "__main__":
    main()"""

#44
"""
def fun1(str1):
    s=set()
    vowels=set("aeiou")
    for i in str1:
        if i in vowels:
            s.add(i)
        else:
            pass
    print(s)
    if len(vowels)==len(s):
        print(" accepted")
    else:
        print("not accepted ")

def main():
    str1=str(input("enter string="  ))
    fun1(str1)


if __name__ == "__main__":
    main()"""

#45
"""
def fun1(str1,str2):
    #1
    s=set()
    for i in str1:
        for j in str2:
            if i==j :
                s.add(i)
    print(s,"--------------","count=",len(s))



def main():
    str1=str(input("enter string="  ))
    str2=str(input("enter string="  ))

    fun1(str1,str2)


if __name__ == "__main__":
    main()"""

#46
"""
def fun2(str1):
    l1=[]
    for i in str1:
        if i not in l1:
            l1.append(i)
    print("removed duplicate list=")
    for j in l1:
        print(j,end="")
    print("\n")
    print("removed duplicate set=")
    for n in set(str1):
        print(n,end="")


def fun1(str1):
    s1="aeiouAEIOU"
    c=0
    for i in str1:
        if i in s1:
            c=c+1
    print("vowel present =",c)

def main():
    str1=str(input("enter string="  ))

    fun1(str1)
    fun2(str1)


if __name__ == "__main__":
    main()"""


#47
#13

#48
"""
def fun1(str1,no):
    for i in range (len(str1)):
        if i==no:
            str2=str1.replace(str1[i],"",1)
    print(str2)

    str1=list(str1)
    for i in range(len(str1)):
        if i==no:
            str1.pop(i)
    for i in str1:
        print(i,end="")



def main():
    str1=str(input("enter string="  ))
    no=int(input("enter no="))

    fun1(str1,no)


if __name__ == "__main__":
    main()"""


#49
"""
def  fun1(str1):
    #split
    #1
    l2=str1.split()
    print("1=",l2)


    return l2

def fun2(l2):
    str3="-".join(l2)
    print(str3)



def main():
    str1="geeks for Geeks"
    print(str1)


    m=fun1(str1)
    fun2(m)

if __name__ == "__main__":
    main()"""

#sub part 49
"""
def fun1(str1):
    l1=[]
    temp=' '
    for i in str1:
        if i==" ":
            l1.append(temp)
            temp=" "
        else:
            temp=temp+i
    print(l1)


def fun2(l1):
    for i in l1:
        if i==" ":
            print("-",end="")
        else:
            print(i,end="")


def main():
    str1 = "geeks for Geeks"
    print(str1)

    fun1(str1+" ")
    fun2(" "+str1)


if __name__ == "__main__":
    main()"""

#50
"""
def fun1(str1):
    str2=set(str1)
    str3={"1","0"}

    if str2==str3 or str2=={"0"} or str2=={"1"}:
        print("yes")
    else:
        print("no")


def main():
    str1 = str(input ("enter string= "))

    fun1(str1)


if __name__ == "__main__":
    main()"""

#51
"""
def fun1(str1,l1):
    s1=set(str1)
    for x in l1:
        s2=set(x)
        if s2.issubset(s1):
            print(x,end=" , ")

def main():
    str1 = str(input ("enter string= "))
    l1=['ape','apple',"peach",'puppy']
    fun1(str1,l1)

if __name__ == "__main__":
    main()"""

#52
"""
def fun1(str1,str2):
    #1
    str1=str1.split()
    str2=str2.split()
    for i in str2:
        if i not in str1:
            print(i,end=" , ")
    print("\n")

    #2
    s1=set(str1)
    s2=set(str2)

    s3=s1.symmetric_difference(s2)
    print(s3)

def main():
    str1 = "geeks for geeks"
    str2="learning from geeks for geeks"
    fun1(str1,str2)

if __name__ == "__main__":
    main()"""

#53
"""
def fun1(no):
#1
    no1=str(no)
    no2=no1.maketrans(",.",".,"," ")
    no3=no1.translate(no2)
    print(no3)

#2
    no4=no3.replace(",.",".,")
    print(no4)

#3
    print("forloop=")
    for i in no1:
        if i==",":
            print(".",end="")
        elif i==".":
            print(",",end="")
        else:
            print(i,end="")
def main():
    no=23,456,567.89
    fun1(no)

if __name__ == "__main__":
    main()"""


#54

#55

#56
"""
def fun2(str1,no):
    l1=str1[:no]
    l2=str1[no:len(str1)]
    print("left join = ",l2+l1)


    x=len(str1)-no
    l3=str1[x:len(str1)]
    l4=str1[:x]
    print("right join=",l3+l4)


def main():
    str1="qwertyu"
    print(str1)
    no=2
    fun2(str1,no)


if __name__ == "__main__":
    main()"""

#13
"""
def fun1(str1,str2,no):
    l1=[]
    for i in range(len(str1)):
        if str1[i]==str2:
            l1.append(i)

    for i in range(len(str1)):
        if i!=l1[no-1]:
            print(str1[i],end=" , ")

def main():
    str1=["geeks","for", "for","geeks" ,"xyx","geeks","for"]
    str2="geeks"
    no=2
    fun1(str1,str2,no)

if __name__ == "__main__":
    main()"""

#14
"""
def main():
        data={"Items": ["saop","wshing_powder","dish_wash","apple","banana","strawberry","mango"
               ,"dragunfruit","capsicum","tomato","onion","potato","garlic","chili"],

              "Price":[100,101,102,103,104,105,106,107,108,109,110,201,202,203,204]
              }
        #
        # items=pd.DataFrame(data)
        # print(items)

        selected_items=[]
        item_no=int(input("Enter How many Items you want add  = "))
        for i in item_no:
            selected_items.append(int(input("Enter Item No=  ")))

        total_price=[]
        for i in selected_items:
            total_price

if __name__ == "__main__":
    main()"""

#15
"""
def main():
    c=0
    for i in  range(1,5):
        for j in range(1,i):
            c=c+1
            print(c,end="   ")
        print("\r")

if __name__=="__main__":
    main()"""

######################################################

####------------------STRING----------------#####
#1
"""
def fun1(str1):
    word=" "
    rev=" "
    for i in str1:
        if i!=" ":
            word=word+i
        else:
            rev=word+" "+rev
            word=" "
    print(rev)
def main():
    str1=str(input("enter string="))
    fun1(str1+" ")

if __name__=="__main__":
    main()"""

#2
"""
def fun1(l1):
    l1.sort()
    for i in range(len(l1)-1):
        w = " "
        for j,k in zip(l1[i],l1[i+1]):
            if j==k:
                w=w+j
            else:
                break
    print(w)

def main():
    #l1=["geeksforgeeks ","geeks","geek","geezer"]
    l1=["apple", "ape", "april"]

    fun1(l1)

if __name__=="__main__":
    main()"""


#3
"""
def  fun1(no):
    for i in
def main():
    no=str(input("enter  no=  "))
    fun1(no)
    I = 1
    IV = 4
    V= 5
    IX= 9
    X =  10
    XL = 40
    L  = 50
    XC  = 90
    C  = 100
    CD =400
    D =500
    CM = 900
    M =1000

if __name__=="__main__":
    main()"""


#4
"""
def main():
    # l1 = ["the", 'quick', 'brown', 'fox', 'quick']
    # w1 = 'the'
    # w2 = 'fox'

    l1 = ["geeks", 'for ', 'geeks', 'contribute', 'practice']
    w1 = 'geeks'
    w2 = 'practice'

    for i in range(len(l1)):
        if l1[i]==w1:
            no1=i
        elif l1[i]==w2:
            no2=i
    print("distance= ",no2-no1)




if __name__=="__main__":
    main()"""


#5
"""
def main():
    d2={}
    str2="abc"           #"aaaaaaaaaaa"
    str2=str2[::-1]
    for i in str2:
        if i in d2:
            d2[i]=d2[i]+1
        else:
            d2[i]=1

    for i,j in d2.items():
        print(j,i,end="")

if __name__=="__main__":
    main()"""

#6
"""
def main():
    str1= "(())))("   #"(()))(()()())))"                                                   #"))"=2
    c1=0
    for i in str1:
        if i==")":
            c1=c1+1

    print(c1)

if __name__=="__main__":
    main()"""

#7
"""
def main():
    str1 = str(input("enter string=  "))                                                          #'aab'
    str2 = str(input("enter string=  "))                                                          #'xxy'
    d1={}
    d2={}

    if len(str1)!=len(str2):
        print("False")
        return
    for i in str1:
        if i in d1:
            d1[i]=d1[i]+1
        else:
            d1[i]=1

    for i in str2:
        if i in d2:
            d2[i]=d2[i]+1
        else:
            d2[i]=1

    f=0
    for i,j in zip(d1.values(),d2.values()):
        if i!=j:
            f=1


    if f==1:
        print("False")
    else:
        print("True")
if __name__=="__main__":
    main()"""

#8
"""
def fun1(str1, str2,k):
    if len(str1)!=len(str2):
        print("False")
        return
    c1=0
    for i in str1:
        if i not in str2:
            c1=c1+1
    print(c1)
    if c1==k:
        print("Y")
    else:
        print("N")

def main():
    str1 = str(input("enter string=  "))                                                          #'aab'
    str2 = str(input("enter string=  "))
    k=int(input("enter k = "))

    fun1(str1,str2,k)
if __name__=="__main__":
    main()"""

#9
"""
def fun1(str1):
    str1=str1.lower()
    s1=set(str1)

    alpha="abcdefghijklmnopqrstuvwxyz "

    if len(alpha)!=len(s1):
        print("not a panagram")
    else:
        print("yes panagram")

def main():
    str1 = str(input("enter string=  "))                                                          #'aab'

    fun1(str1)
if __name__=="__main__":
    main()"""

#10
"""
def fun1(str1):
    mid=len(str1)//2
    l1=[]
    l2=[]
    for i in range(mid):
        l1.append(str1[i])

    for j in range(mid+1,len(str1)):
        l2.append(str1[j])

    print(l1)
    print(l2[::-1])
    l3=[]
    l2=l2[::-1]

    for x,y in zip(l1,l2):
        print(x,y)
        if x!=y:
            l3.extend([x,y])

    print(len(l3))


def main():
    str1 = str(input("enter string=  "))                                                          #'aab'

    fun1(str1)
if __name__=="__main__":
    main()"""

#11
"""
def fun1(str1):
    l1=[" ",]
    l1.append(str1[::-1])
    for i in str1:
        l1.append(i)
    for i in range(len(str1)):
        for j in range(i+1,len(str1)):
            l1.append(str1[i]+str1[j])
    print(set(l1),"--------",len(set(l1)))
def main():
    str1 = str(input("enter string=  "))                                                          #'aab'

    fun1(str1)
if __name__=="__main__":
    main()"""


# #12
# Input: string1 = “amazon”, string2 = “azonam”
# Output: Yes
# Explanation: Rotating string1 by 2 places in anti-clockwise gives the string2.
#
# Input: string1 = “amazon”, string2 = “onamaz”
# Output: Yes
# Explanation: Rotating string1 by 2 places in clockwise gives the string2.
"""
def main():
    s1=str(input("enter string=  "))
    s2=str(input("enter string=  "))
    no=int(input("enter no= " ))

    l1=s1[:no]
    l2=s1[no:len(s1)]

    s3=l2+l1

    l4=s1[:len(s1)-no]
    l5=s1[len(s1)-no:len(s1)]

    s4=l5+l4

    if s2==s3 or s2==s4:
        print("Yes")
    else:
        print("No")

if __name__=="__main__":
    main()"""


#13-------------Python program to remove given character from String
"""
def fun1(str1,chrs):
    for i in str1:
        #1
        # if i in chrs:
        #     pass


        #2
        if i=="1" or  i=="2" or i=="3":
            pass
        else:
            print(i, end="")


def main():
    str1="Geeks123For123Geeks"
    chrs="123"
    print("str1=",str1)
    fun1(str1,chrs)


if __name__=="__main__":
    main()"""


#2Python Program to count occurrence of a given characters in string.    GeeksForGeeks
"""
def fun1(str1,chrs):
    c=0
    for i in str1:
       if i==chrs:
           c=c+1
    print(c)

def main():
    str1="GeeksForGeeks"
    print("str1=",str1)
    chrs=input("enter chr =  ")
    fun1(str1,chrs)


if __name__=="__main__":
    main()"""

#3  Python Program to check if two Strings are Anagram
"""
def fun1(str1,str2):
    #1
    if sorted(str1)==sorted(str2):
        print("YES Anagram")
    else:
        print("NOT Anagram")

    #2
    f=0
    for i in str1:
        if i in str2:
            f=1
    if f==1:
        print("YES Anagram")
    else:
        print("NOT Anagram")



    #3
    t=0
    str1=list(str1)
    for i in range(len(str1)):
        for j in range(i+1,len(str1)):
            if str1[i]>str1[j]:
                t=str1[i]
                str1[i]=str1[j]
                str1[j]=t


    t1=0
    str2=list(str2)
    for i in range(len(str2)):
        for j in range(i+1,len(str2)):
            if str2[i]>str2[j]:
                t1=str2[i]
                str2[i]=str2[j]
                str2[j]=t1


    if str1==str2:
        print("YES Anagram")
    else:
        print("NOT Anagram")



def main():
    str1="listen"
    str2="silent"
    fun1(str1,str2)


if __name__=="__main__":
    main()"""


#4 Python program to check a String is palindrome or not.
"""
def  fun1(str1):
    #1
    str2=str1[::-1][::-1]
    if str1==str2:
        print("YES  palindrome")
    else:
        print("NOT palindrome")

    #2
    str1=list(str1)
    str3=str1.copy()
    t=0
    si=0
    ei=len(str1)-1
    while si<ei:
        t=str3[si]
        str3[si]=str3[ei]
        str3[ei]=t

        si=si+1
        ei=ei-1
    if str1==str3:
        print("YES  palindrome")
    else:
        print("NOT palindrome")

def main():
    str1="madam"
    fun1(str1)


if __name__=="__main__":
    main()"""

#5Python program to check given character is vowel or consonant.
"""
def  fun1(str1):
    vow="aeiouAEIOU"
    if str1 in vow:
        print("vowel")
    else:
        print("consonant")

def main():
    str1=str(input("enter chr = "))
    fun1(str1)


if __name__=="__main__":
    main()"""

#6 Python program to check given character is digit or not.
"""
def fun1(str1):
    if (ord(str1)>=48 )and  (ord(str1)<=57):
        print("YES It is DIGIT ")
    else:
        print("It is NOT DIGIT ")
def main():
    str1=str(input("enter chr = "))
    fun1(str1)


if __name__=="__main__":
    main()"""

#7 Python program to check given character is digit or not using isdigit() method.
"""
def fun1(str1):
    if str1.isdigit():
        print("YES It is DIGIT ")
    else:
        print("It is NOT DIGIT ")
        
def main():
    str1=str(input("enter chr = "))
    fun1(str1)

if __name__=="__main__":
    main()"""

#8 -----#9----Python program to replace the string space with a given character.
"""
def fun1(str1,s):
    #1
    for i in str1:
        if i==" ":
            print(s,end="")
        else:
            print(i,end="")

    #2
    print("\r")
    str2=str1.replace(" ",s)
    print(str2)

    #3
    str1=str1.split()
    str3=s.join(str1)
    print(str3)
def main():
    str1 = "Once in a blue moon"
    s=input("enter =")
    fun1(str1,s)


if __name__ == "__main__":
    main()"""

#10Python program to convert lowercase char to uppercase of string
"""
def  fun1(str1):
    for i in str1:
        if ord(i)>=97 and ord(i)<=122:
            print(chr(ord(i)-32),end="")
        else:
             print(i,end="")

def main():
    str1 = "Once In a Blue Moon"
    fun1(str1)


if __name__ == "__main__":
    main()"""


#11 Python program to convert lowercase vowel to uppercase in string.
"""
def  fun1(str1):
    vow="aeiou"
    for i in str1:
        if i in vow:
            print(chr(ord(i)-32),end="")
        else:
             print(i,end="")

def main():
    str1 = "GeeksforGeeks"
    fun1(str1)


if __name__ == "__main__":
    main()"""

#12 Python program to delete vowels in a given string.
"""
def  fun1(str1):
    vow="aeiou"
    for i in str1:
        if i not in vow:
            print(i,end="")


def main():
    str1 = " welcome to geeksforgeeks"
    fun1(str1)


if __name__ == "__main__":
    main()"""

#13  Python program to count the Occurrence Of Vowels & Consonants in a String.
"""
def  fun1(str1):
    vow="aeiou"
    c1=0
    c2=0
    for i in str1:
        if i  in vow and i!=" ":
            c1=c1+1
        elif i!=" ":
            c2=c2+1
    print("vowel = ",c1)
    print("Consonants = ",c2)

def main():
    str1 = "This is a really simple sentence"
    fun1(str1)


if __name__ == "__main__":
    main()"""

#14  Python program to print the highest frequency character in a String.
"""
def  fun1(str1):
    d1={}
    for i in str1:
        if i in d1:
            d1[i]=d1[i]+1
        else:
            d1[i]=1
    for i,j in d1.items():
        m=max(d1.values())
        if m==j:
            print(i)

def main():
    str1 = "GeeksforGeeks"
    fun1(str1)


if __name__ == "__main__":
    main()"""

#15 Python program to Replace First Occurrence Of Vowel With ‘-‘ in String.
"""
def  fun1(str1,ch):
    vow="AEIOUaeiou"
    for i in str1:
        if i in vow:
            str2=str1.replace(i,ch)
            break
    print(str2)

def main():
    str1 = "Hello World"
    ch="-"
    fun1(str1,ch)


if __name__ == "__main__":
    main()"""

#16 Python program to count alphabets, digits and special characters.
"""
def  fun1(str1):
    str1=str1.lower()
    no="0123456789"
    alph="abcdefghijklmnopqrstuvwxyz"
    c1=0
    c2=0
    c3=0

    for i in str1:
        if i in no:
            c1=c1+1
        elif i in alph:
            c2=c2+1
        else:
            c3=c3+1

    print("alphabets = ",c2)
    print("no =",c1)
    print("special characters = ",c3)


def main():
    str1 = "hello i am" # "Ques123!@we12#"
    fun1(str1)


if __name__ == "__main__":
    main()"""

#17 Python program to separate characters in a given string.     Hello World
"""
def fun1(str1):
     for i in str1:
         yield i

def main():
    str1 = "Hello World"
    for x in fun1(str1):
        print(x)


if __name__ == "__main__":
    main()"""

#18 Python program to remove blank space from string.
"""
def fun1(str1):
     for i in str1:
         if i!=" ":
             yield i

def main():
    str1 = "python is fun "
    print(str1)
    for x in fun1(str1):
        print(x,end="")


if __name__ == "__main__":
    main()"""


#19 Python program to concatenate two strings using join() method.    website
"""
def fun1(str1,str2):
     str3="".join([str1,str2])
     print(str3)

def main():
    str1 = input("enter string = ")
    str2= input("enter string = ")
    fun1(str1,str2)

if __name__ == "__main__":
    main()"""


#20 Python program to concatenate two strings without using join() method.
"""
def fun1(str1,str2):
     str3=str1+str2
     print(str3)

def main():
    str1 = input("enter string = ")
    str2= input("enter string = ")
    fun1(str1,str2)

if __name__ == "__main__":
    main()"""

#21 Python program to remove repeated character from string.
"""
def fun1(str1):
     l1=[]
     for i in str1:
         if i not in l1:
             l1.append(i)
     for j in l1:
        print(j,end="")


def main():
    str1 = "geeksforgeeks"
    fun1(str1)

if __name__ == "__main__":
    main()"""

#22   Python program to calculate sum of integers in string    1%program897Language%
"""
def fun1(str1):
     l1=[]
     s=0
     for i in str1:
         if i in "0987654321":
             l1.append(int(i))
     for i in l1:
         s=s+i
     print("sum= ",s)


def main():
    str1 = "1%program8971Language%"
    fun1(str1)

if __name__ == "__main__":
    main()"""

#23  Python program to print all non repeating character in string.
"""
def fun1(str1):
    #1
    d1={}
    for i in str1:
        if i in d1:
            d1[i]=d1[i]+1
        else:
            d1[i]=1
    for  x ,z in d1.items():
        if z==1:
            print(x,end="")

    #2
    print(" ")
    str1=list(str1)
    l1=[]
    for i in range(len(str1)):
         for j in range(i+1,len(str1)):
             if str1[i]==str1[j]:
                 l1.append(str1[i])
    for x in str1:
        if x not in l1:
            print(x,end="")

def main():
    str1 = "geeksforgeeks"
    print(str1)
    fun1(str1)

if __name__ == "__main__":
    main()"""

#24 Python program to copy one string to another string.
"""
def main():
    str1 = "geeksforgeeks"

    str2=str1
    str3=str1[::]
    
    str4=str1[::-1][::-1]
    
    str5=""
    for i in str1:
        str5=str5+i
        
    print("str1 = ",id(str1))
    print("str2 = ",id(str2))
    print("str3 = ",id(str3))
    print("str4 = ",id(str4))
    print("str5 = ",id(str5))


if __name__ == "__main__":
    main()"""

#25 Python Program to sort characters of string in ascending order
""".
def fun1(str2):
    #1
    str1=list(str2)
    t=0
    for i in range(len(str1)):
        for j in range(i+1,len(str1)-1):
            if  ord(str1[i])>ord(str1[j]):
                t=str1[i]
                str1[i]=str1[j]
                str1[j]=t
    for x in str1:
        print(x,end="")
    print("")

    #2
    str3="".join(sorted(str2))
    print(str3)
def main():
    str1 = "geeksforgeeks"
    print(str1)
    fun1(str1)

if __name__ == "__main__":
    main()"""

#26 Python Program to sort character of string in descending order.
"""
def fun1(str2):
    #1
    str1=list(str2)
    t=0
    for i in range(len(str1)):
        for j in range(i+1,len(str1)-1):
            if  ord(str1[i])<ord(str1[j]):
                t=str1[i]
                str1[i]=str1[j]
                str1[j]=t
    for x in str1:
        print(x,end="")
    print("")

    #2
    str3="".join(sorted(str2))
    print(str3[::-1])
def main():
    #str1 = "alkasingh"   #snlkihgaa
    str1="nupursingh"                   # ##uusrpnnihg

    print(str1)
    fun1(str1)

if __name__ == "__main__":
    main()"""



#----------------LIST--------------
#1 Write a program in Python for, In array 1-100 numbers are stored, one number is missing how do you find it.
"""
def main():
    l1=[1, 2, 4, 6, 3, 7, 8]
    len1=len(l1)
    for i in range(1,len1+2):
        if i not in l1:
            print(i)

if __name__ == "__main__":
    main()"""


#2Write a program in Python for, In a array 1-100 multiple numbers are duplicates, how do you find it.
"""
def main():
    l1=[1, 2, 3, 4, 2, 7, 8, 8, 3]
    for i in range(len(l1)):
        for j in range(i+1,len(l1)):
            if l1[i]==l1[j]:
                print(l1[i],end=",")

if __name__ == "__main__":
    main()"""


#3Write a program in Python for, How to find all pairs in array of integers whose sum is equal to given number.
"""
def fun1(l1,no):
    l2=[]
    for i in range(len(l1)):
        for j in range(i+1,len(l1)):
            if l1[i]+l1[j]==no:
                l2.append((l1[i],l1[j]))
    print(l2)

def main():
    l1=[1, 5, 3, 7, 9]
    no=12

    l2=[2, 1, 5, 7, -1, 4]
    no1=6

    fun1(l2,no1)


if __name__ == "__main__":
    main()"""


#4Write a program in Python for, How to compare two array is equal in size or not.
"""
def fun1(l1,l2):
    s1=set(l1)
    s2=set(l2)
    if len(s1)==len(s2):
        print("yes")
    else:
        print("no")
def main():
    l1=[1,2,3]                                   #[1, 2, 5, 4, 0, 2, 1]
    l2=[1,1,2]                                   #[2, 4, 5, 0, 1, 1, 2]
    fun1(l1,l2)


if __name__ == "__main__":
    main()"""


#5         Write a program in Python to find largest and smallest number in array.
"""
def fun2/(l1):
    max=l1[0]
    for i in l1:
        if i>max:
            max=i
    print("maximum=",max)
def fun1(l1):
    min=l1[0]
    for i in l1:
        if i<min:
            min=i
    print("minimum=",min)
def main():
    l1= [12, 45, 2, 41, 31, 10, 8, 6, 4]
    fun1(l1)
    fun2(l1)




if __name__ == "__main__":
    main()"""

#6 Write a program in Python to find second highest number in an integer array.
"""
def fun1(l1):
    #1
    t=0
    for i in range(len(l1)):
        for j in range(i+1,len(l1)):
            if l1[i]<l1[j]:
                t=l1[i]
                l1[i]=l1[j]
                l1[j]=t
    print("second highest = ",l1[1])



    #2
    l1.sort()
    print("second highest = ",l1[-2])
def main():
    l1= [12, 45, 2, 41, 31, 10, 8, 6, 4]
    fun1(l1)




if __name__ == "__main__":
    main()"""

#7 Write a program in Python to find top two maximum number in array?

"""
def fun1(l1):
    #1
    t=0
    for i in range(len(l1)):
        for j in range(i+1,len(l1)):
            if l1[i]<l1[j]:
                t=l1[i]
                l1[i]=l1[j]
                l1[j]=t
    print("second highest = ",l1[0]," and  ",l1[1])

    #2
    l1.sort()
    print("second highest = ",l1[-1]," and  ",l1[-2])
def main():
    l1= [12, 45, 2, 41, 31, 10, 8, 6, 4]
    fun1(l1)


if __name__ == "__main__":
    main()"""

#8 Write a program in Python to remove duplicate elements form array.
"""
def fun1(l1):
    l2=[]
    for i in l1:
        if i not in l2:
            l2.append(i)
    print(l2)
def main():
    l1=[28, 42, 28, 16, 90, 42, 42, 28]  #[2, 4, 10, 20, 5, 2, 20, 4]
    print(l1)
    fun1(l1)


if __name__ == "__main__":
    main()"""

#9==7

#10 Python program to print array in reverse Order
"""
def fun1(l1):
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


def main():
    l1=[1,2,3,4,5,6,7,8,9] #[2, 4, 10, 20, 5, 2, 20, 4]
    print(l1)
    fun1(l1)


if __name__ == "__main__":
    main()"""



#11 Python program to reverse an Array in two ways.
"""
def fun2(l1):
    l2=[]
    for i in range(len(l1)-1,-1,-1):
        l2.append(l1[i])
    print(l2)

    l3=l1[::-1]
    print(l3)
def fun1(l1):
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


def main():
    l1=[1,2,3,4,5,6,7,8,9] 
    print(l1)
    #fun1(l1)
    fun2(l1)


if __name__ == "__main__":
    main()"""

#12 Python Program to calculate length of an array.
"""
def fun1(l1):
    #1
    len1=len(l1)
    print("length=",len1)

    #2
    c1=0
    for i in l1:
        c1=c1+1
    print("length=",c1)
def main():
    l1=[2, 4, 10, 20, 5, 2, 20, 4]
    print(l1)
    fun1(l1)


if __name__ == "__main__":
    main()"""

#13 Python program to insert an element at end of an Array.
"""

def fun1(l1):
    #1
    l1.append(100)
    print(l1)

    #2
    l1.extend([200])
    print(l1)

    #3
    l1.insert(len(l1),300)
    print(l1)



def main():
    l1=[2, 4, 10, 20, 5, 2, 20, 4]
    print(l1)
    fun1(l1)


if __name__ == "__main__":
    main()"""


#14 Python program to insert element at a given location in Array
"""
def fun1(l1,idx,ele):
    #1
    l1.insert(idx,ele)
    print(l1)

    #2
    l1[idx]=ele
    print(l1)
   
    

def main():
    l1=[1,2,3,4,5,6,7,8,9]
    print(l1)
    idx=int(input("insert indext btween  0 to 8 ="))
    ele=int(input("enter element  = "))

    fun1(l1,idx,ele)


if __name__ == "__main__":
    main()"""

#15Python Program to delete element at end of Array.
"""
def fun1(l1):
    #1
    l1.pop()
    print(l1)

    #2
    del l1[len(l1)-1]
    print(l1)
    
    #3
    l1.remove(l1[-1])
    print(l1)

    #3
    l2=[]
    for i in range(len(l1)-1):
        if i!=len(l1):
            l2.append(l1[i])
    print(l2)


def main():
    l1=[2, 4, 10, 20, 5, 2, 20, 4]
    print(l1)
    fun1(l1)


if __name__ == "__main__":
    main()"""


#16 Python Program to delete given element from Array.
"""
def fun1(l1,no):
    # #1
    # l1.remove(no)
    #print(l1)


    #2
    l2=[]
    for i in l1:
        if i!=no:
            l2.append(i)
    print(l2)



def main():
    l1=[2, 4, 10, 20, 5, 2, 20, 4]
    print(l1)
    no=int(input("no = "))

    fun1(l1,no)


if __name__ == "__main__":
    main()"""


#17 Python Program to delete element from array at given index.
"""
def fun1(l1,idx):
    # #1
    # l1.pop(idx)
    # print(l1)

    #2
    # del  l1[idx]
    # print(l1)

    # #3
    l2=[]
    for i in range(len(l1)):
        if i==idx:
            pass
        else:
            l2.append(l1[i])
    print(l2)



def main():
    l1=[2, 4, 10, 20, 5, 2, 20, 4]
    print(l1)
    idx=int(input("index = "))

    fun1(l1,idx)


if __name__ == "__main__":
    main()"""

#18 Python Program to find sum of array elements.
"""
def main():
    l1=[1,2,3,4]

    #1
    sum=0
    for i in l1:
        sum=sum+i
    print(sum)

    #2
    from functools import reduce
    ans=reduce(lambda x,y : x+y, l1)
    print(ans)
    


if __name__ == "__main__":
    main()"""

#18
"""
def main():
    l1 = [1, 2, 3, 4]

    ans=sum(l1)
    print(ans)


if __name__ == "__main__":
    main()"""


#19 Python Program to print all even numbers in array.
"""
def main():
    l1 = [1, 2, 3, 4,5,6,7,8,9]
    print(l1)
    print("even numbers")


    #1
    for i in l1:
        if i%2==0:
            print(i, end=" , ")

    print()

    #2
    l2=list(filter(lambda x :x%2==0 ,l1))
    print(l2)

    #3
    l3=[i for i in l1 if i%2==0]
    print(l3)


if __name__ == "__main__":
    main()"""

#20 Python Program to print all odd numbers in array.

"""
def main():
    l1 = [1, 2, 3, 4,5,6,7,8,9]
    print(l1)
    print("ODD NO")

    #1
    for i in l1:
        if i%2==1:
            print(i, end=" , ")

    print()

    #2
    l2=list(filter(lambda x :x%2==1 ,l1))
    print(l2)

    #3
    l3=[i for i in l1 if i%2==1]
    print(l3)


if __name__ == "__main__":
    main()"""

#21      Python program to perform---------- left rotation ------of array elements by two positions.
"""
def fun1(l1):

    #2
    l2=l1[2:]+l1[:2]
    print(l2)

    #3
    l3=[]
    l4=[]
    for i in range(len(l1)):
        if i<2:
            l3.append(l1[i])
        else:
            l4.append(l1[i])
    print(l4+l3)


    #1         0 is the 1st
    l1.append(l1.pop(0))
    l1.append(l1.pop(0))
    print(l1)


def main():
    l1=[1,2,3,4,5]
    fun1(l1)

if __name__ == "__main__":
    main()"""

#22 Python program to perform right rotation in array by 2 positions.
"""   
def fun1(l1):

    #2
    no=len(l1)-2
    l2=l1[no:]+l1[:no]
    print(l2)

    #3
    l3=[]
    l4=[]
    no=len(l1)-2                                                                                #12345  ==45312
    for i in range(len(l1)):
        if i<no:
            l3.append(l1[i])
        else:
            l4.append(l1[i])
    print(l4+l3)


    #1         0 is the 1st
    l2= l1[::]
    l2.append(l2.insert(0,l1[-1]))
    l2.pop()
    l2.pop()
    l2.append(l2.insert(0,l1[-2]))
    l2.pop()
    l2.pop()

    print(l2)


def main():
    l1=[9,8,7,6,5]
    print(l1)                                               #6,5,9,8,7
    fun1(l1)

if __name__ == "__main__":
    main()"""


# 23 Python Program to merge two arrays.
"""
def fun1(l1,l2):
    #1
    l3=l1+l2
    print(l3)


    #2
    # for i in l2:
    #     l1.append(i)
    # print(l1)


    #3
    l1.extend(l2)
    print(l1)

    
def main():
    l1=[1,2,3,4]
    l2=[5,6,7,8,9]
    print("l1 =",l1,"     ","l2= ",l2)                                               #6,5,9,8,7
    fun1(l1,l2)

if __name__ == "__main__":
    main()"""


#24 Python Program to find highest frequency element in array. 1, 2, 3, 4, 5, 6, 5, 4, 5, 1, 2, 3, 4, 5, 6, 5,
"""
"def fun1(l1):
    d1={}
    max=0
    for i in l1:
        if i in d1:
            d1[i]=d1[i]+1
        else:
            d1[i]=1
    print(d1)
    for i ,j in d1.items():
        if j>max:
            max=j
    print(i)
    for i ,j in d1.items():
        if j==max:
            print(i)
def main():
    l1=[1, 2, 3, 4, 5, 6, 5, 4, 5, 1, 2, 3, 4, 5, 6, 5,4,5]
    fun1(l1)

if __name__ == "__main__":
    main()"""



#25   Python Program to add two number using recursion.
"""
def add(num1, num2):
    if num2== 0:
        return num1
    else:
cnum1 = 5
num2 = 7
result = add(num1, num2)
print("The sum of", num1, "and", num2, "is", result)"""



"""
def sum(x, y):
    if (y == 0):
        return x;
    else:
        return (1 + sum(x, y - 1));


x = int(input("Enter number first number: "))
y = int(input("Enter number second number: "))
print("Sum of two numbers are: ", sum(x, y))"""





#####--------DIGIT--------------------#####
#1 Write a program to reverse an integer in Python.\
"""
def fun1(no):
    rev=0
    while no>0:
        r=no%10
        rev=rev*10+r
        #print(r,end="")
        no=no//10
    print(rev)

def main():
    no=12345
    fun1(no)

if __name__ == "__main__":
    main()"""

#2 Write a program in Python to check whether an integer is Armstrong number or not.
"""
def fun1(no):
    c1=0
    while no>0:
        r=no%10
        c1=c1+1
        no=no//10
    return c1
def fun2(no,c1):
    no1=no
    sum = 0
    while no>0:
            r=no%10
            sum=sum+(r**c1)
            no=no//10
    print(sum)

    if no1==sum:
        print("its AMSTRONG")
    else:
        print("not AMSTRONG")
def main():
    no=int(input("enter no  =  "))
    c1=fun1(no)
    fun2(no,c1)
if __name__ == "__main__":
    main()"""

#3 Write a program in Python to check given number is prime or not.
"""
def fun1(no):
    f=0
    if no==1:
        print("Not PRime")
        return
    for i in range(2,no):
        if no%i==0:
            f=1
    if f==1:
        print("not prime")
    else:
        print("prime")
def main():
    no=int(input("enter no  =  "))
    fun1(no)
if __name__ == "__main__":
    main()"""

#4 Write a program in Python to print the Fibonacci series using iterative method.
"""
def fun1(no):
    a=0
    b=1
    t=0

    for i in range(no):
        print(a)
        t=a+b
        a=b
        b=t


def main():
    no=int(input("enter no  =  "))
    fun1(no)
if __name__ == "__main__":
    main()"""

#5 Write a program in Python to print the Fibonacci series using recursive method.
"""
a=0
b=1
t=0
i=0
def  fun1(no):
    global a
    global b
    global t
    global i
    if i<no:
        print(a)
        t=a+b
        a=b
        b=t
        i=i+1
        fun1(no)

def main():
    no=int(input("enter no  =  "))
    fun1(no)
if __name__ == "__main__":
    main()"""

#6  Write a program in Python to check whether a number is palindrome or not using iterative method.
"""
def fun1(no):
    #1
    no1=int(str(no)[::-1])
    if no==no1:
        print("yes")
    else:
        print("no")

    #2
    no2=no
    no3=no
    rev=0
    while 0!=no2:
        r=no2%10
        rev=rev*10+r
        no2=no2//10
        
    if no3 == rev:
        print("yes")
    else:
        print("no")


def main():
    no=int(input("enter no  =  "))
    fun1(no)
if __name__ == "__main__":
    main()"""

#7Write a program in Python to check whether a number is palindrome or not using recursive method.
"""
rev=0
def fun1(no):
    global rev
    global no2
    if 0!=no:
        r=no%10
        rev=rev*10+r
        no=no//10
        fun1(no)
    return rev

def main():
    no=int(input("enter no  =  "))
    rev1=fun1(no)

    if rev1== no:
        print("yes")
    else:
        print("no")
        
if __name__ == "__main__":
    main()"""

# 8 Write a program in Python to find greatest among three integers.
"""
def fun1(no1,no2,no3):
    if no1>no2 and no1>no3:
        print(no1)
    elif no2>no3:
        print(no2)
    else:
        print(no3)
def main():
    no1 = int(input("enter no  =  "))
    no2 = int(input("enter no  =  "))
    no3 = int(input("enter no  =  "))
    fun1(no1,no2,no3)


if __name__ == "__main__":
    main()"""

#9  Write a program in Python to check if a number is binary?
"""
def fun1(no1):
    f=0
    while 0!=no1:
         r=no1%10
         no1=no1//10
         if r!=0 and r!=1:
             f=1
    if f==1:
        print("not")
    else:
        print("yes")

def main():
    no1 = int(input("enter no  =  "))
    fun1(no1)


if __name__ == "__main__":
    main()"""

# 9  Python | Check if a given string is binary string or not
"""
def fun1( str1):
    l1=["1","0"]
    f=0
    for i in str1:
        if i not in l1:
            f=1
    if f==1:
        print("no")
    else:
        print("yes")

def main():
    str1 = str(input("enter no  =  "))
    fun1( str1)


if __name__ == "__main__":
    main()"""

#10  Write a program in Python to find sum of digits of a number using recursion?
"""
sum=0
def fun1(no):
    global sum
    if 0!=no:
        r=no%10
        sum=sum+r
        no=no//10
        fun1(no)
    return sum

def main():
    no = int(input("enter no  =  "))
    sum=fun1( no)
    print(sum)


if __name__ == "__main__":
    main()"""

#11 Write a program in Python to swap two numbers without using third variable?
"""
def main():
    c=5
    d=8
    print("c=",c, "  ","d =",d)

    c=c+d
    d=c-d
    c=c-d
    print("c=",c, "  ","d =",d)


if __name__ == "__main__":
    main()"""

#12  Write a program in Python to swap two numbers using third variab
"""
def main():
    c=5
    d=8
    t=0
    print("c=",c, "  ","d =",d)

    t=c
    c=d
    d=t

    print("c=",c, "  ","d =",d)


if __name__ == "__main__":
    main()"""

#13
#14 #soloa
"""
def main():
    str1=list("solanki")
    str2=list("sagar")
    p=min(len(str1),len(str2))

    l1=[]
    for i in range(len(str2)-1):
        for j in range(i+1,len(str2)):
            if str2[i]==str2[j]:
                l1.extend([i,j])

    print(l1,"lenght=",len(l1))

    a=l1[0]
    b=l1[1]

    for i in range(len(str2)):
        if i==a or i==b:
            print(str1[a],end="")
        elif i==b+1:
            print(str1[b],end="")
        else:
             print(str1[i],end="")

if __name__ == "__main__":
    main()"""

#14 Write a program in Python to add two integer without using arithmetic operator?
"""
def main():
    a=int(input("no= "))
    b=int(input("no= "))

    while (b != 0):
        c=a & b
        a=a^b
        b=c<<1

    print(a)

if __name__ == "__main__":
    main()"""


#15  Write a program in Python to find given number is perfect or not?
"""
def fun1(no):
    sum=0
    for i in range(1,no):
        if no%i==0:
            sum=sum+i
    if no==sum:
        print("YES its perfect no")
    else:
        print("NO perfect no")


def main():
    no=int(input("no= "))
    fun1(no)


if __name__ == "__main__":
    main()"""

#16 Python Program to find the Average of numbers with explanations.
"""
def fun1(l1):
    sum=0
    len1=len(l1)
    for i in l1:
        sum=sum+i
    print("ang=" ,sum/len1)


def main():
    l1=[9,5,7,88,21]
    fun1(l1)


if __name__ == "__main__":
    main()"""

#17      Python Program to calculate factorial using iterative method.
"""
def fun1(no):
    mul=1
    for i in range(no,0,-1):
        mul=mul*i
    print(mul)

def main():
    no=int(input("enter no=  "))
    fun1(no)


if __name__ == "__main__":
    main()"""

#18   Python Program to calculate factorial using recursion
"""
mul=1
i=1
def fun1(no):
    global mul
    global i
    if  i<no+1:
        mul=mul*i

        i=i+1
        fun1(no)
    return mul


def main():
    no=int(input("enter no=  "))
    print(fun1(no))


if __name__ == "__main__":
    main()"""

#19  Python Program to check a given number is even or odd.
"""
def fun1(no):
    if no%2==0:
        print("EVEN")
    else:
        print("ODD")
def main():
    no=int(input("enter no=  "))
    fun1(no)

if __name__ == "__main__":
    main()"""

#20  Python program to print first n Prime Number with explanation.
"""
def fun1(no):
   for i in range(2,no):
       for j in range(2,i):
           if i%j==0:
                break
       else:
            print(i,end=",")

def main():
    no=int(input("enter no=  "))
    fun1(no)

if __name__ == "__main__":
    main()"""

#21


#23  Python program to calculate the power using the POW method
"""
def fun1(no,no1):
   print(pow(no,no1))

def main():
    no=int(input("enter no=  "))
    no1=int(input("enter no=  "))

    fun1(no,no1)

if __name__ == "__main__":
    main()"""

#24  Python Program to calculate the power without using POW function.(using for loop)
"""
def fun1(no,no1):
    
    m=1
    for i in range(no1):
        m=m*no
    print(m)

def main():
    no=int(input("enter no=  "))
    no1=int(input("enter no=  "))

    fun1(no,no1)

if __name__ == "__main__":
    main()"""

#25  Python Program to calculate the power without using POW function.(using while loop)
"""
def fun1(no, no1):
    m = 1
    i=0
    while i<no1:
        m=m*no
        i=i+1
    print(m)

def main():
    no = int(input("enter no=  "))
    no1 = int(input("enter no=  "))

    fun1(no, no1)


if __name__ == "__main__":
    main()"""

#26 Python Program to calculate the square of a given numbe
"""
def main():
    no = int(input("enter no=  "))

    print(no**2)


if __name__ == "__main__":
    main()"""

#27   Python Program to calculate the cube of a given numbe
"""
def main():
    no = int(input("enter no=  "))

    print(no**3)


if __name__ == "__main__":
    main()"""



#1
"""
def main():
    no = int(input("enter no=  "))
    x=0
    no1=no
    while no!=0:
        reminder=no%10
        x=x*10+reminder
        no=no//10
        
    if x==no1:
        print(" yes p ")
    else:
        print("not")

if __name__ == "__main__":
    main()"""

#2
"""
def main():
    no = int(input("enter no=  "))

    #1
    len1=len(str(no))

    x=0
    no1=no
    #2
    while no!=0:
        r=no%10
        x=x+r**len1
        no=no//10

    print(x)
    if x==no1:
        print("yes amstrong")
    else:
        print("no")


if __name__ == "__main__":
    main()"""

#3
"""
def main():
    l1=["a","c","f","g"]
    #print(len(l1))

    len1=0
   
    for i in l1:
        len1=len1+1

    print(len1)

if __name__ == "__main__":
    main()"""


#4
"""
def main():
    no=int(input("enter no= "))
    f=0
    
    if no==1:
        print("not prime")
        return

    elif no>1:
        for i in range(2,no):
            print(i)
            if no%i==0:
                 f=1
        if f == 1:
            print("not prime ")
        else:
            print("yes ")


if __name__ == "__main__":
    main()"""


#5
"""
def main():
    no=int(input("enter no= "))
    a=0
    b=1
    temp=0

    for i in range(no):
        print(a)
        temp=a+b
        a=b
        b=temp

if __name__ == "__main__":
    main()"""

#6
"""
def main():
    a=22
    b=7
    c=12

    if ( a>b and a>c):
        print(a)

    elif b>c:
        print(b)

    else:
        print(c)

if __name__ == "__main__":
    main()"""

#7 Write a program in Python to check if a number is binary?
"""
def main():
    no=int(input("enter no= "))
    f=0
    l1=[0,1]

    for i in str(no):
        if int(i) not in l1:
            f=1
    if f==1:
        print("not binary")
    else:
        print("binary")

    # while no!=0:
    #     r=no%10
    #     if r not in l1:
    #         f=1
    #     no=no//10
    #
    # if f==1:
    #     print("not binary")
    # else:
    #     print("binary")

if __name__ == "__main__":
    main()"""


#8 Write a program in Python to find sum of digits of a number
"""
def main():
    no=int(input("enter no= "))
    sum=0
    # for i in str(no):
    #     sum=sum+int(i)
    # print(sum)

    while no!=0:
        r=no%10
        sum=sum+r
        no=no//10
    print(sum)


if __name__ == "__main__":
    main()"""

#9 Write a program in Python to swap two numbers without using third variable
"""
def main():
    a=100
    b=200
    print(" a=",a)
    print("b= ",b)

    print()

    a=a+b
    b=a-b
    a=a-b

    print(" a=", a)
    print("b= ", b)


if __name__ == "__main__":
    main()"""


#10 Write a program in Python to find prime factors of a given integer.
"""
def fun1(no):
    if no>1:
        for num  in range(2,no):  
            for j in range(2,num): 
                if  num%j==0:
                    break
            else:
                print(num)

def main():
    no=int (input ("enter no= "))
    fun1(no)
    
if __name__ == "__main__":
    main()"""


#11 Write a program in Python to find given number is perfect or not
"""
def fun1(no):
    sum=0
    for i in range(1,no):
        if no%i==0:
            sum=sum+i
    if sum==no:
        print("its perfect number")
    else:
        print("not ")

def main():
    no = int(input("enter no= "))
    fun1(no)

if __name__ == "__main__":
    main()"""


#12 Python Program to find the Average of numbers with explanations.
"""
def fun1(l1):
    len1=len(l1)
    print(len1)
    sum=0

    for i in l1:
        sum=sum+i
    print(sum)

    avg=sum//len1
    print("avg= " ,avg)

def main():
    l1=[4, 5, 1, 2]
    fun1(l1)

if __name__ == "__main__":
    main()"""

#13 Python Program to calculate factorial using iterative method.
"""
def fun1(no):
    mul=1
    for i in range(1,no+1):
        mul=mul*i
    print(mul)
def main():
    no=int(input("enter no= "))
    fun1(no)

if __name__ == "__main__":
    main()"""

#14
"""
def fun1(no):
    mul=1
    i=1               
    while i !=(no+1):
        mul=mul*i
        i=i+1#2
    print(mul)
def main():
    no=int(input("enter no= "))
    fun1(no)

if __name__ == "__main__":
    main()"""

#15 Python Program to check a given number is even or odd.
"""
def fun1(no):
   if no%2==0:
       print("even")
   else:
       print("odd")
def main():
    no=int(input("enter no= "))
    fun1(no)

if __name__ == "__main__":
    main()"""

#16
def fun1(l1):
    temp=0
    len1=len(l1)
    for i in range(8):
        for j in range(i+1,8):
            if l1[i]<l1[j]:
                temp=l1[i]
                l1[i]=l1[j]
                l1[j]=temp

    print(l1)
    print(l1[1])

def main():
    l1=[4,3,47,15,21,46,24,48]
    fun1(l1)

if __name__ == "__main__":
    main()