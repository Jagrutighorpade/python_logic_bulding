#1
"""
def fun(no):
    for i in range(no):
        print(chr(65+i),end="  ")
def main():
    no=int(input("enter no="))
    fun(no)
if __name__ == "__main__":
    main()"""

#2---
"""
def fun(no):
    for i in range(no,0,-1):
        print(i,"#",end="  ")
def main():
    no=int(input("enter no="))
    fun(no)
if __name__ == "__main__":
    main()"""

#3
"""
def fun(no):
    for i in range(len(no)-1,-1,-1):
        print(no[i],end="")
def main():
    no=str(input("enter no="))
    fun(no)
if __name__ == "__main__":
    main()"""

#4
"""
def fun(no):
    for i in range(1,no+1):
        print(i,"#",end="  ")
def main():
    no=int(input("enter no="))
    fun(no)
if __name__ == "__main__":
    main()"""

#5
"""
def fun(no):
    for i in range(1,no+1):
        print("*",i,"#",end="  ")
def main():
    no=int(input("enter no="))
    fun(no)
if __name__ == "__main__":
    main()"""

#6
"""
def fun(no):
    for i in range(1,no+1):
        print(i*2,end="  ")
def main():
    no=int(input("enter no="))
    fun(no)
if __name__ == "__main__":
    main()"""

#7
"""
def fun():
    for i in range(4):
        for j in range(3):
            print("*",end="       ")
        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#8
"""
def fun():
    for i in range(4):
        for j in range(1,3+1):
            print(j,end="       ")
        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""


#9
"""
def fun():
    for i in range(3):
        for j in range(5,0,-1):
            print(j,end="       ")
        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#10
"""
def fun():
    for i in range(3):
        for j in range(3):
            print("*","     ","#",end="     ")
        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#11
"""
def fun():
    for i in range(1,3+1):
        for j in range(4):
            print(i,end="     ")
        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#12
"""
def fun():
    for i in range(4):
        for j in range(4):
            print(chr(65+j),end="     ")
        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#13
"""
def fun():
    for i in range(0,4):
        for j in range(0,4):
            if  i%2==0:
                print(chr(65+j),end="     ")
            else:
                print(chr(97 + j), end="     ")

        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#14
"""
def fun():
    for i in range(0,3):
        for j in range(0,5):
            print(chr(65+i),end="      ")
        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#15
"""
def fun():
    for i in range(4,0,-1):
        for j in range(0,5):
            print(i,end="      ")
        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#16
"""
def fun():
    sum=0
    for i in range(1,4):
        for j in range(1,5):
            sum=sum+1
            print(sum,end="      ")
        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#17
"""
def fun():
    sum=0
    sum1=0
    for i in range(1,5):
        for j in range(1,5):
            sum=sum+1
            if sum<10:
                print(sum,end="      ")
            else:
                sum1=sum1+1
                print(sum1,end="       ")

        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""


#18-----
"""
def fun():
    sum=0
    sum1=0
    for i in range(1,5):
        for j in range(1,5):
            sum=sum+1
            if sum==10:
                sum=1
            if(sum<=9):
                print(sum,end=" ")

        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""


#19
"""
def fun():
    for i in range(1,5):
        for j in range(1,9):
            if i%2!=0:
                if j%2==0:
                    print(j, end="  ")
            elif (j%2!=0):
                print(j,end="  ")

        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#20
"""
def fun():
    for i in range(1,5):
        for j in range(1,6):
            if i%2!=0:
                print(j*2,end="      ")
            else:
                print((j*2-1),end="      ")

        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#21
"""
def fun():
    for i in range(1,6):
        for j in range(1,6):
            if i%2!=0:
                print(chr(96+j),end="      ")
            else:
                print((j),end="      ")

        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#22
"""
def fun():
    for i in range(1,6):
        for j in range(1,6):
            if i%2!=0:
                print(j,end="         ")
            else:
                print((-j),end="       ")

        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#23
"""
def fun():
    for i in range(0,5):
        for j in range(1,6):
            print(j+i,end="      ")

        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#1------tringle

#
#  #
#  #  #

#1---****
"""
def fun():
    for i in range(0,5):
        for j in range(0,i):
            print("*",end="      ")

        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#2---1234
"""
def fun():
    for i in range(1,6):
        for j in range(1,i):
            print(j,end="      ")

        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""


#3----4444
"""
def fun():
    for i in range(1,6):
        for j in range(0,i):
            print(i,end="      ")

        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#4 ----1123456789
"""
def fun():
    sum=0
    for i in range(1,5):
        for j in range(0,i):
            sum=sum+1
            print(sum,end="  ")


        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""


#5---abcd
"""
def fun():
    sum=0
    for i in range(1,5):
        for j in range(0,i):
            print(chr(97+j),end="  ")


        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#6---dddd
"""
def fun():
    for i in range(1,5):
        for j in range(0,i):
            print(chr(96+i),end="  ")


        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""




#------ tringle

# #  #
# #
#

#1
"""
def fun():
    for i in range(5,0,-1):
        for j in range(0,i):
            print("*",end="  ")


        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#2
