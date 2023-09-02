#-----reverse the list----1
# def  rev(l1):
#     l1.reverse()
#     print(l1)
# def main():
#     l1 = [1, 2, 3, 4, 5]
#     rev(l1)
# if __name__=="__main__":
#     main()

######----2
# def rev(l1):
#     l2= l1[ : :-1]
#     print(l2)
# def main():
#     l1 = [1, 2, 3, 4, 5]
#     rev(l1)
# if __name__=="__main__":
#     main()

# ###------3
# def rev(l1):
#     l2=[]
#     for i in range(len(l1)-1,-1,-1):
#         l2.append(l1[i])
#     print(l2)
# def main():
#     l1 = [20,30,40,50,60]
#     rev(l1)
# if __name__=="__main__":
#     main()


# ##CONCATINATE-----index wise
# def con(l1,l2):
#     l4=[]
#     # for i in range(len(l1)):
#     #     l3=l1[i]+l2[i]
#     #     l4.append(l3)
#     # print(l4)
#     for i,j in zip(l1,l2):
#         l3=i+j
#         l4.append(l3)
#     print(l4)
# def main():
#     l1 = ['m','na','i','ke']
#     l2=['y','me','s','lly']
#     con(l1,l2)
# if __name__=="__main__":
#     main()

######square of every item----
# def squ(l1):
#     l2=[]
#     for no in l1:
#         nos=no**2
#         l2.append(nos)
#     print(l2)
# def main():
#     l1=[1,2,3,4,5]
#     squ(l1)
# if __name__=="__main__":
#     main()


# ###===iterate both list simultane0usly====
# def con(l1,l2):
#     #l3=l2[::-1]
#     for i,j in zip(l1,l2[::-1]):
#         print(i,j)
# def main():
#     l1=[10,20,30,40]
#     l2=[100,200,300,400]
#     con(l1,l2)
# if __name__=="__main__":
#     main()
#

####remove empty string
# def  rmv(l1):
#     l2=[]
#     for i in l1:
#         if  i!='':
#             l2.append(i)
#     print(l2)
# def main():
#     l1=['ravi','','kashi','','pati']
#     rmv(l1)
# if __name__=="__main__":
#     main()


# #######lenght
# def main():
#     l1=[1,2,3,4]
#     l1.append(5)
#     l1.append([6])
#     len1=len(l1)
#     print(len1,l1)
# if __name__=="__main__":
#     main()



# ##____Insert---
# #---1
# def main():
#     l1=[1,2,3,4,5]
#     l1[1]=6
#     print(l1)
# if __name__=="__main__":
#     main()

   #---2
# def main():
#     l1=[1,2,3,4]
#     print(" l1=",l1)
#     l1.insert(2,66)
#     print("l1.insert(2,66) = ",l1)
#     l1.insert(0,111)
#     print("l1.insert(0,111) = ",l1)
#     no = len(l1)
#     l1.insert(no,998)
#     print("l1.insert(no,998) = ",l1)
#     l1.insert(-10,110)
#     print("l1.insert(-10,110) = ",l1)
#     l1.insert(1000,999)
#     print("l1.insert(1000,999) = ",l1)
# if __name__=="__main__":
#     main()

# ##---Extend---
# def main():
#     l1=[1,2,3,4]
#     l1.extend([5,6,7])
#     print(l1)
#     l2=[1,2,3,4]
#     l3=[5,6,7,8]
#     l2.extend(l3)
#     print(l2)
#     l2.extend([l3])
#     print(l2)
#     l2.append(l3)
#     print(l2)
#     ##copy then extend
#     l5=[1,2,3]
#     l6=[4,5,6]
#     l7=l5.copy()
#     l7.extend(l6)
#     print(l7)
# if __name__=="__main__":
#        main()


# ##----Append
####---1
# def main():
#     l1=[1,2,3,4,5]
#     l1.append(6)
#     print(l1)
#     l2=[6,7,8,9]
#     l1.append(l2)
#     print(l1)
#     l1.append([10,11])
#     print(l1)
#     #for loop
#     lis1=[1,2,3,4]
#     lis2=[5,6,7,8]
#     for i in lis2:
#         lis1.append(i)       # lis1.extend([i])
#     print(lis1)
# if __name__=="__main__":
#        main()

# ##====AADING TWO LIST
# def main():
#     list1=[2,4,5]
#     l2=[44,9,8]
#     print(list1+l2)
# if __name__=="__main__":
#     main()


# ######-----Remove()
# def main():
#     no=21
#     l1=[21,5,8,52,21,87]
#     #l1.remove(5)
#     #l1.remove(21)
#
#     # for i in l1:
#     #     if i==no:
#     #         l1.remove(i)
#
#     # l2=list(filter((no).__ne__,l1))
#     #print(l2)
#
#     # while no in l1:
#     #     l1.remove(no)
#     # print(l1)
# if __name__=="__main__":
#     main()

