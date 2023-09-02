#lists dublicate element
"""
def main():
    l1=[1,3,5,2,3,5,2,1]
#1
    max1=0
    for i in l1:
        if i>max1:
            max1=i
    print("max1=",max1)

#2
    max2=max(l1)
    print("max2=",max2)

#3
    l1.sort(reverse=True)
    print("max3=",l1[0])

if __name__=="__main__":
    main()"""

#last 3rd highest no list
"""
def main():

    l1=[1,3,4,5,6,7,8,9,15,16,18]
    l2=l1.copy()[::-1]
    print("3rd highest no=",l2[2])


if __name__=="__main__":
    main()"""


#check nos atre anagram or not
"""
def main():
    no1=int(input("enter no1="))
    no2=int(input("enter no2="))
    l1=[]
    l2=[]
    while no1!=0:
        rem=no1%10
        l1.append(rem)
        no1=no1//10

    while no2!=0:
        rem=no2%10
        l2.append(rem)
        no2=no2//10

    if  all(i in l1 for i in l2):
        print("its anagram")
    else:
        print(" its not anagram")


if __name__=="__main__":
    main()"""

#palindrome
"""
def main():
    no=121
    no1=no
    k=0
    while no!=0:
        rem=no%10
        k=(k*10)+rem
        no=no//10
    if  k==no1:
        print("yes")
    else:
        print("no")
if __name__=="__main__":
    main()"""

#amstrong
"""
def count(no):
        cnt=0
        while(no!=0):
            irem=no%10
            cnt=cnt+1
            no=no//10
        return cnt
def  power(rem,cnt):
        imult=1
        for i in range(1,cnt+1):
            imult=imult*rem
        return imult

def ana(no):
    no1=no
    sum=0
    disum=count(no)
    while no!=0:
        rem=no%10
        sum=sum+power(rem,disum)
        no=no//10

    if no1==sum:
        print("its amstrong")
    else:
        print("its not amstrong")
def main():
    no=int(input("enter no="))
    ana(no)
if __name__=="__main__":
    main()"""



#factorial
"""
def fact(no):
    mul=1
    for i in range(1,no):
        mul=mul*i
    return mul
def main():
    no=int(input("enter no="))
    x=fact(no)
    print("factoral=",x)

if __name__=="__main__":
    main()"""

#find index
"""
def index1(l1,no):
    for i in range(len(l1)):
        if l1[i]==no:
            print("index=",i)
        else:
            flag=1
    if flag==1:
        print("no such elemnt present")
def main():
    l1=[1,2,3,4,6,8,10,49]
    no=int(input("enter no="))
    index1(l1,no)
if __name__=="__main__":
    main()"""

#perfect no
"""
def perfct(no):
    sum=0
    no1=int(no/2)
    for i in range(1,no1+1):
        if no%i==0:
            sum=sum+i

    if sum==no:
        print("its perfect")
    else:
        print("not a perfect")


def main():
    no=int(input("enter no="))
    perfct(no)
if __name__=="__main__":
    main()"""

#sorting list:
"""
def main():
    l1=[1,6,8,3,7,2]
    for i in range(len(l1)-1):
        for j in range(i+1,len(l1)):
            if l1[i]>l1[j]:
                temp=l1[i]
                l1[i]=l1[j]
                l1[j]=temp
    print(l1)

if __name__=="__main__":
    main()"""

#sum of list elemn
"""
def sum_eve(l1):
    sum1=0
    sum2=0
    for i in l1:
        if  i%2==0:
            sum1=sum1+i
        else:
            sum2=sum2+i
    print("sum of even=", sum1)
    print("diff of odd =",sum2)
    
    
    if sum1>sum2:
        diff1=sum1-sum2
        print("diff of odd even=",diff1)
    else:
        diff2=sum2-sum1
        print("diff of odd even=",diff2)

def  add(l1):
    sum=0
    for i in l1:
        sum=sum+i
    return    sum
def main():
    l1=[1,2,2,3,4,5,6,7,8,9,10]
    sum=add(l1)
    print("total of list=",sum)
    sum_eve(l1)

if __name__=="__main__":
    main()"""

#list implace
def  implace(l1):
    no=len(l1)-1
    end=l1[no]
    start=l1[0]
    temp=0
    while end>start:
        temo=start
        start=end
        end=start
        end=end-1
        start=start+1
    print(l1)

def main():
    l1=[2,4,6,7,8,1,7,55]
    implace(l1)
if __name__=="__main__":
    main()












