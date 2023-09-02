#---TUPLE---
#---count---
"""
def main():
    t1=(1,2,3,4,5,3,3,2,3)
    no=t1.count(3)
    print(no)
if __name__=="__main__":
    main()
"""

#----index--
###----1---
"""
def main():
    t1=(1,2,3,4,5,3,3,2,3)
    no=t1.index(3)
    print(no)
if __name__=="__main__":
    main()
    """
##----2---
#
# def main():
#     t1=('a' , 'b', 'c' ,'d' ,'e' ,'f')
#     index1=t1.index("c")
#     index2=t1.index("e")
#     index3=t1.index("a")
#     print(index1)
#     print(index2)
#     print(index3)
# if __name__=="__main__":
#     main()

#---lenght
"""
def main():
    t1=(1,2,3,4,5,3,3,2,3)
    len1=len(t1)
    print(len1)
    print(len(t1))
if __name__=="__main__":
    main()
    """

#-----ACCESSSING ELE ----
#USING  FOR LOOP
"""
def main():
    t1=(1,2,3,4,5)
    for i in t1:
        print(i)
if __name__=="__main__":
    main()
"""
#USING WHILE LOOP
"""
def main():
    t1=(1,2,3,4,5)
    i=0
    while i<len(t1):
        print(t1[i])
        i=i+1
if __name__=="__main__":
    main()
    """
###using index no
"""
def main():
    t1=(1,2,3,4,5)
    no1=t1[-1]
    no2= t1[2]
    no3 = t1[-3]
    no4 = t1[0]

    print(no1)
    print(no2)
    print(no3)
    print(no4)

if __name__=="__main__":
    main()
  """

# ###----TUPLE Packing
# def main():
#     list1=[1,2,3,4,5]
#     t1=tuple(list1)
#     print(t1)
#     t2=(9,8,7)
#     print(t2)
# if __name__=="__main__":
#     main()

# #-----UNpacking of tuple
#
# def main3():
#     fruite=("apple" ,"banana" ,"cherry","hhj")
#     fruite2=[*fruite,]
#     print(fruite2)
#
# def main2():
#     fruite=("apple" ,"banana" ,"cherry","hhj")
#     (green,yellow,*red)=fruite
#     print(green)
#     print(yellow)
#     print(red)
#     print(red)
#
# def main1():
#     fruite=("apple" ,"banana" ,"cherry","hhj")
#     (green,*yellow,red)=fruite
#     print(green)
#     print(yellow)
# def main():
#     main1()
#     main2()
#     main3()
# if __name__=="__main__":
#     main()

#
# ##convert list into a tuple
# def main2():
#     lis1=[1,2,3]
#     t1=(*lis1,)
#     print(t1)
# def main1():
#     lis1=[1,2,3]
#     t1=tuple(lis1)
#     print(t1)
# def main():
#     main1()
#     main2()
# if __name__=="__main__":
#     main()

#change tuple element
# def main1(t1):
#     l1=list(t1)
#     l1[3]=66
#     l1.insert(2,77)
#     t2=tuple(l1)
#     print("tuple1=",t2)
# def main():
#     t1=(1,2,3,4,5,9,8,7)
#     main1(t1)
# if __name__=="__main__":
#     main()


# #--remove item from tuple
# def main1(t1):
#     l1=list(t1)
#     l1.remove(7)
#     t1=tuple(l1)
#     print(t1)
# def main():
#     t1=(1,2,3,4,5,9,8,7)
#     main1(t1)
# if __name__=="__main__":
#     main()

# ##check ele is present or not
# def main1(t1):
#     flag=0
#     no=int(input("enter no = "))
#     if no not in t1:
#         flag=1
#     if flag==1:
#         print(" not present")
#     else:
#         print(" present")
#
# def main():
#     t1=(1,2,3,4,5,9,8,7)
#     main1(t1)
# if __name__=="__main__":
#     main()


# ####----covert string into tuple
# def main1(str1):
#     t1=tuple("".join(str1))
#     t2=tuple(str1)
#     print(t1)
#     print(t2)
# def main():
#     str1="jagruti"
#     main1(str1)
# if __name__=="__main__":
#     main()

#
# #---tuple to a str--
# def main3(t1):
#     str=" "
#     for i in t1:
#         str=str+i
#     print(str)
# def main2(t1):
#     for i in t1:
#         print(str(i),end="")
# def main1(t1):
#     str1="".join(t1)
#     print(str1)
# def main():
#     t1=('a','b','c','d','h')
# #     main1(t1)
#     main2(t1)
#     main3(t1)
# if __name__=="__main__":
#     main()


###---appened tuple to a list of  tuple
#
# def main():
#     l1=[(1,"a",1.1) , (2,"b",2,4),(3,"f",7.8)]

#     print(l1)
#     l1.append((4,"T",9.9))
#     print(l1)
#
#     l1[3]=(1,"e",9.8)
#     print(l1)
#
#     l1.remove((1,"a",1.1))
#     print(l1)
#
#     del l1[2]
#     print(l1)
#
#     l1.clear()
#     print(l1)
#
# if __name__=="__main__":
#     main()


# #sort list of tuple
# def main():
#     l1=[("a",66),("h",99),("l",55)]
#     l2=l1.sort()
#     print(l2)
# if __name__=="__main__":
#     main()
#


# ### return tuple
# def main2(id ,n):
#           t2=(id,n)
#           print(t2)
# def main1():
#     return (1,"a")
# def main():
#     t1=main1()
#     print(t1)
#     t2=main2(12,"sita")
# if __name__=="__main__":
#     main()


# ##using yeild
# def main1(id,name):
#         yield (id[0],name[0])
#         yield (id[1],name[1])
# def main():
#     t1,t2=main1((1,2),("pooja","rani"))
#     print(t1)
#     print(t2)
# if __name__=="__main__":
#     main()



# ##--concatination
#
# def main3():
#     t1 = (1, 2, 3)
#     t2=(t1+(4,))
#     print(t2)
# def main2():
#     t1 = (1, 2, 3)
#     t2=(t1*4)
#     print(t2)
# def main1():
#     t1=(1,2,3)
#     t2=(4,5,6)
#     t3=(t1+t2)
#     print(t3)
# def main():
#     main1()
#     main2()
#     main3()
# if __name__=="__main__":
#     main()



# ##slicing
# def main1():
#     t1=(1,2,3,4,5,6,1,2,3,4,)
#     print(max(t1))
#     print(min(t1))
#     t2=t1[2:-2]
#     print(t2)
# def main():
#     main1()
# if __name__=="__main__":
#     main()


#comapring operator


def main():
    t1=(1,2,3)
    t2=(4,5,6)
    print(t1==t2)
    print(t1 != t2)
    print(t1 >= t2)
    print(t1 <= t2)

if __name__=="__main__":
    main()