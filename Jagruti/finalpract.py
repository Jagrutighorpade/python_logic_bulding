"""
#1
def str(name):
    for char in name:
        print(char)
def main():
    str("jagruti")
if __name__=="__main__":
    main()"""

#2 occurance
"""
def str(name1):
    name=name1.lower()
    vowel="aeiou"
    count=0
    for char in name:
        for i in vowel:
            if char==i:
                count=count+1
    print(count)
def main():
    str(" Hello World")
if __name__=="__main__":
    main()"""

#vice versa
#1
"""
def str(name1):
    name=name1.swapcase()
    print(name)
def main():
    str(" Hello World")
if __name__=="__main__":
    main()"""


#2
"""
def str(name):
    for i in name:
        if  ord(i)<97 and ord(i)!=(32) :
            print(chr(ord(i)+32),end="")
        elif ord(i)>97:
            print(chr(ord(i)-32),end="")
        else:
            print(" ",end="")
def main():
    str("Hello World")
if __name__=="__main__":
    main()"""

#reverse
#1
"""
def str(name1):
    name=list(name1)
    print(name)
    for i in range(len(name)-1,-1,-1):
        print(name[i],end="")
    #print(name)
def main():
    str("Hello World")
if __name__=="__main__":
    main()"""

#2
"""
def str(name1):
    a=name1[: :-1]
    print(a)
def main():
    str("Hello World")
if __name__=="__main__":
    main()"""

#3
"""
def str(name):
    l1=list(name)
    st_i=0
    ed_i=len(l1)-1
    temp=0
    while st_i < ed_i:
        temp=l1[st_i]
        l1[st_i]=l1[ed_i]
        l1[ed_i]=temp

        st_i=st_i+1
        ed_i=ed_i-1
    for i in l1:
        print(i,end="")


def main():
    str(" Hello World ")
if __name__=="__main__":
    main()"""


#palindrome
#1
"""
def str1(name):
    name1=name[::-1]
    if name== name1:
        print("its palllindrome")
    else:
        print("its not Pallindrom")
def main():
    str1(str (input("enter name  = ")))
if __name__=="__main__":
    main()"""


#2
"""
def str1(name):
    l1=list(name)
    l2=list(name)
    st_i=0
    ed_i=len(l1)-1
    temp=0
    while st_i < ed_i:
        temp=l1[st_i]
        l1[st_i]=l1[ed_i]
        l1[ed_i]=temp

        st_i=st_i+1
        ed_i=ed_i-1

    if l2==l1:
        print("its pallindrome")
    else:
        print("its not pallindrome")

def main():
    str1(str(input("enter name = ")))
if __name__=="__main__":
    main()"""


#anagram
#1
"""
def ana(a,b):
    if(sorted(a)==sorted(b)):
        print("its Anagram")
    else:
        print("its not Anagram")

def main():
    name1=(str(input("enter name1 = ")))
    name2= (str(input("enter name2 = ")))
    ana(name1,name2)

if __name__=="__main__":
    main()"""

#2
"""
def ana(a,b):
    l1=list(a)
    l2=list(b)

    temp1=0
    temp2=0
    
    for i in range(0,len(l1)):
        for j in range(i+1,len(l1)):
            if ord(l1[i]) > ord(l1[j]):   #            if ord(l1[i]) < ord(l1[j]):
                temp=l1[i]
                l1[i]=l1[j]
                l1[j]=temp

    for i in range(0,len(l2)):
        for j in range(i+1,len(l2)):
            if ord(l2[i]) > ord(l2[j]):   #            if ord(l1[i]) < ord(l1[j]):
                temp1=l2[i]
                l2[i]=l2[j]
                l2[j]=temp1

    if str(l1)==str(l2):
        print("its Anagram")
    else:
        print("its not Anagram")

def main():
    name1=(str(input("enter name1 = ")))
    name2=(str(input("enter name1 = ")))

    ana(name1,name2)

if __name__=="__main__":
    main()"""

#count specific char ---not working
"""
def cnt(a):
    l1=list(a)
    sum=0
    i=0
    j=0
    l2=[]
    for i in range(len(l1))
        sum=0
        for j in range(len(l1)):
            if  (l1[i] == l1[j]):
                sum=sum+1
        l2.append(sum)
    for k in range(len(l1)):
        print(f"latter is count {l2[k]}")

def main():
    name1=(str(input("enter name1 = ")))
    cnt(name1)

if __name__=="__main__":
    main()"""

#replace
"""
#1
def cnt(name1,char1,char2):
    name=list(name1)
    for i in name:
        if i==char1 :
            print(char2,end="")
        else:
            print(i,end="")
def main():
    name1=(str(input("enter name1 = ")))
    char1=str(input("enter char which replace ="))
    char2=str(input("enter char  you want ="))

    # cnt(name1,char1,char2)

if __name__=="__main__":
    main()"""