#1234
"""
def fun():
    for i in range(5,0,-1):
        for j in range(1,i):
            print(j,end="  ")


        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#3
#4444
"""
def fun():
    for i in range(5,0,-1):
        for j in range(0,i):
            print(i,end="  ")


        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#abcd
"""
def fun():
    for i in range(5,0,-1):
        for j in range(0,i):
            print(chr(97+j),end="  ")


        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#---eeeee
"""
def fun():
    for i in range(5,0,-1):
        for j in range(0,i):
            print(chr(96+i),end="  ")


        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#---aaaa

"""
def fun():
    for i in range(4+1):
        for j in range(4+1):
            if j<= (4-i):
                print(chr(97+i),end="  ")


        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#-------
#2
"""
def fun():
    for i in range(1,5):
        for j in range(1,5):
            if  j!=5-i:
                print(chr(96+j),end=" ")

            else:
                print("*",end=" ")




        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""
#------------



#---------tringle
            #
        # #
  #  #  #

#1
"""
def fun():
    for i in range(1,4):
        for j in range(4,0,-1):
            if i>=j:
                print("*",end="  ")
            else:
                print("  ",end="  ")


        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""



#2-----4231
"""
def fun():
    for i in range(1,5):
        for j in range(5,0,-1):
            if i>=j:
                print(j,end="  ")
            else:
                print("  ",end="  ")




        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#3
"""
def fun():
    for i in range(1,5):
        a=0
        for j in range(5,0,-1):
            if i>=j:
                a=a+1
                print(a,end="  ")
            else:
                print("  ",end="  ")


        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""


#4----------4444
"""
def fun():
    for i in range(1,5):
        for j in range(5,0,-1):
            if i>=j:
                print(i,end="  ")
            else:
                print("  ",end="  ")


        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#5------6789
"""
def fun():
    s=0
    for i in range(1,5):
        for j in range(5,0,-1):
            if i>=j:
                s=s+1
                print(s,end="  ")
            else:
                print("  ",end="  ")


        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#5===DDDD
"""
def fun():
    for i in range(1,5):
        for j in range(5,0,-1):
            if i>=j:
                print(chr(64+i),end="   ")
            else:
                print("   ",end="  ")


        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#6----ABCD
"""
def fun():
    for i in range(1,5):
        a=0
        for j in range(5,0,-1):
            if i>=j:
                a=a+1
                print(chr(64+a),end="   ")
            else:
                print("   ",end="  ")


        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#----GHIJ
"""
def fun():
    s=0
    for i in range(1,5):
        for j in range(5,0,-1):
            if i>=j:
                s=s+1
                print(chr(64+s),end="   ")
            else:
                print("   ",end="  ")


        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""


#-------------DCBA
"""
def fun():
    for i in range(1,5):
        for j in range(5,0,-1):
            if i>=j:
                print(chr(64+j),end="   ")
            else:
                print("   ",end="  ")


        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#------------------------------------------tringle

#  #  #
   #  #
     #



 #-1------
"""
def fun():
    for i in range(1,5):
        for j in range(1,5):
            if i<=j:
                print("*",end="  ")
            else:
                print("  ",end="  ")

        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#2-----1111
"""
def fun():
    for i in range(1,5):
        for j in range(1,5):
            if i<=j:
                print(i,end="  ")
            else:
                print("  ",end="  ")

        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#3-----1234
"""
def fun():
    for i in range(1,5):
        for j in range(1,5):
            if i<=j:
                print(j,end="  ")
            else:
                print("  ",end="  ")

        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#-----12345678910
"""
def fun():
    s=0
    for i in range(1,5):
        for j in range(1,5):
            if i<=j:
                s=s+1
                print(s,end="   ")
            else:
                print("   ",end="   ")

        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""

#----1234,123,12,1
"""
def fun():
    for i in range(1,5):
        s = 0
        for j in range(1,5):
            if i<=j:
                s=s+1
                print(s,end="   ")
            else:
                print("   ",end="   ")

        print("\r")

def main():
    fun()
if __name__ == "__main__":
    main()"""


#---4444,333,22,1
"""
def fun():
    a=5
    for i in range(1,5):
        a=a-1
        for j in range(1,5):
            if i<=j:
                print(a,end="  ")
            else:
                print("  ",end="  ")
        print("\r")
def main():
    fun()
if __name__ == "__main__":
    main()"""

#4321,321,21,1
"""
def fun():
    a=5
    for i in range(1,5):
        for j in range(1,5):
            if i<=j:
                print(a-j,end="  ")
            else:
                print("  ",end="  ")
        print("\r")
def main():
    fun()
if __name__ == "__main__":
    main()"""


#-----AAAA
"""
def fun():
    for i in range(1,5):
        for j in range(1,5):
            if i<=j:
                print(chr(64+i),end="  ")
            else:
                print("  ",end="  ")
        print("\r")
def main():
    fun()
if __name__ == "__main__":
    main()"""

# A  B  C  D
#     E  F  G
#         H  I
#             J
"""
def fun():
    s=0
    for i in range(1,5):
        for j in range(1,5):
            if i<=j:
                s=s+1
                print(chr(64+s),end="  ")
            else:
                print("  ",end="  ")
        print("\r")