#
# ###---pop(specific index----
# def main():
#     l1=[21,5,8,52,21,87,52]
#     #l1.pop(len(l1)-1)
#     #l1.pop()  #last item remove
#     #l1.pop(-1)
#     #l1.pop(3)
#     #l1.pop(-1)
#     l1.pop(-2)
#     print(l1)
# if __name__=="__main__":
#     main()

####------reverse.list----
# def main():
#     l1=[1,2,3,4,5]
#     #l1.reverse()
#     l2=l1[::-1]
#     print(l2)
# if __name__=="__main__":
#     main()


###---Max value in l1--
# def maxl2(l1):
#     l1.sort()
#     print(l1[-1])
# def  maxl1(l1):
#     max=0
#     for i in l1:
#         if i>max:
#             max=i
#     print(max)
# def main():
#     l1=[1,2,3,9,8,7]
#     max1=max(l1)
#     print(max1)
#     maxl1(l1)
#     maxl2(l1)
# if __name__=="__main__":
#     main()

# ####-----min()___small no in l1
# def minl2(l1):
#     l1.sort()
#     print(l1[0])
# def minl1(l1):
#     min=9
#     for i in l1:
#         if i<min:
#             min=i
#     print(min)
# def main():
#     l1=[7,8,7,1,2,3]
#     l2=min(l1)
#     print(l2)
#     minl1(l1)
#     minl2(l1)
# if __name__=="__main__":
#     main()

# ##----count---
# def main():
#     l1=[1,2,3,1,4,1,5,1,6]
#     no_1=l1.count(1)
#     print(no_1)
# if __name__=="__main__":
#     main()

# ####___-sort()___
# def  Rvwl():
#     l2=['a','o','i','e','u']
#     l2.sort(reverse=True)
#     print(l2)
# def  vwl():
#     l2=['a','o','i','e','u']
#     l2.sort()
#     print(l2)
# def srt1():
#     l1 = [ 2, 3, 11, 4, 19, 5, 1, 6]
#     l1.sort()
#     print(l1)
# def main():
#     srt1()
#     Rvwl()
#     vwl()
# if __name__=="__main__":
#     main()
#
# #####sort list of  Dict---
# def dict1():
#     emlpoyees=[{'name': 'arti','age': 25,'salary':10000 },{'name': 'shruti','age':30 ,'salary': 8000},{'name':'jyoti' ,'age':18 ,'salary':1000 }]
#
#     def get_name(srt_data):
#         return srt_data.get('name')
#     def get_age(srt_data):
#         return srt_data.get('age')
#     def get_salary(srt_data):
#         return srt_data.get('salary')
#
#     emlpoyees.sort(key=get_name)
#     print(emlpoyees,end="\n")
#
#     emlpoyees.sort(key=get_age)
#     print(emlpoyees,end='\n')
#
#     emlpoyees.sort(key=get_salary ,reverse=True)
#     print(emlpoyees,end='')
#
# def  main():
#     dict1()
# if __name__=="__main__":
#     main()


# ##-----sort dict using lambda
# def dict1():
#     emlpoyees=[{'name': 'arti','age': 25,'salary':10000 },{'name': 'shruti','age':30 ,'salary': 8000},{'name':'jyoti' ,'age':18 ,'salary':1000 }]
#     emlpoyees.sort(key=lambda x: x.get("name"))
#     print(emlpoyees)
#     emlpoyees.sort(key=lambda y:y.get('age'))
#     print(emlpoyees)
#     emlpoyees.sort(key=lambda z: z.get('salary'),reverse=True)
#     print(emlpoyees)
# def  main():
#     dict1()
# if __name__=="__main__":
#     main()


####---find Index of item ----
"""
def main():
    #     0    1  2   3    4   5   6   7
    l1=[21, 5, 8, 52, 21, 8, 87, 52]
    #    -8  -7 -6  -5   -4  -3   -2  -1
    i=l1.index(8)
    print(i)
    j=l1.index(8,3,7)
    print(j)
    k=l1.index(52)
    print(k)
   # l=l1.index(99)  #value error for unkown vlaue
if __name__=="__main__":
    main()
"""


####-----shuffle ---
"""
import random
def main():
    l1=[1,2,3,4,5]
    random.shuffle(l1)
    print(l1)
if __name__=="__main__":
    main()
    """