#2
"""
def main():
    name1="aaaannnngggg"
    x=name1.maketrans("a","y")
    print(name1.translate(x))

if __name__=="__main__":
    main()"""


#count white spaces
"""
def cnt(name):
    count = 0
    for i in name:
       # if ord(i)==(32):
       if i==" ":
            count=count+1
    print(count)
def main():
    name1=(str(input("enter name1 = ")))
    cnt(name1)
if __name__=="__main__":
    main()"""


#amstrong
"""
len1=0
def lenght(no):
    while no!=0:
        r=no%10
        global len1
        len1=len1+1
        no=no//10
def  ams(no):
    no1=no
    sum=0
    while no!=0:
        r=no%10
        sum=sum+(r**len1)
        no=no//10
    if no1==sum:
        print("its Amstrong ")
    else:
        print("its no Amstrong")

def main():
    no=(int(input("enter name1 = ")))
    lenght(no)
    ams(no)
if __name__=="__main__":
    main()"""


#2
"""
def lenght(no):
    no1=no
    no2=no
    sum=0
    len1=0
    flag=0
    while no!=0:
        r=no%10
        len1=len1+1
        no=no//10
    print(len1)
    while no1!=0:
        r1=no1%10
        sum=sum+(r1**len1)
        no1=no1//10
    print(sum)
    if no2==sum:
        flag=1
        print("its Amstrong ")
    else:
        print("its not Amstrong")

def main():
    no=(int(input("enter name1 = ")))
    lenght(no)
if __name__=="__main__":
    main()"""


#  find the characters at an odd position
"""
def main():
    str1="Hello World"
    l1=list(str1)
    len1=len(l1)-1
    for i in range(len1):
        if i%2!=0 :
            print(l1[i],end="")
if __name__=="__main__":
    main()"""

#remove\n
"""
def main():
    str1="\nHello\nWorld\nPune"
    for i in str1:
        if i=="\n":
            print(" ",end="")
        else:
            print(i ,end="")
if __name__=="__main__":
    main()"""

#sub string elemt in main string
"""
def main():
    str1="jagruti"
    str2="skruti"
    for i in str1:
         for j in str2:
             if i==j:
                 print(i,end="")
if __name__=="__main__":
    main()"""

#list
"""
def main():
    l1=[10,20,30,40]
    print(l1)
    l2=[]
    l3=[]
    l4=[]
    sum=0
    mul=0
    add=0
    for i in range(0,len(l1)-1):
        sum=l1[i]+l1[i+1]
        l2.append(sum)
    print(l2)

    for j in range(0,len(l2)-1):
        mul=l2[j]*l2[j+1]
        l3.append(mul)
    print(l3)


    for k in range(0,len(l3)-1):
        add=l3[k]+l3[k+1]
        l4.append(add)
    print(l4)
if __name__=="__main__":
    main()"""

#duplicate elemnt
"""
list1 = [1,2,3,4,5,6,6]
list2 = []

for i in list1:
    if i not in list2:
        list2.append(i)

    else:
        print(i)

print(list2)"""

#2
"""
l1 = [1,1,2,3,4,5,6,6]
l2 = []

for i in range(len( l1)):
    for j in range(i+1,len(l1)):
        if l1[i]==l1[j]:
            l2.append(l1[i])

print(l2)"""

#sorting without sort
"""
def main():
    l1=[2,4,7,4,3,9]
    temp=0
    for i in range(0,len(l1)):
        for j in range(i+1,len(l1)):
            if l1[i] >l1[j]:
                temp=l1[i]
                l1[i]=l1[j]
                l1[j]=temp
    print(l1)

if __name__=="__main__":
    main()"""

#two list as key value
"""
def main():
    l1=["a","b","c"]
    l2=[1,2,3,4]

    d1={i:j for i ,j in zip(l1,l2)}
    print(d1)


    d2=dict(zip(l1,l2))
    print(d2)

    d3={l1[i]:l2[i] for i in range(len(l1))}
    print(d3)

if __name__=="__main__":
    main()"""

# # Accessing the List Element with Index
"""
def main():
    l1=["a","b","c"]
    for i in range(len(l1)):
        print(i, "=",l1[i])


    for j,k in enumerate(l1):
        print(j,"=",k)


if __name__=="__main__":
    main()"""



#Second Max No In List
"""
def main():
    l1=[50,20,40,90,10]
    temp=0
    for i in range(len(l1)):
        for j in range(i+1,len(l1)):
            if l1[i]>l1[j]:
                temp=l1[i]
                l1[i]=l1[j]
                l1[j]=temp
    print("2nd max elemrnt=",l1[-2])
if __name__=="__main__":
    main()"""

