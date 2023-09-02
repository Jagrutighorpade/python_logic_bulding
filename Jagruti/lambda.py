#lambada map()
#1
"""
def main():
    l1=[10,20,30,40,50]
    l2=list(map(lambda  x:x+5,l1))
    print(l2)
if __name__=="__main__":
    main()"""

#2 square
"""
def main():
    l1=[10,20,30,40,50]
    l2=list(map(lambda  x:x**2,l1))
    print(l2)
if __name__=="__main__":
    main()"""

#3 hello before name
"""
def main():
    l1=["jay" ,"mau","kau"]
    l2=list(map(lambda  x:"Hello " +x,l1))
    print(l2)
if __name__=="__main__":
    main()"""

#4 lenght of  each elem using len()
"""
def main():
    l1=["jayant" ,"maukk","kauiy"]
    l2=list(map(len,l1))
    print(l2)
if __name__=="__main__":
    main()"""

#5 addn of  2 lis
"""
def main():
    l1=[10,20,30,40,50]
    l2=[1,2,3,4]
    l2=list(map(lambda  x,y: x+y,l1,l2))
    print(l2)
if __name__=="__main__":
    main()"""

#6 count ()=a in list of strings
"""
def main():
    l1=["jayant" ,"maukak","kaaiy"]
    l2=list(map (lambda x: x.count("a"),l1))
    print(l2)
if __name__=="__main__":
    main()"""


#7 count ()=a and A in list of strings
"""
def main():
    l1=["Ajayant" ,"Amaukak","Akaaiy"]
    l2=list(map (lambda x: x.count("A")+ x.count("a"),l1))
    l3=list(map (lambda x: x.lower().count("a"),l1))
    print(l2)
    print(l3)
if __name__=="__main__":
    main()"""

#8 newlist =absulte val of l1 and l2 is sum of all newlist:
"""
from functools import reduce
def main():
    l1=[10,20,-30,-1.40,50]
    # new=list(map(lambda x:x,l1))
    # ans=reduce(lambda a,b:a+b,new)
    new=list(map(abs,l1))
    ans=sum(new)
    print(new)
    print(ans)
if __name__=="__main__":
    main()"""

#____________________Lmabda Filter()___________
#1 filter out -ve element
"""
def main():
    l1=[10,-2,30,-1.40,50]
    l2=list(filter(lambda x: x<0,l1))
    print(l2)
if __name__=="__main__":
    main()"""

#2 filter odd no
"""
def main():
    l1=[10,21,30,43,50]
    l2=list(filter(lambda x: x%2==1,l1))
    print(l2)
if __name__=="__main__":
    main()"""

 #3 find vowel
"""
def main():
    str1="i am a good girl"
    l2=list(filter (lambda x: True  if x.lower() in "aeiou" else False,str1))
    print(l2)
if __name__=="__main__":
    main()"""

#4 find +ve int
"""
def main():
    str1="i am a good girl ans my roll no is 12678"
    l2=list(filter (lambda x: True  if x in "0123456789" else False,str1))
    print(l2)
if __name__=="__main__":
    main()"""

#5 -ve to +ve

"""
def main():
    l1=[100,-200,300,-400,500,-600]
    l2=list(filter(lambda x:x>0 ,map(lambda x:-x,l1)))
    print(l2)

if __name__=="__main__":
    main()"""

#6
"""
def main():
    l1=[10,21,30,43,50]
    t1=tuple(filter(lambda x:x<30,l1))
    print(t1)
if __name__=="__main__":
    main()"""

#7
"""
def main1(n):
    if n>30:
        return n
def main():
    l1=[10,21,30,43,50]
    t1=list(filter(main1,l1))
    print(t1)
if __name__=="__main__":
    main()"""

#---------------reduce().......from functools import reduce()----------------
#1
"""
from functools import reduce
def main():
    l1=[10,21,30,43,50]
    sum=reduce(lambda x,y:x+y,l1)
    print(sum)
if __name__=="__main__":
    main()"""

#2
"""
from functools import reduce
def main():
    l1=[10,21,30,43,50]
    min=reduce(lambda x,y:x if x<y else y,l1)
    print(min)
    max=reduce(lambda x,y:x if x>y else y,l1)
    print(max)
if __name__=="__main__":
    main()"""

#3
"""
from functools import reduce
def main():
    l1=[10,21,30,43,50]
    sum=reduce(lambda x,y:x*y,l1)
    print(sum)
if __name__=="__main__":
    main()"""

#------------lambada----
#1
"""
def main():
    ans=lambda a:a**2
    print(ans(4))
if __name__=="__main__":
    main()"""
    
#2
"""
def main():
    ans=lambda a,b:a+b
    print(ans(4,5))
if __name__=="__main__":
    main()"""



#

