#add()
"""
def main():
    s1={1,2,3,4}
    s1.add(5)
    print(s1)
    s1.add(2)#doesnt take same elmnt
    print(s1)
if __name__=="__main__":
    main()"""

#copy()
"""
def main():
    s1={1,2,3,4}
    s2=s1.copy()
    print(s2)
if __name__=="__main__":
    main()"""

#update()
"""
def main():
    s1={1,2,3,4,5,6,7,8}
    s2={8,2,5,11,26,99}
    s1.update(s2)
    print(s1)
    s2.update(s1)
    print(s2)
    s2.update({9,10,11})
    print(s2)
if __name__=="__main__":
    main()"""

#union()....all same elemnt take only once
"""
def main():
    s1={1,2,3,4,5,6,7,8}
    s2={8,2,5,11,26,99}
    print(s1.union(s2))
    print(s1|s2)
    print(s1.union({6,3,88,99,77}))
    s3=(s1.union(s2))
    print(s3)

    s4={1000,2000,3000}
    s5=s1.union(s2,s4)
    print(s5)

if __name__=="__main__":
    main()"""

#differnce()
"""
def main():
    s1={1,2,3,4,5,6,7,8}
    s2={8,2,5,11,26,99}
    print(s1.difference(s2))
    print(s1-s2)
    print(s1.difference({1,99,6,55}))
    s3=(s1-s2)
    print(s3)
    
    s4={1000,2000,3000}
    
    s5=s1.difference(s2,s4)
    print(s5)
    
    
    s6=s2.difference(s1)
    print(s6)

if __name__=="__main__":
    main()"""


#differnce_update()....made changes in origenal
"""
def main():
    s1={1,2,3,4,5,6,7,8}
    s2={8,2,5,11,26,99}
    
    s1.difference_update(s2)
    print(s1)
    
    s1.difference_update({1,99,6,55})
    print(s1)
    
    s1-s2   #cant take s3=s1-s2
    print(s1)
    
    
    s2.difference(s1)
    print(s2)
if __name__=="__main__":
    main()"""

#..itersection......same elemnt
"""
def main():
    s1={1,2,3,4,5,6,7,8}
    s2={8,2,5,11,26,99}
    print(s1.intersection(s2))

    s3=s1.intersection(s2)
    print(s3)
    

    s4=s1&s2
    print(s4)


    print(s1.intersection({1,99,6,55}))

    s9={1,2,9,66,88,99}
    s10=s1.intersection(s2,s9)
    print(s10)
if __name__=="__main__":
    main()"""


#intersection _update
"""
def main():
    s1={1,2,3,4,5,6,7,8}
    s2={8,2,5,11,26,99}
    s1.intersection_update(s2)
    print(s1)
 #cant take s3=s1-s2

if __name__=="__main__":
    main()"""

#symmetric_difference()..normal sub
"""
def main():
    s1={1,2,3,4,5,6,7,8}
    s2={8,2,5,11,26,99}
    
    s3=s1.symmetric_difference(s2)
    print(s3)
    
    
    #only take 1 arg
    # s4={9,8,5,4,90,100}
    # s5=s1.symmetric_difference(s2,s4)
    # print(s5)
    
    s6=s1.symmetric_difference({3,4,99,11,5})
    print(s6)
    
    
    s7=(s1^s2)
    print(s7)
if __name__=="__main__":
    main()"""

#symmetric_differnce_update()
"""
def main():
    s1={1,2,3,4,5,6,7,8}
    s2={8,2,5,11,26,99}
    s1.symmetric_difference_update(s2)
    print(s1)

    s1^s2   #cant take s3=s1^s2
    print(s1)

    s1.symmetric_difference_update({1,2,5,633,77})
    print(s1)

if __name__=="__main__":
    main()"""


#remove()
"""
def main():
    s1={1,2,3,4,5,6,7,8}
    s1.remove(1)
    print(s1)
    s1.remove(90)
    print(s1)#key error

if __name__=="__main__":
    main()"""



