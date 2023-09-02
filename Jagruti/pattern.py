"""
def main():
    for i in range(1,11 ):
        for j in range(1,11):
            print(i,"=",j,end="    ,    ")
        print("\r")

if __name__=="__main__":
    main()"""

#1
"""
def main():
    for i in  range(1,5):
        for j in range(1,5):
            if 5-i<=j:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print("\r")

if __name__=="__main__":
    main()"""



#6
"""
def main():
    for i in  range(1,5):
        for j in range(1,5):
            if 5-i>=j:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print("\r")

if __name__=="__main__":
    main()"""

#2
"""
def main():
    for i in  range(1,5):
        for j in range(1,5):
            if i==j:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print("\r")


if __name__=="__main__":
    main()"""


#3
"""
def main():
    for i in  range(1,5):
        for j in range(1,5):
            if i>=j:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print("\r")

if __name__=="__main__":
    main()"""

#4
"""
def main():
    for i in  range(1,5):
        for j in range(1,5):
                print("*",end=" ")
        print("\r")

if __name__=="__main__":
    main()"""

#5
"""
def main():
    for i in  range(1,5):
        for j in range(1,5):
            if i==4 or j==1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print("\r")

if __name__=="__main__":
    main()"""

#7
"""
def main():
    for i in  range(1,5):
        for j in range(1,5):
            if i<=j:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print("\r")

if __name__=="__main__":
    main()"""

#8
"""
def main():
    c=0
    for i in  range(1,5):
        for j in range(1,5):
            c=c+1
            print(c,end="      ")
        print("\r")

if __name__=="__main__":
    main()"""

#9
"""
def main():
    c=11
    for i in  range(1,4):
        for j in range(1,4):
            c=c-1
            print(c,end="      ")
        print("\r")

if __name__=="__main__":
    main()"""

#10
"""
def main():
    c=16
    for i in  range(1,4):
        for j in range(1,4):
            c=c-i
            print(c,end="      ")
        print("\r")

if __name__=="__main__":
    main()"""

#11
"""
def main():
    c=0
   # p=0
    for i in  range(1,5):
        for j in range(1,5):
             c=c+1
        #     if c<=9:
        #         print(c,end=" ")
        #     else:
        #         p=p+1
        #         print(p,end=" ")
        # print("\r")
        c = c + 1
        if c == 10:
            c = 1
        print(c, end=" ")
        print("\r")


if __name__=="__main__":
    main()"""

#12
"""
def main():
    for i in  range(1,5):
        for j in range(1,6):
            if (i==1)or (i==4) or(j==1)or (j==5):
                print("#",end="  ")
            else:
                print("@",end=" ")
        print("\r")
if __name__=="__main__":
    main()"""

#13
#1.1
"""
def main():

    for i in  range(1,5):
        for j in range(1,5):
            if  j<=4-i:
                print("@",end=" ")
            else:
                print("*",end="   ")
        print("\r")

if __name__=="__main__":
    main()"""

#1.2
"""
def main():
    for i in  range(1,5):
        for j in range(1,5):
            if  5-i<=j:
                print("*",end="   ")
            else:
                print("@",end=" ")
        print("\r")

if __name__=="__main__":
    main()"""

#14
#1.1
"""
def main():

    for i in  range(1,5):
        for j in range(1,5):
            if  j<=i:
                print("#",end=" ")
            else:
                print("*",end="  ")
        print("\r")

if __name__=="__main__":
    main()"""

#1.2
"""
def main():

    for i in  range(1,5):
        for j in range(1,5):
            if  i<j:
                print("*",end="  ")
            else:
                print("#",end=" ")
        print("\r")
if __name__=="__main__":
    main()"""

#15
"""
def main():

    for i in  range(1,6):
        for j in range(1,6):
            if  i==j or (i==5 and j==1)or (i==4 and j==2) or(i==2 and j==4)or(i==1and j==5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print("\r")
if __name__=="__main__":
    main()"""


#16
"""
def main():
    name="Hello World"
    l1=list(name)
    s_i=0
    e_i=len(l1)-1
    temp=0
    while s_i<e_i:
        temp=l1[s_i]
        l1[s_i]=l1[e_i]
        l1[e_i]=temp

        s_i=s_i+1
        e_i=e_i-1

    name1="".join(l1)
    print(name1)

if __name__=="__main__":
    main()"""

#17
"""
def main1(str1):
    for i in  range(1,len(str1)+1):
        for j in str1 :
            print(j,end="   ")
        print("\r")

def main():
    str1="hello"
    main1(str1)
if __name__=="__main__":
    main()"""

#18
"""
def main():

    for i in  range(1,6):
        for j in range(1,6):
            if  i==3 or j==3:
                print("@",end="  ")
            else:
                print("*",end="    ")
        print("\r")
if __name__=="__main__":
    main()"""

#19
"""
def main():

    for i in  range(1,6):
        for j in range(1,5):
            if  i==5 or j==1 or i==j:
                print("*",end="  ")
            else:
                print(" ",end=" ")
        print("\r")
if __name__=="__main__":
    main()"""

#20
"""
def main():

    for i in  range(1,5):
        for j in range(1,5):
            if  i>=j:
                print(i+1,end="  ")
            else:
                print(" ",end=" ")
        print("\r")

    for i in  range(1,5):
        for j in range(1,5):
            if  j<=5-i:
                print(6-i,end="  ")
            else:
                print(" ",end=" ")
        print("\r")
if __name__=="__main__":
    main()"""

#21
"""
for i in range(1, 5):
    for j in range(1, 5):
        if j<=5-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("\r")"""


#

for i in range(1, 6):
    for j in range(1, 6):
        if i==1 or j==1 or i==5 or j==5 or i==j or (i==2 and j==4)or(i==4 and j==2):
            print("*", end="  ")
        else:
            print("  ", end="  ")
    print("\r")