# max no of list
#1
"""
def main():
    l1=[50,20,40,90,10]
    temp=0
    for i in range(len(l1)):
        for j in range(i+1,len(l1)):
            if l1[i]>l1[j]:
                temp=l1[i]
                l1[i]=l1[j]
                l1[j]=temp
    print("max elemrnt=",l1[-1])
if __name__=="__main__":
    main()"""

#2
"""
def main():
    l1=[50,20,40,90,100]
    max=l1[0]
    for i in l1:
        if  i >max:
            max=i
    print(max)
if __name__=="__main__":
    main()"""

#min element in list
"""
def main():
    l1=[50,20,40,90,10]
    min=l1[0]
    for i in l1:
        if  i <min:
            min=i
    print(min)
if __name__=="__main__":
    main()"""

#reverse list
"""
def main():
    l1=[50,20,40,90,10]
    t=0
    s_i=0
    e_i=len(l1)-1
    while s_i<e_i:
        t=l1[s_i]
        l1[s_i]=l1[e_i]
        l1[e_i]=t

        s_i=s_i+1
        e_i=e_i-1

    print(l1)
    # for i in l1:
    #     print(i,end=" ,")
if __name__=="__main__":
    main()"""

#count occurance of element in list
"""
def main():
    l1=[50,20,20,90,10,10,30,20]
    d1={}
    for i in l1:
        if ( i in d1):
            d1[i]=d1[i]+1
        else:
            d1[i]=1
    print(d1)
if __name__=="__main__":
    main()"""

##list to string
"""
def main():
    l1=["a","n","b"]
    for i in l1:
        print(str(i),end="")
        # print(type(str(i)))
if __name__=="__main__":
    main()"""


"""
#list to dict
from collections import Counter

list = [1,2,3,4,5,6,1,2,3,4,5,6]

res = Counter(list)
print(res)"""

"""
# combining lists
a =[1,2,3]
b = [4,5,6]

res = [(x,y) for x in a for y in b]
print(res)

print("\r")
#
for i in a:
    for j in b:
        print((i,j),",",end="")"""


"""
# swapping
list = [6, 2, 7, 8]
print('list before swapping:', list)
list[1], list[3] = list[3], list[1]
print( list)"""



#Sorting
"""
def dicti(d):

    for i in sorted(d.items()):
        print(i,end=" ")

d = {3:'om', 2:'Pattern', 1:'ram', 6:'Hey', 8:'Love'}
#print(d.keys())
(dicti(d))"""


"""
# Append Dictionary Keys and Values into single list
d = {'a':1, 'b':2, 'c':3, 'd':4}

res = list(d.keys()) + list(d.values())
print(res)"""

#add elemrnt in dict
"""
def main():
    d1= {'a': 10, 'e': 2, 'z': 8, 'd': 10}
    d1["r"]=11
    print(d1)
    d1.update({"y":100})
    print(d1)
if  __name__=="__main__":
    main()"""


#list to dict:
"""
def main():
    l1=[1,"a",2,"b",3,"c"]
    d2={ l1[i]:l1[i+1] for i in range(0,len(l1),2)}
    print(d2)
if  __name__=="__main__":
    main()"""

#list of tuple from dict
"""
def main():
    d1= {'a': 10, 'e': 2, 'z': 8, 'd': 10}
    l1=list(d1.items())
    print(l1)
    
    l4=[(x,y) for x,y in d1.items()]
    print(l4)

#list from dict
    l2=[key  for key in d1.keys()]
    l3=[val for val in d1.values()]
    
    l2.extend(l3)
    print(l2)

if  __name__=="__main__":
    main()"""

#sum of values in dict
"""
def main():
    d1= {'a': 101, 'e': 22, 'z': 81, 'd': 10}
    for no in d1.values():
        sum=0
        while no != 0:
            r = no % 10
            sum = sum + r
            no = no // 10
        print(sum)
if  __name__=="__main__":
    main()"""


#mul of values in dict
"""
def main():
    d1= {'a': 100, 'e': 22, 'z': 81, 'd': 1010}
    for no in d1.values():
        mul=1
        while no != 0:
            r = no % 10
            if r!=0:
                mul = mul * r
            no = no // 10
        print(mul)
if  __name__=="__main__":
    main()"""


# count key
"""
def main():
    d1= {1:"aaaa",   2:"POOja"  ,3:"mau"}
    for str1 in d1.values():
        c1 = 0
        c2 = 0
        for char in str1:
            if ord(char) <97:
                c1=c1+1
            else:
                c2=c2+1
        print(str1,"=","capital =",c1 , " ,", "samll=",c2)

if  __name__=="__main__":
    main()"""