#discard()
"""
def main():
    s1={1,2,3,4,5,6,7,8}
    s1.remove(1)
    print(s1)
    s1.remove(90)
    print(s1)#key error

if __name__=="__main__":
    main()"""

##......pop()...remove random elem
"""
def main():
    s1={1,2,3,4,5,6,7,8}
    s1.pop()
    print(s1)

if __name__=="__main__":
    main()"""


#clear()
"""
def main():
    s1={1,2,3,4,5,6,7,8}
    s1.clear()
    print(s1)

if __name__=="__main__":
    main()"""

#isdijoint()
"""
def main():
    s1={1,2,3,4,5,6,7,8}
    s2={99,88,77}
    print(s1.isdisjoint(s2))
    
if __name__=="__main__":
    main()"""

#issubset():
"""
def main():
    s1 = {1, 2, 3, 4, 5, 6, 7, 8}
    s2 = {99, 88, 77,1,2,3}
    print(s1.issubset(s2))#true
    s3={1,2,3}
    print(s3.issubset(s1))
if __name__ == "__main__":
    main()"""

#add list of element to a set
"""
def main():
    l1=["a","b","c"]
     l2=["d","e"]
    # l1.extend(l2)
    # print(l1)
    # s1=set(l1)
    # print(s1)
    l3=l1+l2
    print(l3)
    set1=set(l3)
    print(set1)

if __name__ == "__main__":
    main()"""

#return identical elemnt from two set
"""
def main():
    s1 = {10,20,30,40,50}
    s2 = {30,40,50,60,70}
    s3=(s1 & s2)
    print(s3)
    s4=s1.intersection(s3)
    print(s4)
if __name__ == "__main__":
    main()"""

#..get only unique elemnt
"""
def main():

    s1 = {10,20,30,40,50}
    s2 = {30,40,50,60,70}
    s3=s1.symmetric_difference(s2)
    print(s3)
    s4=s1^s2
    print(s4)

if __name__ == "__main__":
    main()"""

#update the 1st set with item dont exit in 2nd set
"""
def main():
    s1 = {10, 20, 30}
    s2 = {30, 40, 50,}
    s1.difference_update(s2)
    print(s1)

if __name__ == "__main__":
    main()"""


#remove items from set at one step
"""
def main():

    s1 = {10, 20, 30,40,50}
    s1.difference_update({10,20,30})
    print(s1)

if __name__ == "__main__":
    main()"""

#reurn a set of elemnt which is present in both but not in each other
"""
def main():

    s1 = {10, 20, 30,40,50}
    s2 =  {30,40,50,60,70}
    s3=s1.symmetric_difference(s2)
    print(s3)

if __name__ == "__main__":
    main()"""


#check if two  sets hdave any elmns in common ,if yes display common elemnt
"""
def main():
    s1 = {10, 20, 30,40,50}
    s2 = {30,40,50,60,70}
    s3=s1.intersection(s2)
    print(s3)
    s4=s1&s2
    print(s4)

if __name__ == "__main__":
    main()"""

# updte set1 by adding items from set2 ,except common elemnt
"""
def main():

    s1 = {10, 20, 30,40,50}
    s2={30,40,50,60,70}
    s1.symmetric_difference_update(s2)
    print(s1)

if __name__ == "__main__":
    main()"""

#remove the  from s1 that is not common in s1 and s2
"""
def main():

    s1 = {10, 20, 30,40,50}
    s2={30,40,50,60,70}
    s1.intersection_update(s2)
    print(s1)

if __name__ == "__main__":
    main()"""

#find size of set
"""
import sys
def main():

    s2 = {10, 20, 30,40,50}
    size2=sys.getsizeof(s2)
    print("sizeof set=",size2,"bytes")

    size1=s2.__sizeof__()
    print("set of size=",size1,"bytes")



if __name__ == "__main__":
    main()"""

#iterate set
"""
def main3(s1):
    for i,j in enumerate (s1):
        print(i,"=",j)
def main2(s1):
    l2=[i for i in s1]
    print(l2,end=",")

def main1(s1):
    for i in s1:
        print(i,end=",")
def main():
    str1="jagruti"
    s1=set(str1)
    main1(s1)
    main2(s1)
    main3(s1)
if __name__ == "__main__":
    main()"""