def main():
    fun()
if __name__ == "__main__":
    main()"""


# #
# A  B  C  D
#     A  B  C
#         A  B
#             A
"""
def fun():
    for i in range(1,5):
        s = 0
        for j in range(1,5):
            if i<=j:
                s=s+1
                print(chr(64+s),end="  ")
            else:
                print("  ",end="  ")
        print("\r")
def main():
    fun()
if __name__ == "__main__":
    main()"""

# #
# A  B  C  D
#     B  C  D
#         C  D
#             D
"""
def fun():
    for i in range(1,5):
        for j in range(1,5):
            if i<=j:
                print(chr(64+j),end="  ")
            else:
                print("  ",end="  ")
        print("\r")
def main():
    fun()
if __name__ == "__main__":
    main()"""

#
# E  E  E  E
#     D  D  D
#         C  C
#             B
"""
def fun():
    for i in range(1,5):
        a=6-i
        for j in range(1,5):
            if i<=j:
                print(chr(64+a),end="  ")
            else:
                print("  ",end="  ")
        print("\r")
def main():
    fun()
if __name__ == "__main__":
    main()"""


# #
# *        *        *        *        *        *
#      *        *        *        *        *
#           *        *        *        *
#                *        *        *
#                     *        *
#                          *
"""
def fun():
    for i in range(1,7):
        for j in range(1,7):
            if i<=j:
                print("*",end="        ")
            else:
                print("   ",end="  ")
        print("\r")
def main():
    fun()
if __name__ == "__main__":
    main()"""

# #
# *  *  *  *  *
# *  *  *  *
# *  *  *
# *  *
# *
#
# *
# *  *
# *  *  *
# *  *  *  *
# *  *  *  *  *
"""
def fun1():
    for i in range(1,7):
        for j in range(1,7-i):
            print("*",end="  ")
        print("\r")
    for i in range(1,6):
        for j in range(0,i):
            print("*",end="  ")
        print("\r")
def main():
    fun1()
if __name__ == "__main__":
    main()"""

# #----
#             *
#         *   *   *
#     *   *   *   *   *
# *   *   *   *   *   *   *
"""
def fun1():
    for i in range(1,5):
        for j in range(1,8):
            if ( j>= 5-i and 3+i >=j):
                print("*",end="   ")
            else:
                print("  ",end="  ")
        print("\r")
def main():
    fun1()
if __name__ == "__main__":
    main()"""


# #
# enter=4
# enter=8
#             *
#         *   *   *
#     *   *   *   *   *
"""
def fun1():
    n=int(input("enter="))
    m=int(input("enter="))
    for i in range(1,n):
        for j in range(1,m):
            if ( j>= (n+1)-i and (n-1)+i >=j):
                print("*",end="   ")
            else:
                print("  ",end="  ")
        print("\r")
def main():
    fun1()
if __name__ == "__main__":
    main()"""

#
"""
def fun1():
    #n=int(input("enter="))
  #  m=int(input("enter="))
    s=0

    for i in range(1,5):
        s=i
        for j in range(1,5):
            if ( j>= 5-i and 3+i >=j):
                print(s,end="   ")
                s = s + 1
            # elif(j>=3):
            #     s = s -1
            else:
                 print("  ",end="  ")
        for j in range(i,0,-1):
            s=s-1
            print(s,end=" ")


        print("\r")
def main():
    fun1()
if __name__ == "__main__":
    main()"""

#)
# #
# enter=5
#                 *
#             *   *   *
#         *   *   *   *   *

"""
def fun1():
    n=int(input("enter="))
    m=n+n
    for i in range(1,n):
        for j in range(1,m):
            if ( j>= (n+1)-i and (n-1)+i >=j):
                print("*",end="   ")
            else:
                print("  ",end="  ")
        print("\r")
def main():
    fun1()
if __name__ == "__main__":
    main()"""

# #-------------------------
# enter=5
#      *   *   *   *   *   *   *   *   *
#           *   *   *   *   *   *   *
#                *   *   *   *   *
#                     *   *   *
  #                          *

"""
def fun1():
    n=int(input("enter="))
    m=n+n
    for i in range(n,0,-1):
        for j in range(m,0,-1):
            if ( j>= (n+1)-i and (n-1)+i >=j):
                print("*",end="   ")
            else:
                print("   ",end="  ")
        print("\r")
def main():
    fun1()
if __name__ == "__main__":
    main()"""

  ##################

def fun1():

    n=int(input("enter="))
    m=n+n
    for i in range(1, n):
        for j in range(1, m):
            if (j >= (n + 1) - i and (n - 1) + i >= j):
                print("*", end="   ")
            else:
                print("    ", end="   ")
        print("\r")

    for i in range(n,0,-1):
        for j in range(m,0,-1):
            if ( j>= (n+1)-i and (n-1)+i >=j):
                print("*",end="  ")
            else:
                print(" ",end="  ")
        print("\r")
def main():
    fun1()
if __name__ == "__main__":
    main()