#__________________________*******************________________
#recursion
#count white spaces
"""
c1=0
i=0
def wht(str1):
    global c1
    global i
    if (i<len(str1)):
        if str1[i]==' ':
          c1=c1+1
        i=i+1
        wht(str1)
    return c1
def main():
    l1=list("Hello world pune nashik")
    print(wht(l1))

if  __name__=="__main__":
    main()"""


#lagest digit
"""
max=0
def lrgD(no):
    global max
    if no!=0:
        r=no%10
        if r>max:
            max=r
        no = no // 10

        lrgD(no)
    return max

def main():
    no=int(input("enter no="))
    print(lrgD(no))

if  __name__=="__main__":
    main()"""

#count small char in str
"""
c1=0
i=0
def count1(l1):
    global c1
    global i

    if (i<len(l1)):
        if (ord(l1[i])>=97):
            c1=c1+1
        i=i+1
        count1(l1)
        return c1

def main():
    str1=str(input("enter name="))
    l1=list(str1)
    print(count1(l1))

if  __name__=="__main__":
    main()"""

#smallest  digit in no
"""
min=9
def smllD(no):
    global min
    if no!=0:
        r=no%10
        if r<min:
            min=r
        no = no // 10

        smllD(no)
    return min

def main():
    no=int(input("enter no="))
    print(smllD(no))

if  __name__=="__main__":
    main()"""


#reverse no
"""
def rev(no):
    if no!=0:
        r=no%10
        print(r,end="")
        no = no // 10
        rev(no)

def main():
    no=int(input("enter no="))
    rev(no)

if  __name__=="__main__":
    main()"""


#pattern1
"""
i=0
def pat(no):
    global i
    if (i<no):
        print("*",end="  ")
        i=i+1
        pat(no)

def main():
    no=int(input("enter no="))
    pat(no)

if  __name__=="__main__":
    main()"""

#pattern2
"""
i=1
def pat(no):
    global i
    if (i<=no):
        print(i,end="  ")
        i=i+1
        pat(no)

def main():
    no=int(input("enter no="))
    pat(no)

if  __name__=="__main__":
    main()"""

#pattern3
"""
def pat(no):
    if (no>=1):
        print(no,end="  ")
        no=no-1
        pat(no)

def main():
    no=int(input("enter no="))
    pat(no)

if  __name__=="__main__":
    main()"""

#pattern4(AtoZ)
"""
i=0
def pat(no):
    global i
    if (i<no):
        print(str(chr(i+65)))
        i=i+1
        pat(no)

def main():
    no=int(input("enter no="))
    pat(no)

if  __name__=="__main__":
    main()"""

#pattern5(atoz)
"""
i=0
def pat(no):
    global i
    if (i<no):
        print(str(chr(i+97)))
        i=i+1
        pat(no)

def main():
    no=int(input("enter no="))
    pat(no)

if  __name__=="__main__":
    main()"""

#pattern 6
"""
def pat(no):
    if (no>=1):
        print(no , " " ,"*",end="  ")
        no=no-1
        pat(no)

def main():
    no=int(input("enter no="))
    pat(no)

if  __name__=="__main__":
    main()"""

#sum
"""
sum=0
def  cnt(no):
    global sum
    if no!=0:
        r=no%10
        sum=sum+r
        no=no//10
        cnt(no)
    return sum
def main():
    no=int(input("enter no="))
    print(cnt(no))

if  __name__=="__main__":
    main()"""

#count chr in str
"""
c1=0
i=0
def  cnt(name):
    global c1
    global i
    if (i<len(name)):
        c1=c1+1
        i=i+1
        cnt(name)
    return c1

def main():
    name=str(input("enter name="))
    print(cnt(name))

if  __name__=="__main__":
    main()"""

#factorial
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

#mul
"""
mul=1
def  cnt(no):
    global mul
    if no!=0:
        r=no%10
        mul=mul*r
        no=no//10
        cnt(no)
    return mul
def main():
    no=int(input("enter no="))
    print(cnt(no))

if  __name__=="__main__":
    main()"""

#sum of list
"""
sum=0
i=0
def  cnt(l1):
    global sum
    global i
    if (i<len(l1)):
        sum=sum+l1[i]
        i=i+1
        cnt(l1)
    return sum
def main():
    l1=[1,2,3,4,5]
    print(cnt(l1))

if  __name__=="__main__":
    main()"""

####

def ord(a,b,c):
    if a>b and  a>c:
        print(a)
    elif b>c:
        print(b)
    else:
        print(c)


def main():
     a=int(input("enter="))
     b=int(input("enter="))
     c=int(input("enter="))


     (ord(a,b,c))


if __name__ == "__main__":
     main()"""

















