#find max  in set
"""
def  main2(s1):
    return (max(s1))
def  main1(s1):
    l1=list(s1)
    l1.sort()
    print(l1)
    no=len(l1)-1
    return l1[no]
def main():
    s1={1,2,5,7,3,9,4}
    max1=main1(s1)
    print("max elemt in set =",max1)

    max2=main2(s1)
    print("max elemt in set =",max2)
if __name__ == "__main__":
    main()"""

#find min elemnt in set
"""
def main2(s1):
    return (min(s1))
def main1(s1):
    l1=list(s1)
    l1.sort()
    return l1[0]

def main():
    s1={1,2,5,7,3,9,4}
    min1=main1(s1)
    print("min val in set=",min1)

    min2=main2(s1)
    print("min val in set=",min2)
if __name__ == "__main__":
    main()"""


#check two list  have at list one elemrnt commom
"""
def main3(l1,l2,l3):
    flag=0
    for i in l1:
        for j in l2:
            if i ==j:
                flag=1
    if flag==1:
        print("true")

    else:
        print("false")

def main2(l1,l2,l3):
    s1=set(l1)
    s2=set(l2)
    s3=set(l3)
    if  (s1&s2):
        flag=1
    if flag==1:
        print("True")
    else:
        print("false")
def main1(l1,l2,l3):
    s1=set(l1)
    s2=set(l2)
    s3=set(l3)
    print(s1.isdisjoint(s2))
    print(s1.isdisjoint(s3))
def main():
    l1=[1,2,3,4,5]
    l2=[5,6,7,8,9]
    l3=[6,7,8,9]
    main1(l1,l2,l3)

    main2(l1,l2,l3)

    main3(l1,l2,l3)

if __name__ == "__main__":
    main()"""

#differnce btween to list
"""
def main2(l1,l2):
    for i in l1:
        for j in l2:
            if i==j:
                print(i,end=",")

def main1(l1,l2):
    s1=set(l1)
    s2=set(l2)
    s3=s1.symmetric_difference(s2)
    return s3

def main():
    l1=[1,2,3,4,5]
    l2=[5,4,7,8,9]
    diff1=main1(l1,l2)
    print(diff1)

    main2(l1,l2,)

if __name__ == "__main__":
    main()"""


#find lost elemnt from a duplicate array
"""
def main2(l1,l2):
    l3=[]
    for i in l1:
        for j in l2:
            if i!=j:
                l3.append(i)
                return l3
def main1(l1,l2):
    s1=set(l1)
    s2=set(l2)
    s3=s1.difference(s2)
    s4=s1-s2
    print("s4=",s4)
    return s3
def main():
    l1=[1,2,3,4,5]
    l2=[2,3,4,5]
    ele=main1(l1,l2)
    print("s3=",ele)

    ele2=main2(l1,l2,)
    print("l3=",ele2)

if __name__ == "__main__":
    main()"""

#
# #count no of vowel present in string:
#  """
#  def main1(str1):
#     count=0
#     vowel=set("AEIOUaeiou")
#     for i in str1:
#         if  i in vowel:
#             count=count+1
#     return count
# def main():
#     str1="GeekforGeeks"
#     no1=main1(str1)
#     print("no of vowel=",no1)
# if __name__ == "__main__":
#     main()"""

#concatinate string with ucommon char :
"""
def main1(str1,str2):
    s1=set(str1)
    s2=set(str2)
    s3=s1.symmetric_difference(s2)
    print("uncommonchar=","".join(s3))
    s4=list(s1^s2)
    return s4
def main():
    str1="aacdb"
    str2="gafd"
    uncomm=main1(str1,str2)
    print("uncmmn=","".join(uncomm))
if __name__ == "__main__":
    main()"""


#given string is binary or not
"""
def main1(str1):
    binary1={0,1}
    for char in str1:
        for bin in binary1:
            if char==binary1:
                print("yes")
            else:
                print("no")
                break


def main():
    str1="10101"
    main1(str1)
if __name__ == "__main__":
    main()"""