####check list is empty or not
"""
def emp2():
    l1=[]
    leng=len(l1)
    if leng==0:
        print("empty")
    else:
        print("not empty")

def emp1():
    l1=[]
    if not l1:
        print("empty")
    else:
        print("not empty")
def main():
    emp1()
    emp2()
if __name__=="__main__":
    main()
    """

####---ele present in l1 or not
"""
def P1():
    no1=8
    l1=[1,2,3,4,5,6]
    if no1 in l1:
        print("present")
    else:
        print("not present")

def  P2():
        no1 = 3
        l1 = [1, 2, 3, 4, 5, 6]
        if no1 not in l1:
            print("not present")
        else:
            print("present")
def main():
    P1()
    P2()
if __name__=="__main__":
    main()
    """

###====LOOP ==
##--1 --While Loop
"""
def main():
    l1=[1,2,3]
    i=0
    while i<len(l1):
        print(l1[i])
        i=i+1
if __name__=="__main__":
    main()
"""

###2)---for loop---
"""
def main2():
    l1=['a','b','c']
    for j,i in enumerate(l1):
        print(j,"=",i)

def main1():
    l1=[1,2,3]
    for i in range(0,len(l1)):
        print( l1[i],end=" ")

def main():
    l1=[1,2,3]
    for i in l1:
        print("l2=",i , end=" ")
main1()
main2()

if __name__=="__main__":
    main()
"""

###l2 have l1 all elemnt or not
"""
def main():
    l1=[1,2,3,4,5]
    l2=[1,5,3]
    if all(i in l1 for i in l2):
        print("yes l2 have all")
    else:
        print("not have")
if __name__=="__main__":
    main()
"""

##-----2-----
"""
def main1():
    l1=[1,2,3,4,5,3]
    l2=[1,5,3]
    l3=[]
    flag=0
    for j in l2:
        for i in l1:
            if j==i:
                l3.append(i)
                break
    print(l3 )
    for i in range(len(l2)-1):
        if l2[i]!=l3[i]:
            flag=1
    if (flag==1):
        print("no have")
    else:
        print("yes have")
def main():
    main1()
if __name__=="__main__":
    main()
"""

####        List Comprehension---
#--1
"""
def main1():
    l1=[1,2,3]
    l2=[4,5,6]                                        #['a','b','c']
    l3=[x*y    for x in l1    for y in l2 ]
    print(l3)
def main():
    main1()
if __name__=="__main__":
    main()
"""

##---2   permutation
"""
def main1():
    l1=[1,2,3]
    l2=['a','b','c']
    l3=[(x,y)  for x in l1 for y in l2]
    print(l3)
def main():
    main1()
if __name__=="__main__":
    main()
    """

###--3
"""
def main1():
    l1=[1,2,3,4,5,6,7,8,9]
    l3=[x*x  for x in l1 if x%2==0]
    print(l3)
def main():
    main1()
if __name__=="__main__":
    main()
"""

###################################3
###---4
"""
def main1():
   l1 = [1, 2, 3]
   l2 = [4, 5, 6]
   l3=[x*y   for x in l1   for y in l2  if  (x+y)%2==0]
   print(l3)
def main():
    main1()
if __name__=="__main__":
    main()
    
"""
###############---5
"""
def main1():
   l1 = [1, 2, 3]
   l2 = [4, 5, 6]
   l3=[x*y   for x in l1   for y in l2  if  (x+y)%2==0]
   print(l3)
def main():
    main1()
if __name__=="__main__":
    main()
    """


 ##------6
#
# def main():
#     l1=[-1,9,7,6,2,3,4,5,-6,7,8,0]
#     l2=[x  for x in l1 if x>0  if  x%3==0]  #[x  for x in l1 if x>0 and x%3==0]
#     print(l2)
# if __name__=="__main__":
#     main()


 ######-------7
#
# def main():
#     l1=[-3,-3,-5,1,2,3]
#     l2=[3,4,7,8]
#     l3=[x*y  for x in l1  for y in l2  if x>0  if y%2==0  ]
#     print(l3)
# if __name__=="__main__":
#     main()


 #####-----8.....convert in to a Dict
#
# def main():
#     l1=[-3,-4,-5,-1,2,3]
#     l3={ l1[i]: l1[i+1]  for i in range(0,len(l1),2)}
#     print(l3)
# if __name__=="__main__":
#     main()


####....9
# def main():
#     l1 = [(1, 2), (2, 3), (4, 5), (6, 7)]
#     l3 = [{l1[i][0]: l1[i][1] for i in range(len(l1))}]
#     print(l3)
# if __name__=="__main__":
#     main()

# ###---10
# def main():
#     l1=[1,2,3,4]
#     l2=['a','b','c','d']
#     l3=[{l1[x]: l2[x]  for x in range(len(l1)) }]
#     print(l3)
# if __name__=="__main__":
#     main()

