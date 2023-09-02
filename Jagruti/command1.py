#1
"""
import sys
def main():
    print("my project is in =",sys.argv[0])
    print("____math_____")
    a=int(sys.argv[1])
    b=int(sys.argv[2])
    c=a+b
    print("addtion =" ,c)
if __name__ == "__main__":
    main()"""

#
"""
import sys
def main():
    print("my project is in =",sys.argv[0])
    no=int(sys.argv[1])
    for i in range(1,no):
        print(i)
        
if __name__ == "__main__":
    main()"""

#
"""
import sys
def main():
    print("my project is in =",sys.argv[0])
    sum=0
    no=len(sys.argv)
    for i in range(1,no):
        sum=sum+int(sys.argv[i])
    print(sum)
        
if __name__ == "__main__":
    main()"""

#
"""
import sys
def main():
    print("my project is in =",sys.argv[0])
    sum=0
    no=len(sys.argv)
    for i in range(1,no):
        if int(sys.argv[i])%2==0:
            print(sys.argv[i])
        
if __name__ == "__main__":
    main()"""

#
"""
import sys
def main():
    print("my project is in =",sys.argv[0])
    x=sys.argv[1]
    f=open(x,"x")
if __name__ == "__main__":
    main()"""

#
"""
import os
import sys

def main():
    print("my project is in =",sys.argv[0])
    x=sys.argv[1]
    os.remove(x)
if __name__ == "__main__":
    main()"""

#
import sys
def main():
    print("my project is in =",sys.argv[0])
    sum=0
    no1=len(sys.argv)
    for no in range(1,no1):
        xx=int(sys.argv[no])
        while xx!=0:
            r=xx%10
            sum=sum+r
            xx=xx//10
        print(sum)
        sum=0
if __name__ == "__main__":
    main()