# ###------square of list ele
# def main2():
#     l1 = [1, 2, 3, 4, 5]
#     l2=list(map(lambda x : x**2 ,l1))
#     print(l2)
# def main1():
#     l1 = [1, 2, 3, 4, 5]
#     for i in l1:
#         print(i**2,end=" ")
# def main():
#     l1=[1,2,3,4,5]
#     l3=[x**2 for x in l1]
#     print(l3)
# main1()
# main2()
# if __name__=="__main__":
#     main()


# ###----
# def main():
#     l1=['hellow', 'take']
#     l2=['dear','sir']
#     for i in l1 :
#         for j in l2:
#             print(i+' '+j, ",",end="")
#
# if __name__=="__main__":
#     main()


####concat----2
#
# def con(l1,l2):
#     l3=[]
#     for i in range(len(l1)):
#         for j in range(len(l2)):
#             x=l1[i]+ " "+l2[j]
#             l3.append(x)
#     print(l3,end=" ")
# def main():
#     l1=["Hello","take"]
#     l2=["dear","sir"]
#     con(l1,l2)
# if __name__=="__main__":
#     main()


# ####====ADD ele at specific position   [500 ather 600 anf 6000 qfther 7000]
# def main():
#     l1=[10,20,[300,400,[5000,6000],500],30,40]
#     l1[2][2].append(7000)
#     l1[2].append(600)
#     print(l1)
# if __name__=="__main__":
#     main()

# #----sum of list
# from functools import reduce
# def sum2(l1):
#     sum=reduce(lambda x,y: x+y ,l1)
#     print(sum)
# def sum(l1):
#     sum=0
#     for i in l1:
#         sum=sum+i
#     print(sum,end=' ')
#
# def main():
#     l1=[1,2,3,4,5]
#     sum(l1)
#     sum2(l1)
# if __name__=="__main__":
#     main()


# ####---mul
# from functools import reduce
# def mul2(l1):
#     mul=reduce(lambda x,y: x*y,l1)
#     print(mul)
# def mul1(l1):
#     mul=1
#     for i in l1:
#         mul=mul*i
#     print(mul)
# def main():
#     l1=[1,2,3,4,5]
#     mul1(l1)
#     mul2(l1)
# if __name__=="__main__":
#     main()


#  1st and last char must be same
# def main1(l1):
#     l2=[]
#     for i in l1:
#         if len(i)>1  and  i[0]==i[-1]:
#             l2.append(i)
#     print(l2)
# def main():
#     l1=['anc' ,'aba', 'aaa','yzx','pop']
#     main1(l1)
# if __name__=="__main__":
#     main()


# ####--- find 4 chr string   count
# def main1(no,l1):
#     count=0
#     for i in l1:
#         if  len(i)>=no:
#             count=count+1
#     print(count)
# def main():
#     no=4
#     l1=['angc' ,'aba', 'aaas','yzxtu','pop','12124']
#     main1(no,l1)
# if __name__=="__main__":
#     main()


# ######...clone or copy
# def main():
#     l1=['anc' ,'aba', 'aaa','yzx','pop']
#     l2=list(l1)
#     l3=l1.copy()
#     print(l2)
#     print(l3)
# if __name__=="__main__":
#     main()
#
# ##-----check it have same ele or not
# def main1(l1,l2):
#     flag=0
#     for x in l1 :
#         for y in l2:                          # for x,y in zip(l1,l2):
#               if x==y:
#                 flag=1
#     if flag==1:
#         print("have ")
#     else:
#         print("dont have")
# def main():
#     size1=int(input("enter  size of  1st list="))
#     l1=[]
#     for i in range(size1):
#             l1.append(int(input("enter element=")))
#     print(l1)
#
#     size2=int(input("enter  size of 2nd list="))
#     l2=[]
#     for i in range(size2):
#             l2.append(int(input("enter element=")))
#     print(l2)
#
#     main1(l1,l2)
#
# if __name__=="__main__":
#     main()

# #####-----remove 0th 4th 5th index ele
# def main1(l1):
#     l1=[x for i,x in enumerate(l1) if i not in (0,4,5)]
#     print(l1)
#
# #     for i,j in enumerate(l1):
# #         if i not in (0,4,5):
# #             print(i,"=",j)
#
# def main():
#     l1=[1,9,8,7,6,5,4,3,2,10]
#     main1(l1)
#
# if __name__=="__main__":
#     main()

# dublicate elemnt

def main():
    l1=[1,9,8,7,1,5,4,1,3,2,1,0]
    l2=[]
    for i in range(len(l1)):
        if l1[i]  in l2:
            print(l1[i])

if __name__=="__main__":
    main()